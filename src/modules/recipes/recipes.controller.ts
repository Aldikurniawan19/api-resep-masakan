import { Controller, Get, Param, Query } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse, ApiParam } from '@nestjs/swagger';
import { RecipesService } from './recipes.service';
import { QueryRecipeDto } from './dto/query-recipe.dto';

@ApiTags('Recipes')
@Controller('api/v1/recipes')
export class RecipesController {
  constructor(private readonly recipesService: RecipesService) {}

  @Get()
  @ApiOperation({
    summary: 'Ambil daftar resep dengan filter dan paginasi',
    description:
      'Mendukung filter berdasarkan kata kunci (search), scope (INDONESIA/INTERNATIONAL), kategori, tipe masakan, asal daerah/negara, tingkat kesulitan, kepedasan, dan kalori.',
  })
  @ApiResponse({ status: 200, description: 'Daftar resep berhasil diambil' })
  async findAll(@Query() query: QueryRecipeDto) {
    return this.recipesService.findAll(query);
  }

  @Get(':idOrSlug/raw')
  @ApiOperation({
    summary: 'Ambil teks asli dokumen resep (format mentah verbatim)',
    description: 'Menampilkan teks asli persis seperti yang tertulis di dalam file dokumen docx.',
  })
  @ApiParam({ name: 'idOrSlug', description: 'UUID atau slug resep' })
  @ApiResponse({ status: 200, description: 'Format mentah dokumen berhasil diambil' })
  @ApiResponse({ status: 404, description: 'Resep tidak ditemukan' })
  async findRaw(@Param('idOrSlug') idOrSlug: string) {
    return this.recipesService.findRaw(idOrSlug);
  }

  @Get(':idOrSlug')
  @ApiOperation({
    summary: 'Ambil detail lengkap satu resep',
    description:
      'Menampilkan informasi terstruktur mencakup kelompok bahan baku, tahapan langkah pembuatan, dan profil nutrisi.',
  })
  @ApiParam({ name: 'idOrSlug', description: 'UUID atau slug resep (misal: rendang-daging-khas-minang)' })
  @ApiResponse({ status: 200, description: 'Detail resep berhasil diambil' })
  @ApiResponse({ status: 404, description: 'Resep tidak ditemukan' })
  async findOne(@Param('idOrSlug') idOrSlug: string) {
    return this.recipesService.findOne(idOrSlug);
  }
}

