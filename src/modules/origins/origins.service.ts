import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../prisma/prisma.service';

@Injectable()
export class OriginsService {
  constructor(private readonly prisma: PrismaService) {}

  async findAll() {
    const rawOrigins = await this.prisma.recipe.groupBy({
      by: ['origin', 'scope'],
      where: {
        origin: {
          not: null,
        },
      },
      _count: {
        id: true,
      },
      orderBy: {
        origin: 'asc',
      },
    });

    const data = rawOrigins.map((item) => ({
      origin: item.origin,
      scope: item.scope,
      totalRecipes: item._count.id,
    }));

    return {
      message: 'Daftar wilayah dan negara asal berhasil diambil',
      data,
    };
  }
}

