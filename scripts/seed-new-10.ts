import { PrismaClient, RecipeScope, Difficulty } from '@prisma/client';
import * as fs from 'fs';
import * as path from 'path';

const prisma = new PrismaClient();

async function main() {
  console.log('Menyimpan 10 resep baru ke database Supabase...');

  const dataFilePath = path.join(__dirname, '../src/seeder/recipes-data.json');
  const raw = fs.readFileSync(dataFilePath, 'utf-8');
  const seedData = JSON.parse(raw);

  const categories = await prisma.category.findMany();
  const cuisineTypes = await prisma.cuisineType.findMany();

  const categoryMap = new Map(categories.map((c) => [c.slug, c.id]));
  const cuisineTypeMap = new Map(cuisineTypes.map((c) => [c.slug, c.id]));

  const newRecipes = seedData.recipes.filter((r: any) => r.recipeNumber >= 171);
  console.log(`Ditemukan ${newRecipes.length} resep baru untuk di-seed.`);

  for (const r of newRecipes) {
    const categoryId = categoryMap.get(r.categorySlug);
    const cuisineTypeId = cuisineTypeMap.get(r.cuisineTypeSlug);

    if (!categoryId || !cuisineTypeId) {
      console.warn(`Resep ${r.recipeNumber}: Kategori atau Tipe Masakan tidak valid.`);
      continue;
    }

    console.log(`Menyimpan resep ${r.recipeNumber}: ${r.title}...`);

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

    const record = await prisma.recipe.findUnique({
      where: { recipeNumber: r.recipeNumber },
      select: { id: true },
    });

    if (!record) continue;
    const recipeId = record.id;

    await prisma.ingredientGroup.deleteMany({ where: { recipeId } });
    await prisma.recipeStep.deleteMany({ where: { recipeId } });
    await prisma.recipeNutrition.deleteMany({ where: { recipeId } });

    for (const grp of r.ingredientGroups) {
      await prisma.ingredientGroup.create({
        data: {
          recipeId,
          name: grp.name,
          orderIndex: grp.orderIndex,
          ingredients: {
            create: grp.ingredients.map((ing: any) => ({
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

    if (r.steps.length > 0) {
      await prisma.recipeStep.createMany({
        data: r.steps.map((st: any) => ({
          recipeId,
          stepNumber: st.stepNumber,
          title: st.title,
          instruction: st.instruction,
          rawText: st.rawText,
        })),
      });
    }

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
  }

  const totalInDb = await prisma.recipe.count();
  console.log(`Seeding 10 resep selesai! Total resep di database sekarang: ${totalInDb}`);
}

main()
  .catch((e) => {
    console.error('Error saat seeding resep baru:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

