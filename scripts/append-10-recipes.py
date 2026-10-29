import json
import os

DATA_PATH = 'src/seeder/recipes-data.json'

new_recipes = [
  {
    "recipeNumber": 171,
    "title": "171. Soto Betawi (DKI Jakarta)",
    "name": "Soto Betawi",
    "slug": "soto-betawi",
    "scope": "INDONESIA",
    "origin": "DKI Jakarta",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 25,
    "cookTimeMinutes": 60,
    "servings": 4,
    "difficulty": "MEDIUM",
    "spicinessLevel": 1,
    "categorySlug": "sup-soto",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """171. Soto Betawi (DKI Jakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Daging Sapi (potongan Sandung Lamur / Daging Has, potong dadu 2x2 cm)
200g Babat Sapi (rebus empuk, potong dadu)
1.5 liter Air kaldu rebusan daging
250 ml Santan Kental (dari 1 butir kelapa parut)
250 ml Susu Cair Evaporasi / Susu UHT Full Cream
2 sdm Minyak Samin (opsional, untuk aroma gurih khas Betawi)
Bumbu Halus:
12 siung Bawang merah
6 siung Bawang putih
4 butir Kemiri (sangrai)
2 cm Jahe
2 cm Kunyit (bakar)
1 sdm Ketumbar bubuk sangrai
1/2 sdt Jintan bubuk
1/2 sdt Pala bubuk
1 sdt Lada putih bubuk
1 sdm Garam dan 1 sdt Gula pasir
Bumbu Rempah Cemplung:
3 batang Serai (memarkan)
2 ruas Lengkuas (memarkan)
5 lembar Daun jeruk (buang tulang)
3 lembar Daun salam
3 cm Kayu manis
3 butir Cengkih
2 butir Kapulaga
Pelengkap Penyajian:
2 buah Kentang (potong dadu, goreng matang)
2 buah Tomat merah segar (potong juring)
2 batang Daun bawang dan Seledri (iris halus)
Bawang merah goreng secukupnya
Emping melinjo goreng secukupnya
Sambal rawit rebus
Jeruk limau dan Kecap manis
Langkah-Langkah Pembuatan:
Merebus Daging dan Menyiapkan Kaldu: Rebus daging sapi dalam 2 liter air mendidih hingga setengah empuk. Angkat kotoran busa di permukaan air (skimming). Ambil kaldu sebanyak 1.5 liter, masukkan kembali daging dan babat yang sudah dipotong dadu.
Menumis Bumbu Rempah: Panaskan sedikit minyak dan minyak samin di wajan. Tumis bumbu halus bersama serai, lengkuas, daun jeruk, daun salam, kayu manis, cengkih, dan kapulaga hingga harum, matang tanak, dan minyak bumbu terpisah.
Memasukkan Bumbu ke Kaldu: Tuangkan tumisan bumbu halus ke dalam panci rebusan kaldu daging. Aduk rata dan masak dengan api sedang selama 20 menit agar rempah meresap ke dalam serat daging.
Menuang Santan dan Susu: Tuang santan kental perlahan sambil terus diaduk perlahan agar santan tidak pecah. Masukkan susu cair evaporasi, garam, dan lada. Masak dengan api kecil hingga kuah mendidih beraroma harum gurih dan kuah mengental lembut.
Penyajian: Tata potongan kentang goreng, tomat merah, daging sapi, dan babat di dalam mangkuk saji. Siram dengan kuah soto betawi panas mengepul. Taburi dengan daun bawang, seledri, bawang goreng, dan emping renyah. Sajikan bersama perasan jeruk limau dan sambal cabai rawit.
Nutrisi (Per Porsi Tanpa Nasi): Kalori 350 kkal | Protein 24g | Lemak 22g | Karbohidrat 12g. Kandungan protein tinggi dari daging sapi serta kalsium dari perpaduan kuah susu, seimbang dengan antioksidan likopen dari tomat segar.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "500g Daging Sapi (potongan Sandung Lamur, potong dadu 2x2 cm)", "amount": 500.0, "unit": "g", "name": "Daging Sapi", "notes": "potongan Sandung Lamur, potong dadu 2x2 cm", "orderIndex": 1},
          {"rawText": "200g Babat Sapi (rebus empuk, potong dadu)", "amount": 200.0, "unit": "g", "name": "Babat Sapi", "notes": "rebus empuk, potong dadu", "orderIndex": 2},
          {"rawText": "1.5 liter Air kaldu rebusan daging", "amount": 1.5, "unit": "liter", "name": "Air kaldu rebusan daging", "notes": None, "orderIndex": 3},
          {"rawText": "250 ml Santan Kental (dari 1 butir kelapa parut)", "amount": 250.0, "unit": "ml", "name": "Santan Kental", "notes": "dari 1 butir kelapa parut", "orderIndex": 4},
          {"rawText": "250 ml Susu Cair Evaporasi / Susu UHT Full Cream", "amount": 250.0, "unit": "ml", "name": "Susu Cair Evaporasi", "notes": "atau Susu UHT Full Cream", "orderIndex": 5},
          {"rawText": "2 sdm Minyak Samin", "amount": 2.0, "unit": "sdm", "name": "Minyak Samin", "notes": "opsional, aroma gurih khas Betawi", "orderIndex": 6}
        ]
      },
      {
        "name": "Bumbu Halus",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "12 siung Bawang merah", "amount": 12.0, "unit": "siung", "name": "Bawang merah", "notes": None, "orderIndex": 1},
          {"rawText": "6 siung Bawang putih", "amount": 6.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
          {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 3},
          {"rawText": "2 cm Jahe", "amount": 2.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 4},
          {"rawText": "2 cm Kunyit (bakar)", "amount": 2.0, "unit": "cm", "name": "Kunyit", "notes": "bakar", "orderIndex": 5},
          {"rawText": "1 sdm Ketumbar bubuk sangrai", "amount": 1.0, "unit": "sdm", "name": "Ketumbar bubuk sangrai", "notes": None, "orderIndex": 6},
          {"rawText": "1/2 sdt Jintan bubuk", "amount": 0.5, "unit": "sdt", "name": "Jintan bubuk", "notes": None, "orderIndex": 7},
          {"rawText": "1/2 sdt Pala bubuk", "amount": 0.5, "unit": "sdt", "name": "Pala bubuk", "notes": None, "orderIndex": 8},
          {"rawText": "1 sdt Lada putih bubuk", "amount": 1.0, "unit": "sdt", "name": "Lada putih bubuk", "notes": None, "orderIndex": 9},
          {"rawText": "1 sdm Garam dan 1 sdt Gula pasir", "amount": 1.0, "unit": "sdm", "name": "Garam dan Gula pasir", "notes": None, "orderIndex": 10}
        ]
      },
      {
        "name": "Bumbu Rempah Cemplung",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "3 batang Serai (memarkan)", "amount": 3.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 1},
          {"rawText": "2 ruas Lengkuas (memarkan)", "amount": 2.0, "unit": "ruas", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 2},
          {"rawText": "5 lembar Daun jeruk (buang tulang)", "amount": 5.0, "unit": "lembar", "name": "Daun jeruk", "notes": "buang tulang", "orderIndex": 3},
          {"rawText": "3 lembar Daun salam", "amount": 3.0, "unit": "lembar", "name": "Daun salam", "notes": None, "orderIndex": 4},
          {"rawText": "3 cm Kayu manis", "amount": 3.0, "unit": "cm", "name": "Kayu manis", "notes": None, "orderIndex": 5},
          {"rawText": "3 butir Cengkih", "amount": 3.0, "unit": "butir", "name": "Cengkih", "notes": None, "orderIndex": 6},
          {"rawText": "2 butir Kapulaga", "amount": 2.0, "unit": "butir", "name": "Kapulaga", "notes": None, "orderIndex": 7}
        ]
      },
      {
        "name": "Pelengkap Penyajian",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "2 buah Kentang (potong dadu, goreng matang)", "amount": 2.0, "unit": "buah", "name": "Kentang", "notes": "potong dadu, goreng matang", "orderIndex": 1},
          {"rawText": "2 buah Tomat merah segar (potong juring)", "amount": 2.0, "unit": "buah", "name": "Tomat merah segar", "notes": "potong juring", "orderIndex": 2},
          {"rawText": "2 batang Daun bawang dan Seledri (iris halus)", "amount": 2.0, "unit": "batang", "name": "Daun bawang dan Seledri", "notes": "iris halus", "orderIndex": 3},
          {"rawText": "Bawang merah goreng secukupnya", "amount": None, "unit": "secukupnya", "name": "Bawang merah goreng", "notes": None, "orderIndex": 4},
          {"rawText": "Emping melinjo goreng secukupnya", "amount": None, "unit": "secukupnya", "name": "Emping melinjo goreng", "notes": None, "orderIndex": 5},
          {"rawText": "Jeruk limau dan Kecap manis secukupnya", "amount": None, "unit": "secukupnya", "name": "Jeruk limau dan Kecap manis", "notes": None, "orderIndex": 6}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Merebus Daging dan Menyiapkan Kaldu", "instruction": "Rebus daging sapi dalam 2 liter air mendidih hingga setengah empuk. Angkat kotoran busa di permukaan air (skimming). Ambil kaldu sebanyak 1.5 liter, masukkan kembali daging dan babat yang sudah dipotong dadu.", "rawText": "Merebus Daging dan Menyiapkan Kaldu: Rebus daging sapi dalam 2 liter air mendidih hingga setengah empuk. Angkat kotoran busa di permukaan air (skimming). Ambil kaldu sebanyak 1.5 liter, masukkan kembali daging dan babat yang sudah dipotong dadu."},
      {"stepNumber": 2, "title": "Menumis Bumbu Rempah", "instruction": "Panaskan sedikit minyak dan minyak samin di wajan. Tumis bumbu halus bersama serai, lengkuas, daun jeruk, daun salam, kayu manis, cengkih, dan kapulaga hingga harum, matang tanak, dan minyak bumbu terpisah.", "rawText": "Menumis Bumbu Rempah: Panaskan sedikit minyak dan minyak samin di wajan. Tumis bumbu halus bersama serai, lengkuas, daun jeruk, daun salam, kayu manis, cengkih, dan kapulaga hingga harum, matang tanak, dan minyak bumbu terpisah."},
      {"stepNumber": 3, "title": "Memasukkan Bumbu ke Kaldu", "instruction": "Tuangkan tumisan bumbu halus ke dalam panci rebusan kaldu daging. Aduk rata dan masak dengan api sedang selama 20 menit agar rempah meresap ke dalam serat daging.", "rawText": "Memasukkan Bumbu ke Kaldu: Tuangkan tumisan bumbu halus ke dalam panci rebusan kaldu daging. Aduk rata dan masak dengan api sedang selama 20 menit agar rempah meresap ke dalam serat daging."},
      {"stepNumber": 4, "title": "Menuang Santan dan Susu", "instruction": "Tuang santan kental perlahan sambil terus diaduk perlahan agar santan tidak pecah. Masukkan susu cair evaporasi, garam, dan lada. Masak dengan api kecil hingga kuah mendidih beraroma harum gurih dan kuah mengental lembut.", "rawText": "Menuang Santan dan Susu: Tuang santan kental perlahan sambil terus diaduk perlahan agar santan tidak pecah. Masukkan susu cair evaporasi, garam, dan lada. Masak dengan api kecil hingga kuah mendidih beraroma harum gurih dan kuah mengental lembut."},
      {"stepNumber": 5, "title": "Penyajian", "instruction": "Tata potongan kentang goreng, tomat merah, daging sapi, dan babat di dalam mangkuk saji. Siram dengan kuah soto betawi panas mengepul. Taburi dengan daun bawang, seledri, bawang goreng, dan emping renyah. Sajikan bersama perasan jeruk limau dan sambal cabai rawit.", "rawText": "Penyajian: Tata potongan kentang goreng, tomat merah, daging sapi, dan babat di dalam mangkuk saji. Siram dengan kuah soto betawi panas mengepul. Taburi dengan daun bawang, seledri, bawang goreng, dan emping renyah. Sajikan bersama perasan jeruk limau dan sambal cabai rawit."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Porsi Tanpa Nasi): Kalori 350 kkal | Protein 24g | Lemak 22g | Karbohidrat 12g. Kandungan protein tinggi dari daging sapi serta kalsium dari perpaduan kuah susu, seimbang dengan antioksidan likopen dari tomat segar.",
      "serving": "Per Porsi Tanpa Nasi",
      "calories": 350,
      "protein": 24.0,
      "fat": 22.0,
      "carbohydrates": 12.0,
      "notes": "Kandungan protein tinggi dari daging sapi serta kalsium dari perpaduan kuah susu, seimbang dengan antioksidan likopen dari tomat segar."
    }
  },
  {
    "recipeNumber": 172,
    "title": "172. Sate Maranggi Khas Purwakarta (Jawa Barat)",
    "name": "Sate Maranggi Khas Purwakarta",
    "slug": "sate-maranggi-khas-purwakarta",
    "scope": "INDONESIA",
    "origin": "Purwakarta, Jawa Barat",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 60,
    "cookTimeMinutes": 30,
    "servings": 4,
    "difficulty": "MEDIUM",
    "spicinessLevel": 1,
    "categorySlug": "sate-bakaran",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """172. Sate Maranggi Khas Purwakarta (Jawa Barat)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Daging Sapi Has Dalam / Gandik (potong dadu 2x2 cm)
5 lembar Daun Pepaya (untuk membungkus dan mengempukkan daging)
Tusuk sate secukupnya (rendam air agar tidak mudah hangus)
Bumbu Marinasi Halus:
6 siung Bawang merah
4 siung Bawang putih
1 sdm Ketumbar (sangrai)
2 cm Jahe
2 cm Lengkuas muda
1 sdt Asam jawa (larutkan dengan 3 sdm air hangat)
3 sdm Gula merah aren (sisir halus)
5 sdm Kecap manis
1 sdt Garam dan 1/2 sdt Lada putih bubuk
Bahan Olesan Bakaran:
3 sdm Kecap manis
1 sdm Margarin cair atau minyak sayur
Pelengkap Sambal Tomat Segar:
2 buah Tomat merah segar (potong dadu kecil)
10 buah Cabai rawit hijau dan merah (iris halus)
5 siung Bawang merah (iris tipis)
1 buah Jeruk limau (ambil airnya)
4 sdm Kecap manis
Langkah-Langkah Pembuatan:
Mengempukkan Daging: Remas-remas daun pepaya, lalu bungkus potongan daging sapi rapat-rapat. Diamkan selama 30 menit di suhu ruang agar enzim papain mengempukkan serat daging secara alami tanpa merusak tekstur.
Membuat Bumbu Marinasi: Haluskan bawang merah, bawang putih, ketumbar sangrai, jahe, dan lengkuas. Campurkan dengan kecap manis, larutan air asam jawa, gula merah sisir, lada, dan garam. Aduk hingga bumbu larut merata.
Proses Marinasi: Buka bungkusan daging, masukkan potongan daging ke dalam mangkuk bumbu marinasi. Aduk dan remas perlahan agar bumbu meresap ke dalam daging. Diamkan di lemari pendingin minimal 1 jam (terbaik 2 jam).
Menusuk Sate: Tusukkan potongan daging sapi ke tusuk sate (sekitar 4 potong per tusuk).
Membakar Sate: Siapkan panggangan arang atau grill pan panas. Bakar sate sambil sesekali dibolak-balik. Olesi dengan campuran kecap manis dan margarin cair. Bakar hingga matang kecokelatan, berkaramel, dan tercium aroma asap wangi gurih tanpa gosong.
Penyajian: Sajikan Sate Maranggi hangat bersama sambal tomat kecap segar (campuran tomat, cabai rawit, bawang merah, perasan jeruk limau, dan kecap manis) serta lontong atau nasi pulen hangat.
Nutrisi (Per 10 Tusuk): Kalori 310 kkal | Protein 28g | Lemak 16g | Karbohidrat 14g. Sumber zat besi dan protein hewani murni dari daging sapi tanpa lemak jenuh dari kuah santan.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "500g Daging Sapi Has Dalam (potong dadu 2x2 cm)", "amount": 500.0, "unit": "g", "name": "Daging Sapi Has Dalam", "notes": "potong dadu 2x2 cm", "orderIndex": 1},
          {"rawText": "5 lembar Daun Pepaya (untuk membungkus)", "amount": 5.0, "unit": "lembar", "name": "Daun Pepaya", "notes": "untuk membungkus mengempukkan daging", "orderIndex": 2},
          {"rawText": "Tusuk sate secukupnya (rendam air)", "amount": None, "unit": "secukupnya", "name": "Tusuk sate", "notes": "rendam air agar tidak hangus", "orderIndex": 3}
        ]
      },
      {
        "name": "Bumbu Marinasi Halus",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "6 siung Bawang merah", "amount": 6.0, "unit": "siung", "name": "Bawang merah", "notes": None, "orderIndex": 1},
          {"rawText": "4 siung Bawang putih", "amount": 4.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
          {"rawText": "1 sdm Ketumbar (sangrai)", "amount": 1.0, "unit": "sdm", "name": "Ketumbar", "notes": "sangrai", "orderIndex": 3},
          {"rawText": "2 cm Jahe", "amount": 2.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 4},
          {"rawText": "2 cm Lengkuas muda", "amount": 2.0, "unit": "cm", "name": "Lengkuas muda", "notes": None, "orderIndex": 5},
          {"rawText": "1 sdt Asam jawa (larutkan air)", "amount": 1.0, "unit": "sdt", "name": "Asam jawa", "notes": "larutkan air hangat", "orderIndex": 6},
          {"rawText": "3 sdm Gula merah aren (sisir)", "amount": 3.0, "unit": "sdm", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 7},
          {"rawText": "5 sdm Kecap manis", "amount": 5.0, "unit": "sdm", "name": "Kecap manis", "notes": None, "orderIndex": 8},
          {"rawText": "1 sdt Garam dan 1/2 sdt Lada putih", "amount": 1.0, "unit": "sdt", "name": "Garam dan Lada putih", "notes": None, "orderIndex": 9}
        ]
      },
      {
        "name": "Bahan Olesan Bakaran",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "3 sdm Kecap manis", "amount": 3.0, "unit": "sdm", "name": "Kecap manis", "notes": None, "orderIndex": 1},
          {"rawText": "1 sdm Margarin cair", "amount": 1.0, "unit": "sdm", "name": "Margarin cair", "notes": None, "orderIndex": 2}
        ]
      },
      {
        "name": "Pelengkap Sambal Tomat Segar",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "2 buah Tomat merah segar (potong dadu kecil)", "amount": 2.0, "unit": "buah", "name": "Tomat merah segar", "notes": "potong dadu kecil", "orderIndex": 1},
          {"rawText": "10 buah Cabai rawit hijau dan merah (iris halus)", "amount": 10.0, "unit": "buah", "name": "Cabai rawit", "notes": "iris halus", "orderIndex": 2},
          {"rawText": "5 siung Bawang merah (iris tipis)", "amount": 5.0, "unit": "siung", "name": "Bawang merah", "notes": "iris tipis", "orderIndex": 3},
          {"rawText": "1 buah Jeruk limau (ambil airnya)", "amount": 1.0, "unit": "buah", "name": "Jeruk limau", "notes": "ambil airnya", "orderIndex": 4},
          {"rawText": "4 sdm Kecap manis", "amount": 4.0, "unit": "sdm", "name": "Kecap manis", "notes": None, "orderIndex": 5}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Mengempukkan Daging", "instruction": "Remas-remas daun pepaya, lalu bungkus potongan daging sapi rapat-rapat. Diamkan selama 30 menit di suhu ruang agar enzim papain mengempukkan serat daging secara alami tanpa merusak tekstur.", "rawText": "Mengempukkan Daging: Remas-remas daun pepaya, lalu bungkus potongan daging sapi rapat-rapat. Diamkan selama 30 menit di suhu ruang agar enzim papain mengempukkan serat daging secara alami tanpa merusak tekstur."},
      {"stepNumber": 2, "title": "Membuat Bumbu Marinasi", "instruction": "Haluskan bawang merah, bawang putih, ketumbar sangrai, jahe, dan lengkuas. Campurkan dengan kecap manis, larutan air asam jawa, gula merah sisir, lada, dan garam. Aduk hingga bumbu larut merata.", "rawText": "Membuat Bumbu Marinasi: Haluskan bawang merah, bawang putih, ketumbar sangrai, jahe, dan lengkuas. Campurkan dengan kecap manis, larutan air asam jawa, gula merah sisir, lada, dan garam. Aduk hingga bumbu larut merata."},
      {"stepNumber": 3, "title": "Proses Marinasi", "instruction": "Buka bungkusan daging, masukkan potongan daging ke dalam mangkuk bumbu marinasi. Aduk dan remas perlahan agar bumbu meresap ke dalam daging. Diamkan di lemari pendingin minimal 1 jam (terbaik 2 jam).", "rawText": "Proses Marinasi: Buka bungkusan daging, masukkan potongan daging ke dalam mangkuk bumbu marinasi. Aduk dan remas perlahan agar bumbu meresap ke dalam daging. Diamkan di lemari pendingin minimal 1 jam (terbaik 2 jam)."},
      {"stepNumber": 4, "title": "Menusuk Sate", "instruction": "Tusukkan potongan daging sapi ke tusuk sate (sekitar 4 potong per tusuk).", "rawText": "Menusuk Sate: Tusukkan potongan daging sapi ke tusuk sate (sekitar 4 potong per tusuk)."},
      {"stepNumber": 5, "title": "Membakar Sate", "instruction": "Siapkan panggangan arang atau grill pan panas. Bakar sate sambil sesekali dibolak-balik. Olesi dengan campuran kecap manis dan margarin cair. Bakar hingga matang kecokelatan, berkaramel, dan tercium aroma asap wangi gurih tanpa gosong.", "rawText": "Membakar Sate: Siapkan panggangan arang atau grill pan panas. Bakar sate sambil sesekali dibolak-balik. Olesi dengan campuran kecap manis dan margarin cair. Bakar hingga matang kecokelatan, berkaramel, dan tercium aroma asap wangi gurih tanpa gosong."},
      {"stepNumber": 6, "title": "Penyajian", "instruction": "Sajikan Sate Maranggi hangat bersama sambal tomat kecap segar (campuran tomat, cabai rawit, bawang merah, perasan jeruk limau, dan kecap manis) serta lontong atau nasi pulen hangat.", "rawText": "Penyajian: Sajikan Sate Maranggi hangat bersama sambal tomat kecap segar (campuran tomat, cabai rawit, bawang merah, perasan jeruk limau, dan kecap manis) serta lontong atau nasi pulen hangat."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per 10 Tusuk): Kalori 310 kkal | Protein 28g | Lemak 16g | Karbohidrat 14g. Sumber zat besi dan protein hewani murni dari daging sapi tanpa lemak jenuh dari kuah santan.",
      "serving": "Per 10 Tusuk",
      "calories": 310,
      "protein": 28.0,
      "fat": 16.0,
      "carbohydrates": 14.0,
      "notes": "Sumber zat besi dan protein hewani murni dari daging sapi tanpa lemak jenuh dari kuah santan."
    }
  },
  {
    "recipeNumber": 173,
    "title": "173. Pallubasa Khas Makassar (Sulawesi Selatan)",
    "name": "Pallubasa Khas Makassar",
    "slug": "pallubasa-khas-makassar",
    "scope": "INDONESIA",
    "origin": "Makassar, Sulawesi Selatan",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 30,
    "cookTimeMinutes": 75,
    "servings": 4,
    "difficulty": "HARD",
    "spicinessLevel": 2,
    "categorySlug": "sup-soto",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """173. Pallubasa Khas Makassar (Sulawesi Selatan)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Daging Sapi (potongan Sandung Lamur atau Gandik, potong dadu)
150g Kelapa Parut (sangrai kering kecokelatan, lalu tumbuk/giling hingga berminyak)
1.5 liter Air bersih (untuk kaldu)
30 ml Air asam jawa pekat
1 sdm Gula merah sisir
1 sdm Kecap manis
Bumbu Halus:
8 butir Bawang merah
5 siung Bawang putih
6 buah Cabai merah keriting
2 cm Jahe
1 sdm Ketumbar sangrai
1/2 sdt Jintan bubuk
1/2 sdt Pala bubuk
1 sdm Garam dan 1/2 sdt Lada bubuk
Bumbu Rempah Cemplung:
2 batang Serai (memarkan)
3 cm Lengkuas (memarkan)
3 cm Kayu manis
3 butir Cengkih
Pelengkap Penyajian:
4 butir Kuning Telur Ayam Kampung Mentah (alas khas Pallubasa)
Daun bawang iris tipis
Bawang merah goreng renyah
Jeruk nipis dan sambal cabai rawit rebus
Langkah-Langkah Pembuatan:
Merebus Daging: Rebus daging sapi dalam air mendidih hingga empuk. Angkat daging, tiriskan lalu potong dadu. Saring air rebusannya sebanyak 1.2 liter untuk dijadikan kuah kaldu.
Menumis Bumbu Halus: Panaskan 3 sdm minyak di wajan. Tumis bumbu halus bersama serai, lengkuas, kayu manis, dan cengkih hingga harum, matang tanak, dan berminyak.
Memasak Kuah Rempah: Masukkan tumisan bumbu halus ke dalam panci kaldu sapi. Masukkan kembali potongan daging sapi. Masak dengan api sedang hingga kuah mendidih.
Menambahkan Kelapa Sangrai: Masukkan kelapa parut sangrai yang telah ditumbuk halus berminyak, air asam jawa, gula merah, kecap manis, garam, dan lada. Aduk rata. Kecilkan api dan masak perlahan (simmer) selama 30 menit hingga bumbu meresap sempurna dan kuah menjadi pekat kecokelatan.
Penyajian Tradisional: Siapkan mangkuk saji. Letakkan satu kuning telur ayam kampung mentah di dasar mangkuk (teknik alas). Siram langsung dengan kuah Pallubasa panas mendidih beserta potongan dagingnya (panas kuah akan mematangkan telur secara lembut dan memberi rasa creamy gurih). Taburi daun bawang dan bawang goreng. Sajikan bersama perasan jeruk nipis dan sambal rawit.
Nutrisi (Per Porsi): Kalori 380 kkal | Protein 26g | Lemak 28g | Karbohidrat 8g. Kaya lemak sehat dan serat dari kelapa parut sangrai serta asam amino esensial dari kuning telur kampung.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "500g Daging Sapi (potong dadu)", "amount": 500.0, "unit": "g", "name": "Daging Sapi", "notes": "potong dadu", "orderIndex": 1},
          {"rawText": "150g Kelapa Parut (sangrai kering, tumbuk berminyak)", "amount": 150.0, "unit": "g", "name": "Kelapa Parut", "notes": "sangrai kering, tumbuk berminyak", "orderIndex": 2},
          {"rawText": "1.5 liter Air bersih (untuk kaldu)", "amount": 1.5, "unit": "liter", "name": "Air kaldu", "notes": None, "orderIndex": 3},
          {"rawText": "30 ml Air asam jawa pekat", "amount": 30.0, "unit": "ml", "name": "Air asam jawa", "notes": "pekat", "orderIndex": 4},
          {"rawText": "1 sdm Gula merah sisir", "amount": 1.0, "unit": "sdm", "name": "Gula merah sisir", "notes": None, "orderIndex": 5},
          {"rawText": "1 sdm Kecap manis", "amount": 1.0, "unit": "sdm", "name": "Kecap manis", "notes": None, "orderIndex": 6}
        ]
      },
      {
        "name": "Bumbu Halus",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "8 butir Bawang merah", "amount": 8.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
          {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
          {"rawText": "6 buah Cabai merah keriting", "amount": 6.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 3},
          {"rawText": "2 cm Jahe", "amount": 2.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 4},
          {"rawText": "1 sdm Ketumbar sangrai", "amount": 1.0, "unit": "sdm", "name": "Ketumbar sangrai", "notes": None, "orderIndex": 5},
          {"rawText": "1/2 sdt Jintan bubuk", "amount": 0.5, "unit": "sdt", "name": "Jintan bubuk", "notes": None, "orderIndex": 6},
          {"rawText": "1/2 sdt Pala bubuk", "amount": 0.5, "unit": "sdt", "name": "Pala bubuk", "notes": None, "orderIndex": 7},
          {"rawText": "1 sdm Garam dan 1/2 sdt Lada bubuk", "amount": 1.0, "unit": "sdm", "name": "Garam dan Lada bubuk", "notes": None, "orderIndex": 8}
        ]
      },
      {
        "name": "Bumbu Rempah Cemplung",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 1},
          {"rawText": "3 cm Lengkuas (memarkan)", "amount": 3.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 2},
          {"rawText": "3 cm Kayu manis", "amount": 3.0, "unit": "cm", "name": "Kayu manis", "notes": None, "orderIndex": 3},
          {"rawText": "3 butir Cengkih", "amount": 3.0, "unit": "butir", "name": "Cengkih", "notes": None, "orderIndex": 4}
        ]
      },
      {
        "name": "Pelengkap Penyajian",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "4 butir Kuning Telur Ayam Kampung Mentah", "amount": 4.0, "unit": "butir", "name": "Kuning Telur Ayam Kampung", "notes": "alas mentah khas Pallubasa", "orderIndex": 1},
          {"rawText": "Daun bawang iris tipis secukupnya", "amount": None, "unit": "secukupnya", "name": "Daun bawang", "notes": "iris tipis", "orderIndex": 2},
          {"rawText": "Bawang merah goreng renyah secukupnya", "amount": None, "unit": "secukupnya", "name": "Bawang merah goreng", "notes": None, "orderIndex": 3},
          {"rawText": "Jeruk nipis dan sambal cabai rawit rebus", "amount": None, "unit": "secukupnya", "name": "Jeruk nipis dan sambal rawit", "notes": None, "orderIndex": 4}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Merebus Daging", "instruction": "Rebus daging sapi dalam air mendidih hingga empuk. Angkat daging, tiriskan lalu potong dadu. Saring air rebusannya sebanyak 1.2 liter untuk dijadikan kuah kaldu.", "rawText": "Merebus Daging: Rebus daging sapi dalam air mendidih hingga empuk. Angkat daging, tiriskan lalu potong dadu. Saring air rebusannya sebanyak 1.2 liter untuk dijadikan kuah kaldu."},
      {"stepNumber": 2, "title": "Menumis Bumbu Halus", "instruction": "Panaskan 3 sdm minyak di wajan. Tumis bumbu halus bersama serai, lengkuas, kayu manis, dan cengkih hingga harum, matang tanak, dan berminyak.", "rawText": "Menumis Bumbu Halus: Panaskan 3 sdm minyak di wajan. Tumis bumbu halus bersama serai, lengkuas, kayu manis, dan cengkih hingga harum, matang tanak, dan berminyak."},
      {"stepNumber": 3, "title": "Memasak Kuah Rempah", "instruction": "Masukkan tumisan bumbu halus ke dalam panci kaldu sapi. Masukkan kembali potongan daging sapi. Masak dengan api sedang hingga kuah mendidih.", "rawText": "Memasak Kuah Rempah: Masukkan tumisan bumbu halus ke dalam panci kaldu sapi. Masukkan kembali potongan daging sapi. Masak dengan api sedang hingga kuah mendidih."},
      {"stepNumber": 4, "title": "Menambahkan Kelapa Sangrai", "instruction": "Masukkan kelapa parut sangrai yang telah ditumbuk halus berminyak, air asam jawa, gula merah, kecap manis, garam, dan lada. Aduk rata. Kecilkan api dan masak perlahan (simmer) selama 30 menit hingga bumbu meresap sempurna dan kuah menjadi pekat kecokelatan.", "rawText": "Menambahkan Kelapa Sangrai: Masukkan kelapa parut sangrai yang telah ditumbuk halus berminyak, air asam jawa, gula merah, kecap manis, garam, dan lada. Aduk rata. Kecilkan api dan masak perlahan (simmer) selama 30 menit hingga bumbu meresap sempurna dan kuah menjadi pekat kecokelatan."},
      {"stepNumber": 5, "title": "Penyajian Tradisional", "instruction": "Siapkan mangkuk saji. Letakkan satu kuning telur ayam kampung mentah di dasar mangkuk (teknik alas). Siram langsung dengan kuah Pallubasa panas mendidih beserta potongan dagingnya (panas kuah akan mematangkan telur secara lembut dan memberi rasa creamy gurih). Taburi daun bawang dan bawang goreng. Sajikan bersama perasan jeruk nipis dan sambal rawit.", "rawText": "Penyajian Tradisional: Siapkan mangkuk saji. Letakkan satu kuning telur ayam kampung mentah di dasar mangkuk (teknik alas). Siram langsung dengan kuah Pallubasa panas mendidih beserta potongan dagingnya (panas kuah akan mematangkan telur secara lembut dan memberi rasa creamy gurih). Taburi daun bawang dan bawang goreng. Sajikan bersama perasan jeruk nipis dan sambal rawit."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Porsi): Kalori 380 kkal | Protein 26g | Lemak 28g | Karbohidrat 8g. Kaya lemak sehat dan serat dari kelapa parut sangrai serta asam amino esensial dari kuning telur kampung.",
      "serving": "Per Porsi",
      "calories": 380,
      "protein": 26.0,
      "fat": 28.0,
      "carbohydrates": 8.0,
      "notes": "Kaya lemak sehat dan serat dari kelapa parut sangrai serta asam amino esensial dari kuning telur kampung."
    }
  },
  {
    "recipeNumber": 174,
    "title": "174. Kupat Tahu Magelang (Jawa Tengah)",
    "name": "Kupat Tahu Magelang",
    "slug": "kupat-tahu-magelang",
    "scope": "INDONESIA",
    "origin": "Magelang, Jawa Tengah",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 20,
    "cookTimeMinutes": 25,
    "servings": 4,
    "difficulty": "EASY",
    "spicinessLevel": 1,
    "categorySlug": "sayuran-tumisan",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """174. Kupat Tahu Magelang (Jawa Tengah)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
4 buah Ketupat / Lontong (potong-potong)
5 buah Tahu Putih (goreng setengah kering, bagian dalam tetap lembut, potong dadu)
100g Kol (iris tipis halus)
100g Tauge (seduh air panas sebentar, tiriskan)
4 buah Bakwan Sayur goreng (potong-potong, ciri khas Magelang)
Bahan Kuah Gula Merah:
500 ml Air bersih
100g Gula Merah Aren (sisir halus)
4 sdm Kecap Manis
2 siung Bawang putih (memarkan)
2 cm Lengkuas (memarkan)
2 lembar Daun salam
1 sdt Air asam jawa
1/2 sdt Garam
Bumbu Ulek Sambal Kacang (Per Porsi):
2 sdm Kacang tanah goreng (ulek kasar)
1 siung Bawang putih kecil
3 buah Cabai rawit merah (sesuai selera pedas)
Sedikit garam
Pelengkap Taburan:
1 batang Daun seledri (iris halus)
2 sdm Bawang merah goreng
Kerupuk merah atau kerupuk aci renyah
Langkah-Langkah Pembuatan:
Membuat Kuah Gula Merah: Rebus air di panci bersama gula aren sisir, bawang putih geprek, lengkuas, daun salam, air asam jawa, dan garam. Masak hingga gula larut mendidih. Tambahkan kecap manis, aduk rata. Saring kuah agar jernih dan sisihkan hangat.
Menyiapkan Bahan Isian: Goreng tahu putih hingga berkulit tipis namun bagian dalamnya tetap lembut. Iris kol tipis-tipis. Seduh tauge sebentar dengan air panas, lalu tiriskan.
Mengulek Sambal Kacang: Di atas piring saji, ulek cabai rawit, bawang putih kecil, dan kacang tanah goreng secara kasar dengan sedikit garam.
Menata Isian: Tata potongan ketupat, tahu goreng hangat, bakwan sayur iris, kol iris, dan tauge di atas ulekan kacang.
Penyiraman Kuah: Siram seluruh racikan dengan kuah gula merah hangat yang manis-gurih dan beraroma harum.
Penyajian: Taburi atasnya dengan irisan daun seledri segar dan bawang goreng. Sajikan segera bersama kerupuk renyah.
Nutrisi (Per Porsi Lengkap): Kalori 290 kkal | Protein 12g | Lemak 9g | Karbohidrat 42g. Sumber serat nabati dan isoflavon tinggi dari tahu putih, tauge segar, serta kol mentah renyah.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "4 buah Ketupat / Lontong (potong-potong)", "amount": 4.0, "unit": "buah", "name": "Ketupat", "notes": "potong-potong", "orderIndex": 1},
          {"rawText": "5 buah Tahu Putih (goreng berkulit)", "amount": 5.0, "unit": "buah", "name": "Tahu Putih", "notes": "goreng berkulit, dalam lembut", "orderIndex": 2},
          {"rawText": "100g Kol (iris tipis halus)", "amount": 100.0, "unit": "g", "name": "Kol", "notes": "iris tipis halus", "orderIndex": 3},
          {"rawText": "100g Tauge (seduh air panas)", "amount": 100.0, "unit": "g", "name": "Tauge", "notes": "seduh air panas sebentar", "orderIndex": 4},
          {"rawText": "4 buah Bakwan Sayur goreng (potong)", "amount": 4.0, "unit": "buah", "name": "Bakwan Sayur", "notes": "potong-potong", "orderIndex": 5}
        ]
      },
      {
        "name": "Bahan Kuah Gula Merah",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "500 ml Air bersih", "amount": 500.0, "unit": "ml", "name": "Air bersih", "notes": None, "orderIndex": 1},
          {"rawText": "100g Gula Merah Aren (sisir)", "amount": 100.0, "unit": "g", "name": "Gula Merah Aren", "notes": "sisir", "orderIndex": 2},
          {"rawText": "4 sdm Kecap Manis", "amount": 4.0, "unit": "sdm", "name": "Kecap Manis", "notes": None, "orderIndex": 3},
          {"rawText": "2 siung Bawang putih (memarkan)", "amount": 2.0, "unit": "siung", "name": "Bawang putih", "notes": "memarkan", "orderIndex": 4},
          {"rawText": "2 cm Lengkuas (memarkan)", "amount": 2.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 5},
          {"rawText": "2 lembar Daun salam", "amount": 2.0, "unit": "lembar", "name": "Daun salam", "notes": None, "orderIndex": 6},
          {"rawText": "1 sdt Air asam jawa dan 1/2 sdt Garam", "amount": 1.0, "unit": "sdt", "name": "Air asam jawa dan Garam", "notes": None, "orderIndex": 7}
        ]
      },
      {
        "name": "Bumbu Ulek Sambal Kacang",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "8 sdm Kacang tanah goreng (ulek kasar)", "amount": 8.0, "unit": "sdm", "name": "Kacang tanah goreng", "notes": "ulek kasar", "orderIndex": 1},
          {"rawText": "4 siung Bawang putih kecil", "amount": 4.0, "unit": "siung", "name": "Bawang putih kecil", "notes": None, "orderIndex": 2},
          {"rawText": "12 buah Cabai rawit merah", "amount": 12.0, "unit": "buah", "name": "Cabai rawit merah", "notes": None, "orderIndex": 3}
        ]
      },
      {
        "name": "Pelengkap Taburan",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "1 batang Daun seledri (iris halus)", "amount": 1.0, "unit": "batang", "name": "Daun seledri", "notes": "iris halus", "orderIndex": 1},
          {"rawText": "2 sdm Bawang merah goreng", "amount": 2.0, "unit": "sdm", "name": "Bawang merah goreng", "notes": None, "orderIndex": 2},
          {"rawText": "Kerupuk renyah secukupnya", "amount": None, "unit": "secukupnya", "name": "Kerupuk", "notes": None, "orderIndex": 3}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Membuat Kuah Gula Merah", "instruction": "Rebus air di panci bersama gula aren sisir, bawang putih geprek, lengkuas, daun salam, air asam jawa, dan garam. Masak hingga gula larut mendidih. Tambahkan kecap manis, aduk rata. Saring kuah agar jernih dan sisihkan hangat.", "rawText": "Membuat Kuah Gula Merah: Rebus air di panci bersama gula aren sisir, bawang putih geprek, lengkuas, daun salam, air asam jawa, dan garam. Masak hingga gula larut mendidih. Tambahkan kecap manis, aduk rata. Saring kuah agar jernih dan sisihkan hangat."},
      {"stepNumber": 2, "title": "Menyiapkan Bahan Isian", "instruction": "Goreng tahu putih hingga berkulit tipis namun bagian dalamnya tetap lembut. Iris kol tipis-tipis. Seduh tauge sebentar dengan air panas, lalu tiriskan.", "rawText": "Menyiapkan Bahan Isian: Goreng tahu putih hingga berkulit tipis namun bagian dalamnya tetap lembut. Iris kol tipis-tipis. Seduh tauge sebentar dengan air panas, lalu tiriskan."},
      {"stepNumber": 3, "title": "Mengulek Sambal Kacang", "instruction": "Di atas piring saji, ulek cabai rawit, bawang putih kecil, dan kacang tanah goreng secara kasar dengan sedikit garam.", "rawText": "Mengulek Sambal Kacang: Di atas piring saji, ulek cabai rawit, bawang putih kecil, dan kacang tanah goreng secara kasar dengan sedikit garam."},
      {"stepNumber": 4, "title": "Menata Isian", "instruction": "Tata potongan ketupat, tahu goreng hangat, bakwan sayur iris, kol iris, dan tauge di atas ulekan kacang.", "rawText": "Menata Isian: Tata potongan ketupat, tahu goreng hangat, bakwan sayur iris, kol iris, dan tauge di atas ulekan kacang."},
      {"stepNumber": 5, "title": "Penyiraman Kuah", "instruction": "Siram seluruh racikan dengan kuah gula merah hangat yang manis-gurih dan beraroma harum.", "rawText": "Penyiraman Kuah: Siram seluruh racikan dengan kuah gula merah hangat yang manis-gurih dan beraroma harum."},
      {"stepNumber": 6, "title": "Penyajian", "instruction": "Taburi atasnya dengan irisan daun seledri segar dan bawang goreng. Sajikan segera bersama kerupuk renyah.", "rawText": "Penyajian: Taburi atasnya dengan irisan daun seledri segar dan bawang goreng. Sajikan segera bersama kerupuk renyah."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Porsi Lengkap): Kalori 290 kkal | Protein 12g | Lemak 9g | Karbohidrat 42g. Sumber serat nabati dan isoflavon tinggi dari tahu putih, tauge segar, serta kol mentah renyah.",
      "serving": "Per Porsi Lengkap",
      "calories": 290,
      "protein": 12.0,
      "fat": 9.0,
      "carbohydrates": 42.0,
      "notes": "Sumber serat nabati dan isoflavon tinggi dari tahu putih, tauge segar, serta kol mentah renyah."
    }
  },
  {
    "recipeNumber": 175,
    "title": "175. Sup Brenebon Daging Sapi (Sulawesi Utara)",
    "name": "Sup Brenebon Daging Sapi",
    "slug": "sup-brenebon-daging-sapi",
    "scope": "INDONESIA",
    "origin": "Manado, Sulawesi Utara",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 30,
    "cookTimeMinutes": 90,
    "servings": 4,
    "difficulty": "MEDIUM",
    "spicinessLevel": 1,
    "categorySlug": "sup-soto",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """175. Sup Brenebon Daging Sapi (Sulawesi Utara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Daging Sapi / Iga Sapi / Sandung Lamur (potong dadu 3x3 cm)
250g Kacang Merah (rendam semalaman dalam air dingin agar cepat empuk)
1.8 liter Air kaldu sapi bersih
2 buah Wortel (kupas, potong bulat 1 cm)
Bumbu Halus:
8 siung Bawang merah
5 siung Bawang putih
1/2 butir Biji Pala utuh (tumbuk halus)
1 sdt Lada putih bubuk
1 sdm Garam dan 1 sdt Gula pasir
1 sdt Kaldu sapi bubuk
Bumbu Rempah Cemplung:
4 butir Cengkih
2 batang Daun bawang (iris 2 cm)
2 batang Daun seledri (ikat simpul)
Pelengkap Penyajian:
Bawang merah goreng renyah
Sambal cabai rawit hijau ulek kasar
Perasan jeruk nipis
Langkah-Langkah Pembuatan:
Merebus Kacang Merah: Rebus kacang merah yang telah direndam semalaman dengan air bersih hingga empuk dan merekah lembut. Tiriskan.
Merebus Daging Sapi: Rebus potongan daging sapi dalam air mendidih selama 10 menit, buang busa kotoran di permukaan, lalu rebus kembali dengan api kecil hingga daging empuk dan keluar kaldu gurihnya.
Menumis Bumbu Halus: Panaskan 2 sdm minyak di wajan. Tumis bawang merah, bawang putih, dan bubuk pala halus hingga harum dan matang.
Menggabungkan Kuah Sup: Masukkan tumisan bumbu ke dalam panci kaldu daging sapi. Masukkan kacang merah yang sudah empuk, potongan wortel, dan cengkih. Bumbui dengan garam, lada bubuk, kaldu sapi, dan gula pasir.
Mematangkan Sup: Masak dengan api kecil perlahan (simmer) selama 25 menit agar bumbu meresap ke dalam daging dan kacang merah mengeluarkan kekentalan alami pada kuah. Menjelang diangkat, masukkan irisan daun bawang dan daun seledri. Koreksi rasa.
Penyajian: Tuangkan Sup Brenebon hangat ke dalam mangkuk saji. Taburi bawang merah goreng renyah. Nikmati selagi panas bersama nasi putih dan sambal rawit hijau khas Manado.
Nutrisi (Per Mangkok Porsi): Kalori 310 kkal | Protein 22g | Lemak 10g | Karbohidrat 34g. Sangat kaya zat besi, folat, dan serat larut dari kacang merah yang menjaga kestabilan gula darah.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "500g Daging Sapi / Iga Sapi (potong dadu 3x3 cm)", "amount": 500.0, "unit": "g", "name": "Daging Sapi", "notes": "potong dadu 3x3 cm", "orderIndex": 1},
          {"rawText": "250g Kacang Merah (rendam semalaman)", "amount": 250.0, "unit": "g", "name": "Kacang Merah", "notes": "rendam semalaman", "orderIndex": 2},
          {"rawText": "1.8 liter Air kaldu sapi bersih", "amount": 1.8, "unit": "liter", "name": "Air kaldu sapi", "notes": None, "orderIndex": 3},
          {"rawText": "2 buah Wortel (potong bulat 1 cm)", "amount": 2.0, "unit": "buah", "name": "Wortel", "notes": "potong bulat 1 cm", "orderIndex": 4}
        ]
      },
      {
        "name": "Bumbu Halus",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "8 siung Bawang merah", "amount": 8.0, "unit": "siung", "name": "Bawang merah", "notes": None, "orderIndex": 1},
          {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
          {"rawText": "1/2 butir Biji Pala utuh (tumbuk halus)", "amount": 0.5, "unit": "butir", "name": "Biji Pala utuh", "notes": "tumbuk halus", "orderIndex": 3},
          {"rawText": "1 sdt Lada putih bubuk", "amount": 1.0, "unit": "sdt", "name": "Lada putih bubuk", "notes": None, "orderIndex": 4},
          {"rawText": "1 sdm Garam dan 1 sdt Gula pasir", "amount": 1.0, "unit": "sdm", "name": "Garam dan Gula pasir", "notes": None, "orderIndex": 5}
        ]
      },
      {
        "name": "Bumbu Rempah Cemplung",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "4 butir Cengkih", "amount": 4.0, "unit": "butir", "name": "Cengkih", "notes": None, "orderIndex": 1},
          {"rawText": "2 batang Daun bawang (iris 2 cm)", "amount": 2.0, "unit": "batang", "name": "Daun bawang", "notes": "iris 2 cm", "orderIndex": 2},
          {"rawText": "2 batang Daun seledri (ikat simpul)", "amount": 2.0, "unit": "batang", "name": "Daun seledri", "notes": "ikat simpul", "orderIndex": 3}
        ]
      },
      {
        "name": "Pelengkap Penyajian",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "Bawang merah goreng renyah secukupnya", "amount": None, "unit": "secukupnya", "name": "Bawang merah goreng", "notes": None, "orderIndex": 1},
          {"rawText": "Sambal cabai rawit hijau ulek kasar", "amount": None, "unit": "secukupnya", "name": "Sambal rawit hijau", "notes": None, "orderIndex": 2},
          {"rawText": "Perasan jeruk nipis secukupnya", "amount": None, "unit": "secukupnya", "name": "Perasan jeruk nipis", "notes": None, "orderIndex": 3}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Merebus Kacang Merah", "instruction": "Rebus kacang merah yang telah direndam semalaman dengan air bersih hingga empuk dan merekah lembut. Tiriskan.", "rawText": "Merebus Kacang Merah: Rebus kacang merah yang telah direndam semalaman dengan air bersih hingga empuk dan merekah lembut. Tiriskan."},
      {"stepNumber": 2, "title": "Merebus Daging Sapi", "instruction": "Rebus potongan daging sapi dalam air mendidih selama 10 menit, buang busa kotoran di permukaan, lalu rebus kembali dengan api kecil hingga daging empuk dan keluar kaldu gurihnya.", "rawText": "Merebus Daging Sapi: Rebus potongan daging sapi dalam air mendidih selama 10 menit, buang busa kotoran di permukaan, lalu rebus kembali dengan api kecil hingga daging empuk dan keluar kaldu gurihnya."},
      {"stepNumber": 3, "title": "Menumis Bumbu Halus", "instruction": "Panaskan 2 sdm minyak di wajan. Tumis bawang merah, bawang putih, dan bubuk pala halus hingga harum dan matang.", "rawText": "Menumis Bumbu Halus: Panaskan 2 sdm minyak di wajan. Tumis bawang merah, bawang putih, dan bubuk pala halus hingga harum dan matang."},
      {"stepNumber": 4, "title": "Menggabungkan Kuah Sup", "instruction": "Masukkan tumisan bumbu ke dalam panci kaldu daging sapi. Masukkan kacang merah yang sudah empuk, potongan wortel, dan cengkih. Bumbui dengan garam, lada bubuk, kaldu sapi, dan gula pasir.", "rawText": "Menggabungkan Kuah Sup: Masukkan tumisan bumbu ke dalam panci kaldu daging sapi. Masukkan kacang merah yang sudah empuk, potongan wortel, dan cengkih. Bumbui dengan garam, lada bubuk, kaldu sapi, dan gula pasir."},
      {"stepNumber": 5, "title": "Mematangkan Sup", "instruction": "Masak dengan api kecil perlahan (simmer) selama 25 menit agar bumbu meresap ke dalam daging dan kacang merah mengeluarkan kekentalan alami pada kuah. Menjelang diangkat, masukkan irisan daun bawang dan daun seledri. Koreksi rasa.", "rawText": "Mematangkan Sup: Masak dengan api kecil perlahan (simmer) selama 25 menit agar bumbu meresap ke dalam daging dan kacang merah mengeluarkan kekentalan alami pada kuah. Menjelang diangkat, masukkan irisan daun bawang dan daun seledri. Koreksi rasa."},
      {"stepNumber": 6, "title": "Penyajian", "instruction": "Tuangkan Sup Brenebon hangat ke dalam mangkuk saji. Taburi bawang merah goreng renyah. Nikmati selagi panas bersama nasi putih dan sambal rawit hijau khas Manado.", "rawText": "Penyajian: Tuangkan Sup Brenebon hangat ke dalam mangkuk saji. Taburi bawang merah goreng renyah. Nikmati selagi panas bersama nasi putih dan sambal rawit hijau khas Manado."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Mangkok Porsi): Kalori 310 kkal | Protein 22g | Lemak 10g | Karbohidrat 34g. Sangat kaya zat besi, folat, dan serat larut dari kacang merah yang menjaga kestabilan gula darah.",
      "serving": "Per Mangkok Porsi",
      "calories": 310,
      "protein": 22.0,
      "fat": 10.0,
      "carbohydrates": 34.0,
      "notes": "Sangat kaya zat besi, folat, dan serat larut dari kacang merah yang menjaga kestabilan gula darah."
    }
  },
  {
    "recipeNumber": 176,
    "title": "176. Ikan Bakar Parape Khas Makassar (Sulawesi Selatan)",
    "name": "Ikan Bakar Parape Khas Makassar",
    "slug": "ikan-bakar-parape-khas-makassar",
    "scope": "INDONESIA",
    "origin": "Makassar, Sulawesi Selatan",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 20,
    "cookTimeMinutes": 30,
    "servings": 4,
    "difficulty": "MEDIUM",
    "spicinessLevel": 2,
    "categorySlug": "sate-bakaran",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """176. Ikan Bakar Parape Khas Makassar (Sulawesi Selatan)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
1 ekor Ikan Kakap Merah / Baronang segar (sekitar 700g, belah punggung atau kerat-kerat)
1 buah Jeruk Nipis (ambil airnya)
1 sdt Garam kasar
Bumbu Halus Parape:
12 siung Bawang merah (kunci utama rasa karamelisasi Parape)
5 siung Bawang putih
4 butir Kemiri (sangrai)
2 cm Jahe
5 buah Cabai merah keriting
Bumbu Karamelisasi:
6 sdm Kecap Manis berkualitas
3 sdm Air Asam Jawa pekat
2 sdm Gula Merah Aren (sisir halus)
1/2 sdt Lada putih bubuk
1 sdt Garam dan 1/2 sdt Kaldu bubuk
3 sdm Minyak goreng untuk menumis
Bahan Pelengkap:
Lalapan segar (timun, kemangi, kol)
Sambal tomat terasi atau sambal dabu-dabu
Jeruk limau
Langkah-Langkah Pembuatan:
Marinasi Ikan: Bersihkan ikan, lumuri seluruh badan dan bagian dalam dengan perasan air jeruk nipis dan garam. Diamkan 15 menit agar bau amis hilang dan daging ikan kesat.
Membuat Saus Karamelisasi Parape: Panaskan minyak di wajan. Tumis bumbu halus (bawang merah, bawang putih, kemiri, jahe, cabai) hingga benar-benar harum dan matang. Masukkan air asam jawa, kecap manis, gula merah sisir, lada, garam, dan kaldu bubuk. Masak dengan api kecil sambil terus diaduk hingga bumbu mengental, berkilau, dan mengalami karamelisasi pekat gurih. Angkat dan sisihkan.
Membakar Ikan Setengah Matang: Panaskan pemanggang arang atau grill pan yang dioles sedikit minyak. Bakar ikan di atas api sedang hingga setengah matang di kedua sisinya.
Mengoles Bumbu Parape: Oleskan saus Parape tebal-tebal ke seluruh permukaan tubuh ikan. Bakar kembali sambil dibolak-balik perlahan dan diolesi bumbu secara berulang hingga bumbu Parape meresap dan membentuk lapisan karamel wangi yang menggoda tanpa gosong.
Penyajian: Angkat ikan bakar yang matang sempurna. Letakkan di piring saji, lalu siramkan sisa saus karamelisasi Parape hangat di atasnya. Sajikan bersama lalapan segar dan nasi putih hangat.
Nutrisi (Per Porsi 150g Ikan): Kalori 240 kkal | Protein 26g | Lemak 7g | Karbohidrat 18g. Tinggi asam lemak omega-3 dari ikan laut segar, rendah kolesterol, serta antioksidan allicin dari bawang merah.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "1 ekor Ikan Kakap Merah / Baronang (700g, belah kerat)", "amount": 1.0, "unit": "ekor", "name": "Ikan Kakap Merah", "notes": "700g, belah punggung kerat", "orderIndex": 1},
          {"rawText": "1 buah Jeruk Nipis (ambil air)", "amount": 1.0, "unit": "buah", "name": "Jeruk Nipis", "notes": "ambil air", "orderIndex": 2},
          {"rawText": "1 sdt Garam kasar", "amount": 1.0, "unit": "sdt", "name": "Garam kasar", "notes": None, "orderIndex": 3}
        ]
      },
      {
        "name": "Bumbu Halus Parape",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "12 siung Bawang merah", "amount": 12.0, "unit": "siung", "name": "Bawang merah", "notes": "kunci karamelisasi", "orderIndex": 1},
          {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
          {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 3},
          {"rawText": "2 cm Jahe", "amount": 2.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 4},
          {"rawText": "5 buah Cabai merah keriting", "amount": 5.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 5}
        ]
      },
      {
        "name": "Bumbu Karamelisasi",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "6 sdm Kecap Manis berkualitas", "amount": 6.0, "unit": "sdm", "name": "Kecap Manis", "notes": None, "orderIndex": 1},
          {"rawText": "3 sdm Air Asam Jawa pekat", "amount": 3.0, "unit": "sdm", "name": "Air Asam Jawa", "notes": "pekat", "orderIndex": 2},
          {"rawText": "2 sdm Gula Merah Aren (sisir)", "amount": 2.0, "unit": "sdm", "name": "Gula Merah Aren", "notes": "sisir", "orderIndex": 3},
          {"rawText": "1/2 sdt Lada putih dan 1 sdt Garam", "amount": 0.5, "unit": "sdt", "name": "Lada dan Garam", "notes": None, "orderIndex": 4}
        ]
      },
      {
        "name": "Bahan Pelengkap",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "Lalapan segar secukupnya", "amount": None, "unit": "secukupnya", "name": "Lalapan segar", "notes": None, "orderIndex": 1},
          {"rawText": "Sambal terasi dan jeruk limau secukupnya", "amount": None, "unit": "secukupnya", "name": "Sambal terasi", "notes": None, "orderIndex": 2}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Marinasi Ikan", "instruction": "Bersihkan ikan, lumuri seluruh badan dan bagian dalam dengan perasan air jeruk nipis dan garam. Diamkan 15 menit agar bau amis hilang dan daging ikan kesat.", "rawText": "Marinasi Ikan: Bersihkan ikan, lumuri seluruh badan dan bagian dalam dengan perasan air jeruk nipis dan garam. Diamkan 15 menit agar bau amis hilang dan daging ikan kesat."},
      {"stepNumber": 2, "title": "Membuat Saus Karamelisasi Parape", "instruction": "Panaskan minyak di wajan. Tumis bumbu halus (bawang merah, bawang putih, kemiri, jahe, cabai) hingga benar-benar harum dan matang. Masukkan air asam jawa, kecap manis, gula merah sisir, lada, garam, dan kaldu bubuk. Masak dengan api kecil sambil terus diaduk hingga bumbu mengental, berkilau, dan mengalami karamelisasi pekat gurih. Angkat dan sisihkan.", "rawText": "Membuat Saus Karamelisasi Parape: Panaskan minyak di wajan. Tumis bumbu halus (bawang merah, bawang putih, kemiri, jahe, cabai) hingga benar-benar harum dan matang. Masukkan air asam jawa, kecap manis, gula merah sisir, lada, garam, dan kaldu bubuk. Masak dengan api kecil sambil terus diaduk hingga bumbu mengental, berkilau, dan mengalami karamelisasi pekat gurih. Angkat dan sisihkan."},
      {"stepNumber": 3, "title": "Membakar Ikan Setengah Matang", "instruction": "Panaskan pemanggang arang atau grill pan yang dioles sedikit minyak. Bakar ikan di atas api sedang hingga setengah matang di kedua sisinya.", "rawText": "Membakar Ikan Setengah Matang: Panaskan pemanggang arang atau grill pan yang dioles sedikit minyak. Bakar ikan di atas api sedang hingga setengah matang di kedua sisinya."},
      {"stepNumber": 4, "title": "Mengoles Bumbu Parape", "instruction": "Oleskan saus Parape tebal-tebal ke seluruh permukaan tubuh ikan. Bakar kembali sambil dibolak-balik perlahan dan diolesi bumbu secara berulang hingga bumbu Parape meresap dan membentuk lapisan karamel wangi yang menggoda tanpa gosong.", "rawText": "Mengoles Bumbu Parape: Oleskan saus Parape tebal-tebal ke seluruh permukaan tubuh ikan. Bakar kembali sambil dibolak-balik perlahan dan diolesi bumbu secara berulang hingga bumbu Parape meresap dan membentuk lapisan karamel wangi yang menggoda tanpa gosong."},
      {"stepNumber": 5, "title": "Penyajian", "instruction": "Angkat ikan bakar yang matang sempurna. Letakkan di piring saji, lalu siramkan sisa saus karamelisasi Parape hangat di atasnya. Sajikan bersama lalapan segar dan nasi putih hangat.", "rawText": "Penyajian: Angkat ikan bakar yang matang sempurna. Letakkan di piring saji, lalu siramkan sisa saus karamelisasi Parape hangat di atasnya. Sajikan bersama lalapan segar dan nasi putih hangat."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Porsi 150g Ikan): Kalori 240 kkal | Protein 26g | Lemak 7g | Karbohidrat 18g. Tinggi asam lemak omega-3 dari ikan laut segar, rendah kolesterol, serta antioksidan allicin dari bawang merah.",
      "serving": "Per Porsi 150g Ikan",
      "calories": 240,
      "protein": 26.0,
      "fat": 7.0,
      "carbohydrates": 18.0,
      "notes": "Tinggi asam lemak omega-3 dari ikan laut segar, rendah kolesterol, serta antioksidan allicin dari bawang merah."
    }
  },
  {
    "recipeNumber": 177,
    "title": "177. Gulai Belacan Udang (Riau)",
    "name": "Gulai Belacan Udang",
    "slug": "gulai-belacan-udang",
    "scope": "INDONESIA",
    "origin": "Riau",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 20,
    "cookTimeMinutes": 35,
    "servings": 4,
    "difficulty": "MEDIUM",
    "spicinessLevel": 3,
    "categorySlug": "ikan-seafood",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """177. Gulai Belacan Udang (Riau)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Udang Windu / Udang Galah ukuran sedang (bersihkan kotoran punggung, biarkan ekornya)
300 ml Santan Kental murni
400 ml Santan Encer
2 papan Petai segar (kupas, belah dua)
1 buah Asam Kandis atau 1 sdm air asam jawa
1 sdm Kecap Manis (penyeimbang rasa gurih belacan)
Bumbu Halus Belacan:
12 siung Bawang merah
5 siung Bawang putih
10 buah Cabai merah keriting
10 buah Cabai rawit merah (sesuai selera pedas Melayu)
5 butir Kemiri (sangrai)
1.5 sdm Terasi udang / Belacan kualitas super (bakar harum)
1 cm Kunyit bakar
1 cm Jahe
1 sdt Garam dan 1 sdt Gula pasir
Bumbu Rempah Cemplung:
2 batang Serai (memarkan)
4 lembar Daun jeruk (buang tulang)
1 lembar Daun kunyit (ikat simpul)
3 cm Lengkuas (memarkan)
Langkah-Langkah Pembuatan:
Menumis Bumbu Halus Belacan: Panaskan 3 sdm minyak di wajan. Masukkan bumbu halus bersama serai, lengkuas, daun jeruk, dan daun kunyit. Tumis dengan api sedang hingga bumbu benar-benar matang tanak, harum terasi menyeruak sedap, dan minyaknya keluar.
Memasak Kuah Santan: Tuangkan santan encer ke dalam tumisan bumbu. Masukkan asam kandis, garam, dan gula. Masak sambil sesekali diaduk perlahan agar santan tidak pecah hingga kuah mendidih.
Memasukkan Petai dan Udang: Masukkan petai kupas dan udang segar ke dalam kuah mendidih. Bumbui dengan kecap manis. Aduk rata hingga udang mulai berubah warna kemerahan segar.
Menuang Santan Kental: Tuang santan kental, kecilkan api. Masak selama 5-7 menit sambil terus diaduk perlahan hingga kuah gulai mengental berminyak dan bumbu meresap sempurna. Jangan memasak udang terlalu lama agar dagingnya tetap kenyal manis dan tidak alot.
Penyelesaian: Koreksi rasa (harus dominan gurih legit, pedas menggigit, dan wangi terasi belacan yang khas). Matikan api.
Penyajian: Angkat dan tuang Gulai Belacan Udang ke dalam mangkuk saji. Hidangkan selagi hangat bersama nasi putih pulen panas.
Nutrisi (Per Porsi): Kalori 330 kkal | Protein 23g | Lemak 21g | Karbohidrat 11g. Sumber protein laut tinggi kalsium dan fosfor dari udang segar dengan metabolisme pembakar kalori dari cabai rawit.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "500g Udang Windu / Galah (bersihkan kotoran)", "amount": 500.0, "unit": "g", "name": "Udang Windu", "notes": "bersihkan punggung", "orderIndex": 1},
          {"rawText": "300 ml Santan Kental murni", "amount": 300.0, "unit": "ml", "name": "Santan Kental", "notes": "murni", "orderIndex": 2},
          {"rawText": "400 ml Santan Encer", "amount": 400.0, "unit": "ml", "name": "Santan Encer", "notes": None, "orderIndex": 3},
          {"rawText": "2 papan Petai segar (belah dua)", "amount": 2.0, "unit": "papan", "name": "Petai segar", "notes": "kupas belah dua", "orderIndex": 4},
          {"rawText": "1 buah Asam Kandis", "amount": 1.0, "unit": "buah", "name": "Asam Kandis", "notes": None, "orderIndex": 5},
          {"rawText": "1 sdm Kecap Manis", "amount": 1.0, "unit": "sdm", "name": "Kecap Manis", "notes": None, "orderIndex": 6}
        ]
      },
      {
        "name": "Bumbu Halus Belacan",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "12 siung Bawang merah", "amount": 12.0, "unit": "siung", "name": "Bawang merah", "notes": None, "orderIndex": 1},
          {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
          {"rawText": "10 buah Cabai merah keriting", "amount": 10.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 3},
          {"rawText": "10 buah Cabai rawit merah", "amount": 10.0, "unit": "buah", "name": "Cabai rawit merah", "notes": None, "orderIndex": 4},
          {"rawText": "5 butir Kemiri (sangrai)", "amount": 5.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 5},
          {"rawText": "1.5 sdm Terasi udang / Belacan (bakar)", "amount": 1.5, "unit": "sdm", "name": "Terasi udang / Belacan", "notes": "bakar harum", "orderIndex": 6},
          {"rawText": "1 cm Kunyit bakar dan 1 cm Jahe", "amount": 1.0, "unit": "cm", "name": "Kunyit dan Jahe", "notes": "bakar", "orderIndex": 7},
          {"rawText": "1 sdt Garam dan 1 sdt Gula pasir", "amount": 1.0, "unit": "sdt", "name": "Garam dan Gula", "notes": None, "orderIndex": 8}
        ]
      },
      {
        "name": "Bumbu Rempah Cemplung",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 1},
          {"rawText": "4 lembar Daun jeruk (buang tulang)", "amount": 4.0, "unit": "lembar", "name": "Daun jeruk", "notes": "buang tulang", "orderIndex": 2},
          {"rawText": "1 lembar Daun kunyit (simpul)", "amount": 1.0, "unit": "lembar", "name": "Daun kunyit", "notes": "simpul", "orderIndex": 3},
          {"rawText": "3 cm Lengkuas (memarkan)", "amount": 3.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 4}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Menumis Bumbu Halus Belacan", "instruction": "Panaskan 3 sdm minyak di wajan. Masukkan bumbu halus bersama serai, lengkuas, daun jeruk, dan daun kunyit. Tumis dengan api sedang hingga bumbu benar-benar matang tanak, harum terasi menyeruak sedap, dan minyaknya keluar.", "rawText": "Menumis Bumbu Halus Belacan: Panaskan 3 sdm minyak di wajan. Masukkan bumbu halus bersama serai, lengkuas, daun jeruk, dan daun kunyit. Tumis dengan api sedang hingga bumbu benar-benar matang tanak, harum terasi menyeruak sedap, dan minyaknya keluar."},
      {"stepNumber": 2, "title": "Memasak Kuah Santan", "instruction": "Tuangkan santan encer ke dalam tumisan bumbu. Masukkan asam kandis, garam, dan gula. Masak sambil sesekali diaduk perlahan agar santan tidak pecah hingga kuah mendidih.", "rawText": "Memasak Kuah Santan: Tuangkan santan encer ke dalam tumisan bumbu. Masukkan asam kandis, garam, dan gula. Masak sambil sesekali diaduk perlahan agar santan tidak pecah hingga kuah mendidih."},
      {"stepNumber": 3, "title": "Memasukkan Petai dan Udang", "instruction": "Masukkan petai kupas dan udang segar ke dalam kuah mendidih. Bumbui dengan kecap manis. Aduk rata hingga udang mulai berubah warna kemerahan segar.", "rawText": "Memasukkan Petai dan Udang: Masukkan petai kupas dan udang segar ke dalam kuah mendidih. Bumbui dengan kecap manis. Aduk rata hingga udang mulai berubah warna kemerahan segar."},
      {"stepNumber": 4, "title": "Menuang Santan Kental", "instruction": "Tuang santan kental, kecilkan api. Masak selama 5-7 menit sambil terus diaduk perlahan hingga kuah gulai mengental berminyak dan bumbu meresap sempurna. Jangan memasak udang terlalu lama agar dagingnya tetap kenyal manis dan tidak alot.", "rawText": "Menuang Santan Kental: Tuang santan kental, kecilkan api. Masak selama 5-7 menit sambil terus diaduk perlahan hingga kuah gulai mengental berminyak dan bumbu meresap sempurna. Jangan memasak udang terlalu lama agar dagingnya tetap kenyal manis dan tidak alot."},
      {"stepNumber": 5, "title": "Penyelesaian", "instruction": "Koreksi rasa (harus dominan gurih legit, pedas menggigit, dan wangi terasi belacan yang khas). Matikan api. Angkat dan tuang Gulai Belacan Udang ke dalam mangkuk saji. Hidangkan selagi hangat bersama nasi putih pulen panas.", "rawText": "Penyelesaian: Koreksi rasa (harus dominan gurih legit, pedas menggigit, dan wangi terasi belacan yang khas). Matikan api. Angkat dan tuang Gulai Belacan Udang ke dalam mangkuk saji. Hidangkan selagi hangat bersama nasi putih pulen panas."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Porsi): Kalori 330 kkal | Protein 23g | Lemak 21g | Karbohidrat 11g. Sumber protein laut tinggi kalsium dan fosfor dari udang segar dengan metabolisme pembakar kalori dari cabai rawit.",
      "serving": "Per Porsi",
      "calories": 330,
      "protein": 23.0,
      "fat": 21.0,
      "carbohydrates": 11.0,
      "notes": "Sumber protein laut tinggi kalsium dan fosfor dari udang segar dengan metabolisme pembakar kalori dari cabai rawit."
    }
  },
  {
    "recipeNumber": 178,
    "title": "178. Mie Titi Khas Makassar (Sulawesi Selatan)",
    "name": "Mie Titi Khas Makassar",
    "slug": "mie-titi-khas-makassar",
    "scope": "INDONESIA",
    "origin": "Makassar, Sulawesi Selatan",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 20,
    "cookTimeMinutes": 30,
    "servings": 4,
    "difficulty": "MEDIUM",
    "spicinessLevel": 1,
    "categorySlug": "mi-pasta",
    "cuisineTypeSlug": "street-food-kaki-lima",
    "rawContent": """178. Mie Titi Khas Makassar (Sulawesi Selatan)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Mie Kering:
300g Mie Telur Halus / Mie Basah khusus Mie Kering
Minyak goreng secukupnya untuk menggoreng mie (deep frying)
Bahan Isian Kuah Kental:
200g Dada Ayam Fillet (potong dadu kecil)
100g Udang kupas segar
5 butir Bakso Sapi / Bakso Ikan (iris bulat)
1 ikat Sawi Hijau / Caisim (potong-potong)
1 buah Wortel (iris serong tipis)
1 butir Telur Ayam (kocok lepas)
Bumbu Kuah Gurih:
6 siung Bawang putih (cincang sangat halus, kunci aroma Mie Titi)
1/2 buah Bawang bombay (cincang halus)
700 ml Air kaldu ayam asli
2 sdm Tepung Maizena / Sagu (larutkan dengan 4 sdm air)
1 sdm Saus Tiram
1 sdm Kecap Asin
1 sdt Minyak Wijen
1 sdt Garam, 1/2 sdt Lada putih, dan 1 sdt Gula pasir
Pelengkap Penyajian:
Jeruk nipis segar
Sambal lombok kuning khas Makassar
Bawang goreng renyah
Langkah-Langkah Pembuatan:
Mengolah dan Menggoreng Mie: Rebus mie telur sebentar dalam air mendidih (sekitar 1 menit), tiriskan hingga kering sempurna. Bentuk mie menjadi sarang pipih per porsi. Panaskan minyak banyak di wajan, goreng mie dengan api sedang hingga kering, kaku, garing kriuk, dan berwarna kuning keemasan. Angkat, tiriskan, dan tata di piring saji cekung.
Menumis Isian: Panaskan 2 sdm minyak di wajan. Tumis bawang putih cincang dan bawang bombay hingga sangat harum dan berwarna keemasan. Masukkan potongan daging ayam dan udang, aduk cepat hingga berubah warna. Masukkan bakso dan wortel.
Memasak Kuah Kaldu: Tuang air kaldu ayam ke dalam tumisan. Bumbui dengan saus tiram, kecap asin, minyak wijen, lada, garam, dan gula. Masak hingga mendidih dan kuah beraroma gurih sedap. Masukkan potongan sawi hijau, masak sebentar.
Mengentalkan Kuah dan Menyerabutkan Telur: Kecilkan api, tuangkan larutan tepung maizena perlahan sambil terus diaduk cepat hingga kuah mengental licin dan transparan. Tuang telur kocok perlahan sambil diaduk melingkar agar terbentuk serabut telur halus di dalam kuah. Matikan api.
Penyajian: Siramkan kuah kental panas beserta isian ayam, udang, dan sayuran ke atas mie kering kriuk yang sudah ditata di piring. Sajikan segera selagi mengepul panas bersama perasan jeruk nipis dan sambal lombok kuning Makassar.
Nutrisi (Per Porsi Lengkap): Kalori 460 kkal | Protein 20g | Lemak 18g | Karbohidrat 56g. Menyediakan energi karbohidrat cepat, vitamin A dan C dari sayur sawi hijau, serta protein ayam dan telur.""",
    "ingredientGroups": [
      {
        "name": "Bahan Mie Kering",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "300g Mie Telur Halus / Mie Basah", "amount": 300.0, "unit": "g", "name": "Mie Telur Halus", "notes": "untuk mie kering", "orderIndex": 1},
          {"rawText": "Minyak goreng secukupnya untuk deep fry", "amount": None, "unit": "secukupnya", "name": "Minyak goreng", "notes": "deep fry", "orderIndex": 2}
        ]
      },
      {
        "name": "Bahan Isian Kuah Kental",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "200g Dada Ayam Fillet (potong dadu)", "amount": 200.0, "unit": "g", "name": "Dada Ayam Fillet", "notes": "potong dadu kecil", "orderIndex": 1},
          {"rawText": "100g Udang kupas segar", "amount": 100.0, "unit": "g", "name": "Udang kupas segar", "notes": None, "orderIndex": 2},
          {"rawText": "5 butir Bakso Sapi (iris bulat)", "amount": 5.0, "unit": "butir", "name": "Bakso Sapi", "notes": "iris bulat", "orderIndex": 3},
          {"rawText": "1 ikat Sawi Hijau / Caisim (potong)", "amount": 1.0, "unit": "ikat", "name": "Sawi Hijau", "notes": "potong-potong", "orderIndex": 4},
          {"rawText": "1 buah Wortel (iris serong tipis)", "amount": 1.0, "unit": "buah", "name": "Wortel", "notes": "iris serong", "orderIndex": 5},
          {"rawText": "1 butir Telur Ayam (kocok lepas)", "amount": 1.0, "unit": "butir", "name": "Telur Ayam", "notes": "kocok lepas", "orderIndex": 6}
        ]
      },
      {
        "name": "Bumbu Kuah Gurih",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "6 siung Bawang putih (cincang halus)", "amount": 6.0, "unit": "siung", "name": "Bawang putih", "notes": "cincang halus kunci rasa", "orderIndex": 1},
          {"rawText": "1/2 buah Bawang bombay (cincang)", "amount": 0.5, "unit": "buah", "name": "Bawang bombay", "notes": "cincang", "orderIndex": 2},
          {"rawText": "700 ml Air kaldu ayam asli", "amount": 700.0, "unit": "ml", "name": "Air kaldu ayam", "notes": "asli", "orderIndex": 3},
          {"rawText": "2 sdm Tepung Maizena (larutkan air)", "amount": 2.0, "unit": "sdm", "name": "Tepung Maizena", "notes": "larutkan air", "orderIndex": 4},
          {"rawText": "1 sdm Saus Tiram dan 1 sdm Kecap Asin", "amount": 1.0, "unit": "sdm", "name": "Saus Tiram dan Kecap Asin", "notes": None, "orderIndex": 5},
          {"rawText": "1 sdt Minyak Wijen", "amount": 1.0, "unit": "sdt", "name": "Minyak Wijen", "notes": None, "orderIndex": 6},
          {"rawText": "1 sdt Garam dan 1/2 sdt Lada putih", "amount": 1.0, "unit": "sdt", "name": "Garam dan Lada putih", "notes": None, "orderIndex": 7}
        ]
      },
      {
        "name": "Pelengkap Penyajian",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "Jeruk nipis segar secukupnya", "amount": None, "unit": "secukupnya", "name": "Jeruk nipis", "notes": None, "orderIndex": 1},
          {"rawText": "Sambal lombok kuning khas Makassar", "amount": None, "unit": "secukupnya", "name": "Sambal lombok kuning", "notes": None, "orderIndex": 2},
          {"rawText": "Bawang goreng renyah secukupnya", "amount": None, "unit": "secukupnya", "name": "Bawang goreng", "notes": None, "orderIndex": 3}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Mengolah dan Menggoreng Mie", "instruction": "Rebus mie telur sebentar dalam air mendidih (sekitar 1 menit), tiriskan hingga kering sempurna. Bentuk mie menjadi sarang pipih per porsi. Panaskan minyak banyak di wajan, goreng mie dengan api sedang hingga kering, kaku, garing kriuk, dan berwarna kuning keemasan. Angkat, tiriskan, dan tata di piring saji cekung.", "rawText": "Mengolah dan Menggoreng Mie: Rebus mie telur sebentar dalam air mendidih (sekitar 1 menit), tiriskan hingga kering sempurna. Bentuk mie menjadi sarang pipih per porsi. Panaskan minyak banyak di wajan, goreng mie dengan api sedang hingga kering, kaku, garing kriuk, dan berwarna kuning keemasan. Angkat, tiriskan, dan tata di piring saji cekung."},
      {"stepNumber": 2, "title": "Menumis Isian", "instruction": "Panaskan 2 sdm minyak di wajan. Tumis bawang putih cincang dan bawang bombay hingga sangat harum dan berwarna keemasan. Masukkan potongan daging ayam dan udang, aduk cepat hingga berubah warna. Masukkan bakso dan wortel.", "rawText": "Menumis Isian: Panaskan 2 sdm minyak di wajan. Tumis bawang putih cincang dan bawang bombay hingga sangat harum dan berwarna keemasan. Masukkan potongan daging ayam dan udang, aduk cepat hingga berubah warna. Masukkan bakso dan wortel."},
      {"stepNumber": 3, "title": "Memasak Kuah Kaldu", "instruction": "Tuang air kaldu ayam ke dalam tumisan. Bumbui dengan saus tiram, kecap asin, minyak wijen, lada, garam, dan gula. Masak hingga mendidih dan kuah beraroma gurih sedap. Masukkan potongan sawi hijau, masak sebentar.", "rawText": "Memasak Kuah Kaldu: Tuang air kaldu ayam ke dalam tumisan. Bumbui dengan saus tiram, kecap asin, minyak wijen, lada, garam, dan gula. Masak hingga mendidih dan kuah beraroma gurih sedap. Masukkan potongan sawi hijau, masak sebentar."},
      {"stepNumber": 4, "title": "Mengentalkan Kuah dan Menyerabutkan Telur", "instruction": "Kecilkan api, tuangkan larutan tepung maizena perlahan sambil terus diaduk cepat hingga kuah mengental licin dan transparan. Tuang telur kocok perlahan sambil diaduk melingkar agar terbentuk serabut telur halus di dalam kuah. Matikan api.", "rawText": "Mengentalkan Kuah dan Menyerabutkan Telur: Kecilkan api, tuangkan larutan tepung maizena perlahan sambil terus diaduk cepat hingga kuah mengental licin dan transparan. Tuang telur kocok perlahan sambil diaduk melingkar agar terbentuk serabut telur halus di dalam kuah. Matikan api."},
      {"stepNumber": 5, "title": "Penyajian", "instruction": "Siramkan kuah kental panas beserta isian ayam, udang, dan sayuran ke atas mie kering kriuk yang sudah ditata di piring. Sajikan segera selagi mengepul panas bersama perasan jeruk nipis dan sambal lombok kuning Makassar.", "rawText": "Penyajian: Siramkan kuah kental panas beserta isian ayam, udang, dan sayuran ke atas mie kering kriuk yang sudah ditata di piring. Sajikan segera selagi mengepul panas bersama perasan jeruk nipis dan sambal lombok kuning Makassar."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Porsi Lengkap): Kalori 460 kkal | Protein 20g | Lemak 18g | Karbohidrat 56g. Menyediakan energi karbohidrat cepat, vitamin A dan C dari sayur sawi hijau, serta protein ayam dan telur.",
      "serving": "Per Porsi Lengkap",
      "calories": 460,
      "protein": 20.0,
      "fat": 18.0,
      "carbohydrates": 56.0,
      "notes": "Menyediakan energi karbohidrat cepat, vitamin A dan C dari sayur sawi hijau, serta protein ayam dan telur."
    }
  },
  {
    "recipeNumber": 179,
    "title": "179. Gohu Ikan Khas Ternate (Maluku Utara)",
    "name": "Gohu Ikan Khas Ternate",
    "slug": "gohu-ikan-khas-ternate",
    "scope": "INDONESIA",
    "origin": "Ternate, Maluku Utara",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 15,
    "cookTimeMinutes": 15,
    "servings": 4,
    "difficulty": "EASY",
    "spicinessLevel": 2,
    "categorySlug": "ikan-seafood",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """179. Gohu Ikan Khas Ternate (Maluku Utara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
400g Daging Ikan Tuna Segar atau Cakalang (kualitas sashimi, buang bagian hitam, potong dadu 1x1 cm)
3 buah Jeruk Lemon Cui / Jeruk Nipis (ambil air perasannya)
1 sdt Garam halus
1/2 sdt Gula pasir
Bumbu Iris Segar:
8 butir Bawang merah (iris tipis)
12 buah Cabai rawit merah dan hijau (iris kasar)
1 genggam Daun Kemangi / Balakama segar (petik daunnya)
Minyak Siraman dan Taburan Khas:
4 sdm Minyak Kelapa Asli (bukan minyak sawit, dipanaskan hingga berasap)
3 sdm Kacang Tanah Goreng atau Kenari Sangrai (tumbuk kasar)
Langkah-Langkah Pembuatan:
Persiapan Ikan: Potong dadu daging ikan tuna segar yang telah dibersihkan. Masukkan potongan ikan ke dalam mangkuk kaca atau porselen. Lumuri dengan perasan air jeruk lemon cui dan garam. Aduk rata, lalu diamkan selama 10 menit di lemari pendingin agar asam jeruk mematangkan permukaan daging ikan secara alami hingga warnanya agak memutih.
Mencampur Bumbu Segar: Masukkan irisan bawang merah, irisan cabai rawit, dan daun kemangi ke dalam mangkuk ikan tuna. Aduk perlahan hingga tercampur rata.
Menyiram Minyak Kelapa Mendidih: Panaskan 4 sdm minyak kelapa murni di wajan kecil dengan api sedang hingga benar-benar panas mendidih dan keluar aroma wangi kelapa. Angkat wajan, lalu siramkan minyak kelapa panas mendidih secara merata ke atas campuran ikan dan bumbu di dalam mangkuk (akan terdengar bunyi mendesis harum). Aduk cepat.
Tahap Akhir dan Taburan: Tambahkan sedikit gula pasir untuk menyeimbangkan rasa asam-segar dan gurih minyak. Taburkan kacang tanah goreng atau kenari sangrai yang telah ditumbuk kasar di atasnya untuk memberikan sensasi renyah gurih.
Penyajian: Nikmati Gohu Ikan segera dalam kondisi segar bersama kasbi (singkong rebus), pisang rebus, atau nasi putih hangat.
Nutrisi (Per Porsi): Kalori 210 kkal | Protein 25g | Lemak 11g | Karbohidrat 4g. Superfood alami tinggi asam lemak EPA/DHA omega-3, vitamin C jeruk lemon cui, dan vitamin E dari kenari sangrai.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "400g Daging Ikan Tuna Segar / Cakalang (potong dadu 1x1 cm)", "amount": 400.0, "unit": "g", "name": "Ikan Tuna Segar", "notes": "potong dadu 1x1 cm", "orderIndex": 1},
          {"rawText": "3 buah Jeruk Lemon Cui (ambil air)", "amount": 3.0, "unit": "buah", "name": "Jeruk Lemon Cui", "notes": "ambil air perasan", "orderIndex": 2},
          {"rawText": "1 sdt Garam halus dan 1/2 sdt Gula", "amount": 1.0, "unit": "sdt", "name": "Garam dan Gula", "notes": None, "orderIndex": 3}
        ]
      },
      {
        "name": "Bumbu Iris Segar",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "8 butir Bawang merah (iris tipis)", "amount": 8.0, "unit": "butir", "name": "Bawang merah", "notes": "iris tipis", "orderIndex": 1},
          {"rawText": "12 buah Cabai rawit merah hijau (iris kasar)", "amount": 12.0, "unit": "buah", "name": "Cabai rawit", "notes": "iris kasar", "orderIndex": 2},
          {"rawText": "1 genggam Daun Kemangi segar", "amount": 1.0, "unit": "genggam", "name": "Daun Kemangi segar", "notes": "petik daun", "orderIndex": 3}
        ]
      },
      {
        "name": "Minyak Siraman dan Taburan",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "4 sdm Minyak Kelapa Asli (panaskan)", "amount": 4.0, "unit": "sdm", "name": "Minyak Kelapa Asli", "notes": "panaskan mendidih", "orderIndex": 1},
          {"rawText": "3 sdm Kacang Tanah Goreng / Kenari Sangrai (tumbuk)", "amount": 3.0, "unit": "sdm", "name": "Kacang Tanah Goreng / Kenari", "notes": "tumbuk kasar", "orderIndex": 2}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Persiapan Ikan", "instruction": "Potong dadu daging ikan tuna segar yang telah dibersihkan. Masukkan potongan ikan ke dalam mangkuk kaca atau porselen. Lumuri dengan perasan air jeruk lemon cui dan garam. Aduk rata, lalu diamkan selama 10 menit di lemari pendingin agar asam jeruk mematangkan permukaan daging ikan secara alami hingga warnanya agak memutih.", "rawText": "Persiapan Ikan: Potong dadu daging ikan tuna segar yang telah dibersihkan. Masukkan potongan ikan ke dalam mangkuk kaca atau porselen. Lumuri dengan perasan air jeruk lemon cui dan garam. Aduk rata, lalu diamkan selama 10 menit di lemari pendingin agar asam jeruk mematangkan permukaan daging ikan secara alami hingga warnanya agak memutih."},
      {"stepNumber": 2, "title": "Mencampur Bumbu Segar", "instruction": "Masukkan irisan bawang merah, irisan cabai rawit, dan daun kemangi ke dalam mangkuk ikan tuna. Aduk perlahan hingga tercampur rata.", "rawText": "Mencampur Bumbu Segar: Masukkan irisan bawang merah, irisan cabai rawit, dan daun kemangi ke dalam mangkuk ikan tuna. Aduk perlahan hingga tercampur rata."},
      {"stepNumber": 3, "title": "Menyiram Minyak Kelapa Mendidih", "instruction": "Panaskan 4 sdm minyak kelapa murni di wajan kecil dengan api sedang hingga benar-benar panas mendidih dan keluar aroma wangi kelapa. Angkat wajan, lalu siramkan minyak kelapa panas mendidih secara merata ke atas campuran ikan dan bumbu di dalam mangkuk (akan terdengar bunyi mendesis harum). Aduk cepat.", "rawText": "Menyiram Minyak Kelapa Mendidih: Panaskan 4 sdm minyak kelapa murni di wajan kecil dengan api sedang hingga benar-benar panas mendidih dan keluar aroma wangi kelapa. Angkat wajan, lalu siramkan minyak kelapa panas mendidih secara merata ke atas campuran ikan dan bumbu di dalam mangkuk (akan terdengar bunyi mendesis harum). Aduk cepat."},
      {"stepNumber": 4, "title": "Tahap Akhir dan Taburan", "instruction": "Tambahkan sedikit gula pasir untuk menyeimbangkan rasa asam-segar dan gurih minyak. Taburkan kacang tanah goreng atau kenari sangrai yang telah ditumbuk kasar di atasnya untuk memberikan sensasi renyah gurih.", "rawText": "Tahap Akhir dan Taburan: Tambahkan sedikit gula pasir untuk menyeimbangkan rasa asam-segar dan gurih minyak. Taburkan kacang tanah goreng atau kenari sangrai yang telah ditumbuk kasar di atasnya untuk memberikan sensasi renyah gurih."},
      {"stepNumber": 5, "title": "Penyajian", "instruction": "Nikmati Gohu Ikan segera dalam kondisi segar bersama kasbi (singkong rebus), pisang rebus, atau nasi putih hangat.", "rawText": "Penyajian: Nikmati Gohu Ikan segera dalam kondisi segar bersama kasbi (singkong rebus), pisang rebus, atau nasi putih hangat."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Porsi): Kalori 210 kkal | Protein 25g | Lemak 11g | Karbohidrat 4g. Superfood alami tinggi asam lemak EPA/DHA omega-3, vitamin C jeruk lemon cui, dan vitamin E dari kenari sangrai.",
      "serving": "Per Porsi",
      "calories": 210,
      "protein": 25.0,
      "fat": 11.0,
      "carbohydrates": 4.0,
      "notes": "Superfood alami tinggi asam lemak EPA/DHA omega-3, vitamin C jeruk lemon cui, dan vitamin E dari kenari sangrai."
    }
  },
  {
    "recipeNumber": 180,
    "title": "180. Ayam Cincane Khas Samarinda (Kalimantan Timur)",
    "name": "Ayam Cincane Khas Samarinda",
    "slug": "ayam-cincane-khas-samarinda",
    "scope": "INDONESIA",
    "origin": "Samarinda, Kalimantan Timur",
    "visualRef": "Lihat Ilustrasi Masakan",
    "imageUrl": None,
    "prepTimeMinutes": 25,
    "cookTimeMinutes": 50,
    "servings": 4,
    "difficulty": "MEDIUM",
    "spicinessLevel": 2,
    "categorySlug": "ayam-unggas",
    "cuisineTypeSlug": "masakan-daerah-tradisional",
    "rawContent": """180. Ayam Cincane Khas Samarinda (Kalimantan Timur)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
1 ekor Ayam Kampung segar (sekitar 800g, potong 4 atau 8 bagian)
500 ml Santan kelapa asli sedang
1 buah Jeruk Nipis (untuk lumuran)
3 sdm Gula Merah Aren (sisir halus)
1 sdm Air asam jawa
Bumbu Halus Merah Khas Cincane:
10 buah Cabai merah besar (buang biji untuk warna merah pekat)
6 buah Cabai merah keriting
10 siung Bawang merah
5 siung Bawang putih
4 butir Kemiri (sangrai)
1 sdt Terasi udang (bakar hingga harum)
1 sdm Garam dan 1/2 sdt Kaldu jamur
Bumbu Rempah Cemplung:
2 batang Serai (ambil bagian putih, memarkan)
3 cm Jahe (memarkan)
3 cm Lengkuas (memarkan)
3 lembar Daun salam
Pelengkap Penyajian:
Lalapan timun dan kemangi segar
Sambal terasi mentah
Nasi putih pulen hangat
Langkah-Langkah Pembuatan:
Persiapan Ayam: Bersihkan potongan ayam kampung, lumuri dengan perasan air jeruk nipis dan sedikit garam. Diamkan 15 menit, lalu bilas sebentar dan tiriskan.
Menumis Bumbu Merah Cincane: Panaskan 3 sdm minyak di wajan. Tumis bumbu halus merah bersama serai, jahe, lengkuas, dan daun salam. Tumis dengan api sedang hingga bumbu benar-benar matang tanak, harum terasi menyeruak, dan bumbu berminyak kemerahan.
Mengungkep Ayam dengan Santan: Masukkan potongan ayam kampung ke dalam tumisan bumbu. Aduk-aduk hingga daging ayam berubah warna kaku. Tuangkan santan kelapa, tambahkan gula merah sisir, air asam jawa, garam, dan kaldu bubuk.
Meresapkan Bumbu: Kecilkan api dan tutup wajan. Ungkep ayam secara perlahan sambil sesekali diaduk agar santan tidak pecah. Masak terus hingga kuah santan menyusut pekat, bumbu merah mengental, dan meresap ke dalam serat daging ayam. Sisakan sedikit bumbu kental untuk bahan olesan bakar. Angkat ayam.
Membakar Ayam: Siapkan panggangan arang atau grill pan panas. Bakar ayam kampung sambil diolesi secara merata dengan sisa bumbu merah kental yang pekat tadi. Bolak-balik hingga permukaan ayam agak berkaramel kecokelatan dan tercium aroma asap bakaran khas yang harum.
Penyajian: Angkat Ayam Cincane bakar, tata di atas piring saji. Siramkan sisa bumbu merah kental di atasnya. Sajikan selagi hangat bersama nasi putih, lalapan, dan sambal terasi.
Nutrisi (Per Potong Ayam): Kalori 280 kkal | Protein 25g | Lemak 14g | Karbohidrat 12g. Sumber protein ayam kampung rendah lemak dengan mineral zinc serta capsaicin pembakar energi dari bumbu merah.""",
    "ingredientGroups": [
      {
        "name": "Bahan Utama",
        "orderIndex": 1,
        "ingredients": [
          {"rawText": "1 ekor Ayam Kampung (potong 4/8 bagian)", "amount": 1.0, "unit": "ekor", "name": "Ayam Kampung", "notes": "potong 4 atau 8", "orderIndex": 1},
          {"rawText": "500 ml Santan kelapa asli sedang", "amount": 500.0, "unit": "ml", "name": "Santan kelapa", "notes": "asli sedang", "orderIndex": 2},
          {"rawText": "1 buah Jeruk Nipis (untuk lumuran)", "amount": 1.0, "unit": "buah", "name": "Jeruk Nipis", "notes": "untuk lumuran", "orderIndex": 3},
          {"rawText": "3 sdm Gula Merah Aren (sisir)", "amount": 3.0, "unit": "sdm", "name": "Gula Merah Aren", "notes": "sisir halus", "orderIndex": 4},
          {"rawText": "1 sdm Air asam jawa", "amount": 1.0, "unit": "sdm", "name": "Air asam jawa", "notes": None, "orderIndex": 5}
        ]
      },
      {
        "name": "Bumbu Halus Merah Khas Cincane",
        "orderIndex": 2,
        "ingredients": [
          {"rawText": "10 buah Cabai merah besar", "amount": 10.0, "unit": "buah", "name": "Cabai merah besar", "notes": "buang biji warna merah", "orderIndex": 1},
          {"rawText": "6 buah Cabai merah keriting", "amount": 6.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 2},
          {"rawText": "10 siung Bawang merah", "amount": 10.0, "unit": "siung", "name": "Bawang merah", "notes": None, "orderIndex": 3},
          {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 4},
          {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 5},
          {"rawText": "1 sdt Terasi udang (bakar)", "amount": 1.0, "unit": "sdt", "name": "Terasi udang", "notes": "bakar harum", "orderIndex": 6},
          {"rawText": "1 sdm Garam dan 1/2 sdt Kaldu", "amount": 1.0, "unit": "sdm", "name": "Garam dan Kaldu", "notes": None, "orderIndex": 7}
        ]
      },
      {
        "name": "Bumbu Rempah Cemplung",
        "orderIndex": 3,
        "ingredients": [
          {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 1},
          {"rawText": "3 cm Jahe (memarkan)", "amount": 3.0, "unit": "cm", "name": "Jahe", "notes": "memarkan", "orderIndex": 2},
          {"rawText": "3 cm Lengkuas (memarkan)", "amount": 3.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 3},
          {"rawText": "3 lembar Daun salam", "amount": 3.0, "unit": "lembar", "name": "Daun salam", "notes": None, "orderIndex": 4}
        ]
      },
      {
        "name": "Pelengkap Penyajian",
        "orderIndex": 4,
        "ingredients": [
          {"rawText": "Lalapan timun dan kemangi secukupnya", "amount": None, "unit": "secukupnya", "name": "Lalapan timun dan kemangi", "notes": None, "orderIndex": 1},
          {"rawText": "Sambal terasi mentah secukupnya", "amount": None, "unit": "secukupnya", "name": "Sambal terasi mentah", "notes": None, "orderIndex": 2}
        ]
      }
    ],
    "steps": [
      {"stepNumber": 1, "title": "Persiapan Ayam", "instruction": "Bersihkan potongan ayam kampung, lumuri dengan perasan air jeruk nipis dan sedikit garam. Diamkan 15 menit, lalu bilas sebentar dan tiriskan.", "rawText": "Persiapan Ayam: Bersihkan potongan ayam kampung, lumuri dengan perasan air jeruk nipis dan sedikit garam. Diamkan 15 menit, lalu bilas sebentar dan tiriskan."},
      {"stepNumber": 2, "title": "Menumis Bumbu Merah Cincane", "instruction": "Panaskan 3 sdm minyak di wajan. Tumis bumbu halus merah bersama serai, jahe, lengkuas, dan daun salam. Tumis dengan api sedang hingga bumbu benar-benar matang tanak, harum terasi menyeruak, dan bumbu berminyak kemerahan.", "rawText": "Menumis Bumbu Merah Cincane: Panaskan 3 sdm minyak di wajan. Tumis bumbu halus merah bersama serai, jahe, lengkuas, dan daun salam. Tumis dengan api sedang hingga bumbu benar-benar matang tanak, harum terasi menyeruak, dan bumbu berminyak kemerahan."},
      {"stepNumber": 3, "title": "Mengungkep Ayam dengan Santan", "instruction": "Masukkan potongan ayam kampung ke dalam tumisan bumbu. Aduk-aduk hingga daging ayam berubah warna kaku. Tuangkan santan kelapa, tambahkan gula merah sisir, air asam jawa, garam, dan kaldu bubuk.", "rawText": "Mengungkep Ayam dengan Santan: Masukkan potongan ayam kampung ke dalam tumisan bumbu. Aduk-aduk hingga daging ayam berubah warna kaku. Tuangkan santan kelapa, tambahkan gula merah sisir, air asam jawa, garam, dan kaldu bubuk."},
      {"stepNumber": 4, "title": "Meresapkan Bumbu", "instruction": "Kecilkan api dan tutup wajan. Ungkep ayam secara perlahan sambil sesekali diaduk agar santan tidak pecah. Masak terus hingga kuah santan menyusut pekat, bumbu merah mengental, dan meresap ke dalam serat daging ayam. Sisakan sedikit bumbu kental untuk bahan olesan bakar. Angkat ayam.", "rawText": "Meresapkan Bumbu: Kecilkan api dan tutup wajan. Ungkep ayam secara perlahan sambil sesekali diaduk agar santan tidak pecah. Masak terus hingga kuah santan menyusut pekat, bumbu merah mengental, dan meresap ke dalam serat daging ayam. Sisakan sedikit bumbu kental untuk bahan olesan bakar. Angkat ayam."},
      {"stepNumber": 5, "title": "Membakar Ayam", "instruction": "Siapkan panggangan arang atau grill pan panas. Bakar ayam kampung sambil diolesi secara merata dengan sisa bumbu merah kental yang pekat tadi. Bolak-balik hingga permukaan ayam agak berkaramel kecokelatan dan tercium aroma asap bakaran khas yang harum.", "rawText": "Membakar Ayam: Siapkan panggangan arang atau grill pan panas. Bakar ayam kampung sambil diolesi secara merata dengan sisa bumbu merah kental yang pekat tadi. Bolak-balik hingga permukaan ayam agak berkaramel kecokelatan dan tercium aroma asap bakaran khas yang harum."},
      {"stepNumber": 6, "title": "Penyajian", "instruction": "Angkat Ayam Cincane bakar, tata di atas piring saji. Siramkan sisa bumbu merah kental di atasnya. Sajikan selagi hangat bersama nasi putih, lalapan, dan sambal terasi.", "rawText": "Penyajian: Angkat Ayam Cincane bakar, tata di atas piring saji. Siramkan sisa bumbu merah kental di atasnya. Sajikan selagi hangat bersama nasi putih, lalapan, dan sambal terasi."}
    ],
    "nutrition": {
      "rawText": "Nutrisi (Per Potong Ayam): Kalori 280 kkal | Protein 25g | Lemak 14g | Karbohidrat 12g. Sumber protein ayam kampung rendah lemak dengan mineral zinc serta capsaicin pembakar energi dari bumbu merah.",
      "serving": "Per Potong Ayam",
      "calories": 280,
      "protein": 25.0,
      "fat": 14.0,
      "carbohydrates": 12.0,
      "notes": "Sumber protein ayam kampung rendah lemak dengan mineral zinc serta capsaicin pembakar energi dari bumbu merah."
    }
  }
]

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

# Filter out if any exist with the same recipe numbers
existing_numbers = set(r['recipeNumber'] for r in existing_data['recipes'])
added_count = 0
for r in new_recipes:
    if r['recipeNumber'] not in existing_numbers:
        existing_data['recipes'].append(r)
        added_count += 1

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

total_count = len(existing_data["recipes"])
print(f'Successfully added {added_count} new recipes. Total recipes now: {total_count}')
