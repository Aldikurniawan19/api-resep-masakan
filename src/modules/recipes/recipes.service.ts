import { Injectable, NotFoundException } from '@nestjs/common';
import { RecipesRepository } from './recipes.repository';
import { QueryRecipeDto } from './dto/query-recipe.dto';

@Injectable()
export class RecipesService {
  constructor(private readonly recipesRepository: RecipesRepository) {}

  async findAll(query: QueryRecipeDto) {
    const result = await this.recipesRepository.findMany(query);
    return {
      message: 'Daftar resep berhasil diambil',
      data: result.data,
      meta: result.meta,
    };
  }

  async findOne(idOrSlug: string) {
    const recipe = await this.recipesRepository.findByIdOrSlug(idOrSlug);
    if (!recipe) {
      throw new NotFoundException(`Resep dengan ID atau slug '${idOrSlug}' tidak ditemukan`);
    }
    return {
      message: 'Detail resep berhasil diambil',
      data: recipe,
    };
  }

  async findRaw(idOrSlug: string) {
    const rawRecipe = await this.recipesRepository.findRawByIdOrSlug(idOrSlug);
    if (!rawRecipe) {
      throw new NotFoundException(`Resep dengan ID atau slug '${idOrSlug}' tidak ditemukan`);
    }
    return {
      message: 'Teks asli dokumen resep berhasil diambil',
      data: rawRecipe,
    };
  }
}

