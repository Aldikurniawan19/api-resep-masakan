import { PrismaClient, RecipeScope, Difficulty } from '@prisma/client';
import * as fs from 'fs';
import * as path from 'path';

const prisma = new PrismaClient();

interface RecipeData {
  recipeNumber: number;
  title: string;
  name: string;
  slug: string;
  scope: 'INDONESIA' | 'INTERNATIONAL';
  origin: string | null;
  visualRef: string | null;
  imageUrl: string | null;
  prepTimeMinutes: number | null;
  cookTimeMinutes: number | null;
  servings: number | null;
  difficulty: 'EASY' | 'MEDIUM' | 'HARD';
  spicinessLevel: number;
  categorySlug: string;
  cuisineTypeSlug: string;
  rawContent: string;
  ingredientGroups: {
    name: string;
    orderIndex: number;
    ingredients: {
      rawText: string;
      amount: number | null;
      unit: string | null;
      name: string | null;
      notes: string | null;
      orderIndex: number;
    }[];
  }[];
  steps: {
    stepNumber: number;
    title: string | null;
    instruction: string;
    rawText: string;
  }[];
  nutrition: {
    rawText: string;
    serving: string | null;
    calories: number | null;
    protein: number | null;
    fat: number | null;
    carbohydrates: number | null;
    notes: string | null;
  } | null;
}

interface SeedFile {
  categories: { name: string; slug: string; description: string }[];
  cuisineTypes: { name: string; slug: string; description: string }[];
  recipes: RecipeData[];
}

async function main() {
  console.log('Memulai proses seeding ke database Supabase...');

  const dataFilePath = path.join(__dirname, 'recipes-data.json');
  if (!fs.existsSync(dataFilePath)) {
    throw new Error(`File ${dataFilePath} tidak ditemukan! Jalankan python scripts/extract-recipes.py terlebih dahulu.`);
  }

  const raw = fs.readFileSync(dataFilePath, 'utf-8');
  const seedData: SeedFile = JSON.parse(raw);

  console.log(`Menyimpan ${seedData.categories.length} kategori...`);
  const categoryMap = new Map<string, string>();
  for (const cat of seedData.categories) {
    const upserted = await prisma.category.upsert({
      where: { slug: cat.slug },
      update: { name: cat.name, description: cat.description },
      create: { name: cat.name, slug: cat.slug, description: cat.description },
    });
    categoryMap.set(cat.slug, upserted.id);
  }

  console.log(`Menyimpan ${seedData.cuisineTypes.length} tipe masakan...`);
  const cuisineTypeMap = new Map<string, string>();
  for (const ct of seedData.cuisineTypes) {
    const upserted = await prisma.cuisineType.upsert({
      where: { slug: ct.slug },
      update: { name: ct.name, description: ct.description },
      create: { name: ct.name, slug: ct.slug, description: ct.description },
    });
    cuisineTypeMap.set(ct.slug, upserted.id);
  }

  console.log(`Menyimpan ${seedData.recipes.length} resep makanan lengkap beserta relasi...`);

  let count = 0;
  for (const r of seedData.recipes) {
    const categoryId = categoryMap.get(r.categorySlug);
    const cuisineTypeId = cuisineTypeMap.get(r.cuisineTypeSlug);

    if (!categoryId || !cuisineTypeId) {
      console.warn(`Melewatkan resep ${r.recipeNumber}: Kategori atau Tipe Masakan tidak valid.`);
      continue;
    }

    // Upsert Recipe
    await prisma.recipe.upsert({
      where: { recipeNumber: r.recipeNumber },
      update: {
        title: r.title,
        name: r.name,
        slug: r.slug,
        scope: r.scope as RecipeScope,
        origin: r.origin,
        visualRef: r.visualRef,
        imageUrl: r.imageUrl,
        prepTimeMinutes: r.prepTimeMinutes,
        cookTimeMinutes: r.cookTimeMinutes,
        servings: r.servings,
        difficulty: r.difficulty as Difficulty,
        spicinessLevel: r.spicinessLevel,
        categoryId,
        cuisineTypeId,
        rawContent: r.rawContent,
      },
      create: {
        recipeNumber: r.recipeNumber,
        title: r.title,
        name: r.name,
        slug: r.slug,
        scope: r.scope as RecipeScope,
        origin: r.origin,
        visualRef: r.visualRef,
        imageUrl: r.imageUrl,
        prepTimeMinutes: r.prepTimeMinutes,
        cookTimeMinutes: r.cookTimeMinutes,
        servings: r.servings,
        difficulty: r.difficulty as Difficulty,
        spicinessLevel: r.spicinessLevel,
        categoryId,
        cuisineTypeId,
        rawContent: r.rawContent,
      },
    });

    // Ambil resep ID
    const recipeRecord = await prisma.recipe.findUnique({
      where: { recipeNumber: r.recipeNumber },
      select: { id: true },
    });

    if (!recipeRecord) continue;
    const recipeId = recipeRecord.id;

    // Bersihkan relasi lama jika ada untuk idempotency
    await prisma.ingredientGroup.deleteMany({ where: { recipeId } });
    await prisma.recipeStep.deleteMany({ where: { recipeId } });
    await prisma.recipeNutrition.deleteMany({ where: { recipeId } });

    // Insert Groups & Ingredients
    for (const grp of r.ingredientGroups) {
      await prisma.ingredientGroup.create({
        data: {
          recipeId,
          name: grp.name,
          orderIndex: grp.orderIndex,
          ingredients: {
            create: grp.ingredients.map((ing) => ({
              rawText: ing.rawText,
              amount: ing.amount !== null ? ing.amount : undefined,
              unit: ing.unit,
              name: ing.name,
              notes: ing.notes,
              orderIndex: ing.orderIndex,
            })),
          },
        },
      });
    }

    // Insert Steps
    if (r.steps.length > 0) {
      await prisma.recipeStep.createMany({
        data: r.steps.map((st) => ({
          recipeId,
          stepNumber: st.stepNumber,
          title: st.title,
          instruction: st.instruction,
          rawText: st.rawText,
        })),
      });
    }

    // Insert Nutrition
    if (r.nutrition) {
      await prisma.recipeNutrition.create({
        data: {
          recipeId,
          serving: r.nutrition.serving,
          calories: r.nutrition.calories,
          protein: r.nutrition.protein,
          fat: r.nutrition.fat,
          carbohydrates: r.nutrition.carbohydrates,
          notes: r.nutrition.notes,
          rawText: r.nutrition.rawText,
        },
      });
    }

    count++;
    if (count % 25 === 0 || count === seedData.recipes.length) {
      console.log(`Tersimpan ${count}/${seedData.recipes.length} resep...`);
    }
  }

  console.log('Seeding selesai dengan sukses!');
}

main()
  .catch((e) => {
    console.error('Error saat seeding:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

