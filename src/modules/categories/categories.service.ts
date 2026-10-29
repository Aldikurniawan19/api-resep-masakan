import { Injectable, NotFoundException } from '@nestjs/common';
import { CategoriesRepository } from './categories.repository';

@Injectable()
export class CategoriesService {
  constructor(private readonly categoriesRepository: CategoriesRepository) {}

  async findAll() {
    const categories = await this.categoriesRepository.findAll();
    return {
      message: 'Daftar kategori berhasil diambil',
      data: categories,
    };
  }

  async findOne(slugOrId: string) {
    const category = await this.categoriesRepository.findBySlugOrId(slugOrId);
    if (!category) {
      throw new NotFoundException(`Kategori '${slugOrId}' tidak ditemukan`);
    }
    return {
      message: 'Detail kategori berhasil diambil',
      data: category,
    };
  }
}

