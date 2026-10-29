# API Resep Masakan Indonesia & Internasional

Backend REST API performa tinggi berbasis **NestJS**, **Prisma ORM**, dan **Supabase (PostgreSQL)** untuk mengelola, mencari, dan menyajikan 170 resep autentik Nusantara dan Internasional yang diekstrak langsung dari dokumen resep profesional.

---

## 1. Fitur Utama

- **170 Resep Lengkap & Autentik**:
  - 150 Resep Nusantara (Masakan Daerah Tradisional, Masakan Rumahan, Street Food Kaki Lima, Hidangan Hari Raya, Kudapan Jajanan Pasar, dan Minuman Segar).
  - 20 Resep Internasional (Asia: Jepang, Korea Selatan, Thailand, Singapura, Tiongkok; Barat/Eropa: Italia, Amerika Serikat, Prancis).
- **Pengelompokan Bahan Baku Terstruktur**: Bahan Utama, Bumbu Halus, Bumbu Rempah Cemplung, Pelengkap Penyajian, dan bumbu kuah.
- **Tahapan Memasak Berfase**: Setiap tahapan memiliki nama fase teknik (misal: *Menyangrai Bumbu*, *Memasukkan Daging*, *Slow Cooking*, *Penyelesaian*).
- **Profil Makronutrisi Presisi**: Kalori (kkal), Protein (g), Lemak (g), Karbohidrat (g), dan catatan gizi per porsi/takaran saji.
- **Kombinasi Dual-Layer Format**: Menyediakan data ternormalisasi untuk filter cepat sekaligus teks mentah dokumen (`rawContent`) agar tidak ada detail yang hilang.
- **Filter Multi-Kriteria Canggih**: Pencarian teks (search), cakupan (`INDONESIA` / `INTERNATIONAL`), kategori masakan, tipe masakan, asal daerah/negara, rentang kalori, tingkat kesulitan (`EASY`, `MEDIUM`, `HARD`), dan tingkat kepedasan (0-3).
- **Dokumentasi Interaktif Swagger / OpenAPI**: Siap diakses langsung di `/api/docs`.

---

## 2. Arsitektur & Prinsip Kode

Sesuai dengan standar senior developer pada `aturan-penulisan-kode.md`:
- **Separation of Concerns**: Controller (tipis) $\rightarrow$ Service (logika bisnis) $\rightarrow$ Repository (kueri database Prisma).
- **Bebas N+1 Query**: Menggunakan Prisma `include` dan `select` yang dioptimalkan dalam satu batch query.
- **Bebas `SELECT *`**: Kolom data yang diambil didefinisikan secara eksplisit.
- **Validasi Input Ketat**: DTO divalidasi otomatis menggunakan `class-validator` dan `class-transformer`.
- **Standar Response Terpadu**: Global interceptor membungkus response ke format standar `{ statusCode, success, message, data, meta }`.
- **Penanganan Error Aman**: Global exception filter menyembunyikan detail stack trace database dari pengguna publik.

---

## 3. Daftar Endpoint REST API

Semua endpoint diawali dengan prefix `/api/v1`.

### Resep (`/api/v1/recipes`)

| Method | Endpoint | Deskripsi |
|---|---|---|
| `GET` | `/api/v1/recipes` | Mengambil daftar resep dengan filter dan paginasi |
| `GET` | `/api/v1/recipes/:idOrSlug` | Mengambil detail lengkap 1 resep (bahan bertingkat, langkah berfase, nutrisi) |
| `GET` | `/api/v1/recipes/:idOrSlug/raw` | Mengambil teks asli verbatim persis dari dokumen |

#### Parameter Filter `GET /api/v1/recipes`:
- `page`: Nomor halaman (default: `1`)
- `limit`: Jumlah item per halaman (default: `10`, max: `100`)
- `search`: Pencarian nama masakan, judul, atau bahan baku
- `scope`: `INDONESIA` atau `INTERNATIONAL`
- `category`: Slug atau nama kategori (misal: `daging-sapi-kambing`, `sup-soto`, `sayuran-tumisan`)
- `cuisineType`: Slug atau nama tipe (misal: `masakan-daerah-tradisional`, `masakan-rumahan`, `street-food-kaki-lima`)
- `origin`: Asal daerah atau negara (misal: `Sumatera Barat`, `Jawa Timur`, `Bali`, `Jepang`, `Thailand`)
- `difficulty`: `EASY`, `MEDIUM`, `HARD`
- `spicinessLevel`: `0` (Tidak Pedas) hingga `3` (Sangat Pedas)
- `minCalories` & `maxCalories`: Filter batas kalori (kkal)
- `sortBy`: `recipeNumber`, `name`, `calories`, `createdAt`
- `sortOrder`: `asc` atau `desc`

### Taksonomi & Master Data

| Method | Endpoint | Deskripsi |
|---|---|---|
| `GET` | `/api/v1/categories` | Daftar 11 kategori masakan beserta jumlah resep di tiap kategori |
| `GET` | `/api/v1/categories/:slugOrId` | Detail 1 kategori masakan |
| `GET` | `/api/v1/cuisine-types` | Daftar 7 tipe masakan beserta jumlah resepnya |
| `GET` | `/api/v1/cuisine-types/:slugOrId` | Detail 1 tipe masakan |
| `GET` | `/api/v1/origins` | Daftar seluruh asal daerah (provinsi/kota) dan negara beserta jumlah resepnya |

---

## 4. Cara Menjalankan Project

### Prasyarat
- Node.js v18+ atau v20+
- Database Supabase PostgreSQL aktif

### 1. Salin Konfigurasi Environment
```bash
cp .env.example .env
```
Pastikan `DATABASE_URL` dan `DIRECT_URL` sudah terisi dengan kredensial Supabase Anda.

### 2. Install Dependensi
```bash
npm install
```

### 3. Generate Prisma Client & Sinkronisasi Skema
```bash
npm run prisma:generate
npm run prisma:push
```

### 4. Ekstraksi Data Dokumen & Jalankan Seeder
```bash
python scripts/extract-recipes.py
npm run seed
```

### 5. Jalankan Server NestJS
```bash
# Mode Development (Hot-Reload)
npm run start:dev

# Mode Production
npm run build
npm run start:prod
```

Aplikasi akan aktif di `http://localhost:3000` dan dokumentasi Swagger dapat dibuka di `http://localhost:3000/api/docs`.

