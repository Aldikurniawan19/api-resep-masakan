import { Module } from '@nestjs/common';
import { CuisineTypesController } from './cuisine-types.controller';
import { CuisineTypesService } from './cuisine-types.service';
import { CuisineTypesRepository } from './cuisine-types.repository';

@Module({
  controllers: [CuisineTypesController],
  providers: [CuisineTypesService, CuisineTypesRepository],
  exports: [CuisineTypesService, CuisineTypesRepository],
})
export class CuisineTypesModule {}

