import { Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../prisma/prisma.service';
import { QueryRecipeDto } from './dto/query-recipe.dto';

@Injectable()
export class RecipesRepository {
  constructor(private readonly prisma: PrismaService) {}

  async findMany(query: QueryRecipeDto) {
    const {
      page = 1,
      limit = 10,
      search,
      scope,
      category,
      cuisineType,
      origin,
      difficulty,
      spicinessLevel,
      minCalories,
      maxCalories,
      sortBy = 'recipeNumber',
      sortOrder = 'asc',
    } = query;

    const skip = (page - 1) * limit;
    const where: Prisma.RecipeWhereInput = {};

    if (search) {
      where.OR = [
        { title: { contains: search, mode: 'insensitive' } },
        { name: { contains: search, mode: 'insensitive' } },
        { origin: { contains: search, mode: 'insensitive' } },
        {
          ingredientGroups: {
            some: {
              ingredients: {
                some: {
                  rawText: { contains: search, mode: 'insensitive' },
                },
              },
            },
          },
        },
      ];
    }

    if (scope) {
      where.scope = scope;
    }

    if (category) {
      where.category = {
        OR: [
          { slug: category },
          { name: { contains: category, mode: 'insensitive' } },
          { id: category },
        ],
      };
    }

    if (cuisineType) {
      where.cuisineType = {
        OR: [
          { slug: cuisineType },
          { name: { contains: cuisineType, mode: 'insensitive' } },
          { id: cuisineType },
        ],
      };
    }

    if (origin) {
      where.origin = { contains: origin, mode: 'insensitive' };
    }

    if (difficulty) {
      where.difficulty = difficulty;
    }

    if (spicinessLevel !== undefined) {
      where.spicinessLevel = spicinessLevel;
    }

    if (minCalories !== undefined || maxCalories !== undefined) {
      where.nutrition = {
        calories: {
          ...(minCalories !== undefined ? { gte: minCalories } : {}),
          ...(maxCalories !== undefined ? { lte: maxCalories } : {}),
        },
      };
    }

    // Dynamic sort
    const orderBy: Prisma.RecipeOrderByWithRelationInput = {};
    if (sortBy === 'name' || sortBy === 'title' || sortBy === 'recipeNumber' || sortBy === 'createdAt') {
      orderBy[sortBy] = sortOrder;
    } else if (sortBy === 'calories') {
      orderBy.nutrition = { calories: sortOrder };
    } else {
      orderBy.recipeNumber = sortOrder;
    }

    const [items, totalItems] = await Promise.all([
      this.prisma.recipe.findMany({
        where,
        skip,
        take: limit,
        orderBy,
        select: {
          id: true,
          recipeNumber: true,
          title: true,
          name: true,
          slug: true,
          scope: true,
          origin: true,
          visualRef: true,
          imageUrl: true,
          prepTimeMinutes: true,
          cookTimeMinutes: true,
          servings: true,
          difficulty: true,
          spicinessLevel: true,
          category: {
            select: {
              id: true,
              name: true,
              slug: true,
            },
          },
          cuisineType: {
            select: {
              id: true,
              name: true,
              slug: true,
            },
          },
          nutrition: {
            select: {
              serving: true,
              calories: true,
              protein: true,
              fat: true,
              carbohydrates: true,
            },
          },
        },
      }),
      this.prisma.recipe.count({ where }),
    ]);

    const totalPages = Math.ceil(totalItems / limit);

    return {
      data: items,
      meta: {
        page,
        limit,
        totalItems,
        totalPages,
        hasNextPage: page < totalPages,
        hasPrevPage: page > 1,
      },
    };
  }

  async findByIdOrSlug(idOrSlug: string) {
    const isUuid =
      /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(
        idOrSlug,
      );

    return this.prisma.recipe.findFirst({
      where: isUuid ? { id: idOrSlug } : { slug: idOrSlug },
      select: {
        id: true,
        recipeNumber: true,
        title: true,
        name: true,
        slug: true,
        scope: true,
        origin: true,
        visualRef: true,
        imageUrl: true,
        prepTimeMinutes: true,
        cookTimeMinutes: true,
        servings: true,
        difficulty: true,
        spicinessLevel: true,
        rawContent: true,
        createdAt: true,
        updatedAt: true,
        category: {
          select: {
            id: true,
            name: true,
            slug: true,
            description: true,
          },
        },
        cuisineType: {
          select: {
            id: true,
            name: true,
            slug: true,
            description: true,
          },
        },
        ingredientGroups: {
          orderBy: { orderIndex: 'asc' },
          select: {
            id: true,
            name: true,
            orderIndex: true,
            ingredients: {
              orderBy: { orderIndex: 'asc' },
              select: {
                id: true,
                rawText: true,
                amount: true,
                unit: true,
                name: true,
                notes: true,
                orderIndex: true,
              },
            },
          },
        },
        steps: {
          orderBy: { stepNumber: 'asc' },
          select: {
            id: true,
            stepNumber: true,
            title: true,
            instruction: true,
            rawText: true,
          },
        },
        nutrition: {
          select: {
            id: true,
            serving: true,
            calories: true,
            protein: true,
            fat: true,
            carbohydrates: true,
            notes: true,
            rawText: true,
          },
        },
      },
    });
  }

  async findRawByIdOrSlug(idOrSlug: string) {
    const isUuid =
      /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(
        idOrSlug,
      );

    return this.prisma.recipe.findFirst({
      where: isUuid ? { id: idOrSlug } : { slug: idOrSlug },
      select: {
        id: true,
        recipeNumber: true,
        title: true,
        slug: true,
        rawContent: true,
      },
    });
  }
}

