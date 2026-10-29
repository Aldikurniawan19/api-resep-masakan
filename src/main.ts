import { NestFactory } from '@nestjs/core';
import { ValidationPipe, Logger } from '@nestjs/common';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';
import { HttpExceptionFilter } from './common/filters/http-exception.filter';
import { TransformResponseInterceptor } from './common/interceptors/transform-response.interceptor';

async function bootstrap() {
  const logger = new Logger('Bootstrap');
  const app = await NestFactory.create(AppModule);

  // Enable CORS
  app.enableCors();

  // Global validation pipe
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      transform: true,
      transformOptions: { enableImplicitConversion: true },
      forbidNonWhitelisted: false,
    }),
  );

  // Global filters and interceptors
  app.useGlobalFilters(new HttpExceptionFilter());
  app.useGlobalInterceptors(new TransformResponseInterceptor());

  // Swagger Documentation Setup
  const config = new DocumentBuilder()
    .setTitle('API Resep Masakan Indonesia & Internasional')
    .setDescription(
      'REST API komprehensif untuk data 170 resep masakan Nusantara dan Internasional. Dilengkapi filter kategori, tipe masakan, asal daerah, nutrisi, tingkat kepedasan, dan format teks asli.',
    )
    .setVersion('1.0.0')
    .addTag('Recipes', 'Operasi dan filter data resep masakan')
    .addTag('Categories', 'Kategori masakan (Daging, Soto, Sayur, Kudapan, dll)')
    .addTag('Cuisine Types', 'Tipe masakan (Daerah, Rumahan, Street Food, Hari Raya, Internasional)')
    .addTag('Origins', 'Daftar wilayah provinsi, kota, dan negara asal masakan')
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api/docs', app, document);

  const port = process.env.PORT || 3000;
  await app.listen(port);
  logger.log(`Aplikasi berjalan di: http://localhost:${port}`);
  logger.log(`Dokumentasi Swagger API aktif di: http://localhost:${port}/api/docs`);
}

bootstrap();

