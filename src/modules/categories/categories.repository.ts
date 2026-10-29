import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../prisma/prisma.service';

@Injectable()
export class CategoriesRepository {
  constructor(private readonly prisma: PrismaService) {}

  async findAll() {
    return this.prisma.category.findMany({
      orderBy: { name: 'asc' },
      select: {
        id: true,
        name: true,
        slug: true,
        description: true,
        _count: {
          select: {
            recipes: true,
          },
        },
      },
    });
  }

  async findBySlugOrId(slugOrId: string) {
    const isUuid =
      /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(
        slugOrId,
      );

    return this.prisma.category.findFirst({
      where: isUuid ? { id: slugOrId } : { slug: slugOrId },
      select: {
        id: true,
        name: true,
        slug: true,
        description: true,
        _count: {
          select: {
            recipes: true,
          },
        },
      },
    });
  }
}

