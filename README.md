# Panduan Teknis REST API Resep Masakan Indonesia & Internasional

REST API publik berperforma tinggi untuk mengakses data 210 resep masakan autentik Nusantara dan Internasional. Dokumentasi ini disusun khusus sebagai panduan integrasi bagi pengembang frontend (Web/Mobile), data consumer, dan layanan pihak ketiga.

---

## 1. Informasi Dasar Layanan

- **Base URL**: `/api/v1` (contoh: `http://localhost:3000/api/v1` atau domain produksi aktif)
- **Format Pertukaran Data**: JSON (`application/json`)
- **Autentikasi**: Endpoint saat ini bersifat publik (Read-Only) tanpa memerlukan API Key atau Bearer Token.
- **CORS**: Diaktifkan secara default untuk semua domain (`Access-Control-Allow-Origin: *`).
- **Dokumentasi Interaktif (Swagger UI)**: Dapat diakses melalui browser pada path `/api/docs`.

---

## 2. Format Respon Standar

Setiap respon dari API dibungkus dalam amplop (*envelope*) standar yang konsisten untuk mempermudah penanganan data di sisi klien.

### Format Respon Berhasil (Success)

```json
{
  "statusCode": 200,
  "success": true,
  "message": "Permintaan berhasil diproses",
  "data": {},
  "meta": {
    "page": 1,
    "limit": 10,
    "totalItems": 210,
    "totalPages": 21,
    "hasNextPage": true,
    "hasPrevPage": false
  }
}
```

*Catatan: Objek `meta` hanya disertakan pada endpoint yang mendukung paginasi data.*

### Format Respon Gagal (Error)

```json
{
  "statusCode": 404,
  "success": false,
  "message": "Resep dengan slug atau ID 'menu-tidak-ada' tidak ditemukan",
  "errors": null,
  "timestamp": "2026-10-30T13:30:00.000Z",
  "path": "/api/v1/recipes/menu-tidak-ada"
}
```

---

## 3. Daftar Endpoint Lengkap

### Ringkasan Endpoint

| Method | Endpoint | Deskripsi |
|---|---|---|
| `GET` | `/api/v1/recipes` | Mengambil daftar resep dengan filter pencarian dan paginasi |
| `GET` | `/api/v1/recipes/:idOrSlug` | Mengambil detail lengkap satu resep (bahan bertingkat, langkah, nutrisi) |
| `GET` | `/api/v1/recipes/:idOrSlug/raw` | Mengambil teks asli verbatim persis dari dokumen sumber resep |
| `GET` | `/api/v1/categories` | Mengambil daftar 11 kategori masakan beserta jumlah resepnya |
| `GET` | `/api/v1/categories/:slugOrId` | Mengambil detail 1 kategori masakan |
| `GET` | `/api/v1/cuisine-types` | Mengambil daftar 7 tipe masakan beserta jumlah resepnya |
| `GET` | `/api/v1/cuisine-types/:slugOrId` | Mengambil detail 1 tipe masakan |
| `GET` | `/api/v1/origins` | Mengambil daftar seluruh daerah provinsi, kota, dan negara asal masakan |

---

## 4. Rincian Endpoint Resep

### 4.1. Mengambil Daftar Resep (`GET /api/v1/recipes`)

Endpoint ini digunakan untuk katalog menu, pencarian, dan penyaringan multi-kriteria.

#### Parameter Kueri (Query Parameters)

| Parameter | Tipe | Default | Deskripsi & Nilai yang Diterima |
|---|---|---|---|
| `page` | Integer | `1` | Nomor halaman (mulai dari 1). |
| `limit` | Integer | `10` | Jumlah item per halaman (maksimal 100). |
| `search` | String | - | Pencarian teks bebas pada judul resep, nama menu, asal daerah, atau nama bahan baku. |
| `scope` | String | - | Filter cakupan wilayah: `INDONESIA` atau `INTERNATIONAL`. |
| `category` | String | - | Slug atau ID kategori (contoh: `daging-sapi-kambing`, `sup-soto`, `sayuran-tumisan`). |
| `cuisineType` | String | - | Slug atau ID tipe masakan (contoh: `masakan-daerah-tradisional`, `masakan-rumahan`). |
| `origin` | String | - | Filter wilayah asal (contoh: `Sumatera Barat`, `Jawa Timur`, `Jepang`). |
| `difficulty` | String | - | Tingkat kesulitan memasak: `EASY`, `MEDIUM`, atau `HARD`. |
| `spicinessLevel` | Integer | - | Tingkat kepedasan: `0` (Tidak Pedas), `1` (Sedang), `2` (Pedas), `3` (Sangat Pedas). |
| `minCalories` | Integer | - | Batas minimal kalori per porsi (kkal). |
| `maxCalories` | Integer | - | Batas maksimal kalori per porsi (kkal). |
| `sortBy` | String | `recipeNumber` | Bidang pengurutan: `recipeNumber`, `name`, `title`, `calories`, `createdAt`. |
| `sortOrder` | String | `asc` | Arah pengurutan: `asc` (naik) atau `desc` (turun). |

