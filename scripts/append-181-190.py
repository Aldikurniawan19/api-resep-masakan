import json
import os

new_recipes = [
    {
        "recipeNumber": 181,
        "title": "181. Tempe Mendoan Khas Banyumas (Jawa Tengah)",
        "name": "Tempe Mendoan",
        "slug": "tempe-mendoan-banyumas",
        "scope": "INDONESIA",
        "origin": "Jawa Tengah",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 15,
        "cookTimeMinutes": 15,
        "servings": 5,
        "difficulty": "EASY",
        "spicinessLevel": 1,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "masakan-daerah-tradisional",
        "rawContent": """181. Tempe Mendoan Khas Banyumas (Jawa Tengah)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
10 lembar Tempe mendoan mentah (tipis lebar khas Banyumas, atau tempe papan diiris tipis lebar)
250g Tepung terigu protein sedang
50g Tepung beras (untuk tekstur renyah di tepi)
2 batang Daun bawang (iris tipis halus)
400 ml Air matang dingin
Minyak kelapa sawit secukupnya untuk menggoreng
Bumbu Halus:
5 siung Bawang putih
1 sdm Ketumbar butiran (sangrai)
2 cm Kunyit segar (bakar kupas)
1 cm Kencur (khas aroma mendoan Banyumas)
1 sdt Garam halus
1/2 sdt Kaldu bubuk rasa ayam
Bahan Sambal Kecap Rawit:
5 sdm Kecap manis kental gurih
8 buah Cabai rawit hijau (iris halus)
2 siung Bawang merah (iris tipis)
1/2 sdt Air perasan jeruk limau
Langkah-Langkah Pembuatan:
Membuat Adonan Celupan: Campurkan tepung terigu, tepung beras, dan bumbu halus dalam mangkuk besar. Tuangkan air matang dingin sedikit demi sedikit sambil diaduk dengan whisk hingga adonan licin dan tidak bergerindil. Masukkan irisan daun bawang, aduk rata.
Menyiapkan Sambal Kecap: Campurkan kecap manis, irisan cabai rawit hijau, irisan bawang merah, dan air perasan jeruk limau dalam mangkuk kecil. Aduk rata dan sisihkan sebagai cocolan.
Melumuri Tempe: Celupkan lembaran tempe mendoan satu per satu ke dalam adonan tepung hingga seluruh permukaan tertutup rata.
Menggoreng dengan Teknik Mendo: Panaskan minyak banyak dalam wajan cekung di atas api sedang hingga benar-benar panas. Masukkan tempe yang sudah berlumur adonan. Goreng sebentar saja (sekitar 1-2 menit tiap sisi) hingga tepung matang kenyal namun tidak sampai garing/kering (mendo berarti setengah matang lembek).
Penyajian: Angkat tempe mendoan, tiriskan sejenak di atas kertas minyak. Sajikan hangat-hangat bersama sambal kecap rawit pedas dan cabai rawit utuh.
Nutrisi (Per Porsi 2 Lembar): Kalori 185 kkal | Protein 9g | Lemak 9g | Karbohidrat 18g. Sumber protein nabati berkualitas tinggi dan isoflavon dari kedelai fermentasi, dengan tekstur tepung yang lembut gurih dan minim minyak jenuh bila ditiriskan sempurna.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "10 lembar Tempe mendoan mentah (tipis lebar khas Banyumas)", "amount": 10.0, "unit": "lembar", "name": "Tempe mendoan mentah", "notes": "tipis lebar khas Banyumas", "orderIndex": 1},
                    {"rawText": "250g Tepung terigu protein sedang", "amount": 250.0, "unit": "g", "name": "Tepung terigu protein sedang", "notes": None, "orderIndex": 2},
                    {"rawText": "50g Tepung beras", "amount": 50.0, "unit": "g", "name": "Tepung beras", "notes": "untuk tekstur renyah di tepi", "orderIndex": 3},
                    {"rawText": "2 batang Daun bawang (iris tipis halus)", "amount": 2.0, "unit": "batang", "name": "Daun bawang", "notes": "iris tipis halus", "orderIndex": 4},
                    {"rawText": "400 ml Air matang dingin", "amount": 400.0, "unit": "ml", "name": "Air matang dingin", "notes": None, "orderIndex": 5},
                    {"rawText": "Minyak kelapa sawit secukupnya untuk menggoreng", "amount": None, "unit": "secukupnya", "name": "Minyak kelapa sawit", "notes": "untuk menggoreng", "orderIndex": 6}
                ]
            },
            {
                "name": "Bumbu Halus",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 1},
                    {"rawText": "1 sdm Ketumbar butiran (sangrai)", "amount": 1.0, "unit": "sdm", "name": "Ketumbar butiran", "notes": "sangrai", "orderIndex": 2},
                    {"rawText": "2 cm Kunyit segar (bakar kupas)", "amount": 2.0, "unit": "cm", "name": "Kunyit segar", "notes": "bakar kupas", "orderIndex": 3},
                    {"rawText": "1 cm Kencur", "amount": 1.0, "unit": "cm", "name": "Kencur", "notes": "khas aroma mendoan Banyumas", "orderIndex": 4},
                    {"rawText": "1 sdt Garam halus", "amount": 1.0, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 5},
                    {"rawText": "1/2 sdt Kaldu bubuk rasa ayam", "amount": 0.5, "unit": "sdt", "name": "Kaldu bubuk rasa ayam", "notes": None, "orderIndex": 6}
                ]
            },
            {
                "name": "Bahan Sambal Kecap Rawit",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "5 sdm Kecap manis kental gurih", "amount": 5.0, "unit": "sdm", "name": "Kecap manis", "notes": "kental gurih", "orderIndex": 1},
                    {"rawText": "8 buah Cabai rawit hijau (iris halus)", "amount": 8.0, "unit": "buah", "name": "Cabai rawit hijau", "notes": "iris halus", "orderIndex": 2},
                    {"rawText": "2 siung Bawang merah (iris tipis)", "amount": 2.0, "unit": "siung", "name": "Bawang merah", "notes": "iris tipis", "orderIndex": 3},
                    {"rawText": "1/2 sdt Air perasan jeruk limau", "amount": 0.5, "unit": "sdt", "name": "Air perasan jeruk limau", "notes": None, "orderIndex": 4}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Adonan Celupan", "instruction": "Campurkan tepung terigu, tepung beras, dan bumbu halus dalam mangkuk besar. Tuangkan air matang dingin sedikit demi sedikit sambil diaduk dengan whisk hingga adonan licin dan tidak bergerindil. Masukkan irisan daun bawang, aduk rata.", "rawText": "Membuat Adonan Celupan: Campurkan tepung terigu, tepung beras, dan bumbu halus dalam mangkuk besar. Tuangkan air matang dingin sedikit demi sedikit sambil diaduk dengan whisk hingga adonan licin dan tidak bergerindil. Masukkan irisan daun bawang, aduk rata."},
            {"stepNumber": 2, "title": "Menyiapkan Sambal Kecap", "instruction": "Campurkan kecap manis, irisan cabai rawit hijau, irisan bawang merah, dan air perasan jeruk limau dalam mangkuk kecil. Aduk rata dan sisihkan sebagai cocolan.", "rawText": "Menyiapkan Sambal Kecap: Campurkan kecap manis, irisan cabai rawit hijau, irisan bawang merah, dan air perasan jeruk limau dalam mangkuk kecil. Aduk rata dan sisihkan sebagai cocolan."},
            {"stepNumber": 3, "title": "Melumuri Tempe", "instruction": "Celupkan lembaran tempe mendoan satu per satu ke dalam adonan tepung hingga seluruh permukaan tertutup rata.", "rawText": "Melumuri Tempe: Celupkan lembaran tempe mendoan satu per satu ke dalam adonan tepung hingga seluruh permukaan tertutup rata."},
            {"stepNumber": 4, "title": "Menggoreng dengan Teknik Mendo", "instruction": "Panaskan minyak banyak dalam wajan cekung di atas api sedang hingga benar-benar panas. Masukkan tempe yang sudah berlumur adonan. Goreng sebentar saja (sekitar 1-2 menit tiap sisi) hingga tepung matang kenyal namun tidak sampai garing/kering (mendo berarti setengah matang lembek).", "rawText": "Menggoreng dengan Teknik Mendo: Panaskan minyak banyak dalam wajan cekung di atas api sedang hingga benar-benar panas. Masukkan tempe yang sudah berlumur adonan. Goreng sebentar saja (sekitar 1-2 menit tiap sisi) hingga tepung matang kenyal namun tidak sampai garing/kering (mendo berarti setengah matang lembek)."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Angkat tempe mendoan, tiriskan sejenak di atas kertas minyak. Sajikan hangat-hangat bersama sambal kecap rawit pedas dan cabai rawit utuh.", "rawText": "Penyajian: Angkat tempe mendoan, tiriskan sejenak di atas kertas minyak. Sajikan hangat-hangat bersama sambal kecap rawit pedas dan cabai rawit utuh."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi 2 Lembar): Kalori 185 kkal | Protein 9g | Lemak 9g | Karbohidrat 18g. Sumber protein nabati berkualitas tinggi dan isoflavon dari kedelai fermentasi, dengan tekstur tepung yang lembut gurih dan minim minyak jenuh bila ditiriskan sempurna.",
            "serving": "Per Porsi 2 Lembar",
            "calories": 185,
            "protein": 9.0,
            "fat": 9.0,
            "carbohydrates": 18.0,
            "notes": "Sumber protein nabati berkualitas tinggi dan isoflavon dari kedelai fermentasi, dengan tekstur tepung yang lembut gurih dan minim minyak jenuh bila ditiriskan sempurna."
        }
    },
    {
        "recipeNumber": 182,
        "title": "182. Batagor Bandung (Jawa Barat)",
        "name": "Batagor Bandung",
        "slug": "batagor-bandung",
        "scope": "INDONESIA",
        "origin": "Jawa Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 30,
        "cookTimeMinutes": 25,
        "servings": 4,
        "difficulty": "MEDIUM",
        "spicinessLevel": 2,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "street-food-kaki-lima",
        "rawContent": """182. Batagor Bandung (Jawa Barat)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama Tahu & Kulit Pangsit:
5 buah Tahu putih kotak (potong segitiga, belah tengah untuk isian)
10 lembar Kulit pangsit goreng siap pakai
Minyak goreng secukupnya untuk deep fry
Bahan Adonan Siomay / Isian:
300g Daging ikan tenggiri fillet (giling halus dingin)
100g Daging paha ayam fillet (giling halus)
150g Tepung tapioka / sagu tani berkualitas
2 butir Putih telur dingin
3 batang Daun bawang (iris halus)
4 siung Bawang putih (haluskan)
1 sdm Minyak wijen
1 sdt Kecap asin
1 sdt Garam
1 sdt Gula pasir
1/2 sdt Merica putih bubuk
100 ml Air es dingin
Bahan Saus Bumbu Kacang:
200g Kacang tanah (goreng matang, haluskan)
5 buah Cabai merah keriting
5 buah Cabai rawit merah
4 siung Bawang putih
3 butir Bawang merah
60g Gula aren / gula merah (sisir halus)
1 sdm Air asam jawa kental
1 sdt Garam
500 ml Air matang
Bahan Pelengkap:
2 buah Jeruk limau (belah dua)
Kecap manis secukupnya
Saus sambal secukupnya
Langkah-Langkah Pembuatan:
Membuat Adonan Isian Ikan: Campurkan ikan tenggiri giling, ayam giling, bawang putih halus, putih telur, minyak wijen, kecap asin, garam, gula, dan merica dalam wadah. Uleni sambil menuangkan air es dingin sedikit demi sedikit hingga adonan kalis dan kenyal. Tambahkan tepung tapioka dan daun bawang, aduk perlahan dengan spatula hingga rata (jangan terlalu lama diuleni agar tidak liat).
Mengisi Tahu dan Kulit Pangsit: Ambil potongan tahu putih segitiga, isi rongga tengahnya dengan 1 sendok makan adonan ikan hingga padat. Ambil 1 lembar kulit pangsit, letakkan 1 sendok makan adonan ikan di tengahnya, lalu satukan ujung-ujungnya ke atas seperti bunga menguncup.
Menggoreng Batagor: Panaskan minyak banyak dalam wajan dengan api sedang cenderung kecil. Masukkan tahu dan pangsit isi perlahan. Goreng hingga matang merata, mengapung, dan berwarna kuning kecokelatan keemasan yang renyah. Angkat dan tiriskan.
Membuat Saus Kacang: Haluskan cabai keriting, cabai rawit, bawang putih, dan bawang merah. Tumis dengan 3 sendok makan minyak hingga harum dan matang. Masukkan kacang tanah halus, air, gula aren, air asam jawa, dan garam. Masak di atas api kecil sambil terus diaduk hingga kuah kacang mengental dan mengeluarkan minyak kemerahan alami.
Penyajian: Potong-potong batagor tahu dan siomay goreng renyah ke dalam piring saji. Siram dengan saus kacang gurih kental hangat, tambahkan kucuran kecap manis, perasan jeruk limau, dan saus sambal sesuai selera.
Nutrisi (Per Porsi 3 Potong): Kalori 380 kkal | Protein 22g | Lemak 18g | Karbohidrat 34g. Kaya akan asam lemak omega-3 dan protein berkualitas tinggi dari ikan tenggiri segar, dilengkapi vitamin E dan lemak tak jenuh ganda dari saus kacang tanah.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama Tahu & Kulit Pangsit",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "5 buah Tahu putih kotak (potong segitiga, belah tengah)", "amount": 5.0, "unit": "buah", "name": "Tahu putih kotak", "notes": "potong segitiga, belah tengah", "orderIndex": 1},
                    {"rawText": "10 lembar Kulit pangsit goreng siap pakai", "amount": 10.0, "unit": "lembar", "name": "Kulit pangsit goreng", "notes": "siap pakai", "orderIndex": 2},
                    {"rawText": "Minyak goreng secukupnya untuk deep fry", "amount": None, "unit": "secukupnya", "name": "Minyak goreng", "notes": "untuk deep fry", "orderIndex": 3}
                ]
            },
            {
                "name": "Bahan Adonan Siomay / Isian",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "300g Daging ikan tenggiri fillet (giling halus dingin)", "amount": 300.0, "unit": "g", "name": "Daging ikan tenggiri fillet", "notes": "giling halus dingin", "orderIndex": 1},
                    {"rawText": "100g Daging paha ayam fillet (giling halus)", "amount": 100.0, "unit": "g", "name": "Daging paha ayam fillet", "notes": "giling halus", "orderIndex": 2},
                    {"rawText": "150g Tepung tapioka / sagu tani", "amount": 150.0, "unit": "g", "name": "Tepung tapioka", "notes": "atau sagu tani", "orderIndex": 3},
                    {"rawText": "2 butir Putih telur dingin", "amount": 2.0, "unit": "butir", "name": "Putih telur", "notes": "dingin", "orderIndex": 4},
                    {"rawText": "3 batang Daun bawang (iris halus)", "amount": 3.0, "unit": "batang", "name": "Daun bawang", "notes": "iris halus", "orderIndex": 5},
                    {"rawText": "4 siung Bawang putih (haluskan)", "amount": 4.0, "unit": "siung", "name": "Bawang putih", "notes": "haluskan", "orderIndex": 6},
                    {"rawText": "1 sdm Minyak wijen", "amount": 1.0, "unit": "sdm", "name": "Minyak wijen", "notes": None, "orderIndex": 7},
                    {"rawText": "1 sdt Kecap asin", "amount": 1.0, "unit": "sdt", "name": "Kecap asin", "notes": None, "orderIndex": 8},
                    {"rawText": "1 sdt Garam", "amount": 1.0, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 9},
                    {"rawText": "1 sdt Gula pasir", "amount": 1.0, "unit": "sdt", "name": "Gula pasir", "notes": None, "orderIndex": 10},
                    {"rawText": "1/2 sdt Merica putih bubuk", "amount": 0.5, "unit": "sdt", "name": "Merica putih bubuk", "notes": None, "orderIndex": 11},
                    {"rawText": "100 ml Air es dingin", "amount": 100.0, "unit": "ml", "name": "Air es dingin", "notes": None, "orderIndex": 12}
                ]
            },
            {
                "name": "Bahan Saus Bumbu Kacang",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "200g Kacang tanah (goreng matang, haluskan)", "amount": 200.0, "unit": "g", "name": "Kacang tanah", "notes": "goreng matang, haluskan", "orderIndex": 1},
                    {"rawText": "5 buah Cabai merah keriting", "amount": 5.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 2},
                    {"rawText": "5 buah Cabai rawit merah", "amount": 5.0, "unit": "buah", "name": "Cabai rawit merah", "notes": None, "orderIndex": 3},
                    {"rawText": "4 siung Bawang putih", "amount": 4.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 4},
                    {"rawText": "3 butir Bawang merah", "amount": 3.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 5},
                    {"rawText": "60g Gula aren / gula merah (sisir halus)", "amount": 60.0, "unit": "g", "name": "Gula aren", "notes": "sisir halus", "orderIndex": 6},
                    {"rawText": "1 sdm Air asam jawa kental", "amount": 1.0, "unit": "sdm", "name": "Air asam jawa kental", "notes": None, "orderIndex": 7},
                    {"rawText": "1 sdt Garam", "amount": 1.0, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 8},
                    {"rawText": "500 ml Air matang", "amount": 500.0, "unit": "ml", "name": "Air matang", "notes": None, "orderIndex": 9}
                ]
            },
            {
                "name": "Bahan Pelengkap",
                "orderIndex": 4,
                "ingredients": [
                    {"rawText": "2 buah Jeruk limau (belah dua)", "amount": 2.0, "unit": "buah", "name": "Jeruk limau", "notes": "belah dua", "orderIndex": 1},
                    {"rawText": "Kecap manis secukupnya", "amount": None, "unit": "secukupnya", "name": "Kecap manis", "notes": None, "orderIndex": 2},
                    {"rawText": "Saus sambal secukupnya", "amount": None, "unit": "secukupnya", "name": "Saus sambal", "notes": None, "orderIndex": 3}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Adonan Isian Ikan", "instruction": "Campurkan ikan tenggiri giling, ayam giling, bawang putih halus, putih telur, minyak wijen, kecap asin, garam, gula, dan merica dalam wadah. Uleni sambil menuangkan air es dingin sedikit demi sedikit hingga adonan kalis dan kenyal. Tambahkan tepung tapioka dan daun bawang, aduk perlahan dengan spatula hingga rata.", "rawText": "Membuat Adonan Isian Ikan: Campurkan ikan tenggiri giling, ayam giling, bawang putih halus, putih telur, minyak wijen, kecap asin, garam, gula, dan merica dalam wadah. Uleni sambil menuangkan air es dingin sedikit demi sedikit hingga adonan kalis dan kenyal. Tambahkan tepung tapioka dan daun bawang, aduk perlahan dengan spatula hingga rata."},
            {"stepNumber": 2, "title": "Mengisi Tahu dan Kulit Pangsit", "instruction": "Ambil potongan tahu putih segitiga, isi rongga tengahnya dengan 1 sendok makan adonan ikan hingga padat. Ambil 1 lembar kulit pangsit, letakkan 1 sendok makan adonan ikan di tengahnya, lalu satukan ujung-ujungnya ke atas seperti bunga menguncup.", "rawText": "Mengisi Tahu dan Kulit Pangsit: Ambil potongan tahu putih segitiga, isi rongga tengahnya dengan 1 sendok makan adonan ikan hingga padat. Ambil 1 lembar kulit pangsit, letakkan 1 sendok makan adonan ikan di tengahnya, lalu satukan ujung-ujungnya ke atas seperti bunga menguncup."},
            {"stepNumber": 3, "title": "Menggoreng Batagor", "instruction": "Panaskan minyak banyak dalam wajan dengan api sedang cenderung kecil. Masukkan tahu dan pangsit isi perlahan. Goreng hingga matang merata, mengapung, dan berwarna kuning kecokelatan keemasan yang renyah. Angkat dan tiriskan.", "rawText": "Menggoreng Batagor: Panaskan minyak banyak dalam wajan dengan api sedang cenderung kecil. Masukkan tahu dan pangsit isi perlahan. Goreng hingga matang merata, mengapung, dan berwarna kuning kecokelatan keemasan yang renyah. Angkat dan tiriskan."},
            {"stepNumber": 4, "title": "Membuat Saus Kacang", "instruction": "Haluskan cabai keriting, cabai rawit, bawang putih, dan bawang merah. Tumis dengan 3 sendok makan minyak hingga harum dan matang. Masukkan kacang tanah halus, air, gula aren, air asam jawa, dan garam. Masak di atas api kecil sambil terus diaduk hingga kuah kacang mengental dan mengeluarkan minyak kemerahan alami.", "rawText": "Membuat Saus Kacang: Haluskan cabai keriting, cabai rawit, bawang putih, dan bawang merah. Tumis dengan 3 sendok makan minyak hingga harum dan matang. Masukkan kacang tanah halus, air, gula aren, air asam jawa, dan garam. Masak di atas api kecil sambil terus diaduk hingga kuah kacang mengental dan mengeluarkan minyak kemerahan alami."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Potong-potong batagor tahu dan siomay goreng renyah ke dalam piring saji. Siram dengan saus kacang gurih kental hangat, tambahkan kucuran kecap manis, perasan jeruk limau, dan saus sambal sesuai selera.", "rawText": "Penyajian: Potong-potong batagor tahu dan siomay goreng renyah ke dalam piring saji. Siram dengan saus kacang gurih kental hangat, tambahkan kucuran kecap manis, perasan jeruk limau, dan saus sambal sesuai selera."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi 3 Potong): Kalori 380 kkal | Protein 22g | Lemak 18g | Karbohidrat 34g. Kaya akan asam lemak omega-3 dan protein berkualitas tinggi dari ikan tenggiri segar, dilengkapi vitamin E dan lemak tak jenuh ganda dari saus kacang tanah.",
            "serving": "Per Porsi 3 Potong",
            "calories": 380,
            "protein": 22.0,
            "fat": 18.0,
            "carbohydrates": 34.0,
            "notes": "Kaya akan asam lemak omega-3 dan protein berkualitas tinggi dari ikan tenggiri segar, dilengkapi vitamin E dan lemak tak jenuh ganda dari saus kacang tanah."
        }
    },
    {
        "recipeNumber": 183,
        "title": "183. Tahu Telur Bumbu Petis Khas Surabaya (Jawa Timur)",
        "name": "Tahu Telur Bumbu Petis Surabaya",
        "slug": "tahu-telur-surabaya",
        "scope": "INDONESIA",
        "origin": "Jawa Timur",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 15,
        "servings": 3,
        "difficulty": "EASY",
        "spicinessLevel": 2,
        "categorySlug": "lauk-utama-nusantara",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """183. Tahu Telur Bumbu Petis Khas Surabaya (Jawa Timur)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Dadar Tahu Telur:
300g Tahu putih lembut (potong dadu kecil 1.5 cm)
4 butir Telur ayam ukuran besar
2 batang Daun bawang (iris halus)
1/2 sdt Garam halus
1/4 sdt Merica bubuk
Minyak goreng secukupnya untuk menggoreng dadar
Bahan Bumbu Petis Khas Jawa Timur:
3 sdm Petis udang hitam khas Sidoarjo (berkualitas, harum gurih)
3 siung Bawang putih (goreng utuh sebentar)
6 buah Cabai rawit hijau (sesuai selera pedas)
3 sdm Kacang tanah goreng (haluskan)
3 sdm Kecap manis kental gurih
1 sdm Air asam jawa encer
75 ml Air matang hangat
1/2 sdt Garam
Bahan Pelengkap:
100g Tauge pendek atau tauge panjang (seduh air panas sebentar, tiriskan)
1 batang Seledri (iris halus)
2 sdm Bawang merah goreng
Kerupuk bawang atau emping goreng secukupnya
Langkah-Langkah Pembuatan:
Menyiapkan Bumbu Petis: Di atas cobek batu, ulek bawang putih goreng, cabai rawit hijau, dan garam hingga lumat. Masukkan petis udang dan kacang tanah goreng halus, ulek hingga menyatu. Tambahkan kecap manis, air asam jawa, dan air matang hangat secara bertahap sambil diaduk rata dengan ulekan hingga saus bumbu petis licin, kental, dan hitam mengilap.
Membuat Adonan Tahu Telur: Kocok lepas telur ayam bersama irisan daun bawang, garam, dan merica bubuk dalam mangkuk. Masukkan potongan tahu putih dadu, aduk perlahan agar tahu tidak hancur.
Menggoreng Dadar Tahu Telur: Panaskan minyak goreng yang cukup banyak dalam wajan cekung hingga benar-benar panas. Tuang adonan tahu telur. Goreng dengan api sedang hingga bagian bawah kecokelatan dan kokoh, lalu balik hati-hati. Goreng hingga kedua sisi berkulit renyah keemasan namun bagian dalam tahu tetap lembut basah. Angkat dan tiriskan.
Penyajian: Letakkan dadar tahu telur panas di atas piring saji. Susun tauge seduh segar di atasnya. Siramkan saus bumbu petis gurih hitam secara merata ke seluruh permukaan. Taburi irisan daun seledri segar dan bawang merah goreng renyah. Sajikan segera bersama kerupuk bawang.
Nutrisi (Per Porsi): Kalori 310 kkal | Protein 20g | Lemak 16g | Karbohidrat 22g. Kombinasi protein nabati dan hewani yang seimbang dari tahu kedelai dan telur, diperkaya mineral seng dan zat besi dari petis udang serta serat dari tauge segar.""",
        "ingredientGroups": [
            {
                "name": "Bahan Dadar Tahu Telur",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "300g Tahu putih lembut (potong dadu kecil 1.5 cm)", "amount": 300.0, "unit": "g", "name": "Tahu putih lembut", "notes": "potong dadu kecil 1.5 cm", "orderIndex": 1},
                    {"rawText": "4 butir Telur ayam ukuran besar", "amount": 4.0, "unit": "butir", "name": "Telur ayam", "notes": "ukuran besar", "orderIndex": 2},
                    {"rawText": "2 batang Daun bawang (iris halus)", "amount": 2.0, "unit": "batang", "name": "Daun bawang", "notes": "iris halus", "orderIndex": 3},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 4},
                    {"rawText": "1/4 sdt Merica bubuk", "amount": 0.25, "unit": "sdt", "name": "Merica bubuk", "notes": None, "orderIndex": 5},
                    {"rawText": "Minyak goreng secukupnya", "amount": None, "unit": "secukupnya", "name": "Minyak goreng", "notes": "untuk menggoreng dadar", "orderIndex": 6}
                ]
            },
            {
                "name": "Bahan Bumbu Petis Khas Jawa Timur",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "3 sdm Petis udang hitam khas Sidoarjo", "amount": 3.0, "unit": "sdm", "name": "Petis udang hitam khas Sidoarjo", "notes": "harum gurih", "orderIndex": 1},
                    {"rawText": "3 siung Bawang putih (goreng utuh sebentar)", "amount": 3.0, "unit": "siung", "name": "Bawang putih", "notes": "goreng utuh sebentar", "orderIndex": 2},
                    {"rawText": "6 buah Cabai rawit hijau", "amount": 6.0, "unit": "buah", "name": "Cabai rawit hijau", "notes": "sesuai selera pedas", "orderIndex": 3},
                    {"rawText": "3 sdm Kacang tanah goreng (haluskan)", "amount": 3.0, "unit": "sdm", "name": "Kacang tanah goreng", "notes": "haluskan", "orderIndex": 4},
                    {"rawText": "3 sdm Kecap manis kental gurih", "amount": 3.0, "unit": "sdm", "name": "Kecap manis", "notes": "kental gurih", "orderIndex": 5},
                    {"rawText": "1 sdm Air asam jawa encer", "amount": 1.0, "unit": "sdm", "name": "Air asam jawa encer", "notes": None, "orderIndex": 6},
                    {"rawText": "75 ml Air matang hangat", "amount": 75.0, "unit": "ml", "name": "Air matang hangat", "notes": None, "orderIndex": 7},
                    {"rawText": "1/2 sdt Garam", "amount": 0.5, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 8}
                ]
            },
            {
                "name": "Bahan Pelengkap",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "100g Tauge (seduh air panas sebentar, tiriskan)", "amount": 100.0, "unit": "g", "name": "Tauge", "notes": "seduh air panas sebentar, tiriskan", "orderIndex": 1},
                    {"rawText": "1 batang Seledri (iris halus)", "amount": 1.0, "unit": "batang", "name": "Seledri", "notes": "iris halus", "orderIndex": 2},
                    {"rawText": "2 sdm Bawang merah goreng", "amount": 2.0, "unit": "sdm", "name": "Bawang merah goreng", "notes": None, "orderIndex": 3},
                    {"rawText": "Kerupuk bawang atau emping goreng secukupnya", "amount": None, "unit": "secukupnya", "name": "Kerupuk bawang atau emping", "notes": None, "orderIndex": 4}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menyiapkan Bumbu Petis", "instruction": "Di atas cobek batu, ulek bawang putih goreng, cabai rawit hijau, dan garam hingga lumat. Masukkan petis udang dan kacang tanah goreng halus, ulek hingga menyatu. Tambahkan kecap manis, air asam jawa, dan air matang hangat secara bertahap sambil diaduk rata dengan ulekan hingga saus bumbu petis licin, kental, dan hitam mengilap.", "rawText": "Menyiapkan Bumbu Petis: Di atas cobek batu, ulek bawang putih goreng, cabai rawit hijau, dan garam hingga lumat. Masukkan petis udang dan kacang tanah goreng halus, ulek hingga menyatu. Tambahkan kecap manis, air asam jawa, dan air matang hangat secara bertahap sambil diaduk rata dengan ulekan hingga saus bumbu petis licin, kental, dan hitam mengilap."},
            {"stepNumber": 2, "title": "Membuat Adonan Tahu Telur", "instruction": "Kocok lepas telur ayam bersama irisan daun bawang, garam, dan merica bubuk dalam mangkuk. Masukkan potongan tahu putih dadu, aduk perlahan agar tahu tidak hancur.", "rawText": "Membuat Adonan Tahu Telur: Kocok lepas telur ayam bersama irisan daun bawang, garam, dan merica bubuk dalam mangkuk. Masukkan potongan tahu putih dadu, aduk perlahan agar tahu tidak hancur."},
            {"stepNumber": 3, "title": "Menggoreng Dadar Tahu Telur", "instruction": "Panaskan minyak goreng yang cukup banyak dalam wajan cekung hingga benar-benar panas. Tuang adonan tahu telur. Goreng dengan api sedang hingga bagian bawah kecokelatan dan kokoh, lalu balik hati-hati. Goreng hingga kedua sisi berkulit renyah keemasan namun bagian dalam tahu tetap lembut basah. Angkat dan tiriskan.", "rawText": "Menggoreng Dadar Tahu Telur: Panaskan minyak goreng yang cukup banyak dalam wajan cekung hingga benar-benar panas. Tuang adonan tahu telur. Goreng dengan api sedang hingga bagian bawah kecokelatan dan kokoh, lalu balik hati-hati. Goreng hingga kedua sisi berkulit renyah keemasan namun bagian dalam tahu tetap lembut basah. Angkat dan tiriskan."},
            {"stepNumber": 4, "title": "Penyajian", "instruction": "Letakkan dadar tahu telur panas di atas piring saji. Susun tauge seduh segar di atasnya. Siramkan saus bumbu petis gurih hitam secara merata ke seluruh permukaan. Taburi irisan daun seledri segar dan bawang merah goreng renyah. Sajikan segera bersama kerupuk bawang.", "rawText": "Penyajian: Letakkan dadar tahu telur panas di atas piring saji. Susun tauge seduh segar di atasnya. Siramkan saus bumbu petis gurih hitam secara merata ke seluruh permukaan. Taburi irisan daun seledri segar dan bawang merah goreng renyah. Sajikan segera bersama kerupuk bawang."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 310 kkal | Protein 20g | Lemak 16g | Karbohidrat 22g. Kombinasi protein nabati dan hewani yang seimbang dari tahu kedelai dan telur, diperkaya mineral seng dan zat besi dari petis udang serta serat dari tauge segar.",
            "serving": "Per Porsi",
            "calories": 310,
            "protein": 20.0,
            "fat": 16.0,
            "carbohydrates": 22.0,
            "notes": "Kombinasi protein nabati dan hewani yang seimbang dari tahu kedelai dan telur, diperkaya mineral seng dan zat besi dari petis udang serta serat dari tauge segar."
        }
    },
    {
        "recipeNumber": 184,
        "title": "184. Pindang Bandeng Khas Betawi (DKI Jakarta)",
        "name": "Pindang Bandeng Betawi",
        "slug": "pindang-bandeng-betawi",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 25,
        "cookTimeMinutes": 60,
        "servings": 4,
        "difficulty": "MEDIUM",
        "spicinessLevel": 1,
        "categorySlug": "ikan-seafood",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """184. Pindang Bandeng Khas Betawi (DKI Jakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
2 ekor Ikan bandeng segar (kurang lebih 800g - 1 kg, bersihkan sisik dan insang, potong masing-masing jadi 3-4 bagian)
1 buah Jeruk nipis (peras airnya untuk melumuri ikan)
1.2 liter Air bersih
Bumbu Bakar Aromatik Khas Betawi:
8 butir Bawang merah (bakar utuh beserta kulit tipisnya, lalu kupas)
5 siung Bawang putih (bakar utuh, kupas)
4 cm Kunyit segar (bakar kupas, memarkan)
4 cm Jahe (bakar kupas, memarkan)
Bumbu Kuah Pindang:
3 cm Lengkuas (memarkan)
2 batang Serai (memarkan)
4 lembar Daun salam kering
10 buah Cabai rawit merah utuh (biarkan utuh)
5 buah Belimbing wuluh (belah dua membujur)
2 buah Tomat hijau (potong-potong)
6 sdm Kecap manis kental hitam berkualitas
2 sdm Gula aren / gula merah Betawi (sisir)
2 sdm Air asam jawa kental
1.5 sdt Garam halus
1/2 sdt Kaldu jamur / penyedap rasa
Langkah-Langkah Pembuatan:
Persiapan Ikan: Cuci bersih potongan ikan bandeng, buang lapisan hitam di dinding dalam perut ikan agar tidak amis atau pahit. Lumuri dengan perasan air jeruk nipis dan sedikit garam, diamkan selama 15 menit, lalu bilas bersih dan tiriskan.
Membakar Bumbu Aromatik: Bakar bawang merah, bawang putih, kunyit, dan jahe di atas wajan teflon atau arang hingga mengeluarkan aroma harum khas terpanggang dan sedikit bercak kehitaman. Memarkan bumbu bakar tersebut.
Memasak Kuah Pindang: Didihkan 1.2 liter air dalam panci atau kuali tanah liat. Masukkan bumbu bakar yang sudah dimemarkan, lengkuas, serai, dan daun salam. Masak dengan api sedang hingga aroma rempah keluar semerbak (sekitar 7-10 menit).
Membumbui Kuah: Tambahkan kecap manis, gula aren sisir, air asam jawa, garam, dan kaldu jamur. Aduk rata hingga kuah berubah warna menjadi cokelat kehitaman yang pekat dan harum. Cicipi untuk memastikan perpaduan rasa manis, gurih, dan asam segar seimbang.
Memasak Bandeng Perlahan (Slow Cook): Masukkan potongan ikan bandeng ke dalam kuah mendidih secara perlahan. Kecilkan api ke tingkat minimal. Tutup panci dan masak perlahan selama 45-60 menit agar bumbu kecap dan asam meresap ke dalam serat daging bandeng hingga kecokelatan tanpa membuat daging ikan hancur.
Penyelesaian: 10 menit sebelum diangkat, masukkan cabai rawit merah utuh, potongan belimbing wuluh, dan tomat hijau. Masak sebentar hingga layu dan mengeluarkan aroma segar.
Penyajian: Angkat potongan ikan bandeng dengan spatula lebar ke dalam mangkuk saji saji, tuangkan kuah pindang bening cokelat pekat beserta cabai rawit dan belimbing wuluh. Sajikan hangat bersama nasi putih pulen.
Nutrisi (Per Porsi): Kalori 260 kkal | Protein 28g | Lemak 9g | Karbohidrat 17g. Ikan bandeng kaya akan asam lemak tak jenuh ganda (EPA dan DHA) yang sangat baik untuk fungsi kardiovaskular dan otak, dipadukan antioksidan alami kurkumin dan vitamin C dari belimbing wuluh.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "2 ekor Ikan bandeng segar (kurang lebih 800g - 1 kg, potong 3-4 bagian)", "amount": 2.0, "unit": "ekor", "name": "Ikan bandeng segar", "notes": "800g - 1 kg, potong 3-4 bagian", "orderIndex": 1},
                    {"rawText": "1 buah Jeruk nipis (peras airnya)", "amount": 1.0, "unit": "buah", "name": "Jeruk nipis", "notes": "peras airnya", "orderIndex": 2},
                    {"rawText": "1.2 liter Air bersih", "amount": 1.2, "unit": "liter", "name": "Air bersih", "notes": None, "orderIndex": 3}
                ]
            },
            {
                "name": "Bumbu Bakar Aromatik Khas Betawi",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "8 butir Bawang merah (bakar utuh, kupas)", "amount": 8.0, "unit": "butir", "name": "Bawang merah", "notes": "bakar utuh, kupas", "orderIndex": 1},
                    {"rawText": "5 siung Bawang putih (bakar utuh, kupas)", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": "bakar utuh, kupas", "orderIndex": 2},
                    {"rawText": "4 cm Kunyit segar (bakar kupas, memarkan)", "amount": 4.0, "unit": "cm", "name": "Kunyit segar", "notes": "bakar kupas, memarkan", "orderIndex": 3},
                    {"rawText": "4 cm Jahe (bakar kupas, memarkan)", "amount": 4.0, "unit": "cm", "name": "Jahe", "notes": "bakar kupas, memarkan", "orderIndex": 4}
                ]
            },
            {
                "name": "Bumbu Kuah Pindang",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "3 cm Lengkuas (memarkan)", "amount": 3.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 1},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 2},
                    {"rawText": "4 lembar Daun salam kering", "amount": 4.0, "unit": "lembar", "name": "Daun salam kering", "notes": None, "orderIndex": 3},
                    {"rawText": "10 buah Cabai rawit merah utuh", "amount": 10.0, "unit": "buah", "name": "Cabai rawit merah", "notes": "biarkan utuh", "orderIndex": 4},
                    {"rawText": "5 buah Belimbing wuluh (belah dua membujur)", "amount": 5.0, "unit": "buah", "name": "Belimbing wuluh", "notes": "belah dua membujur", "orderIndex": 5},
                    {"rawText": "2 buah Tomat hijau (potong-potong)", "amount": 2.0, "unit": "buah", "name": "Tomat hijau", "notes": "potong-potong", "orderIndex": 6},
                    {"rawText": "6 sdm Kecap manis kental hitam berkualitas", "amount": 6.0, "unit": "sdm", "name": "Kecap manis", "notes": "kental hitam berkualitas", "orderIndex": 7},
                    {"rawText": "2 sdm Gula aren / gula merah Betawi (sisir)", "amount": 2.0, "unit": "sdm", "name": "Gula aren", "notes": "sisir", "orderIndex": 8},
                    {"rawText": "2 sdm Air asam jawa kental", "amount": 2.0, "unit": "sdm", "name": "Air asam jawa kental", "notes": None, "orderIndex": 9},
                    {"rawText": "1.5 sdt Garam halus", "amount": 1.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 10},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 11}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Persiapan Ikan", "instruction": "Cuci bersih potongan ikan bandeng, buang lapisan hitam di dinding dalam perut ikan agar tidak amis atau pahit. Lumuri dengan perasan air jeruk nipis dan sedikit garam, diamkan selama 15 menit, lalu bilas bersih dan tiriskan.", "rawText": "Persiapan Ikan: Cuci bersih potongan ikan bandeng, buang lapisan hitam di dinding dalam perut ikan agar tidak amis atau pahit. Lumuri dengan perasan air jeruk nipis dan sedikit garam, diamkan selama 15 menit, lalu bilas bersih dan tiriskan."},
            {"stepNumber": 2, "title": "Membakar Bumbu Aromatik", "instruction": "Bakar bawang merah, bawang putih, kunyit, dan jahe di atas wajan teflon atau arang hingga mengeluarkan aroma harum khas terpanggang dan sedikit bercak kehitaman. Memarkan bumbu bakar tersebut.", "rawText": "Membakar Bumbu Aromatik: Bakar bawang merah, bawang putih, kunyit, dan jahe di atas wajan teflon atau arang hingga mengeluarkan aroma harum khas terpanggang dan sedikit bercak kehitaman. Memarkan bumbu bakar tersebut."},
            {"stepNumber": 3, "title": "Memasak Kuah Pindang", "instruction": "Didihkan 1.2 liter air dalam panci atau kuali tanah liat. Masukkan bumbu bakar yang sudah dimemarkan, lengkuas, serai, dan daun salam. Masak dengan api sedang hingga aroma rempah keluar semerbak (sekitar 7-10 menit).", "rawText": "Memasak Kuah Pindang: Didihkan 1.2 liter air dalam panci atau kuali tanah liat. Masukkan bumbu bakar yang sudah dimemarkan, lengkuas, serai, dan daun salam. Masak dengan api sedang hingga aroma rempah keluar semerbak (sekitar 7-10 menit)."},
            {"stepNumber": 4, "title": "Membumbui Kuah", "instruction": "Tambahkan kecap manis, gula aren sisir, air asam jawa, garam, dan kaldu jamur. Aduk rata hingga kuah berubah warna menjadi cokelat kehitaman yang pekat dan harum. Cicipi untuk memastikan perpaduan rasa manis, gurih, dan asam segar seimbang.", "rawText": "Membumbui Kuah: Tambahkan kecap manis, gula aren sisir, air asam jawa, garam, dan kaldu jamur. Aduk rata hingga kuah berubah warna menjadi cokelat kehitaman yang pekat dan harum. Cicipi untuk memastikan perpaduan rasa manis, gurih, dan asam segar seimbang."},
            {"stepNumber": 5, "title": "Memasak Bandeng Perlahan (Slow Cook)", "instruction": "Masukkan potongan ikan bandeng ke dalam kuah mendidih secara perlahan. Kecilkan api ke tingkat minimal. Tutup panci dan masak perlahan selama 45-60 menit agar bumbu kecap dan asam meresap ke dalam serat daging bandeng hingga kecokelatan tanpa membuat daging ikan hancur.", "rawText": "Memasak Bandeng Perlahan (Slow Cook): Masukkan potongan ikan bandeng ke dalam kuah mendidih secara perlahan. Kecilkan api ke tingkat minimal. Tutup panci dan masak perlahan selama 45-60 menit agar bumbu kecap dan asam meresap ke dalam serat daging bandeng hingga kecokelatan tanpa membuat daging ikan hancur."},
            {"stepNumber": 6, "title": "Penyelesaian dan Penyajian", "instruction": "10 menit sebelum diangkat, masukkan cabai rawit merah utuh, potongan belimbing wuluh, dan tomat hijau. Masak sebentar hingga layu dan mengeluarkan aroma segar. Angkat potongan ikan bandeng ke dalam mangkuk saji, tuangkan kuah pindang bening cokelat pekat beserta cabai rawit dan belimbing wuluh. Sajikan hangat.", "rawText": "Penyelesaian dan Penyajian: 10 menit sebelum diangkat, masukkan cabai rawit merah utuh, potongan belimbing wuluh, dan tomat hijau. Masak sebentar hingga layu dan mengeluarkan aroma segar. Angkat potongan ikan bandeng ke dalam mangkuk saji, tuangkan kuah pindang bening cokelat pekat beserta cabai rawit dan belimbing wuluh. Sajikan hangat."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 260 kkal | Protein 28g | Lemak 9g | Karbohidrat 17g. Ikan bandeng kaya akan asam lemak tak jenuh ganda (EPA dan DHA) yang sangat baik untuk fungsi kardiovaskular dan otak, dipadukan antioksidan alami kurkumin dan vitamin C dari belimbing wuluh.",
            "serving": "Per Porsi",
            "calories": 260,
            "protein": 28.0,
            "fat": 9.0,
            "carbohydrates": 17.0,
            "notes": "Ikan bandeng kaya akan asam lemak tak jenuh ganda (EPA dan DHA) yang sangat baik untuk fungsi kardiovaskular dan otak, dipadukan antioksidan alami kurkumin dan vitamin C dari belimbing wuluh."
        }
    },
    {
        "recipeNumber": 185,
        "title": "185. Lumpia Basah Khas Bandung (Jawa Barat)",
        "name": "Lumpia Basah Bandung",
        "slug": "lumpia-basah-bandung",
        "scope": "INDONESIA",
        "origin": "Jawa Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 20,
        "servings": 3,
        "difficulty": "EASY",
        "spicinessLevel": 1,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "street-food-kaki-lima",
        "rawContent": """185. Lumpia Basah Khas Bandung (Jawa Barat)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
6 lembar Kulit lumpia basah siap pakai (lembaran tipis elastis)
200g Tauge segar (buang ekornya, cuci bersih)
2 butir Telur ayam (kocok lepas)
2 batang Daun bawang (iris halus)
3 sdm Minyak goreng untuk menumis
Bahan Olahan Bengkuang Manis:
300g Bengkuang (kupas, potong bentuk korek api tipis)
70g Gula merah aren (sisir halus)
1 sdm Kecap manis
300 ml Air bersih
1/2 sdt Garam
Bahan Saus Perekat Kental Gula Merah:
100g Gula merah aren berkualitas
200 ml Air bersih
1.5 sdm Tepung tapioka / sagu (larutkan dengan 2 sdm air dingin)
1/4 sdt Garam
Bumbu Halus Tumisan:
5 siung Bawang putih
3 butir Bawang merah
4 buah Cabai rawit merah (atau sesuai tingkat kepedasan)
1 sdm Ebi sangrai (haluskan bersama bumbu)
1/2 sdt Garam
1/2 sdt Merica bubuk
1/2 sdt Kaldu jamur / penyedap
Langkah-Langkah Pembuatan:
Membuat Bengkuang Manis: Rebus bengkuang iris bersama air, gula merah sisir, kecap manis, dan sedikit garam dalam panci di atas api sedang hingga air menyusut dan bengkuang berubah warna menjadi cokelat karamel manis serta renyah empuk. Angkat dan tiriskan bengkuang.
Membuat Saus Perekat Gula Merah: Rebus gula merah dan air dengan sedikit garam hingga gula larut sempurna. Saring larutan gula. Masak kembali larutan gula di atas api kecil, lalu tuangkan larutan tepung tapioka. Aduk cepat hingga mengental mengilat seperti lem karamel manis khas pedagang lumpia basah Bandung. Angkat dan sisihkan.
Menumis Isian: Panaskan 3 sendok makan minyak dalam wajan cekung. Tumis bumbu halus ebi hingga wangi matang. Pinggirkan bumbu ke tepi wajan, tuangkan telur kocok, lalu orak-arik hingga butiran telur matang. Masukkan bengkuang manis dan tauge segar. Bumbui dengan merica dan kaldu jamur. Aduk cepat di atas api besar selama 1-2 menit agar tauge tetap renyah (crunchy) dan tidak berair. Angkat.
Merakit Lumpia Basah: Letakkan selembar kulit lumpia basah di atas piring atau kertas nasi bersih. Oleskan 1.5 sendok makan saus perekat gula merah kental di tengah kulit lumpia secara merata. Letakkan tumisan isian tauge-bengkuang-telur panas di atas olesan saus.
Penyajian: Lipat bagian bawah kulit ke atas, lalu lipat sisi kanan dan kiri membungkus isian (atau biarkan terbuka setengah seperti gaya jajanan gerobak Bandung). Nikmati langsung selagi hangat dengan sumpit atau garpu.
Nutrisi (Per Porsi 2 Pcs): Kalori 240 kkal | Protein 8g | Lemak 7g | Karbohidrat 36g. Kaya akan serat inulin dari bengkuang yang mendukung kesehatan mikrobiota usus, serta vitamin C alami dari tauge segar yang dimasak singkat.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "6 lembar Kulit lumpia basah siap pakai", "amount": 6.0, "unit": "lembar", "name": "Kulit lumpia basah", "notes": "siap pakai", "orderIndex": 1},
                    {"rawText": "200g Tauge segar (cuci bersih)", "amount": 200.0, "unit": "g", "name": "Tauge segar", "notes": "cuci bersih", "orderIndex": 2},
                    {"rawText": "2 butir Telur ayam (kocok lepas)", "amount": 2.0, "unit": "butir", "name": "Telur ayam", "notes": "kocok lepas", "orderIndex": 3},
                    {"rawText": "2 batang Daun bawang (iris halus)", "amount": 2.0, "unit": "batang", "name": "Daun bawang", "notes": "iris halus", "orderIndex": 4},
                    {"rawText": "3 sdm Minyak goreng untuk menumis", "amount": 3.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Olahan Bengkuang Manis",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "300g Bengkuang (kupas, potong korek api)", "amount": 300.0, "unit": "g", "name": "Bengkuang", "notes": "potong korek api", "orderIndex": 1},
                    {"rawText": "70g Gula merah aren (sisir halus)", "amount": 70.0, "unit": "g", "name": "Gula merah aren", "notes": "sisir halus", "orderIndex": 2},
                    {"rawText": "1 sdm Kecap manis", "amount": 1.0, "unit": "sdm", "name": "Kecap manis", "notes": None, "orderIndex": 3},
                    {"rawText": "300 ml Air bersih", "amount": 300.0, "unit": "ml", "name": "Air bersih", "notes": None, "orderIndex": 4},
                    {"rawText": "1/2 sdt Garam", "amount": 0.5, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Saus Perekat Kental Gula Merah",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "100g Gula merah aren berkualitas", "amount": 100.0, "unit": "g", "name": "Gula merah aren", "notes": "berkualitas", "orderIndex": 1},
                    {"rawText": "200 ml Air bersih", "amount": 200.0, "unit": "ml", "name": "Air bersih", "notes": None, "orderIndex": 2},
                    {"rawText": "1.5 sdm Tepung tapioka / sagu", "amount": 1.5, "unit": "sdm", "name": "Tepung tapioka", "notes": "larutkan dengan 2 sdm air", "orderIndex": 3},
                    {"rawText": "1/4 sdt Garam", "amount": 0.25, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 4}
                ]
            },
            {
                "name": "Bumbu Halus Tumisan",
                "orderIndex": 4,
                "ingredients": [
                    {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 1},
                    {"rawText": "3 butir Bawang merah", "amount": 3.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 2},
                    {"rawText": "4 buah Cabai rawit merah", "amount": 4.0, "unit": "buah", "name": "Cabai rawit merah", "notes": None, "orderIndex": 3},
                    {"rawText": "1 sdm Ebi sangrai", "amount": 1.0, "unit": "sdm", "name": "Ebi sangrai", "notes": "haluskan bersama bumbu", "orderIndex": 4},
                    {"rawText": "1/2 sdt Garam", "amount": 0.5, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 5},
                    {"rawText": "1/2 sdt Merica bubuk", "amount": 0.5, "unit": "sdt", "name": "Merica bubuk", "notes": None, "orderIndex": 6},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 7}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Bengkuang Manis", "instruction": "Rebus bengkuang iris bersama air, gula merah sisir, kecap manis, dan sedikit garam dalam panci di atas api sedang hingga air menyusut dan bengkuang berubah warna menjadi cokelat karamel manis serta renyah empuk. Angkat dan tiriskan bengkuang.", "rawText": "Membuat Bengkuang Manis: Rebus bengkuang iris bersama air, gula merah sisir, kecap manis, dan sedikit garam dalam panci di atas api sedang hingga air menyusut dan bengkuang berubah warna menjadi cokelat karamel manis serta renyah empuk. Angkat dan tiriskan bengkuang."},
            {"stepNumber": 2, "title": "Membuat Saus Perekat Gula Merah", "instruction": "Rebus gula merah dan air dengan sedikit garam hingga gula larut sempurna. Saring larutan gula. Masak kembali larutan gula di atas api kecil, lalu tuangkan larutan tepung tapioka. Aduk cepat hingga mengental mengilat seperti lem karamel manis. Angkat dan sisihkan.", "rawText": "Membuat Saus Perekat Gula Merah: Rebus gula merah dan air dengan sedikit garam hingga gula larut sempurna. Saring larutan gula. Masak kembali larutan gula di atas api kecil, lalu tuangkan larutan tepung tapioka. Aduk cepat hingga mengental mengilat seperti lem karamel manis. Angkat dan sisihkan."},
            {"stepNumber": 3, "title": "Menumis Isian", "instruction": "Panaskan 3 sendok makan minyak dalam wajan cekung. Tumis bumbu halus ebi hingga wangi matang. Pinggirkan bumbu ke tepi wajan, tuangkan telur kocok, lalu orak-arik hingga butiran telur matang. Masukkan bengkuang manis dan tauge segar. Bumbui dengan merica dan kaldu jamur. Aduk cepat di atas api besar selama 1-2 menit agar tauge tetap renyah dan tidak berair. Angkat.", "rawText": "Menumis Isian: Panaskan 3 sendok makan minyak dalam wajan cekung. Tumis bumbu halus ebi hingga wangi matang. Pinggirkan bumbu ke tepi wajan, tuangkan telur kocok, lalu orak-arik hingga butiran telur matang. Masukkan bengkuang manis dan tauge segar. Bumbui dengan merica dan kaldu jamur. Aduk cepat di atas api besar selama 1-2 menit agar tauge tetap renyah dan tidak berair. Angkat."},
            {"stepNumber": 4, "title": "Merakit Lumpia Basah", "instruction": "Letakkan selembar kulit lumpia basah di atas piring atau kertas nasi bersih. Oleskan 1.5 sendok makan saus perekat gula merah kental di tengah kulit lumpia secara merata. Letakkan tumisan isian tauge-bengkuang-telur panas di atas olesan saus.", "rawText": "Merakit Lumpia Basah: Letakkan selembar kulit lumpia basah di atas piring atau kertas nasi bersih. Oleskan 1.5 sendok makan saus perekat gula merah kental di tengah kulit lumpia secara merata. Letakkan tumisan isian tauge-bengkuang-telur panas di atas olesan saus."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Lipat bagian bawah kulit ke atas, lalu lipat sisi kanan dan kiri membungkus isian. Nikmati langsung selagi hangat dengan sumpit atau garpu.", "rawText": "Penyajian: Lipat bagian bawah kulit ke atas, lalu lipat sisi kanan dan kiri membungkus isian. Nikmati langsung selagi hangat dengan sumpit atau garpu."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi 2 Pcs): Kalori 240 kkal | Protein 8g | Lemak 7g | Karbohidrat 36g. Kaya akan serat inulin dari bengkuang yang mendukung kesehatan mikrobiota usus, serta vitamin C alami dari tauge segar yang dimasak singkat.",
            "serving": "Per Porsi 2 Pcs",
            "calories": 240,
            "protein": 8.0,
            "fat": 7.0,
            "carbohydrates": 36.0,
            "notes": "Kaya akan serat inulin dari bengkuang yang mendukung kesehatan mikrobiota usus, serta vitamin C alami dari tauge segar yang dimasak singkat."
        }
    },
    {
        "recipeNumber": 186,
        "title": "186. Kue Pukis Pandan Khas Banyumas (Jawa Tengah)",
        "name": "Kue Pukis Pandan",
        "slug": "kue-pukis-pandan",
        "scope": "INDONESIA",
        "origin": "Jawa Tengah",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 50,
        "cookTimeMinutes": 20,
        "servings": 6,
        "difficulty": "MEDIUM",
        "spicinessLevel": 0,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "kudapan-minuman-tradisional",
        "rawContent": """186. Kue Pukis Pandan Khas Banyumas (Jawa Tengah)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Biang Ragi:
1 sdt Ragi instan aktif (yeast)
50 ml Air hangat kuku
1 sdt Gula pasir
Bahan Adonan Utama:
250g Tepung terigu protein sedang
150g Gula pasir halus
3 butir Telur ayam utuh
1 butir Kuning telur ayam
300 ml Santan kelapa sedang (rebus bersama selembar daun pandan dan 1/2 sdt garam, dinginkan hingga suhu ruang)
50g Margarin / Mentega tawar (lelehkan, dinginkan)
2 sdm Kental manis putih
1 sdm Endapan jus daun pandan suji alami (atau pasta pandan berkualitas)
1/2 sdt Vanili bubuk
Bahan Topping:
50g Meises cokelat hitam berkualitas
50g Keju cheddar parut
Margarin secukupnya untuk olesan cetakan
Langkah-Langkah Pembuatan:
Mengaktifkan Ragi (Biang): Campurkan ragi instan, air hangat kuku, dan gula pasir dalam mangkuk kecil. Aduk rata dan diamkan selama 8-10 menit hingga muncul buih-buih tebal di permukaan (tanda ragi aktif optimal).
Mengocok Telur dan Gula: Kocok telur ayam, kuning telur, gula pasir, dan vanili bubuk menggunakan mixer kecepatan tinggi atau balloon whisk hingga adonan mengembang, berbusa kental, dan berwarna pucat (sekitar 5-7 menit).
Memasukkan Tepung dan Santan: Turunkan kecepatan mixer ke rendah. Masukkan tepung terigu yang sudah diayak bergantian dengan santan rebus dingin secara bertahap sambil diaduk hingga rata. Masukkan larutan biang ragi aktif, aduk perlahan.
Menambahkan Mentega dan Pandan: Masukkan kental manis, margarin leleh dingin, dan endapan jus pandan suji ke dalam adonan. Aduk balik menggunakan spatula karet hingga benar-benar menyatu tanpa ada endapan minyak di dasar wadah.
Proses Fermentasi (Proofing): Tutup wadah adonan dengan serbet bersih lembap atau plastik wrap. Diamkan selama 45-60 menit hingga adonan mengembang dua kali lipat dan berongga pori-pori halus. Aduk perlahan adonan untuk membuang gas berlebih sebelum dicetak.
Memanggang Pukis: Panaskan cetakan kue pukis di atas kompor dengan api kecil merata. Olesi lubang cetakan dengan tipis margarin. Tuangkan adonan pandan hingga 3/4 tinggi cetakan (adonan akan mengembang naik). Tutup cetakan dan panggang selama 3-4 menit hingga setengah matang.
Menaburi Topping: Buka tutup cetakan, taburkan meises cokelat dan keju cheddar parut di atas permukaan pukis yang mulai mengeras. Tutup kembali dan panggang lagi selama 2-3 menit hingga pukis matang, bagian bawahnya berkulit kecokelatan wangi, dan permukaannya kering tidak lengket disentuh.
Penyajian: Angkat kue pukis menggunakan spatula kecil khusus. Oleskan sedikit mentega pada sisi-sisi pukis selagi panas agar tetap harum, lembut, dan lembap tahan lama. Sajikan hangat untuk teman minum kopi atau teh.
Nutrisi (Per Porsi 2 Pcs): Kalori 220 kkal | Protein 5g | Lemak 9g | Karbohidrat 30g. Karbohidrat kompleks dan lemak nabati yang memanjakan lidah, dengan aroma alami senyawa aromatik klorofil daun pandan yang meredakan stres.""",
        "ingredientGroups": [
            {
                "name": "Bahan Biang Ragi",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "1 sdt Ragi instan aktif (yeast)", "amount": 1.0, "unit": "sdt", "name": "Ragi instan aktif", "notes": None, "orderIndex": 1},
                    {"rawText": "50 ml Air hangat kuku", "amount": 50.0, "unit": "ml", "name": "Air hangat kuku", "notes": None, "orderIndex": 2},
                    {"rawText": "1 sdt Gula pasir", "amount": 1.0, "unit": "sdt", "name": "Gula pasir", "notes": None, "orderIndex": 3}
                ]
            },
            {
                "name": "Bahan Adonan Utama",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "250g Tepung terigu protein sedang", "amount": 250.0, "unit": "g", "name": "Tepung terigu protein sedang", "notes": None, "orderIndex": 1},
                    {"rawText": "150g Gula pasir halus", "amount": 150.0, "unit": "g", "name": "Gula pasir halus", "notes": None, "orderIndex": 2},
                    {"rawText": "3 butir Telur ayam utuh", "amount": 3.0, "unit": "butir", "name": "Telur ayam utuh", "notes": None, "orderIndex": 3},
                    {"rawText": "1 butir Kuning telur ayam", "amount": 1.0, "unit": "butir", "name": "Kuning telur ayam", "notes": None, "orderIndex": 4},
                    {"rawText": "300 ml Santan kelapa sedang (rebus bersama pandan dan garam)", "amount": 300.0, "unit": "ml", "name": "Santan kelapa sedang", "notes": "rebus bersama pandan dan garam", "orderIndex": 5},
                    {"rawText": "50g Margarin / Mentega tawar (lelehkan)", "amount": 50.0, "unit": "g", "name": "Margarin atau mentega", "notes": "lelehkan, dinginkan", "orderIndex": 6},
                    {"rawText": "2 sdm Kental manis putih", "amount": 2.0, "unit": "sdm", "name": "Kental manis putih", "notes": None, "orderIndex": 7},
                    {"rawText": "1 sdm Endapan jus daun pandan suji alami", "amount": 1.0, "unit": "sdm", "name": "Endapan jus daun pandan suji", "notes": "alami", "orderIndex": 8},
                    {"rawText": "1/2 sdt Vanili bubuk", "amount": 0.5, "unit": "sdt", "name": "Vanili bubuk", "notes": None, "orderIndex": 9}
                ]
            },
            {
                "name": "Bahan Topping",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "50g Meises cokelat hitam", "amount": 50.0, "unit": "g", "name": "Meises cokelat hitam", "notes": "berkualitas", "orderIndex": 1},
                    {"rawText": "50g Keju cheddar parut", "amount": 50.0, "unit": "g", "name": "Keju cheddar parut", "notes": None, "orderIndex": 2},
                    {"rawText": "Margarin secukupnya untuk olesan cetakan", "amount": None, "unit": "secukupnya", "name": "Margarin", "notes": "untuk olesan", "orderIndex": 3}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Mengaktifkan Ragi (Biang)", "instruction": "Campurkan ragi instan, air hangat kuku, dan gula pasir dalam mangkuk kecil. Aduk rata dan diamkan selama 8-10 menit hingga muncul buih-buih tebal di permukaan (tanda ragi aktif optimal).", "rawText": "Mengaktifkan Ragi (Biang): Campurkan ragi instan, air hangat kuku, dan gula pasir dalam mangkuk kecil. Aduk rata dan diamkan selama 8-10 menit hingga muncul buih-buih tebal di permukaan (tanda ragi aktif optimal)."},
            {"stepNumber": 2, "title": "Mengocok Telur dan Gula", "instruction": "Kocok telur ayam, kuning telur, gula pasir, dan vanili bubuk menggunakan mixer kecepatan tinggi atau balloon whisk hingga adonan mengembang, berbusa kental, dan berwarna pucat (sekitar 5-7 menit).", "rawText": "Mengocok Telur dan Gula: Kocok telur ayam, kuning telur, gula pasir, dan vanili bubuk menggunakan mixer kecepatan tinggi atau balloon whisk hingga adonan mengembang, berbusa kental, dan berwarna pucat (sekitar 5-7 menit)."},
            {"stepNumber": 3, "title": "Memasukkan Tepung dan Santan", "instruction": "Turunkan kecepatan mixer ke rendah. Masukkan tepung terigu yang sudah diayak bergantian dengan santan rebus dingin secara bertahap sambil diaduk hingga rata. Masukkan larutan biang ragi aktif, aduk perlahan.", "rawText": "Memasukkan Tepung dan Santan: Turunkan kecepatan mixer ke rendah. Masukkan tepung terigu yang sudah diayak bergantian dengan santan rebus dingin secara bertahap sambil diaduk hingga rata. Masukkan larutan biang ragi aktif, aduk perlahan."},
            {"stepNumber": 4, "title": "Menambahkan Mentega dan Pandan", "instruction": "Masukkan kental manis, margarin leleh dingin, dan endapan jus pandan suji ke dalam adonan. Aduk balik menggunakan spatula karet hingga benar-benar menyatu tanpa ada endapan minyak di dasar wadah.", "rawText": "Menambahkan Mentega dan Pandan: Masukkan kental manis, margarin leleh dingin, dan endapan jus pandan suji ke dalam adonan. Aduk balik menggunakan spatula karet hingga benar-benar menyatu tanpa ada endapan minyak di dasar wadah."},
            {"stepNumber": 5, "title": "Proses Fermentasi (Proofing)", "instruction": "Tutup wadah adonan dengan serbet bersih lembap atau plastik wrap. Diamkan selama 45-60 menit hingga adonan mengembang dua kali lipat dan berongga pori-pori halus. Aduk perlahan adonan untuk membuang gas berlebih sebelum dicetak.", "rawText": "Proses Fermentasi (Proofing): Tutup wadah adonan dengan serbet bersih lembap atau plastik wrap. Diamkan selama 45-60 menit hingga adonan mengembang dua kali lipat dan berongga pori-pori halus. Aduk perlahan adonan untuk membuang gas berlebih sebelum dicetak."},
            {"stepNumber": 6, "title": "Memanggang Pukis dan Topping", "instruction": "Panaskan cetakan kue pukis di atas kompor dengan api kecil merata. Olesi lubang cetakan dengan tipis margarin. Tuangkan adonan pandan hingga 3/4 tinggi cetakan. Tutup dan panggang 3-4 menit hingga setengah matang. Buka tutup, taburi meises cokelat dan keju parut. Tutup dan panggang kembali 2-3 menit hingga matang.", "rawText": "Memanggang Pukis dan Topping: Panaskan cetakan kue pukis di atas kompor dengan api kecil merata. Olesi lubang cetakan dengan tipis margarin. Tuangkan adonan pandan hingga 3/4 tinggi cetakan. Tutup dan panggang 3-4 menit hingga setengah matang. Buka tutup, taburi meises cokelat dan keju parut. Tutup dan panggang kembali 2-3 menit hingga matang."},
            {"stepNumber": 7, "title": "Penyajian", "instruction": "Angkat kue pukis menggunakan spatula kecil khusus. Oleskan sedikit mentega pada sisi-sisi pukis selagi panas agar tetap harum, lembut, dan lembap tahan lama. Sajikan hangat untuk teman minum kopi atau teh.", "rawText": "Penyajian: Angkat kue pukis menggunakan spatula kecil khusus. Oleskan sedikit mentega pada sisi-sisi pukis selagi panas agar tetap harum, lembut, dan lembap tahan lama. Sajikan hangat untuk teman minum kopi atau teh."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi 2 Pcs): Kalori 220 kkal | Protein 5g | Lemak 9g | Karbohidrat 30g. Karbohidrat kompleks dan lemak nabati yang memanjakan lidah, dengan aroma alami senyawa aromatik klorofil daun pandan yang meredakan stres.",
            "serving": "Per Porsi 2 Pcs",
            "calories": 220,
            "protein": 5.0,
            "fat": 9.0,
            "carbohydrates": 30.0,
            "notes": "Karbohidrat kompleks dan lemak nabati yang memanjakan lidah, dengan aroma alami senyawa aromatik klorofil daun pandan yang meredakan stres."
        }
    },
    {
        "recipeNumber": 187,
        "title": "187. Pisang Goreng Madu Khas Nusantara",
        "name": "Pisang Goreng Madu",
        "slug": "pisang-goreng-madu",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 15,
        "cookTimeMinutes": 20,
        "servings": 5,
        "difficulty": "EASY",
        "spicinessLevel": 0,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """187. Pisang Goreng Madu Khas Nusantara
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Pisang raja masak pohon atau pisang tanduk (potong bulat tebal 1.5 cm)
Minyak kelapa sawit secukupnya untuk deep fry
Bahan Adonan Tepung Madu:
150g Tepung terigu protein sedang
50g Tepung beras (untuk menciptakan kerenyahan tahan lama)
25g Tepung maizena
4 sdm Madu murni alami
2 sdm Gula pasir / gula palem
1/2 sdt Garam halus
1/2 sdt Vanili bubuk
1/2 sdt Baking powder
200 ml Air es dingin
Bahan Larutan Celupan Karamel Tambahan:
3 sdm Madu murni
3 sdm Air matang
Langkah-Langkah Pembuatan:
Membuat Adonan Tepung: Ayak tepung terigu, tepung beras, maizena, dan baking powder ke dalam wadah mangkuk. Masukkan gula pasir, garam, vanili bubuk, dan madu murni. Tuang air es dingin bertahap sambil diaduk dengan whisk hingga tercapai kekentalan adonan yang pas (tidak terlalu encer dan licin membungkus sendok).
Mencampur Pisang: Masukkan potongan buah pisang matang ke dalam adonan tepung madu, aduk perlahan menggunakan sendok agar setiap potongan pisang terselimuti adonan kental secara merata.
Memanaskan Minyak dan Cetakan: Panaskan minyak goreng dalam jumlah banyak di wajan cekung di atas api sedang. Rendam sendok sayur besi / cetakan bulat ke dalam minyak panas selama 1 menit agar anti-lengket saat adonan dituangkan.
Menggoreng Tahap Pertama: Angkat sendok sayur dari minyak panas, isi dengan adonan pisang beserta kuah tepungnya secukupnya (membentuk lempengan bulat tebal). Celupkan sendok sayur berisi adonan ke dalam minyak panas. Biarkan hingga adonan mulai mengeras dan terlepas sendiri dari sendok ke dalam minyak.
Proses Karamelisasi Madu: Goreng lempengan pisang hingga setengah matang dan mulai kekuningan. Angkat pisang sejenak, celupkan cepat ke dalam larutan madu tambahan, lalu masukkan kembali ke minyak panas. Goreng hingga permukaan adonan terkaramelisasi menjadi cokelat gelap eksotis, berkulit renyah gosong madu (bukan hangus pahit), dan mengeluarkan wangi madu legit.
Penyajian: Angkat pisang goreng madu dan tiriskan di atas rak kawat peniris hingga minyak tiris sempurna. Sajikan hangat dalam keadaan kulit luar renyah karamel dan bagian dalam pisang lumer manis lembut.
Nutrisi (Per Buah Porsi): Kalori 210 kkal | Protein 2g | Lemak 6g | Karbohidrat 38g. Sumber energi instan yang kaya kalium dan vitamin B6 dari buah pisang alami, berpadu dengan enzim alami dan antioksidan fenolik dari madu murni lebah.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "500g Pisang raja masak pohon atau pisang tanduk (potong bulat 1.5 cm)", "amount": 500.0, "unit": "g", "name": "Pisang raja atau pisang tanduk", "notes": "potong bulat 1.5 cm", "orderIndex": 1},
                    {"rawText": "Minyak kelapa sawit secukupnya untuk deep fry", "amount": None, "unit": "secukupnya", "name": "Minyak kelapa sawit", "notes": "untuk deep fry", "orderIndex": 2}
                ]
            },
            {
                "name": "Bahan Adonan Tepung Madu",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "150g Tepung terigu protein sedang", "amount": 150.0, "unit": "g", "name": "Tepung terigu protein sedang", "notes": None, "orderIndex": 1},
                    {"rawText": "50g Tepung beras", "amount": 50.0, "unit": "g", "name": "Tepung beras", "notes": "untuk kerenyahan", "orderIndex": 2},
                    {"rawText": "25g Tepung maizena", "amount": 25.0, "unit": "g", "name": "Tepung maizena", "notes": None, "orderIndex": 3},
                    {"rawText": "4 sdm Madu murni alami", "amount": 4.0, "unit": "sdm", "name": "Madu murni alami", "notes": None, "orderIndex": 4},
                    {"rawText": "2 sdm Gula pasir / gula palem", "amount": 2.0, "unit": "sdm", "name": "Gula pasir", "notes": "atau gula palem", "orderIndex": 5},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 6},
                    {"rawText": "1/2 sdt Vanili bubuk", "amount": 0.5, "unit": "sdt", "name": "Vanili bubuk", "notes": None, "orderIndex": 7},
                    {"rawText": "1/2 sdt Baking powder", "amount": 0.5, "unit": "sdt", "name": "Baking powder", "notes": None, "orderIndex": 8},
                    {"rawText": "200 ml Air es dingin", "amount": 200.0, "unit": "ml", "name": "Air es dingin", "notes": None, "orderIndex": 9}
                ]
            },
            {
                "name": "Bahan Larutan Celupan Karamel Tambahan",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "3 sdm Madu murni", "amount": 3.0, "unit": "sdm", "name": "Madu murni", "notes": None, "orderIndex": 1},
                    {"rawText": "3 sdm Air matang", "amount": 3.0, "unit": "sdm", "name": "Air matang", "notes": None, "orderIndex": 2}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Adonan Tepung", "instruction": "Ayak tepung terigu, tepung beras, maizena, dan baking powder ke dalam wadah mangkuk. Masukkan gula pasir, garam, vanili bubuk, dan madu murni. Tuang air es dingin bertahap sambil diaduk dengan whisk hingga tercapai kekentalan adonan yang pas.", "rawText": "Membuat Adonan Tepung: Ayak tepung terigu, tepung beras, maizena, dan baking powder ke dalam wadah mangkuk. Masukkan gula pasir, garam, vanili bubuk, dan madu murni. Tuang air es dingin bertahap sambil diaduk dengan whisk hingga tercapai kekentalan adonan yang pas."},
            {"stepNumber": 2, "title": "Mencampur Pisang", "instruction": "Masukkan potongan buah pisang matang ke dalam adonan tepung madu, aduk perlahan menggunakan sendok agar setiap potongan pisang terselimuti adonan kental secara merata.", "rawText": "Mencampur Pisang: Masukkan potongan buah pisang matang ke dalam adonan tepung madu, aduk perlahan menggunakan sendok agar setiap potongan pisang terselimuti adonan kental secara merata."},
            {"stepNumber": 3, "title": "Memanaskan Minyak dan Cetakan", "instruction": "Panaskan minyak goreng dalam jumlah banyak di wajan cekung di atas api sedang. Rendam sendok sayur besi / cetakan bulat ke dalam minyak panas selama 1 menit agar anti-lengket saat adonan dituangkan.", "rawText": "Memanaskan Minyak dan Cetakan: Panaskan minyak goreng dalam jumlah banyak di wajan cekung di atas api sedang. Rendam sendok sayur besi / cetakan bulat ke dalam minyak panas selama 1 menit agar anti-lengket saat adonan dituangkan."},
            {"stepNumber": 4, "title": "Menggoreng Tahap Pertama", "instruction": "Angkat sendok sayur dari minyak panas, isi dengan adonan pisang beserta kuah tepungnya secukupnya. Celupkan sendok sayur berisi adonan ke dalam minyak panas. Biarkan hingga adonan mulai mengeras dan terlepas sendiri dari sendok ke dalam minyak.", "rawText": "Menggoreng Tahap Pertama: Angkat sendok sayur dari minyak panas, isi dengan adonan pisang beserta kuah tepungnya secukupnya. Celupkan sendok sayur berisi adonan ke dalam minyak panas. Biarkan hingga adonan mulai mengeras dan terlepas sendiri dari sendok ke dalam minyak."},
            {"stepNumber": 5, "title": "Proses Karamelisasi Madu", "instruction": "Goreng lempengan pisang hingga setengah matang dan mulai kekuningan. Angkat pisang sejenak, celupkan cepat ke dalam larutan madu tambahan, lalu masukkan kembali ke minyak panas. Goreng hingga permukaan adonan terkaramelisasi menjadi cokelat gelap eksotis, berkulit renyah gosong madu, dan mengeluarkan wangi madu legit.", "rawText": "Proses Karamelisasi Madu: Goreng lempengan pisang hingga setengah matang dan mulai kekuningan. Angkat pisang sejenak, celupkan cepat ke dalam larutan madu tambahan, lalu masukkan kembali ke minyak panas. Goreng hingga permukaan adonan terkaramelisasi menjadi cokelat gelap eksotis, berkulit renyah gosong madu, dan mengeluarkan wangi madu legit."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Angkat pisang goreng madu dan tiriskan di atas rak kawat peniris hingga minyak tiris sempurna. Sajikan hangat dalam keadaan kulit luar renyah karamel dan bagian dalam pisang lumer manis lembut.", "rawText": "Penyajian: Angkat pisang goreng madu dan tiriskan di atas rak kawat peniris hingga minyak tiris sempurna. Sajikan hangat dalam keadaan kulit luar renyah karamel dan bagian dalam pisang lumer manis lembut."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Buah Porsi): Kalori 210 kkal | Protein 2g | Lemak 6g | Karbohidrat 38g. Sumber energi instan yang kaya kalium dan vitamin B6 dari buah pisang alami, berpadu dengan enzim alami dan antioksidan fenolik dari madu murni lebah.",
            "serving": "Per Buah Porsi",
            "calories": 210,
            "protein": 2.0,
            "fat": 6.0,
            "carbohydrates": 38.0,
            "notes": "Sumber energi instan yang kaya kalium dan vitamin B6 dari buah pisang alami, berpadu dengan enzim alami dan antioksidan fenolik dari madu murni lebah."
        }
    },
    {
        "recipeNumber": 188,
        "title": "188. Es Pisang Ijo Khas Makassar (Sulawesi Selatan)",
        "name": "Es Pisang Ijo Makassar",
        "slug": "es-pisang-ijo-makassar",
        "scope": "INDONESIA",
        "origin": "Sulawesi Selatan",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 35,
        "cookTimeMinutes": 30,
        "servings": 5,
        "difficulty": "MEDIUM",
        "spicinessLevel": 0,
        "categorySlug": "minuman-segar",
        "cuisineTypeSlug": "kudapan-minuman-tradisional",
        "rawContent": """188. Es Pisang Ijo Khas Makassar (Sulawesi Selatan)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Pisang & Balutan Kulit Ijo:
5 buah Pisang raja matang manis (kukus utuh selama 10 menit, kupas kulitnya)
150g Tepung beras
50g Tepung terigu protein sedang
50g Gula pasir
400 ml Santan sedang (dari kelapa parut segar)
100 ml Air perasan daun pandan dan suji (pewarna alami hijau segar)
1/2 sdt Garam halus
Daun pisang atau plastik tahan panas untuk membungkus kukusan
Bahan Bubur Sumsum Lembut:
100g Tepung beras
750 ml Santan kelapa gurih sedang
2 lembar Daun pandan (ikat simpul)
1/2 sdt Garam halus
Bahan Kuah dan Pelengkap Es:
150 ml Sirup DHT khas Makassar rasa pisang ambon (atau sirup cocopandan merah)
100 ml Kental manis putih
Es serut / es batu secukupnya
Langkah-Langkah Pembuatan:
Membuat Adonan Kulit Pisang Ijo: Campurkan tepung beras, tepung terigu, gula pasir, garam, santan sedang, dan air perasan daun pandan suji dalam panci. Aduk rata hingga larut dan saring agar tidak bergerindil. Masak adonan di atas api kecil sambil terus diaduk dengan spatula hingga adonan menggumpal kalis, licin, dan matang wangi pandan. Angkat dan biarkan hingga hangat.
Membungkus Pisang: Ambil selembar daun pisang atau plastik tahan panas yang telah diolesi tipis minyak kelapa. Ambil adonan hijau secukupnya, pipihkan rata. Letakkan 1 buah pisang raja kukus di atasnya, lalu gulung dan rapatkan adonan hijau hingga menyelimuti seluruh permukaan pisang dengan ketebalan yang rapi menyerupai bentuk pisang utuh.
Mengukus Pisang Ijo: Bungkus gulungan pisang dengan daun pisang seperti membungkus lontong, semat ujungnya dengan tusuk gigi. Panaskan kukusan hingga beruap banyak. Kukus pisang ijo selama 15-20 menit hingga kulit hijau benar-benar matang matang kenyal. Angkat dan dinginkan pada suhu ruang sebelum dipotong.
Membuat Bubur Sumsum: Campurkan tepung beras, santan, garam, dan daun pandan simpul ke dalam panci. Aduk hingga tepung larut rata. Masak di atas api sedang cenderung kecil sambil terus diaduk tanpa henti agar dasar panci tidak berkerak. Masak hingga bubur mengental pekat, meletup-letup halus, dan bertekstur selembut sutra. Angkat dan sisihkan.
Penyajian: Potong-potong pisang ijo yang sudah dingin miring setebal 2 cm. Tuangkan 2-3 sendok sayur bubur sumsum lembut ke dalam mangkuk saji saji. Susun irisan pisang ijo di atas bubur. Beri serutan es batu di atasnya, lalu siramkan sirup merah DHT aroma pisang ambon dan kucuran kental manis putih secara melimpah. Sajikan segera selagi dingin segar.
Nutrisi (Per Porsi Mangkuk): Kalori 340 kkal | Protein 6g | Lemak 9g | Karbohidrat 60g. Menyegarkan hidrasi tubuh dengan elektrolit alami kalium pisang dan santan, serta kaya fitonutrien klorofil antioksidan dari sari daun pandan suji murni.""",
        "ingredientGroups": [
            {
                "name": "Bahan Pisang & Balutan Kulit Ijo",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "5 buah Pisang raja matang manis (kukus utuh, kupas)", "amount": 5.0, "unit": "buah", "name": "Pisang raja matang manis", "notes": "kukus utuh, kupas", "orderIndex": 1},
                    {"rawText": "150g Tepung beras", "amount": 150.0, "unit": "g", "name": "Tepung beras", "notes": None, "orderIndex": 2},
                    {"rawText": "50g Tepung terigu protein sedang", "amount": 50.0, "unit": "g", "name": "Tepung terigu protein sedang", "notes": None, "orderIndex": 3},
                    {"rawText": "50g Gula pasir", "amount": 50.0, "unit": "g", "name": "Gula pasir", "notes": None, "orderIndex": 4},
                    {"rawText": "400 ml Santan sedang", "amount": 400.0, "unit": "ml", "name": "Santan sedang", "notes": "dari kelapa parut segar", "orderIndex": 5},
                    {"rawText": "100 ml Air perasan daun pandan dan suji", "amount": 100.0, "unit": "ml", "name": "Air perasan daun pandan dan suji", "notes": "pewarna alami", "orderIndex": 6},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 7}
                ]
            },
            {
                "name": "Bahan Bubur Sumsum Lembut",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "100g Tepung beras", "amount": 100.0, "unit": "g", "name": "Tepung beras", "notes": None, "orderIndex": 1},
                    {"rawText": "750 ml Santan kelapa gurih sedang", "amount": 750.0, "unit": "ml", "name": "Santan kelapa gurih sedang", "notes": None, "orderIndex": 2},
                    {"rawText": "2 lembar Daun pandan (ikat simpul)", "amount": 2.0, "unit": "lembar", "name": "Daun pandan", "notes": "ikat simpul", "orderIndex": 3},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 4}
                ]
            },
            {
                "name": "Bahan Kuah dan Pelengkap Es",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "150 ml Sirup DHT khas Makassar (atau cocopandan merah)", "amount": 150.0, "unit": "ml", "name": "Sirup DHT khas Makassar", "notes": "atau sirup cocopandan", "orderIndex": 1},
                    {"rawText": "100 ml Kental manis putih", "amount": 100.0, "unit": "ml", "name": "Kental manis putih", "notes": None, "orderIndex": 2},
                    {"rawText": "Es serut atau es batu secukupnya", "amount": None, "unit": "secukupnya", "name": "Es serut atau es batu", "notes": None, "orderIndex": 3}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Adonan Kulit Pisang Ijo", "instruction": "Campurkan tepung beras, tepung terigu, gula pasir, garam, santan sedang, dan air perasan daun pandan suji dalam panci. Aduk rata hingga larut dan saring agar tidak bergerindil. Masak adonan di atas api kecil sambil terus diaduk dengan spatula hingga adonan menggumpal kalis, licin, dan matang wangi pandan. Angkat dan biarkan hingga hangat.", "rawText": "Membuat Adonan Kulit Pisang Ijo: Campurkan tepung beras, tepung terigu, gula pasir, garam, santan sedang, dan air perasan daun pandan suji dalam panci. Aduk rata hingga larut dan saring agar tidak bergerindil. Masak adonan di atas api kecil sambil terus diaduk dengan spatula hingga adonan menggumpal kalis, licin, dan matang wangi pandan. Angkat dan biarkan hingga hangat."},
            {"stepNumber": 2, "title": "Membungkus Pisang", "instruction": "Ambil selembar daun pisang atau plastik tahan panas yang telah diolesi tipis minyak kelapa. Ambil adonan hijau secukupnya, pipihkan rata. Letakkan 1 buah pisang raja kukus di atasnya, lalu gulung dan rapatkan adonan hijau hingga menyelimuti seluruh permukaan pisang dengan ketebalan yang rapi menyerupai bentuk pisang utuh.", "rawText": "Membungkus Pisang: Ambil selembar daun pisang atau plastik tahan panas yang telah diolesi tipis minyak kelapa. Ambil adonan hijau secukupnya, pipihkan rata. Letakkan 1 buah pisang raja kukus di atasnya, lalu gulung dan rapatkan adonan hijau hingga menyelimuti seluruh permukaan pisang dengan ketebalan yang rapi menyerupai bentuk pisang utuh."},
            {"stepNumber": 3, "title": "Mengukus Pisang Ijo", "instruction": "Bungkus gulungan pisang dengan daun pisang seperti membungkus lontong, semat ujungnya dengan tusuk gigi. Panaskan kukusan hingga beruap banyak. Kukus pisang ijo selama 15-20 menit hingga kulit hijau benar-benar matang matang kenyal. Angkat dan dinginkan pada suhu ruang sebelum dipotong.", "rawText": "Mengukus Pisang Ijo: Bungkus gulungan pisang dengan daun pisang seperti membungkus lontong, semat ujungnya dengan tusuk gigi. Panaskan kukusan hingga beruap banyak. Kukus pisang ijo selama 15-20 menit hingga kulit hijau benar-benar matang matang kenyal. Angkat dan dinginkan pada suhu ruang sebelum dipotong."},
            {"stepNumber": 4, "title": "Membuat Bubur Sumsum", "instruction": "Campurkan tepung beras, santan, garam, dan daun pandan simpul ke dalam panci. Aduk hingga tepung larut rata. Masak di atas api sedang cenderung kecil sambil terus diaduk tanpa henti agar dasar panci tidak berkerak. Masak hingga bubur mengental pekat, meletup-letup halus, dan bertekstur selembut sutra. Angkat dan sisihkan.", "rawText": "Membuat Bubur Sumsum: Campurkan tepung beras, santan, garam, dan daun pandan simpul ke dalam panci. Aduk hingga tepung larut rata. Masak di atas api sedang cenderung kecil sambil terus diaduk tanpa henti agar dasar panci tidak berkerak. Masak hingga bubur mengental pekat, meletup-letup halus, dan bertekstur selembut sutra. Angkat dan sisihkan."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Potong-potong pisang ijo yang sudah dingin miring setebal 2 cm. Tuangkan 2-3 sendok sayur bubur sumsum lembut ke dalam mangkuk saji. Susun irisan pisang ijo di atas bubur. Beri serutan es batu di atasnya, lalu siramkan sirup merah DHT aroma pisang ambon dan kucuran kental manis putih secara melimpah. Sajikan segera selagi dingin segar.", "rawText": "Penyajian: Potong-potong pisang ijo yang sudah dingin miring setebal 2 cm. Tuangkan 2-3 sendok sayur bubur sumsum lembut ke dalam mangkuk saji. Susun irisan pisang ijo di atas bubur. Beri serutan es batu di atasnya, lalu siramkan sirup merah DHT aroma pisang ambon dan kucuran kental manis putih secara melimpah. Sajikan segera selagi dingin segar."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi Mangkuk): Kalori 340 kkal | Protein 6g | Lemak 9g | Karbohidrat 60g. Menyegarkan hidrasi tubuh dengan elektrolit alami kalium pisang dan santan, serta kaya fitonutrien klorofil antioksidan dari sari daun pandan suji murni.",
            "serving": "Per Porsi Mangkuk",
            "calories": 340,
            "protein": 6.0,
            "fat": 9.0,
            "carbohydrates": 60.0,
            "notes": "Menyegarkan hidrasi tubuh dengan elektrolit alami kalium pisang dan santan, serta kaya fitonutrien klorofil antioksidan dari sari daun pandan suji murni."
        }
    },
    {
        "recipeNumber": 189,
        "title": "189. Es Teler Spesial (Nusantara)",
        "name": "Es Teler Spesial",
        "slug": "es-teler-spesial",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 10,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 0,
        "categorySlug": "minuman-segar",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """189. Es Teler Spesial (Nusantara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Isian Buah Segar:
2 buah Alpukat mentega matang (keruk dagingnya dengan sendok)
1 butir Kelapa muda (keruk memanjang daging buahnya)
6 butir Nangka matang manis harum (buang biji, potong dadu 1.5 cm)
1 sdm Biji selasih (rendam air hangat hingga mengembang mekar)
Bahan Kuah Santan Manis Gurih:
300 ml Santan kelapa kental sedang (rebus bersama selembar daun pandan dan 1/2 sdt garam, dinginkan)
200 ml Air kelapa muda murni segar
150 ml Kental manis putih
Bahan Sirup Gula Pandan:
100g Gula pasir murni
100 ml Air bersih
2 lembar Daun pandan wangi (ikat simpul)
Pelengkap:
Es serut / pecahan es batu kristal secukupnya
Langkah-Langkah Pembuatan:
Membuat Sirup Gula Pandan: Didihkan air, gula pasir, dan daun pandan simpul di atas api sedang hingga gula larut sempurna dan harum pandan semerbak keluar. Matikan api dan biarkan sirup gula dingin pada suhu ruang.
Menyiapkan Kuah Santan Kelapa: Campurkan santan rebus yang sudah dingin dengan air kelapa muda segar, sirup gula pandan, dan sebagian kental manis. Aduk rata hingga tercipta kuah yang gurih beraroma kelapa alami.
Menyiapkan Isian Buah: Keruk daging buah alpukat mentega secara rapi, serut daging kelapa muda memanjang lembut, dan potong dadu nangka kuning manis. Pastikan biji selasih sudah mengembang sempurna.
Penyusunan Es Teler: Siapkan gelas saji tinggi atau mangkuk kaca. Masukkan potongan alpukat, daging kelapa muda serut, dan potongan nangka manis ke dalam wadah. Beri 1 sendok teh biji selasih di atasnya.
Penyajian: Beri gunungan es serut menutupi buah-buahan, lalu siramkan kuah santan kelapa gurih di atas es serut hingga meresap ke dasar mangkuk. Kucuri bagian atas es dengan kental manis putih melingkar. Sajikan segera selagi dingin menyegarkan.
Nutrisi (Per Porsi): Kalori 290 kkal | Protein 4g | Lemak 14g | Karbohidrat 42g. Kaya akan asam lemak tak jenuh tunggal yang menyehatkan jantung dari buah alpukat mentega, elektrolit alami peremaja sel tubuh dari air kelapa murni, serta vitamin C dari nangka segar.""",
        "ingredientGroups": [
            {
                "name": "Bahan Isian Buah Segar",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "2 buah Alpukat mentega matang (keruk dagingnya)", "amount": 2.0, "unit": "buah", "name": "Alpukat mentega matang", "notes": "keruk dagingnya", "orderIndex": 1},
                    {"rawText": "1 butir Kelapa muda (keruk memanjang dagingnya)", "amount": 1.0, "unit": "butir", "name": "Kelapa muda", "notes": "keruk memanjang", "orderIndex": 2},
                    {"rawText": "6 butir Nangka matang manis harum (potong dadu 1.5 cm)", "amount": 6.0, "unit": "butir", "name": "Nangka matang", "notes": "potong dadu 1.5 cm", "orderIndex": 3},
                    {"rawText": "1 sdm Biji selasih (rendam air hangat)", "amount": 1.0, "unit": "sdm", "name": "Biji selasih", "notes": "rendam air hangat hingga mekar", "orderIndex": 4}
                ]
            },
            {
                "name": "Bahan Kuah Santan Manis Gurih",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "300 ml Santan kelapa kental sedang (rebus bersama pandan dan garam)", "amount": 300.0, "unit": "ml", "name": "Santan kelapa kental sedang", "notes": "rebus bersama pandan dan garam", "orderIndex": 1},
                    {"rawText": "200 ml Air kelapa muda murni segar", "amount": 200.0, "unit": "ml", "name": "Air kelapa muda murni segar", "notes": None, "orderIndex": 2},
                    {"rawText": "150 ml Kental manis putih", "amount": 150.0, "unit": "ml", "name": "Kental manis putih", "notes": None, "orderIndex": 3}
                ]
            },
            {
                "name": "Bahan Sirup Gula Pandan & Pelengkap",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "100g Gula pasir murni", "amount": 100.0, "unit": "g", "name": "Gula pasir", "notes": None, "orderIndex": 1},
                    {"rawText": "100 ml Air bersih", "amount": 100.0, "unit": "ml", "name": "Air bersih", "notes": None, "orderIndex": 2},
                    {"rawText": "2 lembar Daun pandan wangi (ikat simpul)", "amount": 2.0, "unit": "lembar", "name": "Daun pandan wangi", "notes": "ikat simpul", "orderIndex": 3},
                    {"rawText": "Es serut / es batu kristal secukupnya", "amount": None, "unit": "secukupnya", "name": "Es serut atau es batu", "notes": None, "orderIndex": 4}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Sirup Gula Pandan", "instruction": "Didihkan air, gula pasir, dan daun pandan simpul di atas api sedang hingga gula larut sempurna dan harum pandan semerbak keluar. Matikan api dan biarkan sirup gula dingin pada suhu ruang.", "rawText": "Membuat Sirup Gula Pandan: Didihkan air, gula pasir, dan daun pandan simpul di atas api sedang hingga gula larut sempurna dan harum pandan semerbak keluar. Matikan api dan biarkan sirup gula dingin pada suhu ruang."},
            {"stepNumber": 2, "title": "Menyiapkan Kuah Santan Kelapa", "instruction": "Campurkan santan rebus yang sudah dingin dengan air kelapa muda segar, sirup gula pandan, dan sebagian kental manis. Aduk rata hingga tercipta kuah yang gurih beraroma kelapa alami.", "rawText": "Menyiapkan Kuah Santan Kelapa: Campurkan santan rebus yang sudah dingin dengan air kelapa muda segar, sirup gula pandan, dan sebagian kental manis. Aduk rata hingga tercipta kuah yang gurih beraroma kelapa alami."},
            {"stepNumber": 3, "title": "Menyiapkan Isian Buah", "instruction": "Keruk daging buah alpukat mentega secara rapi, serut daging kelapa muda memanjang lembut, dan potong dadu nangka kuning manis. Pastikan biji selasih sudah mengembang sempurna.", "rawText": "Menyiapkan Isian Buah: Keruk daging buah alpukat mentega secara rapi, serut daging kelapa muda memanjang lembut, dan potong dadu nangka kuning manis. Pastikan biji selasih sudah mengembang sempurna."},
            {"stepNumber": 4, "title": "Penyusunan Es Teler", "instruction": "Siapkan gelas saji tinggi atau mangkuk kaca. Masukkan potongan alpukat, daging kelapa muda serut, dan potongan nangka manis ke dalam wadah. Beri 1 sendok teh biji selasih di atasnya.", "rawText": "Penyusunan Es Teler: Siapkan gelas saji tinggi atau mangkuk kaca. Masukkan potongan alpukat, daging kelapa muda serut, dan potongan nangka manis ke dalam wadah. Beri 1 sendok teh biji selasih di atasnya."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Beri gunungan es serut menutupi buah-buahan, lalu siramkan kuah santan kelapa gurih di atas es serut hingga meresap ke dasar mangkuk. Kucuri bagian atas es dengan kental manis putih melingkar. Sajikan segera selagi dingin menyegarkan.", "rawText": "Penyajian: Beri gunungan es serut menutupi buah-buahan, lalu siramkan kuah santan kelapa gurih di atas es serut hingga meresap ke dasar mangkuk. Kucuri bagian atas es dengan kental manis putih melingkar. Sajikan segera selagi dingin menyegarkan."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 290 kkal | Protein 4g | Lemak 14g | Karbohidrat 42g. Kaya akan asam lemak tak jenuh tunggal yang menyehatkan jantung dari buah alpukat mentega, elektrolit alami peremaja sel tubuh dari air kelapa murni, serta vitamin C dari nangka segar.",
            "serving": "Per Porsi",
            "calories": 290,
            "protein": 4.0,
            "fat": 14.0,
            "carbohydrates": 42.0,
            "notes": "Kaya akan asam lemak tak jenuh tunggal yang menyehatkan jantung dari buah alpukat mentega, elektrolit alami peremaja sel tubuh dari air kelapa murni, serta vitamin C dari nangka segar."
        }
    },
    {
        "recipeNumber": 190,
        "title": "190. Wedang Ronde Khas Yogyakarta (DI Yogyakarta)",
        "name": "Wedang Ronde Yogyakarta",
        "slug": "wedang-ronde-yogyakarta",
        "scope": "INDONESIA",
        "origin": "DI Yogyakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 40,
        "cookTimeMinutes": 30,
        "servings": 4,
        "difficulty": "MEDIUM",
        "spicinessLevel": 0,
        "categorySlug": "minuman-segar",
        "cuisineTypeSlug": "kudapan-minuman-tradisional",
        "rawContent": """190. Wedang Ronde Khas Yogyakarta (DI Yogyakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Kulit Bola Ronde:
200g Tepung ketan putih berkualitas
25g Tepung tapioka / sagu tani
175 ml Air hangat suam-suam kuku
1/4 sdt Garam halus
Pewarna makanan alami merah muda dan hijau pandan secukupnya (sebagian adonan dibiarkan putih)
Bahan Isian Kacang Manis:
100g Kacang tanah tanpa kulit (sangrai hingga matang harum, tumbuk kasar)
50g Gula aren / gula pasir
1/4 sdt Garam halus
1-2 sdm Air hangat (untuk memadatkan isian)
Bahan Kuah Jahe Rempah Hangat:
1 liter Air bersih
150g Jahe emprit atau jahe merah (bakar di atas api, memarkan)
2 batang Serai (memarkan)
2 lembar Daun pandan (ikat simpul)
1 batang Kayu manis (sekitar 3 cm)
120g Gula merah aren (sisir halus)
30g Gula pasir
1/4 sdt Garam halus
Bahan Pelengkap Wedang:
50g Kolang-kaling (rebus empuk, iris tipis memanjang)
2 lembar Roti tawar (potong dadu 1 cm)
30g Kacang tanah sangrai renyah tanpa kulit
Langkah-Langkah Pembuatan:
Membuat Isian Kacang: Campurkan kacang tanah sangrai tumbuk kasar, gula aren sisir, garam, dan 1 sendok makan air hangat. Aduk dan tekan-tekan hingga adonan padat kalis. Bentuk menjadi bulatan-bulatan kecil seukuran kelereng kecil (sekitar 3-4 gram per butir). Sisihkan di atas piring.
Membuat Adonan Kulit Ronde: Campurkan tepung ketan, tepung tapioka, dan garam dalam mangkuk. Tuangkan air hangat sedikit demi sedikit sambil diuleni dengan tangan hingga adonan kalis, elastis, dan mudah dibentuk. Bagi adonan menjadi 3 bagian: 1 bagian diberi setetes pewarna merah muda, 1 bagian diberi pewarna hijau, dan 1 bagian dibiarkan putih alami.
Membentuk Bola Ronde: Ambil sekitar 12-15 gram adonan kulit, bulatkan lalu pipihkan cekung dengan ibu jari. Letakkan bulatan isian kacang di tengahnya, lalu tutup rapat kulit ketan dan putar di telapak tangan hingga membentuk bola bulat licin kedap tanpa celah agar tidak bocor saat direbus.
Merebus Bola Ronde: Didihkan air yang banyak dalam panci. Masukkan bola-bola ronde ke dalam air mendidih. Masak hingga bola ronde terapung ke permukaan air (tanda adonan ketan telah matang sempurna hingga ke bagian dalam). Angkat menggunakan saringan dan rendam sejenak dalam air matang dingin agar tidak saling menempel.
Membuat Kuah Jahe Rempah: Didihkan 1 liter air bersama jahe bakar memarkan, serai, daun pandan simpul, dan kayu manis di atas api sedang selama 15 menit agar sari pedas hangat jahe keluar maksimal. Masukkan gula merah aren sisir, gula pasir, dan sedikit garam. Aduk hingga gula larut sempurna. Cicipi hingga terasa hangat pedas menggigit yang manis legit. Saring kuah jahe agar bersih bening.
Penyajian: Siapkan mangkuk saji keramik kecil. Masukkan masing-masing varian warna bola ronde (merah, hijau, putih) ke dalam mangkuk. Tambahkan irisan kolang-kaling, potongan dadu roti tawar, dan taburan kacang tanah sangrai renyah. Siramkan kuah jahe rempah mendidih panas ke dalam mangkuk. Sajikan hangat mengepul untuk menghangatkan tubuh di malam hari atau cuaca dingin.
Nutrisi (Per Porsi Mangkuk): Kalori 270 kkal | Protein 6g | Lemak 7g | Karbohidrat 48g. Minuman herbal penghangat tubuh tradisional yang kaya gingerol dan shogaol dari jahe alami untuk meredakan inflamasi serta meningkatkan sirkulasi darah, dipadukan energi karbohidrat dari ketan lembut.""",
        "ingredientGroups": [
            {
                "name": "Bahan Kulit Bola Ronde",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "200g Tepung ketan putih", "amount": 200.0, "unit": "g", "name": "Tepung ketan putih", "notes": "berkualitas", "orderIndex": 1},
                    {"rawText": "25g Tepung tapioka / sagu tani", "amount": 25.0, "unit": "g", "name": "Tepung tapioka", "notes": "atau sagu tani", "orderIndex": 2},
                    {"rawText": "175 ml Air hangat", "amount": 175.0, "unit": "ml", "name": "Air hangat", "notes": "suam kuku", "orderIndex": 3},
                    {"rawText": "1/4 sdt Garam halus", "amount": 0.25, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 4},
                    {"rawText": "Pewarna alami merah muda dan hijau pandan secukupnya", "amount": None, "unit": "secukupnya", "name": "Pewarna makanan alami", "notes": "merah muda dan hijau pandan", "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Isian Kacang Manis",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "100g Kacang tanah tanpa kulit (sangrai, tumbuk kasar)", "amount": 100.0, "unit": "g", "name": "Kacang tanah tanpa kulit", "notes": "sangrai, tumbuk kasar", "orderIndex": 1},
                    {"rawText": "50g Gula aren / gula pasir", "amount": 50.0, "unit": "g", "name": "Gula aren atau gula pasir", "notes": None, "orderIndex": 2},
                    {"rawText": "1/4 sdt Garam halus", "amount": 0.25, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 3},
                    {"rawText": "1-2 sdm Air hangat", "amount": 1.5, "unit": "sdm", "name": "Air hangat", "notes": "untuk memadatkan isian", "orderIndex": 4}
                ]
            },
            {
                "name": "Bahan Kuah Jahe Rempah Hangat",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "1 liter Air bersih", "amount": 1.0, "unit": "liter", "name": "Air bersih", "notes": None, "orderIndex": 1},
                    {"rawText": "150g Jahe emprit atau jahe merah (bakar, memarkan)", "amount": 150.0, "unit": "g", "name": "Jahe emprit atau jahe merah", "notes": "bakar, memarkan", "orderIndex": 2},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 3},
                    {"rawText": "2 lembar Daun pandan (ikat simpul)", "amount": 2.0, "unit": "lembar", "name": "Daun pandan", "notes": "ikat simpul", "orderIndex": 4},
                    {"rawText": "1 batang Kayu manis (sekitar 3 cm)", "amount": 1.0, "unit": "batang", "name": "Kayu manis", "notes": "sekitar 3 cm", "orderIndex": 5},
                    {"rawText": "120g Gula merah aren (sisir halus)", "amount": 120.0, "unit": "g", "name": "Gula merah aren", "notes": "sisir halus", "orderIndex": 6},
                    {"rawText": "30g Gula pasir", "amount": 30.0, "unit": "g", "name": "Gula pasir", "notes": None, "orderIndex": 7},
                    {"rawText": "1/4 sdt Garam halus", "amount": 0.25, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 8}
                ]
            },
            {
                "name": "Bahan Pelengkap Wedang",
                "orderIndex": 4,
                "ingredients": [
                    {"rawText": "50g Kolang-kaling (rebus empuk, iris tipis)", "amount": 50.0, "unit": "g", "name": "Kolang-kaling", "notes": "rebus empuk, iris tipis", "orderIndex": 1},
                    {"rawText": "2 lembar Roti tawar (potong dadu 1 cm)", "amount": 2.0, "unit": "lembar", "name": "Roti tawar", "notes": "potong dadu 1 cm", "orderIndex": 2},
                    {"rawText": "30g Kacang tanah sangrai renyah", "amount": 30.0, "unit": "g", "name": "Kacang tanah sangrai", "notes": "renyah tanpa kulit", "orderIndex": 3}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Isian Kacang", "instruction": "Campurkan kacang tanah sangrai tumbuk kasar, gula aren sisir, garam, dan 1 sendok makan air hangat. Aduk dan tekan-tekan hingga adonan padat kalis. Bentuk menjadi bulatan-bulatan kecil seukuran kelereng kecil (sekitar 3-4 gram per butir). Sisihkan di atas piring.", "rawText": "Membuat Isian Kacang: Campurkan kacang tanah sangrai tumbuk kasar, gula aren sisir, garam, dan 1 sendok makan air hangat. Aduk dan tekan-tekan hingga adonan padat kalis. Bentuk menjadi bulatan-bulatan kecil seukuran kelereng kecil (sekitar 3-4 gram per butir). Sisihkan di atas piring."},
            {"stepNumber": 2, "title": "Membuat Adonan Kulit Ronde", "instruction": "Campurkan tepung ketan, tepung tapioka, dan garam dalam mangkuk. Tuangkan air hangat sedikit demi sedikit sambil diuleni dengan tangan hingga adonan kalis, elastis, dan mudah dibentuk. Bagi adonan menjadi 3 bagian: 1 bagian diberi setetes pewarna merah muda, 1 bagian diberi pewarna hijau, dan 1 bagian dibiarkan putih alami.", "rawText": "Membuat Adonan Kulit Ronde: Campurkan tepung ketan, tepung tapioka, dan garam dalam mangkuk. Tuangkan air hangat sedikit demi sedikit sambil diuleni dengan tangan hingga adonan kalis, elastis, dan mudah dibentuk. Bagi adonan menjadi 3 bagian: 1 bagian diberi setetes pewarna merah muda, 1 bagian diberi pewarna hijau, dan 1 bagian dibiarkan putih alami."},
            {"stepNumber": 3, "title": "Membentuk Bola Ronde", "instruction": "Ambil sekitar 12-15 gram adonan kulit, bulatkan lalu pipihkan cekung dengan ibu jari. Letakkan bulatan isian kacang di tengahnya, lalu tutup rapat kulit ketan dan putar di telapak tangan hingga membentuk bola bulat licin kedap tanpa celah agar tidak bocor saat direbus.", "rawText": "Membentuk Bola Ronde: Ambil sekitar 12-15 gram adonan kulit, bulatkan lalu pipihkan cekung dengan ibu jari. Letakkan bulatan isian kacang di tengahnya, lalu tutup rapat kulit ketan dan putar di telapak tangan hingga membentuk bola bulat licin kedap tanpa celah agar tidak bocor saat direbus."},
            {"stepNumber": 4, "title": "Merebus Bola Ronde", "instruction": "Didihkan air yang banyak dalam panci. Masukkan bola-bola ronde ke dalam air mendidih. Masak hingga bola ronde terapung ke permukaan air (tanda adonan ketan telah matang sempurna hingga ke bagian dalam). Angkat menggunakan saringan dan rendam sejenak dalam air matang dingin agar tidak saling menempel.", "rawText": "Merebus Bola Ronde: Didihkan air yang banyak dalam panci. Masukkan bola-bola ronde ke dalam air mendidih. Masak hingga bola ronde terapung ke permukaan air (tanda adonan ketan telah matang sempurna hingga ke bagian dalam). Angkat menggunakan saringan dan rendam sejenak dalam air matang dingin agar tidak saling menempel."},
            {"stepNumber": 5, "title": "Membuat Kuah Jahe Rempah", "instruction": "Didihkan 1 liter air bersama jahe bakar memarkan, serai, daun pandan simpul, dan kayu manis di atas api sedang selama 15 menit agar sari pedas hangat jahe keluar maksimal. Masukkan gula merah aren sisir, gula pasir, dan sedikit garam. Aduk hingga gula larut sempurna. Saring kuah jahe agar bersih bening.", "rawText": "Membuat Kuah Jahe Rempah: Didihkan 1 liter air bersama jahe bakar memarkan, serai, daun pandan simpul, dan kayu manis di atas api sedang selama 15 menit agar sari pedas hangat jahe keluar maksimal. Masukkan gula merah aren sisir, gula pasir, dan sedikit garam. Aduk hingga gula larut sempurna. Saring kuah jahe agar bersih bening."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Siapkan mangkuk saji keramik kecil. Masukkan masing-masing varian warna bola ronde (merah, hijau, putih) ke dalam mangkuk. Tambahkan irisan kolang-kaling, potongan dadu roti tawar, dan taburan kacang tanah sangrai renyah. Siramkan kuah jahe rempah mendidih panas ke dalam mangkuk. Sajikan hangat mengepul.", "rawText": "Penyajian: Siapkan mangkuk saji keramik kecil. Masukkan masing-masing varian warna bola ronde (merah, hijau, putih) ke dalam mangkuk. Tambahkan irisan kolang-kaling, potongan dadu roti tawar, dan taburan kacang tanah sangrai renyah. Siramkan kuah jahe rempah mendidih panas ke dalam mangkuk. Sajikan hangat mengepul."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi Mangkuk): Kalori 270 kkal | Protein 6g | Lemak 7g | Karbohidrat 48g. Minuman herbal penghangat tubuh tradisional yang kaya gingerol dan shogaol dari jahe alami untuk meredakan inflamasi serta meningkatkan sirkulasi darah, dipadukan energi karbohidrat dari ketan lembut.",
            "serving": "Per Porsi Mangkuk",
            "calories": 270,
            "protein": 6.0,
            "fat": 7.0,
            "carbohydrates": 48.0,
            "notes": "Minuman herbal penghangat tubuh tradisional yang kaya gingerol dan shogaol dari jahe alami untuk meredakan inflamasi serta meningkatkan sirkulasi darah, dipadukan energi karbohidrat dari ketan lembut."
        }
    }
]

# Load existing JSON
file_path = os.path.join(os.path.dirname(__file__), '../src/seeder/recipes-data.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter out if any 181-190 already exist to be idempotent
data['recipes'] = [r for r in data['recipes'] if r['recipeNumber'] < 181]

# Append new recipes
data['recipes'].extend(new_recipes)

# Save back to JSON
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total_count = len(data['recipes'])
print(f"Berhasil menambahkan 10 resep baru! Total resep saat ini: {total_count}")

