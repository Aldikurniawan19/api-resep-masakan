import { Controller, Get } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';
import { OriginsService } from './origins.service';

@ApiTags('Origins')
@Controller('api/v1/origins')
export class OriginsController {
  constructor(private readonly originsService: OriginsService) {}

  @Get()
  @ApiOperation({
    summary: 'Ambil daftar seluruh asal daerah / negara',
    description: 'Menampilkan seluruh asal daerah (provinsi/kota) dan negara beserta jumlah resepnya.',
  })
  @ApiResponse({ status: 200, description: 'Daftar asal daerah berhasil diambil' })
  async findAll() {
    return this.originsService.findAll();
  }
}

