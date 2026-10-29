import { IsOptional, IsString, IsEnum, IsNumber, Min } from 'class-validator';
import { Type } from 'class-transformer';
import { ApiPropertyOptional } from '@nestjs/swagger';
import { PaginationQueryDto } from '../../../common/dto/pagination-query.dto';

export enum RecipeScopeEnum {
  INDONESIA = 'INDONESIA',
  INTERNATIONAL = 'INTERNATIONAL',
}

export enum DifficultyEnum {
  EASY = 'EASY',
  MEDIUM = 'MEDIUM',
  HARD = 'HARD',
}

export class QueryRecipeDto extends PaginationQueryDto {
  @ApiPropertyOptional({ description: 'Kata kunci pencarian (nama masakan, judul, atau bahan)' })
  @IsOptional()
  @IsString()
  search?: string;

  @ApiPropertyOptional({ enum: RecipeScopeEnum, description: 'Cakupan resep: INDONESIA atau INTERNATIONAL' })
  @IsOptional()
  @IsEnum(RecipeScopeEnum)
  scope?: RecipeScopeEnum;

  @ApiPropertyOptional({ description: 'Slug atau nama kategori masakan (misal: sup-soto, daging-sapi-kambing)' })
  @IsOptional()
  @IsString()
  category?: string;

  @ApiPropertyOptional({ description: 'Slug atau nama tipe masakan (misal: masakan-daerah, masakan-rumahan)' })
  @IsOptional()
  @IsString()
  cuisineType?: string;

  @ApiPropertyOptional({ description: 'Asal daerah atau negara (misal: Sumatera Barat, Jawa Timur, Bali, Jepang)' })
  @IsOptional()
  @IsString()
  origin?: string;

  @ApiPropertyOptional({ enum: DifficultyEnum, description: 'Tingkat kesulitan memasak' })
  @IsOptional()
  @IsEnum(DifficultyEnum)
  difficulty?: DifficultyEnum;

  @ApiPropertyOptional({ description: 'Tingkat kepedasan (0: tidak pedas, 1: sedang, 2: pedas, 3: sangat pedas)' })
  @IsOptional()
  @Type(() => Number)
  @IsNumber()
  spicinessLevel?: number;

  @ApiPropertyOptional({ description: 'Batas kalori minimum (kkal)' })
  @IsOptional()
  @Type(() => Number)
  @IsNumber()
  @Min(0)
  minCalories?: number;

  @ApiPropertyOptional({ description: 'Batas kalori maksimum (kkal)' })
  @IsOptional()
  @Type(() => Number)
  @IsNumber()
  @Min(0)
  maxCalories?: number;
}
