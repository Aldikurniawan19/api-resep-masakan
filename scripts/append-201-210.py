import json
import os

new_recipes = [
    {
        "recipeNumber": 201,
        "title": "201. Ayam Goreng Lengkuas Khas Sunda (Jawa Barat)",
        "name": "Ayam Goreng Lengkuas",
        "slug": "ayam-goreng-lengkuas",
        "scope": "INDONESIA",
        "origin": "Jawa Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 25,
        "cookTimeMinutes": 40,
        "servings": 5,
        "difficulty": "MEDIUM",
        "spicinessLevel": 1,
        "categorySlug": "ayam-unggas",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """201. Ayam Goreng Lengkuas Khas Sunda (Jawa Barat)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
1 ekor Ayam pejantan / ayam kampung (potong menjadi 8-10 bagian, cuci bersih)
250g Lengkuas muda (kupas, parut kasar memanjang untuk menciptakan serundeng serat renyah)
500 ml Air kelapa murni (atau air bersih biasa)
Minyak kelapa sawit secukupnya untuk deep fry
Bumbu Rempah Daun:
2 batang Serai (memarkan)
4 lembar Daun salam kering
4 lembar Daun jeruk purut (sobek buang tulang daun)
Bumbu Halus Ungkep:
10 butir Bawang merah
6 siung Bawang putih
4 cm Kunyit segar (bakar kupas)
3 cm Jahe
1 sdm Ketumbar butiran (sangrai)
4 butir Kemiri (sangrai)
1.5 sdt Garam halus
1 sdt Kaldu jamur / ayam bubuk
1/2 sdt Merica bubuk
Langkah-Langkah Pembuatan:
Mengungkep Ayam dan Lengkuas: Masukkan potongan ayam ke dalam wajan besar. Tambahkan parutan lengkuas, bumbu halus, serai memarkan, daun salam, dan daun jeruk. Tuangkan air kelapa murni. Aduk rata hingga seluruh bumbu membaluri ayam. Masak di atas api sedang hingga mendidih.
Mengecilkan Api dan Meresapkan Bumbu: Kecilkan api kompor ke tingkat sedang-rendah. Tutup wajan dan ungkep ayam selama 30-35 menit hingga cairan menyusut hampir habis, daging ayam empuk, dan bumbu kuning meresap ke dalam pori-pori daging serta serat lengkuas.
Meniriskan Ayam dan Bumbu Lengkuas: Angkat potongan ayam dari wajan. Tiriskan sisa parutan lengkuas menggunakan saringan kawat halus sambil sedikit ditekan agar tidak terlalu basah saat digoreng nantinya.
Menggoreng Ayam: Panaskan minyak goreng yang cukup banyak dalam wajan cekung di atas api sedang. Goreng potongan ayam ungkep hingga berwarna kuning kecokelatan keemasan dan kulitnya kering harum. Angkat dan tiriskan di atas peniris kawat.
Menggoreng Serundeng Lengkuas: Goreng parutan bumbu lengkuas dalam minyak panas menggunakan api sedang cenderung kecil sambil terus diaduk perlahan agar matang merata. Saat busa minyak mulai hilang dan serundeng lengkuas berwarna cokelat keemasan renyah (crispy), segera angkat dan saring dengan saringan halus agar tidak gosong. Tiriskan minyaknya di atas kertas serap.
Penyajian: Tata ayam goreng di piring saji, taburkan serundeng lengkuas renyah melimpah di atas permukaan ayam. Sajikan hangat bersama nasi putih pulen, lalapan segar, dan sambal terasi terasi goreng.
Nutrisi (Per Porsi): Kalori 310 kkal | Protein 28g | Lemak 18g | Karbohidrat 8g. Sumber protein hewani berkualitas tinggi dipadukan khasiat anti-inflamasi alami dari senyawa galangin pada lengkuas segar yang membantu melancarkan pencernaan.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "1 ekor Ayam pejantan / kampung (potong 8-10)", "amount": 1.0, "unit": "ekor", "name": "Ayam pejantan", "notes": "potong 8-10 bagian", "orderIndex": 1},
                    {"rawText": "250g Lengkuas muda (parut kasar memanjang)", "amount": 250.0, "unit": "g", "name": "Lengkuas muda", "notes": "parut kasar memanjang", "orderIndex": 2},
                    {"rawText": "500 ml Air kelapa murni", "amount": 500.0, "unit": "ml", "name": "Air kelapa murni", "notes": "atau air biasa", "orderIndex": 3},
                    {"rawText": "Minyak kelapa sawit secukupnya untuk deep fry", "amount": None, "unit": "secukupnya", "name": "Minyak kelapa sawit", "notes": "untuk menggoreng", "orderIndex": 4}
                ]
            },
            {
                "name": "Bumbu Rempah Daun",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 1},
                    {"rawText": "4 lembar Daun salam kering", "amount": 4.0, "unit": "lembar", "name": "Daun salam kering", "notes": None, "orderIndex": 2},
                    {"rawText": "4 lembar Daun jeruk purut", "amount": 4.0, "unit": "lembar", "name": "Daun jeruk purut", "notes": "buang tulang", "orderIndex": 3}
                ]
            },
            {
                "name": "Bumbu Halus Ungkep",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "10 butir Bawang merah", "amount": 10.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "6 siung Bawang putih", "amount": 6.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "4 cm Kunyit segar (bakar kupas)", "amount": 4.0, "unit": "cm", "name": "Kunyit segar", "notes": "bakar kupas", "orderIndex": 3},
                    {"rawText": "3 cm Jahe", "amount": 3.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 4},
                    {"rawText": "1 sdm Ketumbar butiran (sangrai)", "amount": 1.0, "unit": "sdm", "name": "Ketumbar butiran", "notes": "sangrai", "orderIndex": 5},
                    {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 6},
                    {"rawText": "1.5 sdt Garam halus", "amount": 1.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 7},
                    {"rawText": "1 sdt Kaldu jamur / ayam bubuk", "amount": 1.0, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 8},
                    {"rawText": "1/2 sdt Merica bubuk", "amount": 0.5, "unit": "sdt", "name": "Merica bubuk", "notes": None, "orderIndex": 9}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Mengungkep Ayam dan Lengkuas", "instruction": "Masukkan potongan ayam ke dalam wajan besar. Tambahkan parutan lengkuas, bumbu halus, serai memarkan, daun salam, dan daun jeruk. Tuangkan air kelapa murni. Aduk rata hingga seluruh bumbu membaluri ayam. Masak di atas api sedang hingga mendidih.", "rawText": "Mengungkep Ayam dan Lengkuas: Masukkan potongan ayam ke dalam wajan besar. Tambahkan parutan lengkuas, bumbu halus, serai memarkan, daun salam, dan daun jeruk. Tuangkan air kelapa murni. Aduk rata hingga seluruh bumbu membaluri ayam. Masak di atas api sedang hingga mendidih."},
            {"stepNumber": 2, "title": "Mengecilkan Api dan Meresapkan Bumbu", "instruction": "Kecilkan api kompor ke tingkat sedang-rendah. Tutup wajan dan ungkep ayam selama 30-35 menit hingga cairan menyusut hampir habis, daging ayam empuk, dan bumbu kuning meresap ke dalam pori-pori daging serta serat lengkuas.", "rawText": "Mengecilkan Api dan Meresapkan Bumbu: Kecilkan api kompor ke tingkat sedang-rendah. Tutup wajan dan ungkep ayam selama 30-35 menit hingga cairan menyusut hampir habis, daging ayam empuk, dan bumbu kuning meresap ke dalam pori-pori daging serta serat lengkuas."},
            {"stepNumber": 3, "title": "Meniriskan Ayam dan Bumbu Lengkuas", "instruction": "Angkat potongan ayam dari wajan. Tiriskan sisa parutan lengkuas menggunakan saringan kawat halus sambil sedikit ditekan agar tidak terlalu basah saat digoreng nantinya.", "rawText": "Meniriskan Ayam dan Bumbu Lengkuas: Angkat potongan ayam dari wajan. Tiriskan sisa parutan lengkuas menggunakan saringan kawat halus sambil sedikit ditekan agar tidak terlalu basah saat digoreng nantinya."},
            {"stepNumber": 4, "title": "Menggoreng Ayam", "instruction": "Panaskan minyak goreng yang cukup banyak dalam wajan cekung di atas api sedang. Goreng potongan ayam ungkep hingga berwarna kuning kecokelatan keemasan dan kulitnya kering harum. Angkat dan tiriskan di atas peniris kawat.", "rawText": "Menggoreng Ayam: Panaskan minyak goreng yang cukup banyak dalam wajan cekung di atas api sedang. Goreng potongan ayam ungkep hingga berwarna kuning kecokelatan keemasan dan kulitnya kering harum. Angkat dan tiriskan di atas peniris kawat."},
            {"stepNumber": 5, "title": "Menggoreng Serundeng Lengkuas", "instruction": "Goreng parutan bumbu lengkuas dalam minyak panas menggunakan api sedang cenderung kecil sambil terus diaduk perlahan agar matang merata. Saat berwarna cokelat keemasan renyah, segera angkat dan saring dengan saringan halus agar tidak gosong.", "rawText": "Menggoreng Serundeng Lengkuas: Goreng parutan bumbu lengkuas dalam minyak panas menggunakan api sedang cenderung kecil sambil terus diaduk perlahan agar matang merata. Saat berwarna cokelat keemasan renyah, segera angkat dan saring dengan saringan halus agar tidak gosong."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Tata ayam goreng di piring saji, taburkan serundeng lengkuas renyah melimpah di atas permukaan ayam. Sajikan hangat bersama nasi putih pulen, lalapan segar, dan sambal terasi.", "rawText": "Penyajian: Tata ayam goreng di piring saji, taburkan serundeng lengkuas renyah melimpah di atas permukaan ayam. Sajikan hangat bersama nasi putih pulen, lalapan segar, dan sambal terasi."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 310 kkal | Protein 28g | Lemak 18g | Karbohidrat 8g. Sumber protein hewani berkualitas tinggi dipadukan khasiat anti-inflamasi alami dari senyawa galangin pada lengkuas segar yang membantu melancarkan pencernaan.",
            "serving": "Per Porsi",
            "calories": 310,
            "protein": 28.0,
            "fat": 18.0,
            "carbohydrates": 8.0,
            "notes": "Sumber protein hewani berkualitas tinggi dipadukan khasiat anti-inflamasi alami dari senyawa galangin pada lengkuas segar yang membantu melancarkan pencernaan."
        }
    },
    {
        "recipeNumber": 202,
        "title": "202. Semur Daging Sapi Kentang Khas Betawi (DKI Jakarta)",
        "name": "Semur Daging Sapi Kentang Betawi",
        "slug": "semur-daging-kentang-betawi",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 25,
        "cookTimeMinutes": 60,
        "servings": 5,
        "difficulty": "MEDIUM",
        "spicinessLevel": 1,
        "categorySlug": "daging-sapi-kambing",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """202. Semur Daging Sapi Kentang Khas Betawi (DKI Jakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Daging sapi sengkel / has luar (potong melebar tebal 1.5 cm)
300g Kentang (kupas, potong dadu besar, goreng setengah matang)
1 liter Air kaldu daging
8 sdm Kecap manis kental gurih berkualitas
3 sdm Minyak goreng untuk menumis
Bahan Rempah Aromatik Semur:
1/2 butir Biji pala (parut halus)
4 butir Cengkih utuh
4 cm Kayu manis batangan
2 batang Serai (memarkan)
3 lembar Daun salam kering
Bumbu Halus:
8 butir Bawang merah
5 siung Bawang putih
4 butir Kemiri (sangrai)
3 cm Jahe
1 sdt Merica putih butiran
1.5 sdt Garam halus
1 sdm Gula merah aren (sisir)
1/2 sdt Kaldu jamur / penyedap
Bahan Pelengkap:
2 sdm Bawang merah goreng renyah
Sambal cabai rawit kecap secukupnya
Langkah-Langkah Pembuatan:
Menumis Bumbu Halus dan Rempah: Panaskan 3 sendok makan minyak dalam wajan atau panci tebal. Masukkan bumbu halus bersama serai memarkan, daun salam, cengkih, kayu manis, dan parutan biji pala. Tumis di atas api sedang hingga bumbu benar-benar harum matang tanak dan tidak langu.
Memasak Daging: Masukkan potongan daging sapi ke dalam tumisan bumbu. Aduk rata hingga daging berubah warna dan pori-porinya mengunci sari gurih daging (sekitar 5 menit).
Menuang Kecap dan Merebus Perlahan: Tuangkan kecap manis kental ke atas daging, aduk rata hingga seluruh daging terlumuri warna cokelat pekat harum. Tuangkan air kaldu daging. Masak di atas api sedang hingga mendidih.
Proses Pengempukan Daging (Simmering): Kecilkan api kompor ke tingkat minimal, tutup panci, dan masak perlahan selama 45 menit hingga daging sapi menjadi sangat empuk dan bumbu semur meresap pekat ke dalam serat daging.
Memasukkan Kentang Goreng: Masukkan potongan kentang yang sudah digoreng setengah matang ke dalam kuah semur. Bumbui dengan garam, gula aren, dan kaldu jamur. Masak kembali selama 15 menit hingga kuah semur mengental kecokelatan mengilat dan kentang empuk meresap. Cicipi dan angkat.
Penyajian: Tuangkan semur daging sapi kentang ke dalam piring atau mangkuk saji saji. Taburi bawang merah goreng renyah di atasnya. Sajikan hangat bersama nasi putih pulen dan emping melinjo.
Nutrisi (Per Porsi): Kalori 320 kkal | Protein 26g | Lemak 14g | Karbohidrat 24g. Kaya protein lengkap dan zat besi heme dari daging sapi untuk pembentukan sel darah merah, berpadu karbohidrat potasium dari kentang dan senyawa myristicin penenang dari pala alami.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "500g Daging sapi sengkel / has luar (potong 1.5 cm)", "amount": 500.0, "unit": "g", "name": "Daging sapi sengkel", "notes": "potong tebal 1.5 cm", "orderIndex": 1},
                    {"rawText": "300g Kentang (potong dadu besar, goreng setengah matang)", "amount": 300.0, "unit": "g", "name": "Kentang", "notes": "potong dadu besar, goreng", "orderIndex": 2},
                    {"rawText": "1 liter Air kaldu daging", "amount": 1.0, "unit": "liter", "name": "Air kaldu daging", "notes": None, "orderIndex": 3},
                    {"rawText": "8 sdm Kecap manis kental gurih", "amount": 8.0, "unit": "sdm", "name": "Kecap manis", "notes": "kental gurih", "orderIndex": 4},
                    {"rawText": "3 sdm Minyak goreng untuk menumis", "amount": 3.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Rempah Aromatik Semur",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "1/2 butir Biji pala (parut halus)", "amount": 0.5, "unit": "butir", "name": "Biji pala", "notes": "parut halus", "orderIndex": 1},
                    {"rawText": "4 butir Cengkih utuh", "amount": 4.0, "unit": "butir", "name": "Cengkih utuh", "notes": None, "orderIndex": 2},
                    {"rawText": "4 cm Kayu manis batangan", "amount": 4.0, "unit": "cm", "name": "Kayu manis batangan", "notes": None, "orderIndex": 3},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 4},
                    {"rawText": "3 lembar Daun salam kering", "amount": 3.0, "unit": "lembar", "name": "Daun salam kering", "notes": None, "orderIndex": 5}
                ]
            },
            {
                "name": "Bumbu Halus",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "8 butir Bawang merah", "amount": 8.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 3},
                    {"rawText": "3 cm Jahe", "amount": 3.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 4},
                    {"rawText": "1 sdt Merica putih butiran", "amount": 1.0, "unit": "sdt", "name": "Merica putih butiran", "notes": None, "orderIndex": 5},
                    {"rawText": "1.5 sdt Garam halus", "amount": 1.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 6},
                    {"rawText": "1 sdm Gula merah aren (sisir)", "amount": 1.0, "unit": "sdm", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 7},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 8}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menumis Bumbu Halus dan Rempah", "instruction": "Panaskan 3 sendok makan minyak dalam wajan tebal. Masukkan bumbu halus bersama serai memarkan, daun salam, cengkih, kayu manis, dan parutan biji pala. Tumis di atas api sedang hingga bumbu benar-benar harum matang tanak dan tidak langu.", "rawText": "Menumis Bumbu Halus dan Rempah: Panaskan 3 sendok makan minyak dalam wajan tebal. Masukkan bumbu halus bersama serai memarkan, daun salam, cengkih, kayu manis, dan parutan biji pala. Tumis di atas api sedang hingga bumbu benar-benar harum matang tanak dan tidak langu."},
            {"stepNumber": 2, "title": "Memasak Daging", "instruction": "Masukkan potongan daging sapi ke dalam tumisan bumbu. Aduk rata hingga daging berubah warna dan pori-porinya mengunci sari gurih daging sekitar 5 menit.", "rawText": "Memasak Daging: Masukkan potongan daging sapi ke dalam tumisan bumbu. Aduk rata hingga daging berubah warna dan pori-porinya mengunci sari gurih daging sekitar 5 menit."},
            {"stepNumber": 3, "title": "Menuang Kecap dan Merebus Perlahan", "instruction": "Tuangkan kecap manis kental ke atas daging, aduk rata hingga seluruh daging terlumuri warna cokelat pekat harum. Tuangkan air kaldu daging. Masak di atas api sedang hingga mendidih.", "rawText": "Menuang Kecap dan Merebus Perlahan: Tuangkan kecap manis kental ke atas daging, aduk rata hingga seluruh daging terlumuri warna cokelat pekat harum. Tuangkan air kaldu daging. Masak di atas api sedang hingga mendidih."},
            {"stepNumber": 4, "title": "Proses Pengempukan Daging (Simmering)", "instruction": "Kecilkan api kompor ke tingkat minimal, tutup panci, dan masak perlahan selama 45 menit hingga daging sapi menjadi sangat empuk dan bumbu semur meresap pekat ke dalam serat daging.", "rawText": "Proses Pengempukan Daging (Simmering): Kecilkan api kompor ke tingkat minimal, tutup panci, dan masak perlahan selama 45 menit hingga daging sapi menjadi sangat empuk dan bumbu semur meresap pekat ke dalam serat daging."},
            {"stepNumber": 5, "title": "Memasukkan Kentang Goreng", "instruction": "Masukkan potongan kentang yang sudah digoreng setengah matang ke dalam kuah semur. Bumbui dengan garam, gula aren, dan kaldu jamur. Masak kembali selama 15 menit hingga kuah semur mengental kecokelatan mengilat dan kentang empuk meresap.", "rawText": "Memasukkan Kentang Goreng: Masukkan potongan kentang yang sudah digoreng setengah matang ke dalam kuah semur. Bumbui dengan garam, gula aren, dan kaldu jamur. Masak kembali selama 15 menit hingga kuah semur mengental kecokelatan mengilat dan kentang empuk meresap."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Tuangkan semur daging sapi kentang ke dalam mangkuk saji. Taburi bawang merah goreng renyah di atasnya. Sajikan hangat bersama nasi putih pulen.", "rawText": "Penyajian: Tuangkan semur daging sapi kentang ke dalam mangkuk saji. Taburi bawang merah goreng renyah di atasnya. Sajikan hangat bersama nasi putih pulen."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 320 kkal | Protein 26g | Lemak 14g | Karbohidrat 24g. Kaya protein lengkap dan zat besi heme dari daging sapi untuk pembentukan sel darah merah, berpadu karbohidrat potasium dari kentang dan senyawa myristicin penenang dari pala alami.",
            "serving": "Per Porsi",
            "calories": 320,
            "protein": 26.0,
            "fat": 14.0,
            "carbohydrates": 24.0,
            "notes": "Kaya protein lengkap dan zat besi heme dari daging sapi untuk pembentukan sel darah merah, berpadu karbohidrat potasium dari kentang dan senyawa myristicin penenang dari pala alami."
        }
    },
    {
        "recipeNumber": 203,
        "title": "203. Ikan Kembung Goreng Sambal Dabu-Dabu (Sulawesi Utara)",
        "name": "Ikan Kembung Sambal Dabu-Dabu",
        "slug": "ikan-kembung-dabu-dabu",
        "scope": "INDONESIA",
        "origin": "Sulawesi Utara",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 15,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 3,
        "categorySlug": "ikan-seafood",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """203. Ikan Kembung Goreng Sambal Dabu-Dabu (Sulawesi Utara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama Ikan:
4 ekor Ikan kembung banjar segar (bersihkan insang dan isi perut, cuci bersih, kerat-kerat badannya)
1 buah Jeruk nipis (peras airnya untuk melumuri ikan)
1 sdt Kunyit bubuk
1 sdt Ketumbar bubuk
1 sdt Garam halus
Minyak goreng secukupnya untuk menggoreng ikan
Bahan Sambal Dabu-Dabu Iris:
10 buah Cabai rawit merah (iris tipis)
8 buah Cabai rawit hijau (iris tipis)
6 butir Bawang merah (iris tipis)
2 buah Tomat merah matang (buang biji, potong dadu kecil)
2 buah Tomat hijau segar (potong dadu kecil)
1/2 sdt Garam halus
1/2 sdt Gula pasir
2 buah Jeruk limau / jeruk kasturi (peras airnya)
4 sdm Minyak kelapa sawit panas mendidih
Langkah-Langkah Pembuatan:
Marinasi Ikan: Lumuri ikan kembung bersih dengan perasan air jeruk nipis, kunyit bubuk, ketumbar bubuk, dan garam hingga merata ke celah keratan badan ikan. Diamkan selama 15 menit agar bumbu meresap dan bau amis hilang.
Menggoreng Ikan: Panaskan minyak banyak dalam wajan di atas api sedang. Masukkan ikan kembung secara perlahan. Goreng hingga matang berkulit renyah keemasan di kedua sisi namun daging bagian dalamnya tetap lembut juicy. Angkat dan tiriskan di atas piring saji.
Meracik Sambal Dabu-Dabu: Campurkan irisan cabai rawit merah, cabai rawit hijau, bawang merah, potongan tomat merah, dan tomat hijau ke dalam mangkuk kaca. Bumbui dengan garam, gula pasir, dan perasan air jeruk limau/kasturi. Aduk rata menggunakan sendok.
Menyiram Minyak Panas: Panaskan 4 sendok makan minyak goreng hingga benar-benar berasap panas mendidih. Siramkan minyak panas secara langsung ke atas campuran bahan sambal dabu-dabu (akan terdengar bunyi mendesis harum). Aduk cepat agar rasa bumbu menyatu segar dan layu sedikit.
Penyajian: Sendokkan sambal dabu-dabu segar beserta kuah minyak jeruk aromatiknya ke atas badan ikan kembung goreng yang masih hangat. Sajikan segera bersama nasi putih hangat.
Nutrisi (Per Porsi): Kalori 240 kkal | Protein 24g | Lemak 12g | Karbohidrat 6g. Ikan kembung merupakan salah satu sumber asam lemak omega-3 (DHA & EPA) tertinggi di antara ikan lokal, dipadukan vitamin C melimpah dari tomat dan cabai segar mentah.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama Ikan",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "4 ekor Ikan kembung banjar segar (bersihkan, kerat)", "amount": 4.0, "unit": "ekor", "name": "Ikan kembung banjar", "notes": "bersihkan, kerat-kerat badannya", "orderIndex": 1},
                    {"rawText": "1 buah Jeruk nipis (peras airnya)", "amount": 1.0, "unit": "buah", "name": "Jeruk nipis", "notes": "peras airnya", "orderIndex": 2},
                    {"rawText": "1 sdt Kunyit bubuk", "amount": 1.0, "unit": "sdt", "name": "Kunyit bubuk", "notes": None, "orderIndex": 3},
                    {"rawText": "1 sdt Ketumbar bubuk", "amount": 1.0, "unit": "sdt", "name": "Ketumbar bubuk", "notes": None, "orderIndex": 4},
                    {"rawText": "1 sdt Garam halus", "amount": 1.0, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 5},
                    {"rawText": "Minyak goreng secukupnya", "amount": None, "unit": "secukupnya", "name": "Minyak goreng", "notes": "untuk menggoreng ikan", "orderIndex": 6}
                ]
            },
            {
                "name": "Bahan Sambal Dabu-Dabu Iris",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "10 buah Cabai rawit merah (iris tipis)", "amount": 10.0, "unit": "buah", "name": "Cabai rawit merah", "notes": "iris tipis", "orderIndex": 1},
                    {"rawText": "8 buah Cabai rawit hijau (iris tipis)", "amount": 8.0, "unit": "buah", "name": "Cabai rawit hijau", "notes": "iris tipis", "orderIndex": 2},
                    {"rawText": "6 butir Bawang merah (iris tipis)", "amount": 6.0, "unit": "butir", "name": "Bawang merah", "notes": "iris tipis", "orderIndex": 3},
                    {"rawText": "2 buah Tomat merah matang (potong dadu kecil)", "amount": 2.0, "unit": "buah", "name": "Tomat merah matang", "notes": "potong dadu kecil", "orderIndex": 4},
                    {"rawText": "2 buah Tomat hijau segar (potong dadu kecil)", "amount": 2.0, "unit": "buah", "name": "Tomat hijau segar", "notes": "potong dadu kecil", "orderIndex": 5},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 6},
                    {"rawText": "1/2 sdt Gula pasir", "amount": 0.5, "unit": "sdt", "name": "Gula pasir", "notes": None, "orderIndex": 7},
                    {"rawText": "2 buah Jeruk limau / kasturi (peras)", "amount": 2.0, "unit": "buah", "name": "Jeruk limau", "notes": "peras airnya", "orderIndex": 8},
                    {"rawText": "4 sdm Minyak kelapa sawit panas mendidih", "amount": 4.0, "unit": "sdm", "name": "Minyak kelapa sawit", "notes": "panas mendidih", "orderIndex": 9}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Marinasi Ikan", "instruction": "Lumuri ikan kembung bersih dengan perasan air jeruk nipis, kunyit bubuk, ketumbar bubuk, dan garam hingga merata ke celah keratan badan ikan. Diamkan selama 15 menit agar bumbu meresap dan bau amis hilang.", "rawText": "Marinasi Ikan: Lumuri ikan kembung bersih dengan perasan air jeruk nipis, kunyit bubuk, ketumbar bubuk, dan garam hingga merata ke celah keratan badan ikan. Diamkan selama 15 menit agar bumbu meresap dan bau amis hilang."},
            {"stepNumber": 2, "title": "Menggoreng Ikan", "instruction": "Panaskan minyak banyak dalam wajan di atas api sedang. Masukkan ikan kembung secara perlahan. Goreng hingga matang berkulit renyah keemasan di kedua sisi namun daging bagian dalamnya tetap lembut juicy. Angkat dan tiriskan di atas piring saji.", "rawText": "Menggoreng Ikan: Panaskan minyak banyak dalam wajan di atas api sedang. Masukkan ikan kembung secara perlahan. Goreng hingga matang berkulit renyah keemasan di kedua sisi namun daging bagian dalamnya tetap lembut juicy. Angkat dan tiriskan di atas piring saji."},
            {"stepNumber": 3, "title": "Meracik Sambal Dabu-Dabu", "instruction": "Campurkan irisan cabai rawit merah, cabai rawit hijau, bawang merah, potongan tomat merah, dan tomat hijau ke dalam mangkuk kaca. Bumbui dengan garam, gula pasir, dan perasan air jeruk limau/kasturi. Aduk rata menggunakan sendok.", "rawText": "Meracik Sambal Dabu-Dabu: Campurkan irisan cabai rawit merah, cabai rawit hijau, bawang merah, potongan tomat merah, dan tomat hijau ke dalam mangkuk kaca. Bumbui dengan garam, gula pasir, dan perasan air jeruk limau/kasturi. Aduk rata menggunakan sendok."},
            {"stepNumber": 4, "title": "Menyiram Minyak Panas", "instruction": "Panaskan 4 sendok makan minyak goreng hingga benar-benar berasap panas mendidih. Siramkan minyak panas secara langsung ke atas campuran bahan sambal dabu-dabu. Aduk cepat agar rasa bumbu menyatu segar dan layu sedikit.", "rawText": "Menyiram Minyak Panas: Panaskan 4 sendok makan minyak goreng hingga benar-benar berasap panas mendidih. Siramkan minyak panas secara langsung ke atas campuran bahan sambal dabu-dabu. Aduk cepat agar rasa bumbu menyatu segar dan layu sedikit."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Sendokkan sambal dabu-dabu segar beserta kuah minyak jeruk aromatiknya ke atas badan ikan kembung goreng yang masih hangat. Sajikan segera bersama nasi putih hangat.", "rawText": "Penyajian: Sendokkan sambal dabu-dabu segar beserta kuah minyak jeruk aromatiknya ke atas badan ikan kembung goreng yang masih hangat. Sajikan segera bersama nasi putih hangat."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 240 kkal | Protein 24g | Lemak 12g | Karbohidrat 6g. Ikan kembung merupakan salah satu sumber asam lemak omega-3 (DHA & EPA) tertinggi di antara ikan lokal, dipadukan vitamin C melimpah dari tomat dan cabai segar mentah.",
            "serving": "Per Porsi",
            "calories": 240,
            "protein": 24.0,
            "fat": 12.0,
            "carbohydrates": 6.0,
            "notes": "Ikan kembung merupakan salah satu sumber asam lemak omega-3 (DHA & EPA) tertinggi di antara ikan lokal, dipadukan vitamin C melimpah dari tomat dan cabai segar mentah."
        }
    },
    {
        "recipeNumber": 204,
        "title": "204. Sayur Oyong Soun Bakso Telur Puyuh (Nusantara)",
        "name": "Sayur Oyong Soun Bakso",
        "slug": "sayur-oyong-soun-bakso",
        "scope": "INDONESIA",
        "origin": "Jawa Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 15,
        "cookTimeMinutes": 15,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 0,
        "categorySlug": "sup-soto",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """204. Sayur Oyong Soun Bakso Telur Puyuh (Nusantara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Sayuran & Isian:
2 buah Oyong muda / gambas (kupas bagian siku tajamnya, cuci bersih, potong bulat tebal 1.5 cm)
50g Soun putih (rendam air hangat sebentar hingga lunak, tiriskan dan potong-potong)
8 butir Bakso sapi berkualitas (kerat silang bagian atasnya)
10 butir Telur puyuh rebus (kupas kulitnya)
1 buah Wortel (kupas, potong bulat tipis)
Bahan Kuah Kaldu Bening:
1.2 liter Air kaldu ayam bersih
4 siung Bawang putih (cincang halus)
3 butir Bawang merah (iris tipis)
1 batang Daun bawang (iris serong)
1 batang Seledri (iris halus)
1 sdt Garam halus
1/2 sdt Merica putih bubuk
1/2 sdt Kaldu jamur / ayam bubuk
1 sdm Minyak goreng untuk menumis bumbu
Bahan Pelengkap:
2 sdm Bawang merah goreng renyah
Langkah-Langkah Pembuatan:
Menumis Bawang: Panaskan 1 sendok makan minyak dalam panci sop. Masukkan bawang putih cincang dan irisan bawang merah. Tumis di atas api sedang hingga harum matang keemasan.
Membuat Kuah Kaldu: Tuangkan air kaldu ayam ke dalam panci berisi tumisan bawang. Masak dengan api sedang hingga kuah mendidih.
Memasukkan Sayuran Keras dan Bakso: Masukkan potongan wortel dan bakso sapi ke dalam air mendidih. Masak selama 3-4 menit hingga wortel mulai empuk dan bakso merekah mekar.
Memasukkan Oyong dan Telur Puyuh: Masukkan potongan oyong dan telur puyuh rebus. Bumbui dengan garam, merica bubuk, dan kaldu jamur. Masak selama 2-3 menit saja hingga oyong matang empuk berair namun tetap berwarna hijau segar (jangan terlalu lama agar tidak lembek).
Memasukkan Soun: Masukkan soun yang sudah ditiriskan, irisan daun bawang, dan daun seledri. Aduk sebentar selama 30 detik agar soun menyerap kaldu, lalu segera matikan api kompor.
Penyajian: Tuangkan sayur oyong soun bakso panas ke dalam mangkuk saji saji. Taburi bawang merah goreng renyah di atasnya. Sajikan selagi hangat sebagai menu sayur segar keluarga.
Nutrisi (Per Porsi): Kalori 140 kkal | Protein 9g | Lemak 4g | Karbohidrat 18g. Kuah kaldu bening yang sangat menyegarkan dan ringan di lambung, kaya serat larut air dari oyong serta protein komplit dari telur puyuh dan bakso sapi.""",
        "ingredientGroups": [
            {
                "name": "Bahan Sayuran & Isian",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "2 buah Oyong muda (kupas siku, potong bulat 1.5 cm)", "amount": 2.0, "unit": "buah", "name": "Oyong muda", "notes": "kupas siku, potong bulat 1.5 cm", "orderIndex": 1},
                    {"rawText": "50g Soun putih (rendam air hangat, tiriskan)", "amount": 50.0, "unit": "g", "name": "Soun putih", "notes": "rendam air hangat, tiriskan", "orderIndex": 2},
                    {"rawText": "8 butir Bakso sapi (kerat silang)", "amount": 8.0, "unit": "butir", "name": "Bakso sapi", "notes": "kerat silang", "orderIndex": 3},
                    {"rawText": "10 butir Telur puyuh rebus (kupas)", "amount": 10.0, "unit": "butir", "name": "Telur puyuh rebus", "notes": "kupas", "orderIndex": 4},
                    {"rawText": "1 buah Wortel (potong bulat tipis)", "amount": 1.0, "unit": "buah", "name": "Wortel", "notes": "potong bulat tipis", "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Kuah Kaldu Bening",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "1.2 liter Air kaldu ayam bersih", "amount": 1.2, "unit": "liter", "name": "Air kaldu ayam", "notes": None, "orderIndex": 1},
                    {"rawText": "4 siung Bawang putih (cincang halus)", "amount": 4.0, "unit": "siung", "name": "Bawang putih", "notes": "cincang halus", "orderIndex": 2},
                    {"rawText": "3 butir Bawang merah (iris tipis)", "amount": 3.0, "unit": "butir", "name": "Bawang merah", "notes": "iris tipis", "orderIndex": 3},
                    {"rawText": "1 batang Daun bawang (iris serong)", "amount": 1.0, "unit": "batang", "name": "Daun bawang", "notes": "iris serong", "orderIndex": 4},
                    {"rawText": "1 batang Seledri (iris halus)", "amount": 1.0, "unit": "batang", "name": "Seledri", "notes": "iris halus", "orderIndex": 5},
                    {"rawText": "1 sdt Garam halus", "amount": 1.0, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 6},
                    {"rawText": "1/2 sdt Merica putih bubuk", "amount": 0.5, "unit": "sdt", "name": "Merica putih bubuk", "notes": None, "orderIndex": 7},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 8},
                    {"rawText": "1 sdm Minyak goreng untuk menumis", "amount": 1.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 9}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menumis Bawang", "instruction": "Panaskan 1 sendok makan minyak dalam panci sop. Masukkan bawang putih cincang dan irisan bawang merah. Tumis di atas api sedang hingga harum matang keemasan.", "rawText": "Menumis Bawang: Panaskan 1 sendok makan minyak dalam panci sop. Masukkan bawang putih cincang dan irisan bawang merah. Tumis di atas api sedang hingga harum matang keemasan."},
            {"stepNumber": 2, "title": "Membuat Kuah Kaldu", "instruction": "Tuangkan air kaldu ayam ke dalam panci berisi tumisan bawang. Masak dengan api sedang hingga kuah mendidih.", "rawText": "Membuat Kuah Kaldu: Tuangkan air kaldu ayam ke dalam panci berisi tumisan bawang. Masak dengan api sedang hingga kuah mendidih."},
            {"stepNumber": 3, "title": "Memasukkan Sayuran Keras dan Bakso", "instruction": "Masukkan potongan wortel dan bakso sapi ke dalam air mendidih. Masak selama 3-4 menit hingga wortel mulai empuk dan bakso merekah mekar.", "rawText": "Memasukkan Sayuran Keras dan Bakso: Masukkan potongan wortel dan bakso sapi ke dalam air mendidih. Masak selama 3-4 menit hingga wortel mulai empuk dan bakso merekah mekar."},
            {"stepNumber": 4, "title": "Memasukkan Oyong dan Telur Puyuh", "instruction": "Masukkan potongan oyong dan telur puyuh rebus. Bumbui dengan garam, merica bubuk, dan kaldu jamur. Masak selama 2-3 menit saja hingga oyong matang empuk berair namun tetap berwarna hijau segar.", "rawText": "Memasukkan Oyong dan Telur Puyuh: Masukkan potongan oyong dan telur puyuh rebus. Bumbui dengan garam, merica bubuk, dan kaldu jamur. Masak selama 2-3 menit saja hingga oyong matang empuk berair namun tetap berwarna hijau segar."},
            {"stepNumber": 5, "title": "Memasukkan Soun", "instruction": "Masukkan soun yang sudah ditiriskan, irisan daun bawang, dan daun seledri. Aduk sebentar selama 30 detik agar soun menyerap kaldu, lalu segera matikan api kompor.", "rawText": "Memasukkan Soun: Masukkan soun yang sudah ditiriskan, irisan daun bawang, dan daun seledri. Aduk sebentar selama 30 detik agar soun menyerap kaldu, lalu segera matikan api kompor."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Tuangkan sayur oyong soun bakso panas ke dalam mangkuk saji. Taburi bawang merah goreng renyah di atasnya. Sajikan selagi hangat.", "rawText": "Penyajian: Tuangkan sayur oyong soun bakso panas ke dalam mangkuk saji. Taburi bawang merah goreng renyah di atasnya. Sajikan selagi hangat."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 140 kkal | Protein 9g | Lemak 4g | Karbohidrat 18g. Kuah kaldu bening yang sangat menyegarkan dan ringan di lambung, kaya serat larut air dari oyong serta protein komplit dari telur puyuh dan bakso sapi.",
            "serving": "Per Porsi",
            "calories": 140,
            "protein": 9.0,
            "fat": 4.0,
            "carbohydrates": 18.0,
            "notes": "Kuah kaldu bening yang sangat menyegarkan dan ringan di lambung, kaya serat larut air dari oyong serta protein komplit dari telur puyuh dan bakso sapi."
        }
    },
    {
        "recipeNumber": 205,
        "title": "205. Ayam Suwir Pedas Kemangi (Nusantara)",
        "name": "Ayam Suwir Pedas Kemangi",
        "slug": "ayam-suwir-kemangi",
        "scope": "INDONESIA",
        "origin": "Bali",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 25,
        "servings": 5,
        "difficulty": "EASY",
        "spicinessLevel": 3,
        "categorySlug": "ayam-unggas",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """205. Ayam Suwir Pedas Kemangi (Nusantara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Dada ayam fillet tanpa kulit (cuci bersih)
2 ikat Daun kemangi segar (petik daunnya, cuci bersih)
2 batang Serai (memarkan)
4 lembar Daun jeruk purut (buang tulang daunnya, sobek)
100 ml Air kaldu sisa rebusan ayam
3 sdm Minyak goreng untuk menumis
Bumbu Halus Balado Merah:
8 butir Bawang merah
5 siung Bawang putih
10 buah Cabai merah keriting
6 buah Cabai rawit merah
2 buah Tomat merah matang ukuran sedang
2 cm Kunyit segar (bakar)
1 sdt Terasi bakar berkualitas
1 sdt Garam halus
1 sdt Gula merah aren (sisir)
1/2 sdt Kaldu jamur / penyedap rasa
Langkah-Langkah Pembuatan:
Merebus dan Menyuwir Daging Ayam: Rebus dada ayam fillet dalam air mendidih bersama 1 sendok teh garam dan 2 cm jahe memarkan selama 15 menit hingga daging matang empuk. Angkat, tiriskan, dan biarkan dingin. Ambil 100 ml air sisa rebusan sebagai kaldu. Suwir-suwir serat daging ayam secara kasar dengan tangan atau garpu.
Menumis Bumbu Halus: Panaskan 3 sendok makan minyak dalam wajan cekung di atas api sedang. Masukkan bumbu halus bersama serai memarkan dan sobekan daun jeruk purut. Tumis sambil diaduk perlahan hingga bumbu matang tanak, harum semerbak, dan mengeluarkan minyak cabai kemerahan.
Memasukkan Ayam Suwir: Masukkan suwiran daging ayam ke dalam tumisan bumbu balado. Aduk rata hingga seluruh suwiran ayam terbalut bumbu pekat. Tuangkan 100 ml air kaldu ayam.
Meresapkan Bumbu: Masak di atas api sedang-rendah sambil terus diaduk hingga cairan menyusut habis dan bumbu meresap sempurna ke dalam serat ayam (bumbu tampak basah kesat berminyak). Bumbui dengan garam, gula aren, dan kaldu jamur. Cicipi rasanya.
Memasukkan Daun Kemangi: Masukkan daun kemangi segar ke dalam wajan. Aduk cepat di atas api besar selama 30 detik saja hingga daun kemangi layu dan mengeluarkan aroma harum khas, lalu segera matikan api agar daun kemangi tidak menghitam.
Penyajian: Pindahkan ayam suwir pedas kemangi ke piring saji. Nikmati bersama nasi putih hangat pulen dan lauk pelengkap seperti tempe goreng atau telur dadar.
Nutrisi (Per Porsi): Kalori 210 kkal | Protein 27g | Lemak 7g | Karbohidrat 9g. Tinggi protein murni rendah lemak jenuh dari dada ayam tanpa kulit, dipadukan antioksidan alami eugenol dari daun kemangi dan capsaicin cabai yang meningkatkan metabolisme.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "500g Dada ayam fillet (rebus, suwir kasar)", "amount": 500.0, "unit": "g", "name": "Dada ayam fillet", "notes": "rebus, suwir kasar", "orderIndex": 1},
                    {"rawText": "2 ikat Daun kemangi segar (petik daunnya)", "amount": 2.0, "unit": "ikat", "name": "Daun kemangi segar", "notes": "petik daunnya", "orderIndex": 2},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 3},
                    {"rawText": "4 lembar Daun jeruk purut", "amount": 4.0, "unit": "lembar", "name": "Daun jeruk purut", "notes": "buang tulang", "orderIndex": 4},
                    {"rawText": "100 ml Air kaldu sisa rebusan ayam", "amount": 100.0, "unit": "ml", "name": "Air kaldu ayam", "notes": None, "orderIndex": 5},
                    {"rawText": "3 sdm Minyak goreng untuk menumis", "amount": 3.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 6}
                ]
            },
            {
                "name": "Bumbu Halus Balado Merah",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "8 butir Bawang merah", "amount": 8.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "10 buah Cabai merah keriting", "amount": 10.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 3},
                    {"rawText": "6 buah Cabai rawit merah", "amount": 6.0, "unit": "buah", "name": "Cabai rawit merah", "notes": None, "orderIndex": 4},
                    {"rawText": "2 buah Tomat merah matang", "amount": 2.0, "unit": "buah", "name": "Tomat merah matang", "notes": None, "orderIndex": 5},
                    {"rawText": "2 cm Kunyit segar (bakar)", "amount": 2.0, "unit": "cm", "name": "Kunyit segar", "notes": "bakar", "orderIndex": 6},
                    {"rawText": "1 sdt Terasi bakar", "amount": 1.0, "unit": "sdt", "name": "Terasi bakar", "notes": "berkualitas", "orderIndex": 7},
                    {"rawText": "1 sdt Garam halus", "amount": 1.0, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 8},
                    {"rawText": "1 sdt Gula merah aren (sisir)", "amount": 1.0, "unit": "sdt", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 9},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 10}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Merebus dan Menyuwir Daging Ayam", "instruction": "Rebus dada ayam fillet dalam air mendidih bersama garam dan jahe selama 15 menit hingga matang empuk. Angkat, tiriskan, dan biarkan dingin. Ambil 100 ml air rebusan sebagai kaldu. Suwir-suwir serat daging ayam secara kasar.", "rawText": "Merebus dan Menyuwir Daging Ayam: Rebus dada ayam fillet dalam air mendidih bersama garam dan jahe selama 15 menit hingga matang empuk. Angkat, tiriskan, dan biarkan dingin. Ambil 100 ml air rebusan sebagai kaldu. Suwir-suwir serat daging ayam secara kasar."},
            {"stepNumber": 2, "title": "Menumis Bumbu Halus", "instruction": "Panaskan 3 sendok makan minyak dalam wajan cekung di atas api sedang. Masukkan bumbu halus bersama serai memarkan dan sobekan daun jeruk purut. Tumis sambil diaduk perlahan hingga bumbu matang tanak, harum semerbak, dan mengeluarkan minyak cabai kemerahan.", "rawText": "Menumis Bumbu Halus: Panaskan 3 sendok makan minyak dalam wajan cekung di atas api sedang. Masukkan bumbu halus bersama serai memarkan dan sobekan daun jeruk purut. Tumis sambil diaduk perlahan hingga bumbu matang tanak, harum semerbak, dan mengeluarkan minyak cabai kemerahan."},
            {"stepNumber": 3, "title": "Memasukkan Ayam Suwir", "instruction": "Masukkan suwiran daging ayam ke dalam tumisan bumbu balado. Aduk rata hingga seluruh suwiran ayam terbalut bumbu pekat. Tuangkan 100 ml air kaldu ayam.", "rawText": "Memasukkan Ayam Suwir: Masukkan suwiran daging ayam ke dalam tumisan bumbu balado. Aduk rata hingga seluruh suwiran ayam terbalut bumbu pekat. Tuangkan 100 ml air kaldu ayam."},
            {"stepNumber": 4, "title": "Meresapkan Bumbu", "instruction": "Masak di atas api sedang-rendah sambil terus diaduk hingga cairan menyusut habis dan bumbu meresap sempurna ke dalam serat ayam. Bumbui dengan garam, gula aren, dan kaldu jamur. Cicipi rasanya.", "rawText": "Meresapkan Bumbu: Masak di atas api sedang-rendah sambil terus diaduk hingga cairan menyusut habis dan bumbu meresap sempurna ke dalam serat ayam. Bumbui dengan garam, gula aren, dan kaldu jamur. Cicipi rasanya."},
            {"stepNumber": 5, "title": "Memasukkan Daun Kemangi", "instruction": "Masukkan daun kemangi segar ke dalam wajan. Aduk cepat di atas api besar selama 30 detik saja hingga daun kemangi layu dan mengeluarkan aroma harum khas, lalu segera matikan api.", "rawText": "Memasukkan Daun Kemangi: Masukkan daun kemangi segar ke dalam wajan. Aduk cepat di atas api besar selama 30 detik saja hingga daun kemangi layu dan mengeluarkan aroma harum khas, lalu segera matikan api."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Pindahkan ayam suwir pedas kemangi ke piring saji. Nikmati bersama nasi putih hangat pulen dan lauk pelengkap.", "rawText": "Penyajian: Pindahkan ayam suwir pedas kemangi ke piring saji. Nikmati bersama nasi putih hangat pulen dan lauk pelengkap."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 210 kkal | Protein 27g | Lemak 7g | Karbohidrat 9g. Tinggi protein murni rendah lemak jenuh dari dada ayam tanpa kulit, dipadukan antioksidan alami eugenol dari daun kemangi dan capsaicin cabai yang meningkatkan metabolisme.",
            "serving": "Per Porsi",
            "calories": 210,
            "protein": 27.0,
            "fat": 7.0,
            "carbohydrates": 9.0,
            "notes": "Tinggi protein murni rendah lemak jenuh dari dada ayam tanpa kulit, dipadukan antioksidan alami eugenol dari daun kemangi dan capsaicin cabai yang meningkatkan metabolisme."
        }
    },
    {
        "recipeNumber": 206,
        "title": "206. Ikan Sambal Pecak Khas Betawi (DKI Jakarta)",
        "name": "Ikan Nila Sambal Pecak Betawi",
        "slug": "ikan-sambal-pecak-betawi",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 20,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 3,
        "categorySlug": "ikan-seafood",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """206. Ikan Sambal Pecak Khas Betawi (DKI Jakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Ikan:
2 ekor Ikan nila atau ikan gurame segar (kurang lebih 600g - 700g, bersihkan sisik dan insang, kerat badannya)
1 buah Jeruk nipis (peras airnya untuk marinasi)
1 sdt Bawang putih bubuk
1/2 sdt Kunyit bubuk
1 sdt Garam halus
Minyak goreng secukupnya untuk menggoreng ikan
Bahan Bumbu Pecak Sangrai / Bakar:
8 butir Bawang merah (sangrai atau bakar di atas teflon hingga harum bercak hitam)
4 siung Bawang putih (sangrai / bakar)
10 buah Cabai rawit merah
6 buah Cabai rawit hijau
4 cm Temu kunci atau jahe segar (bakar kupas)
2 cm Kencur segar
1 sdt Terasi bakar berkualitas
1/2 sdt Garam halus
1 sdt Gula pasir
Bahan Kuah Siraman:
150 ml Air bersih mendidih panas
2 buah Jeruk limau (belah dua, peras airnya)
Langkah-Langkah Pembuatan:
Marinasi Ikan: Lumuri ikan nila/gurame bersih dengan air perasan jeruk nipis, kunyit bubuk, bawang putih bubuk, dan garam. Diamkan selama 15 menit agar bumbu meresap dan bau tanah pada ikan air tawar hilang.
Menggoreng Ikan: Panaskan minyak banyak dalam wajan cekung. Masukkan ikan secara perlahan, goreng dengan api sedang hingga seluruh badan ikan kering renyah, garing keemasan, dan matang sempurna ke bagian dalam. Angkat dan tiriskan di atas piring saji lebar.
Membakar Bumbu Pecak: Sangrai atau bakar bawang merah, bawang putih, jahe, dan kencur di atas wajan tanpa minyak hingga beraroma wangi terpanggang.
Mengulek Kasar Bumbu: Di atas cobek batu, ulek kasar cabai rawit merah, cabai rawit hijau, bumbu bakar, terasi, garam, dan gula pasir (tekstur bumbu pecak harus kasar dan tidak sampai halus lembut).
Menyiram Air Panas Mendidih: Tuangkan 150 ml air mendidih panas secara langsung ke atas cobek berisi bumbu ulek kasar. Aduk rata menggunakan ulekan hingga aroma pedas asam segar langsung merebak. Beri perasan air jeruk limau beserta kulitnya ke dalam kuah sambal pecak.
Penyajian: Siramkan kuah sambal pecak hangat beserta cabai dan bawang kasar secara melimpah ke atas badan ikan goreng renyah. Sajikan segera bersama nasi putih hangat.
Nutrisi (Per Porsi): Kalori 230 kkal | Protein 25g | Lemak 11g | Karbohidrat 7g. Perpaduan rempah segar rimpang jahe dan kencur melancarkan peredaran darah, dilengkapi protein rendah lemak dari ikan air tawar segar.""",
        "ingredientGroups": [
            {
                "name": "Bahan Ikan",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "2 ekor Ikan nila atau gurame segar (600g, kerat badannya)", "amount": 2.0, "unit": "ekor", "name": "Ikan nila atau gurame", "notes": "600g, kerat badannya", "orderIndex": 1},
                    {"rawText": "1 buah Jeruk nipis (peras airnya)", "amount": 1.0, "unit": "buah", "name": "Jeruk nipis", "notes": "peras airnya", "orderIndex": 2},
                    {"rawText": "1 sdt Bawang putih bubuk", "amount": 1.0, "unit": "sdt", "name": "Bawang putih bubuk", "notes": None, "orderIndex": 3},
                    {"rawText": "1/2 sdt Kunyit bubuk", "amount": 0.5, "unit": "sdt", "name": "Kunyit bubuk", "notes": None, "orderIndex": 4},
                    {"rawText": "1 sdt Garam halus", "amount": 1.0, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 5},
                    {"rawText": "Minyak goreng secukupnya", "amount": None, "unit": "secukupnya", "name": "Minyak goreng", "notes": "untuk menggoreng ikan", "orderIndex": 6}
                ]
            },
            {
                "name": "Bahan Bumbu Pecak Sangrai",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "8 butir Bawang merah (sangrai / bakar)", "amount": 8.0, "unit": "butir", "name": "Bawang merah", "notes": "sangrai / bakar", "orderIndex": 1},
                    {"rawText": "4 siung Bawang putih (sangrai / bakar)", "amount": 4.0, "unit": "siung", "name": "Bawang putih", "notes": "sangrai / bakar", "orderIndex": 2},
                    {"rawText": "10 buah Cabai rawit merah", "amount": 10.0, "unit": "buah", "name": "Cabai rawit merah", "notes": None, "orderIndex": 3},
                    {"rawText": "6 buah Cabai rawit hijau", "amount": 6.0, "unit": "buah", "name": "Cabai rawit hijau", "notes": None, "orderIndex": 4},
                    {"rawText": "4 cm Temu kunci atau jahe segar (bakar)", "amount": 4.0, "unit": "cm", "name": "Jahe segar", "notes": "bakar kupas", "orderIndex": 5},
                    {"rawText": "2 cm Kencur segar", "amount": 2.0, "unit": "cm", "name": "Kencur segar", "notes": None, "orderIndex": 6},
                    {"rawText": "1 sdt Terasi bakar", "amount": 1.0, "unit": "sdt", "name": "Terasi bakar", "notes": "berkualitas", "orderIndex": 7},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 8},
                    {"rawText": "1 sdt Gula pasir", "amount": 1.0, "unit": "sdt", "name": "Gula pasir", "notes": None, "orderIndex": 9}
                ]
            },
            {
                "name": "Bahan Kuah Siraman",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "150 ml Air bersih mendidih panas", "amount": 150.0, "unit": "ml", "name": "Air mendidih panas", "notes": None, "orderIndex": 1},
                    {"rawText": "2 buah Jeruk limau (peras airnya)", "amount": 2.0, "unit": "buah", "name": "Jeruk limau", "notes": "peras airnya", "orderIndex": 2}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Marinasi Ikan", "instruction": "Lumuri ikan nila/gurame bersih dengan air perasan jeruk nipis, kunyit bubuk, bawang putih bubuk, dan garam. Diamkan selama 15 menit agar bumbu meresap dan bau tanah pada ikan air tawar hilang.", "rawText": "Marinasi Ikan: Lumuri ikan nila/gurame bersih dengan air perasan jeruk nipis, kunyit bubuk, bawang putih bubuk, dan garam. Diamkan selama 15 menit agar bumbu meresap dan bau tanah pada ikan air tawar hilang."},
            {"stepNumber": 2, "title": "Menggoreng Ikan", "instruction": "Panaskan minyak banyak dalam wajan cekung. Masukkan ikan secara perlahan, goreng dengan api sedang hingga seluruh badan ikan kering renyah, garing keemasan, dan matang sempurna ke bagian dalam. Angkat dan tiriskan di atas piring saji lebar.", "rawText": "Menggoreng Ikan: Panaskan minyak banyak dalam wajan cekung. Masukkan ikan secara perlahan, goreng dengan api sedang hingga seluruh badan ikan kering renyah, garing keemasan, dan matang sempurna ke bagian dalam. Angkat dan tiriskan di atas piring saji lebar."},
            {"stepNumber": 3, "title": "Membakar Bumbu Pecak", "instruction": "Sangrai atau bakar bawang merah, bawang putih, jahe, dan kencur di atas wajan tanpa minyak hingga beraroma wangi terpanggang.", "rawText": "Membakar Bumbu Pecak: Sangrai atau bakar bawang merah, bawang putih, jahe, dan kencur di atas wajan tanpa minyak hingga beraroma wangi terpanggang."},
            {"stepNumber": 4, "title": "Mengulek Kasar Bumbu", "instruction": "Di atas cobek batu, ulek kasar cabai rawit merah, cabai rawit hijau, bumbu bakar, terasi, garam, dan gula pasir (tekstur bumbu pecak harus kasar dan tidak sampai halus lembut).", "rawText": "Mengulek Kasar Bumbu: Di atas cobek batu, ulek kasar cabai rawit merah, cabai rawit hijau, bumbu bakar, terasi, garam, dan gula pasir (tekstur bumbu pecak harus kasar dan tidak sampai halus lembut)."},
            {"stepNumber": 5, "title": "Menyiram Air Panas Mendidih", "instruction": "Tuangkan 150 ml air mendidih panas secara langsung ke atas cobek berisi bumbu ulek kasar. Aduk rata menggunakan ulekan hingga aroma pedas asam segar langsung merebak. Beri perasan air jeruk limau beserta kulitnya ke dalam kuah sambal pecak.", "rawText": "Menyiram Air Panas Mendidih: Tuangkan 150 ml air mendidih panas secara langsung ke atas cobek berisi bumbu ulek kasar. Aduk rata menggunakan ulekan hingga aroma pedas asam segar langsung merebak. Beri perasan air jeruk limau beserta kulitnya ke dalam kuah sambal pecak."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Siramkan kuah sambal pecak hangat beserta cabai dan bawang kasar secara melimpah ke atas badan ikan goreng renyah. Sajikan segera bersama nasi putih hangat.", "rawText": "Penyajian: Siramkan kuah sambal pecak hangat beserta cabai dan bawang kasar secara melimpah ke atas badan ikan goreng renyah. Sajikan segera bersama nasi putih hangat."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 230 kkal | Protein 25g | Lemak 11g | Karbohidrat 7g. Perpaduan rempah segar rimpang jahe dan kencur melancarkan peredaran darah, dilengkapi protein rendah lemak dari ikan air tawar segar.",
            "serving": "Per Porsi",
            "calories": 230,
            "protein": 25.0,
            "fat": 11.0,
            "carbohydrates": 7.0,
            "notes": "Perpaduan rempah segar rimpang jahe dan kencur melancarkan peredaran darah, dilengkapi protein rendah lemak dari ikan air tawar segar."
        }
    },
    {
        "recipeNumber": 207,
        "title": "207. Tumis Tauge Ikan Asin Jambal Roti (Jawa Barat)",
        "name": "Tumis Tauge Ikan Asin Jambal Roti",
        "slug": "tumis-tauge-ikan-asin",
        "scope": "INDONESIA",
        "origin": "Jawa Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 15,
        "cookTimeMinutes": 10,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 2,
        "categorySlug": "sayuran-tumisan",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """207. Tumis Tauge Ikan Asin Jambal Roti (Jawa Barat)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
250g Tauge segar montok (buang ekornya, cuci bersih, tiriskan)
100g Ikan asin jambal roti (potong dadu kecil 1 cm, rendam air hangat 10 menit agar tidak keasinan, tiriskan)
2 batang Daun bawang (iris serong)
3 sdm Minyak goreng untuk menumis
Bumbu Iris & Saus:
5 butir Bawang merah (iris tipis)
3 siung Bawang putih (cincang halus)
3 buah Cabai merah keriting (iris serong)
5 buah Cabai rawit merah (iris tipis)
1 buah Tomat hijau (potong-potong)
1/2 sdt Saus tiram
1/4 sdt Gula pasir (penyeimbang rasa gurih asin)
1/4 sdt Merica bubuk
50 ml Air bersih
Langkah-Langkah Pembuatan:
Menggoreng Ikan Asin Jambal Roti: Panaskan 3 sendok makan minyak goreng dalam wajan cekung. Masukkan potongan dadu ikan asin jambal roti. Goreng di atas api sedang hingga berwarna kuning keemasan, renyah, dan harum gurih. Pinggirkan ikan asin ke tepi wajan (atau tiriskan sejenak).
Menumis Bumbu Iris: Gunakan minyak sisa menggoreng ikan asin dalam wajan. Masukkan bawang putih cincang, irisan bawang merah, cabai keriting, cabai rawit, dan potongan tomat hijau. Tumis di atas api sedang hingga bumbu layu dan harum semerbak.
Mencampurkan Bahan: Kembalikan ikan asin jambal roti ke tengah wajan, aduk bersama tumisan bumbu. Tambahkan saus tiram, merica bubuk, dan gula pasir. Tuang 50 ml air bersih, aduk sebentar hingga mendidih.
Memasak Tauge Cepat (High Heat): Besarkan api kompor ke tingkat maksimal. Masukkan tauge segar dan irisan daun bawang. Aduk cepat selama 1-2 menit saja hingga tauge mulai layu namun tetap renyah (*crunchy*) dan tidak mengeluarkan banyak air. Segera matikan api kompor.
Penyajian: Pindahkan tumis tauge ikan asin jambal roti ke atas piring saji saji. Hidangan rumahan sederhana ini sangat lezat dinikmati hangat-hangat bersama nasi putih panas.
Nutrisi (Per Porsi): Kalori 130 kkal | Protein 9g | Lemak 6g | Karbohidrat 10g. Sayuran rendah kalori kaya vitamin C dan serat dari tauge segar yang dimasak cepat, berpadu gurih protein kalsium dari ikan asin jambal roti.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "250g Tauge segar montok (cuci bersih)", "amount": 250.0, "unit": "g", "name": "Tauge segar", "notes": "cuci bersih, tiriskan", "orderIndex": 1},
                    {"rawText": "100g Ikan asin jambal roti (potong dadu 1 cm)", "amount": 100.0, "unit": "g", "name": "Ikan asin jambal roti", "notes": "potong dadu 1 cm", "orderIndex": 2},
                    {"rawText": "2 batang Daun bawang (iris serong)", "amount": 2.0, "unit": "batang", "name": "Daun bawang", "notes": "iris serong", "orderIndex": 3},
                    {"rawText": "3 sdm Minyak goreng untuk menumis", "amount": 3.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 4}
                ]
            },
            {
                "name": "Bumbu Iris & Saus",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "5 butir Bawang merah (iris tipis)", "amount": 5.0, "unit": "butir", "name": "Bawang merah", "notes": "iris tipis", "orderIndex": 1},
                    {"rawText": "3 siung Bawang putih (cincang halus)", "amount": 3.0, "unit": "siung", "name": "Bawang putih", "notes": "cincang halus", "orderIndex": 2},
                    {"rawText": "3 buah Cabai merah keriting (iris serong)", "amount": 3.0, "unit": "buah", "name": "Cabai merah keriting", "notes": "iris serong", "orderIndex": 3},
                    {"rawText": "5 buah Cabai rawit merah (iris tipis)", "amount": 5.0, "unit": "buah", "name": "Cabai rawit merah", "notes": "iris tipis", "orderIndex": 4},
                    {"rawText": "1 buah Tomat hijau (potong-potong)", "amount": 1.0, "unit": "buah", "name": "Tomat hijau", "notes": "potong-potong", "orderIndex": 5},
                    {"rawText": "1/2 sdt Saus tiram", "amount": 0.5, "unit": "sdt", "name": "Saus tiram", "notes": None, "orderIndex": 6},
                    {"rawText": "1/4 sdt Gula pasir", "amount": 0.25, "unit": "sdt", "name": "Gula pasir", "notes": None, "orderIndex": 7},
                    {"rawText": "1/4 sdt Merica bubuk", "amount": 0.25, "unit": "sdt", "name": "Merica bubuk", "notes": None, "orderIndex": 8},
                    {"rawText": "50 ml Air bersih", "amount": 50.0, "unit": "ml", "name": "Air bersih", "notes": None, "orderIndex": 9}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menggoreng Ikan Asin Jambal Roti", "instruction": "Panaskan 3 sendok makan minyak goreng dalam wajan cekung. Masukkan potongan dadu ikan asin jambal roti. Goreng di atas api sedang hingga berwarna kuning keemasan, renyah, dan harum gurih. Pinggirkan ikan asin ke tepi wajan.", "rawText": "Menggoreng Ikan Asin Jambal Roti: Panaskan 3 sendok makan minyak goreng dalam wajan cekung. Masukkan potongan dadu ikan asin jambal roti. Goreng di atas api sedang hingga berwarna kuning keemasan, renyah, dan harum gurih. Pinggirkan ikan asin ke tepi wajan."},
            {"stepNumber": 2, "title": "Menumis Bumbu Iris", "instruction": "Gunakan minyak sisa menggoreng ikan asin dalam wajan. Masukkan bawang putih cincang, irisan bawang merah, cabai keriting, cabai rawit, dan potongan tomat hijau. Tumis di atas api sedang hingga bumbu layu dan harum semerbak.", "rawText": "Menumis Bumbu Iris: Gunakan minyak sisa menggoreng ikan asin dalam wajan. Masukkan bawang putih cincang, irisan bawang merah, cabai keriting, cabai rawit, dan potongan tomat hijau. Tumis di atas api sedang hingga bumbu layu dan harum semerbak."},
            {"stepNumber": 3, "title": "Mencampurkan Bahan", "instruction": "Kembalikan ikan asin jambal roti ke tengah wajan, aduk bersama tumisan bumbu. Tambahkan saus tiram, merica bubuk, dan gula pasir. Tuang 50 ml air bersih, aduk sebentar hingga mendidih.", "rawText": "Mencampurkan Bahan: Kembalikan ikan asin jambal roti ke tengah wajan, aduk bersama tumisan bumbu. Tambahkan saus tiram, merica bubuk, dan gula pasir. Tuang 50 ml air bersih, aduk sebentar hingga mendidih."},
            {"stepNumber": 4, "title": "Memasak Tauge Cepat (High Heat)", "instruction": "Besarkan api kompor ke tingkat maksimal. Masukkan tauge segar dan irisan daun bawang. Aduk cepat selama 1-2 menit saja hingga tauge mulai layu namun tetap renyah (crunchy) dan tidak mengeluarkan banyak air. Segera matikan api kompor.", "rawText": "Memasak Tauge Cepat (High Heat): Besarkan api kompor ke tingkat maksimal. Masukkan tauge segar dan irisan daun bawang. Aduk cepat selama 1-2 menit saja hingga tauge mulai layu namun tetap renyah (crunchy) dan tidak mengeluarkan banyak air. Segera matikan api kompor."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Pindahkan tumis tauge ikan asin jambal roti ke atas piring saji. Hidangan rumahan sederhana ini sangat lezat dinikmati hangat-hangat bersama nasi putih panas.", "rawText": "Penyajian: Pindahkan tumis tauge ikan asin jambal roti ke atas piring saji. Hidangan rumahan sederhana ini sangat lezat dinikmati hangat-hangat bersama nasi putih panas."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 130 kkal | Protein 9g | Lemak 6g | Karbohidrat 10g. Sayuran rendah kalori kaya vitamin C dan serat dari tauge segar yang dimasak cepat, berpadu gurih protein kalsium dari ikan asin jambal roti.",
            "serving": "Per Porsi",
            "calories": 130,
            "protein": 9.0,
            "fat": 6.0,
            "carbohydrates": 10.0,
            "notes": "Sayuran rendah kalori kaya vitamin C dan serat dari tauge segar yang dimasak cepat, berpadu gurih protein kalsium dari ikan asin jambal roti."
        }
    },
    {
        "recipeNumber": 208,
        "title": "208. Sayur Bobor Bayam Labu Siam (Jawa Tengah)",
        "name": "Sayur Bobor Bayam Labu Siam",
        "slug": "sayur-bobor-bayam-labu",
        "scope": "INDONESIA",
        "origin": "Jawa Tengah",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 20,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 1,
        "categorySlug": "sayuran-tumisan",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """208. Sayur Bobor Bayam Labu Siam (Jawa Tengah)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Sayuran:
2 ikat Daun bayam hijau segar (petik daun dan pucuk mudanya, cuci bersih)
1 buah Labu siam ukuran sedang (kupas, buang getah, potong dadu 2 cm)
1 buah Jagung manis (potong bulat setebal 2 cm)
800 ml Santan kelapa encer segar (dari 1/2 butir kelapa parut)
2 lembar Daun salam kering
3 cm Lengkuas (memarkan)
Bumbu Halus Khas Bobor Jawa:
5 butir Bawang merah
3 siung Bawang putih
3 cm Kencur segar (kunci aroma khas sayur bobor)
1 sdt Ketumbar butiran (sangrai)
3 butir Kemiri (sangrai)
1.5 sdt Garam halus
1 sdt Gula merah aren (sisir)
1/2 sdt Kaldu jamur / penyedap rasa
Langkah-Langkah Pembuatan:
Merebus Kuah Santan Berbumbu: Didihkan santan encer bersama bumbu halus, lengkuas memarkan, dan daun salam dalam panci di atas api sedang. Aduk perlahan secara berkala agar santan tidak pecah dan bumbu larut matang merata.
Memasak Jagung Manis dan Labu Siam: Masukkan potongan jagung manis ke dalam kuah santan mendidih. Masak selama 5 menit hingga jagung mulai empuk. Masukkan potongan labu siam, masak kembali selama 5 menit hingga labu siam empuk dan kuah bobor terasa manis gurih harum kencur.
Membumbui Kuah: Tambahkan garam, gula merah aren, dan kaldu jamur. Cicipi untuk memastikan rasa gurih santan, manis lembut, dan aroma kencurnya seimbang sempurna.
Memasukkan Daun Bayam (Masak Cepat): Masukkan daun bayam hijau segar ke dalam kuah mendidih. Aduk perlahan dan masak selama 1-2 menit saja hingga daun bayam layu dan empuk namun tetap berwarna hijau cerah. Segera matikan api kompor agar bayam tidak *overcooked*.
Penyajian: Tuangkan sayur bobor bayam labu siam hangat ke dalam mangkuk saji saji. Sajikan bersama lauk pendamping rumahan khas Jawa seperti tempe goreng garit, ikan asin goreng garing, dan sambal terasi terasi matang.
Nutrisi (Per Porsi): Kalori 120 kkal | Protein 4g | Lemak 6g | Karbohidrat 14g. Kombinasi serat tinggi, zat besi folat dari bayam hijau, dan asam laurat santan encer yang sangat mudah dicerna serta menyejukkan pencernaan.""",
        "ingredientGroups": [
            {
                "name": "Bahan Sayuran",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "2 ikat Daun bayam hijau segar (petik daunnya)", "amount": 2.0, "unit": "ikat", "name": "Daun bayam hijau", "notes": "petik daunnya", "orderIndex": 1},
                    {"rawText": "1 buah Labu siam (potong dadu 2 cm)", "amount": 1.0, "unit": "buah", "name": "Labu siam", "notes": "potong dadu 2 cm", "orderIndex": 2},
                    {"rawText": "1 buah Jagung manis (potong bulat 2 cm)", "amount": 1.0, "unit": "buah", "name": "Jagung manis", "notes": "potong bulat 2 cm", "orderIndex": 3},
                    {"rawText": "800 ml Santan kelapa encer segar", "amount": 800.0, "unit": "ml", "name": "Santan kelapa encer", "notes": None, "orderIndex": 4},
                    {"rawText": "2 lembar Daun salam kering", "amount": 2.0, "unit": "lembar", "name": "Daun salam kering", "notes": None, "orderIndex": 5},
                    {"rawText": "3 cm Lengkuas (memarkan)", "amount": 3.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 6}
                ]
            },
            {
                "name": "Bumbu Halus Khas Bobor Jawa",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "5 butir Bawang merah", "amount": 5.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "3 siung Bawang putih", "amount": 3.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "3 cm Kencur segar", "amount": 3.0, "unit": "cm", "name": "Kencur segar", "notes": "aroma khas bobor", "orderIndex": 3},
                    {"rawText": "1 sdt Ketumbar butiran (sangrai)", "amount": 1.0, "unit": "sdt", "name": "Ketumbar butiran", "notes": "sangrai", "orderIndex": 4},
                    {"rawText": "3 butir Kemiri (sangrai)", "amount": 3.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 5},
                    {"rawText": "1.5 sdt Garam halus", "amount": 1.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 6},
                    {"rawText": "1 sdt Gula merah aren (sisir)", "amount": 1.0, "unit": "sdt", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 7},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 8}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Merebus Kuah Santan Berbumbu", "instruction": "Didihkan santan encer bersama bumbu halus, lengkuas memarkan, dan daun salam dalam panci di atas api sedang. Aduk perlahan secara berkala agar santan tidak pecah dan bumbu larut matang merata.", "rawText": "Merebus Kuah Santan Berbumbu: Didihkan santan encer bersama bumbu halus, lengkuas memarkan, dan daun salam dalam panci di atas api sedang. Aduk perlahan secara berkala agar santan tidak pecah dan bumbu larut matang merata."},
            {"stepNumber": 2, "title": "Memasak Jagung Manis dan Labu Siam", "instruction": "Masukkan potongan jagung manis ke dalam kuah santan mendidih. Masak selama 5 menit hingga jagung mulai empuk. Masukkan potongan labu siam, masak kembali selama 5 menit hingga labu siam empuk dan kuah bobor terasa manis gurih harum kencur.", "rawText": "Memasak Jagung Manis dan Labu Siam: Masukkan potongan jagung manis ke dalam kuah santan mendidih. Masak selama 5 menit hingga jagung mulai empuk. Masukkan potongan labu siam, masak kembali selama 5 menit hingga labu siam empuk dan kuah bobor terasa manis gurih harum kencur."},
            {"stepNumber": 3, "title": "Membumbui Kuah", "instruction": "Tambahkan garam, gula merah aren, dan kaldu jamur. Cicipi untuk memastikan rasa gurih santan, manis lembut, dan aroma kencurnya seimbang sempurna.", "rawText": "Membumbui Kuah: Tambahkan garam, gula merah aren, dan kaldu jamur. Cicipi untuk memastikan rasa gurih santan, manis lembut, dan aroma kencurnya seimbang sempurna."},
            {"stepNumber": 4, "title": "Memasukkan Daun Bayam", "instruction": "Masukkan daun bayam hijau segar ke dalam kuah mendidih. Aduk perlahan dan masak selama 1-2 menit saja hingga daun bayam layu dan empuk namun tetap berwarna hijau cerah. Segera matikan api kompor.", "rawText": "Memasukkan Daun Bayam: Masukkan daun bayam hijau segar ke dalam kuah mendidih. Aduk perlahan dan masak selama 1-2 menit saja hingga daun bayam layu dan empuk namun tetap berwarna hijau cerah. Segera matikan api kompor."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Tuangkan sayur bobor bayam labu siam hangat ke dalam mangkuk saji. Sajikan bersama lauk tempe goreng, ikan asin, dan sambal terasi.", "rawText": "Penyajian: Tuangkan sayur bobor bayam labu siam hangat ke dalam mangkuk saji. Sajikan bersama lauk tempe goreng, ikan asin, dan sambal terasi."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 120 kkal | Protein 4g | Lemak 6g | Karbohidrat 14g. Kombinasi serat tinggi, zat besi folat dari bayam hijau, dan asam laurat santan encer yang sangat mudah dicerna serta menyejukkan pencernaan.",
            "serving": "Per Porsi",
            "calories": 120,
            "protein": 4.0,
            "fat": 6.0,
            "carbohydrates": 14.0,
            "notes": "Kombinasi serat tinggi, zat besi folat dari bayam hijau, dan asam laurat santan encer yang sangat mudah dicerna serta menyejukkan pencernaan."
        }
    },
    {
        "recipeNumber": 209,
        "title": "209. Urap Sayur Bumbu Kelapa Gurih Sangrai (Jawa Tengah)",
        "name": "Urap Sayur Kelapa Sangrai",
        "slug": "urap-sayur-kelapa-sangrai",
        "scope": "INDONESIA",
        "origin": "Jawa Tengah",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 25,
        "cookTimeMinutes": 20,
        "servings": 5,
        "difficulty": "EASY",
        "spicinessLevel": 2,
        "categorySlug": "sayuran-tumisan",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """209. Urap Sayur Bumbu Kelapa Gurih Sangrai (Jawa Tengah)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Sayuran Rebus:
1 ikat Kangkung segar (siangi daun dan batangnya, rebus matang, peras airnya)
100g Tauge segar (seduh air mendidih sebentar selama 30 detik, tiriskan)
100g Kacang panjang (potong 3 cm, rebus matang, tiriskan)
100g Kol / kubis (iris kasar, rebus matang, tiriskan)
Bahan Bumbu Kelapa Urap Sangrai:
200g Kelapa setengah tua (kupas kulit ari, parut memanjang kasar)
4 lembar Daun jeruk purut (buang tulang daun, iris tipis halus)
2 sdm Air matang
Bumbu Halus:
5 buah Cabai merah keriting
4 buah Cabai rawit merah (atau sesuai selera pedas)
5 butir Bawang merah
3 siung Bawang putih
4 cm Kencur segar (kunci utama aroma urap)
1/2 sdt Terasi bakar berkualitas
1.5 sdm Gula merah aren (sisir halus)
1 sdt Garam halus
1/2 sdt Kaldu jamur
Langkah-Langkah Pembuatan:
Membuat Bumbu Kelapa: Ulek cabai merah, cabai rawit, bawang merah, bawang putih, kencur, terasi bakar, gula aren, dan garam hingga halus. Campurkan bumbu halus bersama parutan kelapa setengah tua dan irisan daun jeruk purut di dalam wadah. Aduk dan remas-remas perlahan menggunakan sarung tangan hingga warna merah bumbu meresap merata ke seluruh serat kelapa.
Menyangrai Bumbu Kelapa: Masukkan kelapa berbumbu ke dalam wajan wajan anti-lengket di atas api kecil (tanpa minyak). Sangrai sambil terus diaduk bolak-balik tanpa henti hingga kelapa matang, beraroma harum semerbak, dan agak kesat kering (teknik sangrai ini membuat bumbu urap sangat gurih dan tahan basi seharian tanpa lemari es). Angkat dan biarkan dingin.
Menyiapkan Sayuran Rebus: Rebus masing-masing sayuran (kangkung, kacang panjang, kol, tauge) secara terpisah agar tingkat kematangannya pas. Setelah direbus, segera siram sayuran dengan air es dingin agar warnanya tetap hijau segar, lalu peras airnya hingga benar-benar tuntas kesat.
Mencampur Urap: Campurkan aneka sayuran rebus yang telah ditiriskan ke dalam wadah mangkuk besar. Masukkan bumbu kelapa sangrai harum secukupnya. Aduk rata menggunakan tangan atau sendok sayur hingga seluruh sayuran terselimuti bumbu kelapa secara merata.
Penyajian: Tata urap sayur bumbu kelapa di atas piring saji yang dialasi daun pisang. Sajikan segera sebagai menu sayur sehat kaya serat pelengkap ayam goreng, tahu tempe, atau ikan bakar.
Nutrisi (Per Porsi): Kalori 140 kkal | Protein 5g | Lemak 7g | Karbohidrat 16g. Menu sayuran murni kaya antioksidan dan serat mikronutrien, dilengkapi lemak nabati rantai sedang (MCT) dari kelapa parut segar yang memberikan energi berkelanjutan.""",
        "ingredientGroups": [
            {
                "name": "Bahan Sayuran Rebus",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "1 ikat Kangkung segar (rebus matang, peras airnya)", "amount": 1.0, "unit": "ikat", "name": "Kangkung segar", "notes": "rebus matang, peras airnya", "orderIndex": 1},
                    {"rawText": "100g Tauge segar (seduh air panas, tiriskan)", "amount": 100.0, "unit": "g", "name": "Tauge segar", "notes": "seduh air panas, tiriskan", "orderIndex": 2},
                    {"rawText": "100g Kacang panjang (potong 3 cm, rebus)", "amount": 100.0, "unit": "g", "name": "Kacang panjang", "notes": "potong 3 cm, rebus", "orderIndex": 3},
                    {"rawText": "100g Kol / kubis (iris kasar, rebus)", "amount": 100.0, "unit": "g", "name": "Kol", "notes": "iris kasar, rebus", "orderIndex": 4}
                ]
            },
            {
                "name": "Bahan Bumbu Kelapa Urap Sangrai",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "200g Kelapa setengah tua (parut memanjang kasar)", "amount": 200.0, "unit": "g", "name": "Kelapa setengah tua", "notes": "parut memanjang kasar", "orderIndex": 1},
                    {"rawText": "4 lembar Daun jeruk purut (iris halus)", "amount": 4.0, "unit": "lembar", "name": "Daun jeruk purut", "notes": "iris halus", "orderIndex": 2},
                    {"rawText": "2 sdm Air matang", "amount": 2.0, "unit": "sdm", "name": "Air matang", "notes": None, "orderIndex": 3}
                ]
            },
            {
                "name": "Bumbu Halus",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "5 buah Cabai merah keriting", "amount": 5.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 1},
                    {"rawText": "4 buah Cabai rawit merah", "amount": 4.0, "unit": "buah", "name": "Cabai rawit merah", "notes": None, "orderIndex": 2},
                    {"rawText": "5 butir Bawang merah", "amount": 5.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 3},
                    {"rawText": "3 siung Bawang putih", "amount": 3.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 4},
                    {"rawText": "4 cm Kencur segar", "amount": 4.0, "unit": "cm", "name": "Kencur segar", "notes": "aroma khas urap", "orderIndex": 5},
                    {"rawText": "1/2 sdt Terasi bakar", "amount": 0.5, "unit": "sdt", "name": "Terasi bakar", "notes": "berkualitas", "orderIndex": 6},
                    {"rawText": "1.5 sdm Gula merah aren (sisir)", "amount": 1.5, "unit": "sdm", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 7},
                    {"rawText": "1 sdt Garam halus", "amount": 1.0, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 8},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 9}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Bumbu Kelapa", "instruction": "Ulek cabai merah, cabai rawit, bawang merah, bawang putih, kencur, terasi bakar, gula aren, dan garam hingga halus. Campurkan bumbu halus bersama parutan kelapa setengah tua dan irisan daun jeruk purut di dalam wadah. Aduk dan remas-remas perlahan hingga warna bumbu merata ke seluruh serat kelapa.", "rawText": "Membuat Bumbu Kelapa: Ulek cabai merah, cabai rawit, bawang merah, bawang putih, kencur, terasi bakar, gula aren, dan garam hingga halus. Campurkan bumbu halus bersama parutan kelapa setengah tua dan irisan daun jeruk purut di dalam wadah. Aduk dan remas-remas perlahan hingga warna bumbu merata ke seluruh serat kelapa."},
            {"stepNumber": 2, "title": "Menyangrai Bumbu Kelapa", "instruction": "Masukkan kelapa berbumbu ke dalam wajan anti-lengket di atas api kecil tanpa minyak. Sangrai sambil terus diaduk bolak-balik tanpa henti hingga kelapa matang, beraroma harum semerbak, dan agak kesat kering. Angkat dan biarkan dingin.", "rawText": "Menyangrai Bumbu Kelapa: Masukkan kelapa berbumbu ke dalam wajan anti-lengket di atas api kecil tanpa minyak. Sangrai sambil terus diaduk bolak-balik tanpa henti hingga kelapa matang, beraroma harum semerbak, dan agak kesat kering. Angkat dan biarkan dingin."},
            {"stepNumber": 3, "title": "Menyiapkan Sayuran Rebus", "instruction": "Rebus masing-masing sayuran (kangkung, kacang panjang, kol, tauge) secara terpisah agar tingkat kematangannya pas. Setelah direbus, siram air es dingin agar warnanya tetap hijau segar, lalu peras airnya hingga benar-benar tuntas kesat.", "rawText": "Menyiapkan Sayuran Rebus: Rebus masing-masing sayuran (kangkung, kacang panjang, kol, tauge) secara terpisah agar tingkat kematangannya pas. Setelah direbus, siram air es dingin agar warnanya tetap hijau segar, lalu peras airnya hingga benar-benar tuntas kesat."},
            {"stepNumber": 4, "title": "Mencampur Urap", "instruction": "Campurkan aneka sayuran rebus yang telah ditiriskan ke dalam wadah mangkuk besar. Masukkan bumbu kelapa sangrai harum secukupnya. Aduk rata menggunakan tangan atau sendok sayur hingga seluruh sayuran terselimuti bumbu kelapa secara merata.", "rawText": "Mencampur Urap: Campurkan aneka sayuran rebus yang telah ditiriskan ke dalam wadah mangkuk besar. Masukkan bumbu kelapa sangrai harum secukupnya. Aduk rata menggunakan tangan atau sendok sayur hingga seluruh sayuran terselimuti bumbu kelapa secara merata."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Tata urap sayur bumbu kelapa di atas piring saji yang dialasi daun pisang. Sajikan segera sebagai menu sayur sehat kaya serat pelengkap lauk harian.", "rawText": "Penyajian: Tata urap sayur bumbu kelapa di atas piring saji yang dialasi daun pisang. Sajikan segera sebagai menu sayur sehat kaya serat pelengkap lauk harian."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 140 kkal | Protein 5g | Lemak 7g | Karbohidrat 16g. Menu sayuran murni kaya antioksidan dan serat mikronutrien, dilengkapi lemak nabati rantai sedang (MCT) dari kelapa parut segar yang memberikan energi berkelanjutan.",
            "serving": "Per Porsi",
            "calories": 140,
            "protein": 5.0,
            "fat": 7.0,
            "carbohydrates": 16.0,
            "notes": "Menu sayuran murni kaya antioksidan dan serat mikronutrien, dilengkapi lemak nabati rantai sedang (MCT) dari kelapa parut segar yang memberikan energi berkelanjutan."
        }
    },
    {
        "recipeNumber": 210,
        "title": "210. Sup Ayam Makaroni Jagung Manis (Nusantara)",
        "name": "Sup Ayam Makaroni Jagung",
        "slug": "sup-ayam-makaroni-jagung",
        "scope": "INDONESIA",
        "origin": "Jawa Tengah",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 20,
        "cookTimeMinutes": 25,
        "servings": 5,
        "difficulty": "EASY",
        "spicinessLevel": 0,
        "categorySlug": "sup-soto",
        "cuisineTypeSlug": "masakan-rumahan",
        "rawContent": """210. Sup Ayam Makaroni Jagung Manis (Nusantara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama & Isian:
300g Daging ayam fillet (potong dadu 1.5 cm)
100g Makaroni elbow (rebus hingga matang al dente, tiriskan dan lumuri sedikit minyak agar tidak lengket)
1 buah Jagung manis (serut / pipil bijinya)
2 buah Wortel (kupas, potong bulat tipis 0.5 cm)
5 batang Buncis (potong 1 cm)
Bahan Kuah Sup Gurih Aromatik:
1.5 liter Air kaldu ayam bersih
5 siung Bawang putih (cincang halus)
1/2 buah Bawang bombay (cincang halus)
1/2 sdt Biji pala bubuk (khas aroma sup rumahan Indonesia)
1/2 sdt Merica putih bubuk
1.5 sdt Garam halus
1 sdt Gula pasir
1 sdt Kaldu jamur / ayam bubuk
1 batang Daun bawang (iris halus)
2 batang Daun seledri (ikat simpul)
1 sdm Mentega / margarin untuk menumis bumbu
Bahan Pelengkap:
2 sdm Bawang merah goreng renyah
Langkah-Langkah Pembuatan:
Menumis Bumbu Bawang dan Pala: Panaskan 1 sendok makan mentega dalam panci sup di atas api sedang. Masukkan bawang putih cincang dan bawang bombay cincang. Tumis hingga harum matang layu keemasan. Masukkan pala bubuk dan merica bubuk, aduk cepat selama 30 detik hingga aroma rempah keluar.
Membuat Kuah Kaldu dan Memasak Ayam: Masukkan potongan dadu daging ayam fillet ke dalam tumisan bumbu. Aduk hingga ayam berubah warna keputihan dan pori-porinya mengunci sari gurihnya. Tuangkan air kaldu ayam dan masukkan ikatan daun seledri. Masak dengan api sedang hingga kuah mendidih perlahan.
Memasukkan Sayuran Keras: Masukkan potongan wortel dan serutan jagung manis pipil ke dalam kuah mendidih. Masak selama 5-7 menit hingga wortel dan jagung mulai empuk manis.
Memasukkan Makaroni dan Buncis: Masukkan potongan buncis dan makaroni elbow yang sudah direbus. Bumbui dengan garam halus, gula pasir, dan kaldu jamur. Masak selama 2-3 menit hingga seluruh bahan matang sempurna dan rasa kuah berpadu gurih sedap. Cicipi rasanya.
Penyelesaian: Masukkan irisan daun bawang segar, aduk sebentar, lalu segera matikan api kompor agar sup tetap jernih dan daun bawang tetap harum segar.
Penyajian: Sendokkan sup ayam makaroni jagung manis panas ke dalam mangkuk saji saji. Beri taburan bawang merah goreng renyah di atasnya. Sajikan selagi hangat sebagai menu sup favorit keluarga tercinta.
Nutrisi (Per Porsi): Kalori 210 kkal | Protein 16g | Lemak 6g | Karbohidrat 24g. Pilihan makanan rumahan bernutrisi seimbang yang sangat disukai anak-anak dan keluarga, memadukan protein ayam, karbohidrat makaroni, serta lutein dan vitamin A dari wortel dan jagung manis.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama & Isian",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "300g Daging ayam fillet (potong dadu 1.5 cm)", "amount": 300.0, "unit": "g", "name": "Daging ayam fillet", "notes": "potong dadu 1.5 cm", "orderIndex": 1},
                    {"rawText": "100g Makaroni elbow (rebus al dente, tiriskan)", "amount": 100.0, "unit": "g", "name": "Makaroni elbow", "notes": "rebus al dente, tiriskan", "orderIndex": 2},
                    {"rawText": "1 buah Jagung manis (serut / pipil)", "amount": 1.0, "unit": "buah", "name": "Jagung manis", "notes": "serut / pipil", "orderIndex": 3},
                    {"rawText": "2 buah Wortel (potong bulat tipis)", "amount": 2.0, "unit": "buah", "name": "Wortel", "notes": "potong bulat tipis", "orderIndex": 4},
                    {"rawText": "5 batang Buncis (potong 1 cm)", "amount": 5.0, "unit": "batang", "name": "Buncis", "notes": "potong 1 cm", "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Kuah Sup Gurih Aromatik",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "1.5 liter Air kaldu ayam bersih", "amount": 1.5, "unit": "liter", "name": "Air kaldu ayam", "notes": None, "orderIndex": 1},
                    {"rawText": "5 siung Bawang putih (cincang halus)", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": "cincang halus", "orderIndex": 2},
                    {"rawText": "1/2 buah Bawang bombay (cincang halus)", "amount": 0.5, "unit": "buah", "name": "Bawang bombay", "notes": "cincang halus", "orderIndex": 3},
                    {"rawText": "1/2 sdt Biji pala bubuk", "amount": 0.5, "unit": "sdt", "name": "Biji pala bubuk", "notes": None, "orderIndex": 4},
                    {"rawText": "1/2 sdt Merica putih bubuk", "amount": 0.5, "unit": "sdt", "name": "Merica putih bubuk", "notes": None, "orderIndex": 5},
                    {"rawText": "1.5 sdt Garam halus", "amount": 1.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 6},
                    {"rawText": "1 sdt Gula pasir", "amount": 1.0, "unit": "sdt", "name": "Gula pasir", "notes": None, "orderIndex": 7},
                    {"rawText": "1 sdt Kaldu jamur / ayam bubuk", "amount": 1.0, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 8},
                    {"rawText": "1 batang Daun bawang (iris halus)", "amount": 1.0, "unit": "batang", "name": "Daun bawang", "notes": "iris halus", "orderIndex": 9},
                    {"rawText": "2 batang Seledri (ikat simpul)", "amount": 2.0, "unit": "batang", "name": "Seledri", "notes": "ikat simpul", "orderIndex": 10},
                    {"rawText": "1 sdm Mentega / margarin untuk menumis", "amount": 1.0, "unit": "sdm", "name": "Mentega", "notes": "untuk menumis", "orderIndex": 11}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menumis Bumbu Bawang dan Pala", "instruction": "Panaskan 1 sendok makan mentega dalam panci sup di atas api sedang. Masukkan bawang putih cincang dan bawang bombay cincang. Tumis hingga harum matang layu keemasan. Masukkan pala bubuk dan merica bubuk, aduk cepat selama 30 detik hingga aroma rempah keluar.", "rawText": "Menumis Bumbu Bawang dan Pala: Panaskan 1 sendok makan mentega dalam panci sup di atas api sedang. Masukkan bawang putih cincang dan bawang bombay cincang. Tumis hingga harum matang layu keemasan. Masukkan pala bubuk dan merica bubuk, aduk cepat selama 30 detik hingga aroma rempah keluar."},
            {"stepNumber": 2, "title": "Membuat Kuah Kaldu dan Memasak Ayam", "instruction": "Masukkan potongan dadu daging ayam fillet ke dalam tumisan bumbu. Aduk hingga ayam berubah warna keputihan dan pori-porinya mengunci sari gurihnya. Tuangkan air kaldu ayam dan masukkan ikatan daun seledri. Masak dengan api sedang hingga kuah mendidih perlahan.", "rawText": "Membuat Kuah Kaldu dan Memasak Ayam: Masukkan potongan dadu daging ayam fillet ke dalam tumisan bumbu. Aduk hingga ayam berubah warna keputihan dan pori-porinya mengunci sari gurihnya. Tuangkan air kaldu ayam dan masukkan ikatan daun seledri. Masak dengan api sedang hingga kuah mendidih perlahan."},
            {"stepNumber": 3, "title": "Memasukkan Sayuran Keras", "instruction": "Masukkan potongan wortel dan serutan jagung manis pipil ke dalam kuah mendidih. Masak selama 5-7 menit hingga wortel dan jagung mulai empuk manis.", "rawText": "Memasukkan Sayuran Keras: Masukkan potongan wortel dan serutan jagung manis pipil ke dalam kuah mendidih. Masak selama 5-7 menit hingga wortel dan jagung mulai empuk manis."},
            {"stepNumber": 4, "title": "Memasukkan Makaroni dan Buncis", "instruction": "Masukkan potongan buncis dan makaroni elbow yang sudah direbus. Bumbui dengan garam halus, gula pasir, dan kaldu jamur. Masak selama 2-3 menit hingga seluruh bahan matang sempurna dan rasa kuah berpadu gurih sedap.", "rawText": "Memasukkan Makaroni dan Buncis: Masukkan potongan buncis dan makaroni elbow yang sudah direbus. Bumbui dengan garam halus, gula pasir, dan kaldu jamur. Masak selama 2-3 menit hingga seluruh bahan matang sempurna dan rasa kuah berpadu gurih sedap."},
            {"stepNumber": 5, "title": "Penyelesaian dan Penyajian", "instruction": "Masukkan irisan daun bawang segar, aduk sebentar, lalu segera matikan api kompor. Sendokkan sup ayam makaroni jagung manis panas ke dalam mangkuk saji, taburi bawang merah goreng renyah di atasnya. Sajikan hangat.", "rawText": "Penyelesaian dan Penyajian: Masukkan irisan daun bawang segar, aduk sebentar, lalu segera matikan api kompor. Sendokkan sup ayam makaroni jagung manis panas ke dalam mangkuk saji, taburi bawang merah goreng renyah di atasnya. Sajikan hangat."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 210 kkal | Protein 16g | Lemak 6g | Karbohidrat 24g. Pilihan makanan rumahan bernutrisi seimbang yang sangat disukai anak-anak dan keluarga, memadukan protein ayam, karbohidrat makaroni, serta lutein dan vitamin A dari wortel dan jagung manis.",
            "serving": "Per Porsi",
            "calories": 210,
            "protein": 16.0,
            "fat": 6.0,
            "carbohydrates": 24.0,
            "notes": "Pilihan makanan rumahan bernutrisi seimbang yang sangat disukai anak-anak dan keluarga, memadukan protein ayam, karbohidrat makaroni, serta lutein dan vitamin A dari wortel dan jagung manis."
        }
    }
]

file_path = os.path.join(os.path.dirname(__file__), '../src/seeder/recipes-data.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter out if any 201-210 already exist to be idempotent
data['recipes'] = [r for r in data['recipes'] if r['recipeNumber'] < 201]

# Append new recipes
data['recipes'].extend(new_recipes)

# Save back to JSON
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total_count = len(data['recipes'])
print(f"Berhasil menambahkan 10 resep Masakan Rumahan! Total resep saat ini: {total_count}")

