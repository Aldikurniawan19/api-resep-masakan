import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { PrismaModule } from './prisma/prisma.module';
import { RecipesModule } from './modules/recipes/recipes.module';
import { CategoriesModule } from './modules/categories/categories.module';
import { CuisineTypesModule } from './modules/cuisine-types/cuisine-types.module';
import { OriginsModule } from './modules/origins/origins.module';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: '.env',
    }),
    PrismaModule,
    RecipesModule,
    CategoriesModule,
    CuisineTypesModule,
    OriginsModule,
  ],
})
export class AppModule {}

