import { Controller, Get, Param } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse, ApiParam } from '@nestjs/swagger';
import { CategoriesService } from './categories.service';

@ApiTags('Categories')
@Controller('api/v1/categories')
export class CategoriesController {
  constructor(private readonly categoriesService: CategoriesService) {}

  @Get()
  @ApiOperation({
    summary: 'Ambil seluruh kategori masakan',
    description: 'Menampilkan seluruh kategori masakan beserta jumlah resep di masing-masing kategori.',
  })
  @ApiResponse({ status: 200, description: 'Daftar kategori berhasil diambil' })
  async findAll() {
    return this.categoriesService.findAll();
  }

  @Get(':slugOrId')
  @ApiOperation({ summary: 'Ambil detail satu kategori masakan' })
  @ApiParam({ name: 'slugOrId', description: 'UUID atau slug kategori (misal: sup-soto)' })
  @ApiResponse({ status: 200, description: 'Detail kategori berhasil diambil' })
  @ApiResponse({ status: 404, description: 'Kategori tidak ditemukan' })
  async findOne(@Param('slugOrId') slugOrId: string) {
    return this.categoriesService.findOne(slugOrId);
  }
}

