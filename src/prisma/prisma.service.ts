import { Injectable, OnModuleInit, OnModuleDestroy, Logger } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit, OnModuleDestroy {
  private readonly logger = new Logger(PrismaService.name);

  async onModuleInit(): Promise<void> {
    try {
      await this.$connect();
      this.logger.log('Koneksi ke database Supabase berhasil diinisialisasi.');
    } catch (error) {
      this.logger.error('Peringatan: Gagal melakukan inisialisasi koneksi awal ke database:', error);
    }
  }

  async onModuleDestroy(): Promise<void> {
    await this.$disconnect();
  }
}

