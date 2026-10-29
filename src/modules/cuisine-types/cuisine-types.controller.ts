import { Controller, Get, Param } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse, ApiParam } from '@nestjs/swagger';
import { CuisineTypesService } from './cuisine-types.service';

@ApiTags('Cuisine Types')
@Controller('api/v1/cuisine-types')
export class CuisineTypesController {
  constructor(private readonly cuisineTypesService: CuisineTypesService) {}

  @Get()
  @ApiOperation({
    summary: 'Ambil seluruh tipe masakan',
    description:
      'Menampilkan tipe masakan (seperti Masakan Daerah, Masakan Rumahan, Street Food / Kaki Lima, Hari Raya / Perayaan, Kudapan, Internasional) beserta jumlah resepnya.',
  })
  @ApiResponse({ status: 200, description: 'Daftar tipe masakan berhasil diambil' })
  async findAll() {
    return this.cuisineTypesService.findAll();
  }

  @Get(':slugOrId')
  @ApiOperation({ summary: 'Ambil detail satu tipe masakan' })
  @ApiParam({ name: 'slugOrId', description: 'UUID atau slug tipe masakan (misal: masakan-daerah)' })
  @ApiResponse({ status: 200, description: 'Detail tipe masakan berhasil diambil' })
  @ApiResponse({ status: 404, description: 'Tipe masakan tidak ditemukan' })
  async findOne(@Param('slugOrId') slugOrId: string) {
    return this.cuisineTypesService.findOne(slugOrId);
  }
}

