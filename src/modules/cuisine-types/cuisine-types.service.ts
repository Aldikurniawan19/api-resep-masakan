import { Injectable, NotFoundException } from '@nestjs/common';
import { CuisineTypesRepository } from './cuisine-types.repository';

@Injectable()
export class CuisineTypesService {
  constructor(private readonly cuisineTypesRepository: CuisineTypesRepository) {}

  async findAll() {
    const cuisineTypes = await this.cuisineTypesRepository.findAll();
    return {
      message: 'Daftar tipe masakan berhasil diambil',
      data: cuisineTypes,
    };
  }

  async findOne(slugOrId: string) {
    const cuisineType = await this.cuisineTypesRepository.findBySlugOrId(slugOrId);
    if (!cuisineType) {
      throw new NotFoundException(`Tipe masakan '${slugOrId}' tidak ditemukan`);
    }
    return {
      message: 'Detail tipe masakan berhasil diambil',
      data: cuisineType,
    };
  }
}