#### Contoh Permintaan (Request)

```bash
# Mengambil 5 resep masakan berkuah dari Jawa Timur yang pedas
curl -X GET "http://localhost:3000/api/v1/recipes?category=sup-soto&origin=Jawa%20Timur&limit=5"
```

```javascript
// Contoh pemanggilan menggunakan JavaScript Fetch API
const fetchRecipes = async () => {
  const params = new URLSearchParams({
    scope: 'INDONESIA',
    difficulty: 'MEDIUM',
    page: '1',
    limit: '10'
  });
  
  const response = await fetch(`http://localhost:3000/api/v1/recipes?${params}`);
  const json = await response.json();
  return json.data;
};
```

#### Contoh Respon (Response)

```json
{
  "statusCode": 200,
  "success": true,
  "message": "Permintaan berhasil diproses",
  "data": [
    {
      "id": "927ea8d8-cfa2-4fc0-a91a-adc0ff8a32d1",
      "recipeNumber": 1,
      "title": "1. Rendang Daging Khas Minang (Sumatera Barat)",
      "name": "Rendang Daging Khas Minang",
      "slug": "rendang-daging-khas-minang",
      "scope": "INDONESIA",
      "origin": "Sumatera Barat",
      "visualRef": "Lihat Ilustrasi Masakan",
      "imageUrl": "https://nbilkbsqdrbtudqdehik.supabase.co/storage/v1/object/public/recipes/rendang-daging-khas-minang.jpg",
      "prepTimeMinutes": 30,
      "cookTimeMinutes": 240,
      "servings": 8,
      "difficulty": "HARD",
      "spicinessLevel": 2,
      "category": {
        "id": "787c88b0-a6ff-4796-af01-1b7713dca77c",
        "name": "Olahan Daging Sapi & Kambing",
        "slug": "daging-sapi-kambing"
      },
      "cuisineType": {
        "id": "2d1b82fa-255e-44ca-873b-554160d5b6c3",
        "name": "Masakan Daerah Tradisional",
        "slug": "masakan-daerah-tradisional"
      },
      "nutrition": {
        "calories": 420,
        "protein": 34,
        "fat": 28,
        "carbohydrates": 8,
        "serving": "Per Porsi"
      }
    }
  ],
  "meta": {
    "page": 1,
    "limit": 10,
    "totalItems": 210,
    "totalPages": 21,
    "hasNextPage": true,
    "hasPrevPage": false
  }
}
```

---

### 4.2. Mengambil Detail Lengkap Resep (`GET /api/v1/recipes/:idOrSlug`)

Menampilkan struktur mendalam satu menu: kelompok bahan baku bertingkat, tahapan langkah berfase, dan rincian nutrisi lengkap.

#### Parameter Jalur (Path Parameter)

- `idOrSlug`: UUID resep atau string slug resep (misal: `rendang-daging-khas-minang`, `soto-betawi`). Disarankan menggunakan `slug` untuk implementasi URL ramah SEO di frontend.

#### Contoh Permintaan (Request)

```bash
curl -X GET "http://localhost:3000/api/v1/recipes/rendang-daging-khas-minang"
```

#### Contoh Respon (Response)

```json
{
  "statusCode": 200,
  "success": true,
  "message": "Permintaan berhasil diproses",
  "data": {
    "id": "927ea8d8-cfa2-4fc0-a91a-adc0ff8a32d1",
    "recipeNumber": 1,
    "title": "1. Rendang Daging Khas Minang (Sumatera Barat)",
    "name": "Rendang Daging Khas Minang",
    "slug": "rendang-daging-khas-minang",
    "scope": "INDONESIA",
    "origin": "Sumatera Barat",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": "https://nbilkbsqdrbtudqdehik.supabase.co/storage/v1/object/public/recipes/rendang-daging-khas-minang.jpg",
    "prepTimeMinutes": 30,
    "cookTimeMinutes": 240,
    "servings": 8,
    "difficulty": "HARD",
    "spicinessLevel": 2,
    "category": {
      "id": "787c88b0-a6ff-4796-af01-1b7713dca77c",
      "name": "Olahan Daging Sapi & Kambing",
      "slug": "daging-sapi-kambing",
      "description": "Hidangan utama berbahan dasar daging sapi, kambing, iga, tetelan, atau jeroan."
    },
    "cuisineType": {
      "id": "2d1b82fa-255e-44ca-873b-554160d5b6c3",
      "name": "Masakan Daerah Tradisional",
      "slug": "masakan-daerah-tradisional",
      "description": "Kuliner otentik warisan budaya berbagai suku bangsa Nusantara."
    },
    "ingredientGroups": [
      {
        "id": "ig-1",
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {
            "id": "ing-1",
            "rawText": "1 kg Daging Sapi (bagian paha/gandik), potong tebal",
            "name": "Daging Sapi",
            "amount": 1,
            "unit": "kg",
            "notes": "bagian paha/gandik, potong tebal",
            "orderIndex": 1
          },
          {
            "id": "ing-2",
            "rawText": "1.5 liter Santan kental dari 3 butir kelapa tua",
            "name": "Santan kental",
            "amount": 1.5,
            "unit": "liter",
            "notes": "dari 3 butir kelapa tua",
            "orderIndex": 2
          }
        ]
      },
      {
        "id": "ig-2",
        "name": "Bumbu Halus",
        "orderIndex": 2,
        "ingredients": [
          {
            "id": "ing-3",
            "rawText": "15 siung Bawang merah",
            "name": "Bawang merah",
            "amount": 15,
            "unit": "siung",
            "notes": null,
            "orderIndex": 1
          }
        ]
      }
    ],
    "steps": [
      {
        "id": "st-1",
        "stepNumber": 1,
        "title": "Memasak Santan & Bumbu Aromatik",
        "instruction": "Rebus santan bersama bumbu halus, serai, daun kunyit, daun jeruk, dan asam kandis hingga mendidih dan mengeluarkan minyak kemerahan.",
        "rawText": "Memasak Santan & Bumbu Aromatik: Rebus santan bersama bumbu halus..."
      },
      {
        "id": "st-2",
        "stepNumber": 2,
        "title": "Memasukkan Daging",
        "instruction": "Masukkan potongan daging sapi, aduk perlahan dengan api sedang hingga kuah menyusut menjadi kalio kental berwarna cokelat muda.",
        "rawText": "Memasukkan Daging: Masukkan potongan daging sapi..."
      }
    ],
    "nutrition": {
      "id": "nut-1",
      "serving": "Per Porsi",
      "calories": 420,
      "protein": 34,
      "fat": 28,
      "carbohydrates": 8,
      "notes": "Kaya zat besi dan asam lemak esensial",
      "rawText": "Nutrisi (Per Porsi): Kalori 420 kkal | Protein 34g | Lemak 28g | Karbohidrat 8g."
    }
  }
}
```

---

### 4.3. Mengambil Format Teks Asli Dokumen (`GET /api/v1/recipes/:idOrSlug/raw`)

Mengembalikan teks mentah asli persis seperti dalam catatan arsip kuliner untuk kebutuhan cetak, rendering artikel gaya teks, atau ekspor data tanpa format parsing.

#### Contoh Permintaan (Request)

```bash
curl -X GET "http://localhost:3000/api/v1/recipes/rendang-daging-khas-minang/raw"
```

#### Contoh Respon (Response)

```json
{
  "statusCode": 200,
  "success": true,
  "message": "Format mentah dokumen berhasil diambil",
  "data": {
    "recipeNumber": 1,
    "title": "1. Rendang Daging Khas Minang (Sumatera Barat)",
    "slug": "rendang-daging-khas-minang",
    "rawContent": "1. Rendang Daging Khas Minang (Sumatera Barat)\nReferensi Visual: Lihat Ilustrasi Masakan\nDeskripsi Bahan Baku:..."
  }
}
```

---

## 5. Rincian Endpoint Taksonomi & Master Data

### 5.1. Kategori Masakan (`GET /api/v1/categories`)

Menampilkan daftar 11 kategori hidangan beserta agregasi jumlah resep di setiap kategori (`recipeCount`).

```bash
curl -X GET "http://localhost:3000/api/v1/categories"
```

#### Nilai Slug Kategori yang Tersedia:
- `daging-sapi-kambing` — Olahan Daging Sapi & Kambing
- `ayam-unggas` — Olahan Ayam & Unggas
- `ikan-seafood` — Olahan Ikan & Hasil Laut
- `sayuran-tumisan` — Aneka Sayuran & Tumisan
- `sup-soto` — Sup, Soto & Masakan Berkuah
- `tahu-tempe-telur` — Olahan Tahu, Tempe & Telur
- `mie-pasta-olahan-tepung` — Mie, Pasta & Olahan Tepung
- `nasi-olahan-beras` — Hidangan Nasi & Olahan Beras
- `kudapan-jajanan-pasar` — Kudapan, Kue & Jajanan Pasar
- `minuman-segar-hangat` — Minuman Segar & Tradisional
- `sambal-saus-kondimen` — Aneka Sambal, Saus & Kondimen Pelengkap

---

### 5.2. Tipe Masakan (`GET /api/v1/cuisine-types`)

Menampilkan daftar klasifikasi budaya penyajian kuliner beserta jumlah resepnya.

```bash
curl -X GET "http://localhost:3000/api/v1/cuisine-types"
```

#### Nilai Slug Tipe Masakan yang Tersedia:
- `masakan-daerah-tradisional` — Masakan Daerah Tradisional Nusantara
- `masakan-rumahan` — Masakan Sehari-hari / Rumahan
- `street-food-kaki-lima` — Street Food & Jajanan Kaki Lima
- `hidangan-hari-raya` — Hidangan Hari Raya & Pesta Adat
- `kudapan-jajanan-pasar` — Kudapan & Jajanan Tradisional
- `minuman-tradisional-segar` — Minuman Tradisional & Pelepas Dahaga
- `masakan-internasional` — Masakan Internasional Populer

---

### 5.3. Asal Daerah / Negara (`GET /api/v1/origins`)

Menampilkan daftar asal wilayah (provinsi di Indonesia atau negara untuk resep internasional) terurut dari jumlah resep terbanyak. Sangat cocok untuk komponen *dropdown* filter atau peta penjelajahan kuliner.

```bash
curl -X GET "http://localhost:3000/api/v1/origins"
```

Contoh respon:
```json
{
  "statusCode": 200,
  "success": true,
  "message": "Daftar asal daerah berhasil diambil",
  "data": [
    { "origin": "Jawa Tengah", "recipeCount": 38 },
    { "origin": "Jawa Timur", "recipeCount": 26 },
    { "origin": "DKI Jakarta", "recipeCount": 21 },
    { "origin": "Sumatera Barat", "recipeCount": 18 },
    { "origin": "Jawa Barat", "recipeCount": 16 },
    { "origin": "DI Yogyakarta", "recipeCount": 12 },
    { "origin": "Jepang", "recipeCount": 5 }
  ]
}
```

---

## 6. Penanganan Aset Visual (`imageUrl`)

Setiap objek resep menyediakan kolom `imageUrl`. 

- **Hosting & Pengiriman**: Berkas gambar di-host pada CDN Supabase Storage publik berkinerja tinggi.
- **Spesifikasi Aset**: Format JPEG dengan optimasi bicubic beresolusi 1080px dan ukuran berkas efisien (~140–200 KB) untuk memastikan kecepatan *rendering* pada jaringan seluler.
- **Cache Browser**: Header cache `cache-control: 31536000` (1 tahun) disematkan otomatis pada CDN.
- **Rekomendasi Frontend**: Jika nilai `imageUrl` bernilai `null` (dalam proses peluncuran bertahap), gunakan gambar cadangan (*placeholder*) di sisi antarmuka pengguna.

Contoh penanganan fallback pada komponen frontend:

```typescript
function RecipeThumbnail({ imageUrl, title }: { imageUrl: string | null; title: string }) {
  const fallbackUrl = '/assets/images/placeholder-recipe.jpg';
  
  return (
    <img
      src={imageUrl || fallbackUrl}
      alt={title}
      loading="lazy"
      width={400}
      height={300}
      className="recipe-card-img"
    />
  );
}
```

---

## 7. Praktik Terbaik Integrasi Frontend & Mobile

1. **Debounce pada Kotak Pencarian**: Terapkan jeda waktu (*debounce*) sekitar 300ms–400ms pada input pencarian pengguna sebelum memanggil endpoint `GET /api/v1/recipes?search=...` untuk menghemat bandwidth dan beban server.
2. **Navigasi Berbasis Slug**: Gunakan field `slug` pada URL rute aplikasi Anda (misal: `/resep/:slug`) untuk hasil pencarian mesin telusur yang optimal (SEO).
3. **Paginasi Halus**: Manfaatkan objek `meta` (`hasNextPage`, `page`, `totalPages`) untuk membangun komponen *infinite scroll* atau penomoran halaman yang informatif.
4. **Caching Klien**: Karena data resep bersifat statis dan jarang berubah secara *real-time*, disarankan mengaktifkan *stale-while-revalidate* (seperti React Query, SWR, atau RTK Query) dengan durasi `staleTime` minimal 10–30 menit.

---

## 8. Kode Status HTTP

API menggunakan kode status HTTP standar:

| Status Code | Makna | Kondisi Terjadinya |
|---|---|---|
| `200 OK` | Berhasil | Permintaan berhasil diproses dan mengembalikan data yang valid. |
| `400 Bad Request` | Permintaan Tidak Valid | Parameter kueri salah tipe (misal `spicinessLevel=abc` atau `page=-1`). |
| `404 Not Found` | Tidak Ditemukan | Resep, kategori, atau tipe masakan dengan ID/slug tersebut tidak ada di sistem. |
| `500 Internal Error` | Kesalahan Server | Terjadi kendala koneksi ke basis data internal. Pesan teknis disembunyikan demi keamanan. |
