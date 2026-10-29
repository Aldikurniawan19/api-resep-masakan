import { NestFactory } from '@nestjs/core';
import { ExpressAdapter } from '@nestjs/platform-express';
import { AppModule } from '../src/app.module';
import { ValidationPipe } from '@nestjs/common';
import { HttpExceptionFilter } from '../src/common/filters/http-exception.filter';
import { TransformResponseInterceptor } from '../src/common/interceptors/transform-response.interceptor';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import express, { Request, Response, Express } from 'express';

let cachedServer: Express;

async function bootstrapServer(): Promise<Express> {
  const expressApp = express();
  const app = await NestFactory.create(AppModule, new ExpressAdapter(expressApp));

  app.enableCors();

  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      transform: true,
      transformOptions: { enableImplicitConversion: true },
      forbidNonWhitelisted: false,
    }),
  );

  app.useGlobalFilters(new HttpExceptionFilter());
  app.useGlobalInterceptors(new TransformResponseInterceptor());

  const config = new DocumentBuilder()
    .setTitle('API Resep Masakan Indonesia & Internasional')
    .setDescription(
      'REST API komprehensif untuk data 200 resep masakan Nusantara dan Internasional. Dilengkapi filter kategori, tipe masakan, asal daerah, nutrisi, dan tingkat kepedasan.',
    )
    .setVersion('1.0.0')
    .addTag('Recipes', 'Operasi dan filter data resep masakan')
    .addTag('Categories', 'Kategori masakan')
    .addTag('Cuisine Types', 'Tipe masakan')
    .addTag('Origins', 'Daftar wilayah asal masakan')
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api/docs', app, document);

  await app.init();
  return expressApp;
}

export default async function handler(req: Request, res: Response) {
  if (!cachedServer) {
    cachedServer = await bootstrapServer();
  }
  return cachedServer(req, res);
}

