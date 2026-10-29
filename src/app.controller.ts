import { Controller, Get } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';

@ApiTags('Root')
@Controller()
export class AppController {
  @Get()
  @ApiOperation({ summary: 'Informasi status dan endpoint API' })
  @ApiResponse({ status: 200, description: 'API aktif dan siap digunakan' })
  getRoot() {
    return {
      name: 'API Resep Masakan Indonesia & Internasional',
      version: '1.0.0',
      status: 'online',
      documentation: '/api/docs',
      endpoints: {
        recipes: '/api/v1/recipes',
        categories: '/api/v1/categories',
        cuisineTypes: '/api/v1/cuisine-types',
        origins: '/api/v1/origins',
      },
    };
  }

  @Get('health')
  @ApiOperation({ summary: 'Health check API' })
  @ApiResponse({ status: 200, description: 'Layanan sehat' })
  getHealth() {
    return {
      status: 'ok',
      timestamp: new Date().toISOString(),
    };
  }
}

