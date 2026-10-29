import json
import os

new_recipes = [
    {
        "recipeNumber": 191,
        "title": "191. Ketupat Sayur Betawi (DKI Jakarta)",
        "name": "Ketupat Sayur Betawi",
        "slug": "ketupat-sayur-betawi",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 25,
        "cookTimeMinutes": 45,
        "servings": 5,
        "difficulty": "MEDIUM",
        "spicinessLevel": 2,
        "categorySlug": "sayuran-tumisan",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """191. Ketupat Sayur Betawi (DKI Jakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama & Sayuran:
5 buah Ketupat matang (potong-potong sesuai selera)
300g Pepaya muda (kupas, serut kasar atau potong bentuk korek api)
200g Labu siam (kupas, potong bentuk korek api)
100g Kacang panjang (potong-potong 3 cm)
5 buah Tahu cokelat segitiga (belah dua)
5 butir Telur ayam rebus (kupas kulitnya)
500 ml Santan kental murni (dari 1 butir kelapa tua)
1 liter Santan encer
3 sdm Minyak goreng untuk menumis
Bumbu Rempah Aromatik:
3 cm Lengkuas (memarkan)
2 batang Serai (memarkan)
3 lembar Daun salam kering
4 lembar Daun jeruk purut (buang tulang daunnya)
Bumbu Halus:
8 butir Bawang merah
5 siung Bawang putih
6 buah Cabai merah keriting
4 buah Cabai merah besar (buang sebagian biji)
4 butir Kemiri (sangrai)
1 sdm Ebi sangrai (haluskan bersama bumbu)
1 sdt Ketumbar bubuk
2 cm Kunyit bakar
1 sdt Terasi bakar
1.5 sdt Garam
1.5 sdm Gula merah aren (sisir)
1/2 sdt Kaldu jamur / kaldu ayam
Bahan Pelengkap Lebaran:
3 sdm Bawang merah goreng renyah
Kerupuk merah bawang atau emping melinjo secukupnya
Sambal rawit rebus secukupnya
Langkah-Langkah Pembuatan:
Menyiapkan Sayuran: Remas potongan pepaya muda dan labu siam dengan 1 sendok teh garam hingga lemas agar getahnya hilang. Bilas bersih dengan air mengalir, lalu tiriskan.
Menumis Bumbu Halus dan Rempah: Panaskan 3 sendok makan minyak goreng dalam panci atau wajan besar. Masukkan bumbu halus, lengkuas, serai, daun salam, dan daun jeruk. Tumis dengan api sedang hingga matang harum, tanak, dan mengeluarkan minyak kemerahan.
Memasak Kuah Sayur Santan: Tuangkan santan encer ke dalam tumisan bumbu. Aduk perlahan dan masak hingga mendidih agar bumbu larut merata. Masukkan pepaya muda dan labu siam. Masak hingga sayuran setengah matang (sekitar 7 menit).
Memasukkan Tahu, Telur, dan Santan Kental: Masukkan potongan kacang panjang, tahu cokelat, dan telur rebus. Tuangkan santan kental murni secara perlahan sambil terus diaduk perlahan dari bawah ke atas agar santan tidak pecah (curdling). Bumbui dengan garam, gula merah aren, dan kaldu jamur.
Mematangkan Sayur Godhog: Masak di atas api sedang cenderung kecil hingga seluruh sayuran empuk matang, kuah santan berwarna oranye kemerahan berminyak gurih, dan bumbu meresap sempurna ke dalam tahu serta telur. Cicipi untuk memastikan rasa gurih, pedas manis pas. Angkat.
Penyajian Lebaran: Tata potongan ketupat di dalam mangkuk saji saji. Siram dengan kuah sayur godhog panas beserta labu siam, pepaya muda, potongan tahu, dan 1 butir telur rebus. Taburi bawang merah goreng melimpah dan sajikan bersama kerupuk merah Betawi serta emping melinjo.
Nutrisi (Per Porsi Komplit): Kalori 340 kkal | Protein 12g | Lemak 16g | Karbohidrat 38g. Hidangan khas Idul Fitri yang kaya serat alami dari pepaya muda dan labu siam, berpadu asam laurat lemak nabati santan serta protein komplit dari telur dan ebi.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama & Sayuran",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "5 buah Ketupat matang (potong-potong)", "amount": 5.0, "unit": "buah", "name": "Ketupat matang", "notes": "potong-potong", "orderIndex": 1},
                    {"rawText": "300g Pepaya muda (serut kasar atau korek api)", "amount": 300.0, "unit": "g", "name": "Pepaya muda", "notes": "serut kasar atau korek api", "orderIndex": 2},
                    {"rawText": "200g Labu siam (potong korek api)", "amount": 200.0, "unit": "g", "name": "Labu siam", "notes": "potong korek api", "orderIndex": 3},
                    {"rawText": "100g Kacang panjang (potong 3 cm)", "amount": 100.0, "unit": "g", "name": "Kacang panjang", "notes": "potong 3 cm", "orderIndex": 4},
                    {"rawText": "5 buah Tahu cokelat segitiga (belah dua)", "amount": 5.0, "unit": "buah", "name": "Tahu cokelat segitiga", "notes": "belah dua", "orderIndex": 5},
                    {"rawText": "5 butir Telur ayam rebus (kupas)", "amount": 5.0, "unit": "butir", "name": "Telur ayam rebus", "notes": "kupas", "orderIndex": 6},
                    {"rawText": "500 ml Santan kental murni", "amount": 500.0, "unit": "ml", "name": "Santan kental murni", "notes": "dari kelapa tua", "orderIndex": 7},
                    {"rawText": "1 liter Santan encer", "amount": 1.0, "unit": "liter", "name": "Santan encer", "notes": None, "orderIndex": 8},
                    {"rawText": "3 sdm Minyak goreng untuk menumis", "amount": 3.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 9}
                ]
            },
            {
                "name": "Bumbu Rempah Aromatik",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "3 cm Lengkuas (memarkan)", "amount": 3.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 1},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 2},
                    {"rawText": "3 lembar Daun salam kering", "amount": 3.0, "unit": "lembar", "name": "Daun salam kering", "notes": None, "orderIndex": 3},
                    {"rawText": "4 lembar Daun jeruk purut", "amount": 4.0, "unit": "lembar", "name": "Daun jeruk purut", "notes": "buang tulang", "orderIndex": 4}
                ]
            },
            {
                "name": "Bumbu Halus",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "8 butir Bawang merah", "amount": 8.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "6 buah Cabai merah keriting", "amount": 6.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 3},
                    {"rawText": "4 buah Cabai merah besar", "amount": 4.0, "unit": "buah", "name": "Cabai merah besar", "notes": "buang biji", "orderIndex": 4},
                    {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 5},
                    {"rawText": "1 sdm Ebi sangrai", "amount": 1.0, "unit": "sdm", "name": "Ebi sangrai", "notes": "haluskan bersama bumbu", "orderIndex": 6},
                    {"rawText": "1 sdt Ketumbar bubuk", "amount": 1.0, "unit": "sdt", "name": "Ketumbar bubuk", "notes": None, "orderIndex": 7},
                    {"rawText": "2 cm Kunyit bakar", "amount": 2.0, "unit": "cm", "name": "Kunyit bakar", "notes": None, "orderIndex": 8},
                    {"rawText": "1 sdt Terasi bakar", "amount": 1.0, "unit": "sdt", "name": "Terasi bakar", "notes": None, "orderIndex": 9},
                    {"rawText": "1.5 sdt Garam", "amount": 1.5, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 10},
                    {"rawText": "1.5 sdm Gula merah aren (sisir)", "amount": 1.5, "unit": "sdm", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 11},
                    {"rawText": "1/2 sdt Kaldu jamur", "amount": 0.5, "unit": "sdt", "name": "Kaldu jamur", "notes": None, "orderIndex": 12}
                ]
            },
            {
                "name": "Bahan Pelengkap Lebaran",
                "orderIndex": 4,
                "ingredients": [
                    {"rawText": "3 sdm Bawang merah goreng renyah", "amount": 3.0, "unit": "sdm", "name": "Bawang merah goreng", "notes": None, "orderIndex": 1},
                    {"rawText": "Kerupuk merah bawang atau emping melinjo secukupnya", "amount": None, "unit": "secukupnya", "name": "Kerupuk merah bawang atau emping", "notes": None, "orderIndex": 2},
                    {"rawText": "Sambal rawit rebus secukupnya", "amount": None, "unit": "secukupnya", "name": "Sambal rawit rebus", "notes": None, "orderIndex": 3}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menyiapkan Sayuran", "instruction": "Remas potongan pepaya muda dan labu siam dengan 1 sendok teh garam hingga lemas agar getahnya hilang. Bilas bersih dengan air mengalir, lalu tiriskan.", "rawText": "Menyiapkan Sayuran: Remas potongan pepaya muda dan labu siam dengan 1 sendok teh garam hingga lemas agar getahnya hilang. Bilas bersih dengan air mengalir, lalu tiriskan."},
            {"stepNumber": 2, "title": "Menumis Bumbu Halus dan Rempah", "instruction": "Panaskan 3 sendok makan minyak goreng dalam panci atau wajan besar. Masukkan bumbu halus, lengkuas, serai, daun salam, dan daun jeruk. Tumis dengan api sedang hingga matang harum, tanak, dan mengeluarkan minyak kemerahan.", "rawText": "Menumis Bumbu Halus dan Rempah: Panaskan 3 sendok makan minyak goreng dalam panci atau wajan besar. Masukkan bumbu halus, lengkuas, serai, daun salam, dan daun jeruk. Tumis dengan api sedang hingga matang harum, tanak, dan mengeluarkan minyak kemerahan."},
            {"stepNumber": 3, "title": "Memasak Kuah Sayur Santan", "instruction": "Tuangkan santan encer ke dalam tumisan bumbu. Aduk perlahan dan masak hingga mendidih agar bumbu larut merata. Masukkan pepaya muda dan labu siam. Masak hingga sayuran setengah matang (sekitar 7 menit).", "rawText": "Memasak Kuah Sayur Santan: Tuangkan santan encer ke dalam tumisan bumbu. Aduk perlahan dan masak hingga mendidih agar bumbu larut merata. Masukkan pepaya muda dan labu siam. Masak hingga sayuran setengah matang (sekitar 7 menit)."},
            {"stepNumber": 4, "title": "Memasukkan Tahu, Telur, dan Santan Kental", "instruction": "Masukkan potongan kacang panjang, tahu cokelat, dan telur rebus. Tuangkan santan kental murni secara perlahan sambil terus diaduk perlahan dari bawah ke atas agar santan tidak pecah. Bumbui dengan garam, gula merah aren, dan kaldu jamur.", "rawText": "Memasukkan Tahu, Telur, dan Santan Kental: Masukkan potongan kacang panjang, tahu cokelat, dan telur rebus. Tuangkan santan kental murni secara perlahan sambil terus diaduk perlahan dari bawah ke atas agar santan tidak pecah. Bumbui dengan garam, gula merah aren, dan kaldu jamur."},
            {"stepNumber": 5, "title": "Mematangkan Sayur Godhog", "instruction": "Masak di atas api sedang cenderung kecil hingga seluruh sayuran empuk matang, kuah santan berwarna oranye kemerahan berminyak gurih, dan bumbu meresap sempurna ke dalam tahu serta telur. Cicipi dan angkat.", "rawText": "Mematangkan Sayur Godhog: Masak di atas api sedang cenderung kecil hingga seluruh sayuran empuk matang, kuah santan berwarna oranye kemerahan berminyak gurih, dan bumbu meresap sempurna ke dalam tahu serta telur. Cicipi dan angkat."},
            {"stepNumber": 6, "title": "Penyajian Lebaran", "instruction": "Tata potongan ketupat di dalam mangkuk saji. Siram dengan kuah sayur godhog panas beserta labu siam, pepaya muda, potongan tahu, dan 1 butir telur rebus. Taburi bawang merah goreng melimpah dan sajikan bersama kerupuk merah Betawi serta emping melinjo.", "rawText": "Penyajian Lebaran: Tata potongan ketupat di dalam mangkuk saji. Siram dengan kuah sayur godhog panas beserta labu siam, pepaya muda, potongan tahu, dan 1 butir telur rebus. Taburi bawang merah goreng melimpah dan sajikan bersama kerupuk merah Betawi serta emping melinjo."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi Komplit): Kalori 340 kkal | Protein 12g | Lemak 16g | Karbohidrat 38g. Hidangan khas Idul Fitri yang kaya serat alami dari pepaya muda dan labu siam, berpadu asam laurat lemak nabati santan serta protein komplit dari telur dan ebi.",
            "serving": "Per Porsi Komplit",
            "calories": 340,
            "protein": 12.0,
            "fat": 16.0,
            "carbohydrates": 38.0,
            "notes": "Hidangan khas Idul Fitri yang kaya serat alami dari pepaya muda dan labu siam, berpadu asam laurat lemak nabati santan serta protein komplit dari telur dan ebi."
        }
    },
    {
        "recipeNumber": 192,
        "title": "192. Sambal Goreng Ati Kentang Petai (Jawa Tengah)",
        "name": "Sambal Goreng Ati Kentang Petai",
        "slug": "sambal-goreng-ati-kentang",
        "scope": "INDONESIA",
        "origin": "Jawa Tengah",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 30,
        "cookTimeMinutes": 35,
        "servings": 6,
        "difficulty": "MEDIUM",
        "spicinessLevel": 3,
        "categorySlug": "lauk-utama-nusantara",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """192. Sambal Goreng Ati Kentang Petai (Jawa Tengah)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Hati sapi segar (cuci bersih, rebus dengan daun salam dan jahe hingga matang, potong dadu 2 cm)
500g Kentang (kupas, potong dadu 1.5 cm, goreng hingga berkulit keemasan)
2 papan Petai segar (kupas, belah dua)
3 buah Cabai merah besar (buang biji, iris serong tipis memanjang untuk hiasan)
300 ml Santan kelapa sedang
4 sdm Minyak goreng untuk menumis
Bumbu Rempah Aromatik:
3 cm Lengkuas (memarkan)
2 batang Serai (memarkan)
3 lembar Daun salam
3 lembar Daun jeruk purut (sobek)
Bumbu Halus:
10 butir Bawang merah
6 siung Bawang putih
8 buah Cabai merah besar (buang biji)
6 buah Cabai merah keriting
4 butir Kemiri (sangrai)
2 cm Jahe
1 sdt Terasi bakar berkualitas
1.5 sdt Garam halus
1.5 sdm Gula merah aren (sisir)
1/2 sdt Kaldu sapi bubuk
Langkah-Langkah Pembuatan:
Merebus Hati Sapi: Rebus hati sapi dalam air mendidih bersama 2 lembar daun salam dan 2 cm jahe memarkan selama 20 menit hingga matang dan tidak berdarah. Angkat, dinginkan, lalu potong dadu ukuran 2x2 cm. Goreng sebentar dalam minyak panas (sekitar 1 menit) agar berkulit dan tidak hancur saat dimasak.
Menggoreng Kentang: Goreng potongan dadu kentang dalam minyak panas banyak hingga matang, berkulit kuning keemasan, dan tiriskan.
Menumis Bumbu Halus: Panaskan 4 sendok makan minyak dalam wajan cekung. Masukkan bumbu halus bersama lengkuas, serai, daun salam, dan daun jeruk. Tumis di atas api sedang hingga bumbu benar-benar matang tanak, harum, dan mengeluarkan minyak merah cabai.
Memasak dengan Santan: Masukkan santan kelapa sedang, gula merah aren, garam, dan kaldu sapi bubuk. Aduk perlahan hingga kuah mendidih dan mulai mengental. Masukkan irisan cabai merah besar dan petai belah dua, masak sebentar hingga petai layu harum.
Memasukkan Hati dan Kentang: Masukkan potongan hati sapi dan kentang goreng ke dalam wajan. Aduk perlahan dengan api sedang cenderung kecil hingga bumbu sambal meresap merata dan kuah menyusut menjadi bumbu kental berkilap (*nyemek* berminyak).
Penyajian: Angkat dan sajikan sambal goreng ati kentang petai di piring saji. Hidangan ini merupakan pelengkap wajib opor ayam dan ketupat pada hari raya Idul Fitri.
Nutrisi (Per Porsi): Kalori 280 kkal | Protein 18g | Lemak 14g | Karbohidrat 22g. Sangat kaya zat besi heme dan vitamin B12 dari hati sapi untuk mencegah anemia, berpadu potasium kentang dan antioksidan alami dari rempah cabai merah.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "500g Hati sapi segar (rebus, potong dadu 2 cm)", "amount": 500.0, "unit": "g", "name": "Hati sapi segar", "notes": "rebus, potong dadu 2 cm", "orderIndex": 1},
                    {"rawText": "500g Kentang (potong dadu 1.5 cm, goreng)", "amount": 500.0, "unit": "g", "name": "Kentang", "notes": "potong dadu, goreng keemasan", "orderIndex": 2},
                    {"rawText": "2 papan Petai segar (kupas, belah dua)", "amount": 2.0, "unit": "papan", "name": "Petai segar", "notes": "kupas, belah dua", "orderIndex": 3},
                    {"rawText": "3 buah Cabai merah besar (iris serong tipis)", "amount": 3.0, "unit": "buah", "name": "Cabai merah besar", "notes": "iris serong tipis", "orderIndex": 4},
                    {"rawText": "300 ml Santan kelapa sedang", "amount": 300.0, "unit": "ml", "name": "Santan kelapa sedang", "notes": None, "orderIndex": 5},
                    {"rawText": "4 sdm Minyak goreng untuk menumis", "amount": 4.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 6}
                ]
            },
            {
                "name": "Bumbu Rempah Aromatik",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "3 cm Lengkuas (memarkan)", "amount": 3.0, "unit": "cm", "name": "Lengkuas", "notes": "memarkan", "orderIndex": 1},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 2},
                    {"rawText": "3 lembar Daun salam", "amount": 3.0, "unit": "lembar", "name": "Daun salam", "notes": None, "orderIndex": 3},
                    {"rawText": "3 lembar Daun jeruk purut", "amount": 3.0, "unit": "lembar", "name": "Daun jeruk purut", "notes": "sobek", "orderIndex": 4}
                ]
            },
            {
                "name": "Bumbu Halus",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "10 butir Bawang merah", "amount": 10.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "6 siung Bawang putih", "amount": 6.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "8 buah Cabai merah besar (buang biji)", "amount": 8.0, "unit": "buah", "name": "Cabai merah besar", "notes": "buang biji", "orderIndex": 3},
                    {"rawText": "6 buah Cabai merah keriting", "amount": 6.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 4},
                    {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 5},
                    {"rawText": "2 cm Jahe", "amount": 2.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 6},
                    {"rawText": "1 sdt Terasi bakar", "amount": 1.0, "unit": "sdt", "name": "Terasi bakar", "notes": "berkualitas", "orderIndex": 7},
                    {"rawText": "1.5 sdt Garam halus", "amount": 1.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 8},
                    {"rawText": "1.5 sdm Gula merah aren (sisir)", "amount": 1.5, "unit": "sdm", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 9},
                    {"rawText": "1/2 sdt Kaldu sapi bubuk", "amount": 0.5, "unit": "sdt", "name": "Kaldu sapi bubuk", "notes": None, "orderIndex": 10}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Merebus Hati Sapi", "instruction": "Rebus hati sapi dalam air mendidih bersama daun salam dan jahe memarkan selama 20 menit hingga matang dan tidak berdarah. Angkat, dinginkan, lalu potong dadu ukuran 2x2 cm. Goreng sebentar dalam minyak panas sekitar 1 menit agar berkulit.", "rawText": "Merebus Hati Sapi: Rebus hati sapi dalam air mendidih bersama daun salam dan jahe memarkan selama 20 menit hingga matang dan tidak berdarah. Angkat, dinginkan, lalu potong dadu ukuran 2x2 cm. Goreng sebentar dalam minyak panas sekitar 1 menit agar berkulit."},
            {"stepNumber": 2, "title": "Menggoreng Kentang", "instruction": "Goreng potongan dadu kentang dalam minyak panas banyak hingga matang, berkulit kuning keemasan, dan tiriskan.", "rawText": "Menggoreng Kentang: Goreng potongan dadu kentang dalam minyak panas banyak hingga matang, berkulit kuning keemasan, dan tiriskan."},
            {"stepNumber": 3, "title": "Menumis Bumbu Halus", "instruction": "Panaskan 4 sendok makan minyak dalam wajan cekung. Masukkan bumbu halus bersama lengkuas, serai, daun salam, dan daun jeruk. Tumis di atas api sedang hingga bumbu benar-benar matang tanak, harum, dan mengeluarkan minyak merah cabai.", "rawText": "Menumis Bumbu Halus: Panaskan 4 sendok makan minyak dalam wajan cekung. Masukkan bumbu halus bersama lengkuas, serai, daun salam, dan daun jeruk. Tumis di atas api sedang hingga bumbu benar-benar matang tanak, harum, dan mengeluarkan minyak merah cabai."},
            {"stepNumber": 4, "title": "Memasak dengan Santan", "instruction": "Masukkan santan kelapa sedang, gula merah aren, garam, dan kaldu sapi bubuk. Aduk perlahan hingga kuah mendidih dan mulai mengental. Masukkan irisan cabai merah besar dan petai belah dua, masak sebentar hingga petai layu harum.", "rawText": "Memasak dengan Santan: Masukkan santan kelapa sedang, gula merah aren, garam, dan kaldu sapi bubuk. Aduk perlahan hingga kuah mendidih dan mulai mengental. Masukkan irisan cabai merah besar dan petai belah dua, masak sebentar hingga petai layu harum."},
            {"stepNumber": 5, "title": "Memasukkan Hati dan Kentang", "instruction": "Masukkan potongan hati sapi dan kentang goreng ke dalam wajan. Aduk perlahan dengan api sedang cenderung kecil hingga bumbu sambal meresap merata dan kuah menyusut menjadi bumbu kental berkilap nyemek berminyak.", "rawText": "Memasukkan Hati dan Kentang: Masukkan potongan hati sapi dan kentang goreng ke dalam wajan. Aduk perlahan dengan api sedang cenderung kecil hingga bumbu sambal meresap merata dan kuah menyusut menjadi bumbu kental berkilap nyemek berminyak."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Angkat dan sajikan sambal goreng ati kentang petai di piring saji sebagai pelengkap hidangan hari raya Idul Fitri.", "rawText": "Penyajian: Angkat dan sajikan sambal goreng ati kentang petai di piring saji sebagai pelengkap hidangan hari raya Idul Fitri."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 280 kkal | Protein 18g | Lemak 14g | Karbohidrat 22g. Sangat kaya zat besi heme dan vitamin B12 dari hati sapi untuk mencegah anemia, berpadu potasium kentang dan antioksidan alami dari rempah cabai merah.",
            "serving": "Per Porsi",
            "calories": 280,
            "protein": 18.0,
            "fat": 14.0,
            "carbohydrates": 22.0,
            "notes": "Sangat kaya zat besi heme dan vitamin B12 dari hati sapi untuk mencegah anemia, berpadu potasium kentang dan antioksidan alami dari rempah cabai merah."
        }
    },
    {
        "recipeNumber": 193,
        "title": "193. Kue Nastar Keju Klasik (Nusantara)",
        "name": "Kue Nastar Keju Klasik",
        "slug": "kue-nastar-keju",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 60,
        "cookTimeMinutes": 35,
        "servings": 8,
        "difficulty": "MEDIUM",
        "spicinessLevel": 0,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """193. Kue Nastar Keju Klasik (Nusantara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Adonan Kulit Nastar:
150g Mentega butter berkualitas (Wijsman / salted butter)
100g Margarin
50g Gula halus (ayak)
2 butir Kuning telur ayam
50g Susu bubuk full cream
50g Tepung maizena
350g Tepung terigu protein rendah (diayak)
50g Keju edam tua atau keju parmesan (parut halus)
Bahan Selai Nanas Isian:
1 kg Nanas madu atau nanas palembang (kupas, buang mata, parut halus)
200g Gula pasir (sesuaikan tingkat kemanisan nanas)
4 butir Cengkih utuh
3 cm Kayu manis batangan
1/4 sdt Garam halus
Bahan Olesan Mengilap & Taburan:
2 butir Kuning telur ayam omega (kuning cerah)
1 sdm Minyak goreng
1 sdt Kental manis putih
50g Keju cheddar parut halus untuk taburan atas
Langkah-Langkah Pembuatan:
Membuat Selai Nanas: Masak parutan nanas bersama kayu manis dan cengkih di atas wajan dengan api sedang hingga airnya menyusut banyak. Tambahkan gula pasir dan sedikit garam. Kecilkan api, aduk terus tanpa henti hingga selai mengental pekat, berwarna cokelat keemasan, liat, dan mudah dipulung. Dinginkan, lalu bentuk menjadi bulatan-bulatan kecil seberat 4 gram.
Membuat Adonan Kulit: Kocok mentega butter, margarin, dan gula halus menggunakan mixer kecepatan rendah selama 1-2 menit saja (jangan terlalu lama agar nastar tidak melebar saat dipanggang). Masukkan kuning telur satu per satu sambil diaduk rata. Masukkan keju edam parut, aduk rata.
Mencampurkan Bahan Kering: Masukkan tepung terigu, maizena, dan susu bubuk yang telah diayak. Aduk menggunakan spatula atau sendok kayu hingga adonan tercampur rata, lembut, dan tidak lengket di tangan.
Membentuk Nastar: Ambil sekitar 7-8 gram adonan kulit, bulatkan lalu pipihkan. Letakkan bulatan selai nanas di tengahnya. Rapatkan kulit dan bulatkan kembali hingga permukaan mulus tanpa retakan. Susun di atas loyang yang telah diolesi tipis margarin.
Memanggang Tahap Pertama: Panaskan oven pada suhu 140°C. Panggang nastar selama 20-25 menit hingga setengah matang dan kokoh. Keluarkan loyang dan biarkan nastar dingin pada suhu ruang.
Mengoles dan Menaburi Keju: Campurkan bahan olesan (kuning telur, minyak, kental manis). Olesi permukaan nastar dingin dengan kuas halus sebanyak 2 kali olesan agar warnanya kuning mengilap sempurna. Beri taburan keju cheddar parut di atasnya.
Memanggang Tahap Akhir: Panggang kembali ke dalam oven dengan suhu 140°C selama 10-15 menit hingga permukaan kuning keemasan matang cantik dan renyah lumer. Angkat dan dinginkan sebelum disimpan dalam toples kedap udara.
Nutrisi (Per 3 Butir Kue): Kalori 140 kkal | Protein 2g | Lemak 7g | Karbohidrat 17g. Kue kering ikonik hari raya dengan kelezatan mentega butter kaya vitamin A dan D, serta enzim bromelain dan serat alami dari buah nanas asli.""",
        "ingredientGroups": [
            {
                "name": "Bahan Adonan Kulit Nastar",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "150g Mentega butter berkualitas (Wijsman)", "amount": 150.0, "unit": "g", "name": "Mentega butter", "notes": "berkualitas", "orderIndex": 1},
                    {"rawText": "100g Margarin", "amount": 100.0, "unit": "g", "name": "Margarin", "notes": None, "orderIndex": 2},
                    {"rawText": "50g Gula halus (ayak)", "amount": 50.0, "unit": "g", "name": "Gula halus", "notes": "ayak", "orderIndex": 3},
                    {"rawText": "2 butir Kuning telur ayam", "amount": 2.0, "unit": "butir", "name": "Kuning telur ayam", "notes": None, "orderIndex": 4},
                    {"rawText": "50g Susu bubuk full cream", "amount": 50.0, "unit": "g", "name": "Susu bubuk full cream", "notes": None, "orderIndex": 5},
                    {"rawText": "50g Tepung maizena", "amount": 50.0, "unit": "g", "name": "Tepung maizena", "notes": None, "orderIndex": 6},
                    {"rawText": "350g Tepung terigu protein rendah", "amount": 350.0, "unit": "g", "name": "Tepung terigu protein rendah", "notes": "ayak", "orderIndex": 7},
                    {"rawText": "50g Keju edam tua (parut halus)", "amount": 50.0, "unit": "g", "name": "Keju edam tua", "notes": "parut halus", "orderIndex": 8}
                ]
            },
            {
                "name": "Bahan Selai Nanas Isian",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "1 kg Nanas madu / palembang (parut halus)", "amount": 1.0, "unit": "kg", "name": "Nanas madu", "notes": "parut halus", "orderIndex": 1},
                    {"rawText": "200g Gula pasir", "amount": 200.0, "unit": "g", "name": "Gula pasir", "notes": None, "orderIndex": 2},
                    {"rawText": "4 butir Cengkih utuh", "amount": 4.0, "unit": "butir", "name": "Cengkih utuh", "notes": None, "orderIndex": 3},
                    {"rawText": "3 cm Kayu manis batangan", "amount": 3.0, "unit": "cm", "name": "Kayu manis batangan", "notes": None, "orderIndex": 4},
                    {"rawText": "1/4 sdt Garam halus", "amount": 0.25, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Olesan Mengilap & Taburan",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "2 butir Kuning telur ayam omega", "amount": 2.0, "unit": "butir", "name": "Kuning telur ayam omega", "notes": None, "orderIndex": 1},
                    {"rawText": "1 sdm Minyak goreng", "amount": 1.0, "unit": "sdm", "name": "Minyak goreng", "notes": None, "orderIndex": 2},
                    {"rawText": "1 sdt Kental manis putih", "amount": 1.0, "unit": "sdt", "name": "Kental manis putih", "notes": None, "orderIndex": 3},
                    {"rawText": "50g Keju cheddar parut halus", "amount": 50.0, "unit": "g", "name": "Keju cheddar", "notes": "parut halus untuk taburan", "orderIndex": 4}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Selai Nanas", "instruction": "Masak parutan nanas bersama kayu manis dan cengkih di atas wajan dengan api sedang hingga airnya menyusut banyak. Tambahkan gula pasir dan sedikit garam. Kecilkan api, aduk terus tanpa henti hingga selai mengental pekat, liat, dan mudah dipulung. Bentuk bulatan kecil 4 gram.", "rawText": "Membuat Selai Nanas: Masak parutan nanas bersama kayu manis dan cengkih di atas wajan dengan api sedang hingga airnya menyusut banyak. Tambahkan gula pasir dan sedikit garam. Kecilkan api, aduk terus tanpa henti hingga selai mengental pekat, liat, dan mudah dipulung. Bentuk bulatan kecil 4 gram."},
            {"stepNumber": 2, "title": "Membuat Adonan Kulit", "instruction": "Kocok mentega butter, margarin, dan gula halus menggunakan mixer kecepatan rendah selama 1-2 menit saja. Masukkan kuning telur satu per satu sambil diaduk rata. Masukkan keju edam parut, aduk rata.", "rawText": "Membuat Adonan Kulit: Kocok mentega butter, margarin, dan gula halus menggunakan mixer kecepatan rendah selama 1-2 menit saja. Masukkan kuning telur satu per satu sambil diaduk rata. Masukkan keju edam parut, aduk rata."},
            {"stepNumber": 3, "title": "Mencampurkan Bahan Kering", "instruction": "Masukkan tepung terigu, maizena, dan susu bubuk yang telah diayak. Aduk menggunakan spatula hingga adonan tercampur rata, lembut, dan tidak lengket di tangan.", "rawText": "Mencampurkan Bahan Kering: Masukkan tepung terigu, maizena, dan susu bubuk yang telah diayak. Aduk menggunakan spatula hingga adonan tercampur rata, lembut, dan tidak lengket di tangan."},
            {"stepNumber": 4, "title": "Membentuk Nastar", "instruction": "Ambil sekitar 7-8 gram adonan kulit, bulatkan lalu pipihkan. Letakkan bulatan selai nanas di tengahnya. Rapatkan kulit dan bulatkan kembali hingga permukaan mulus tanpa retakan. Susun di atas loyang.", "rawText": "Membentuk Nastar: Ambil sekitar 7-8 gram adonan kulit, bulatkan lalu pipihkan. Letakkan bulatan selai nanas di tengahnya. Rapatkan kulit dan bulatkan kembali hingga permukaan mulus tanpa retakan. Susun di atas loyang."},
            {"stepNumber": 5, "title": "Memanggang Tahap Pertama", "instruction": "Panaskan oven pada suhu 140°C. Panggang nastar selama 20-25 menit hingga setengah matang dan kokoh. Keluarkan loyang dan biarkan nastar dingin pada suhu ruang.", "rawText": "Memanggang Tahap Pertama: Panaskan oven pada suhu 140°C. Panggang nastar selama 20-25 menit hingga setengah matang dan kokoh. Keluarkan loyang dan biarkan nastar dingin pada suhu ruang."},
            {"stepNumber": 6, "title": "Mengoles dan Menaburi Keju", "instruction": "Campurkan bahan olesan (kuning telur, minyak, kental manis). Olesi permukaan nastar dingin dengan kuas halus sebanyak 2 kali olesan agar warnanya kuning mengilap sempurna. Beri taburan keju cheddar parut di atasnya.", "rawText": "Mengoles dan Menaburi Keju: Campurkan bahan olesan (kuning telur, minyak, kental manis). Olesi permukaan nastar dingin dengan kuas halus sebanyak 2 kali olesan agar warnanya kuning mengilap sempurna. Beri taburan keju cheddar parut di atasnya."},
            {"stepNumber": 7, "title": "Memanggang Tahap Akhir", "instruction": "Panggang kembali ke dalam oven dengan suhu 140°C selama 10-15 menit hingga permukaan kuning keemasan matang cantik dan renyah lumer. Angkat dan dinginkan sebelum disimpan dalam toples.", "rawText": "Memanggang Tahap Akhir: Panggang kembali ke dalam oven dengan suhu 140°C selama 10-15 menit hingga permukaan kuning keemasan matang cantik dan renyah lumer. Angkat dan dinginkan sebelum disimpan dalam toples."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per 3 Butir Kue): Kalori 140 kkal | Protein 2g | Lemak 7g | Karbohidrat 17g. Kue kering ikonik hari raya dengan kelezatan mentega butter kaya vitamin A dan D, serta enzim bromelain dan serat alami dari buah nanas asli.",
            "serving": "Per 3 Butir Kue",
            "calories": 140,
            "protein": 2.0,
            "fat": 7.0,
            "carbohydrates": 17.0,
            "notes": "Kue kering ikonik hari raya dengan kelezatan mentega butter kaya vitamin A dan D, serta enzim bromelain dan serat alami dari buah nanas asli."
        }
    },
    {
        "recipeNumber": 194,
        "title": "194. Kastengel Keju Edam Renyah (Nusantara)",
        "name": "Kastengel Keju Edam Renyah",
        "slug": "kastengel-keju-edam",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 40,
        "cookTimeMinutes": 35,
        "servings": 8,
        "difficulty": "MEDIUM",
        "spicinessLevel": 0,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """194. Kastengel Keju Edam Renyah (Nusantara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Adonan Kastengel:
175g Mentega butter dingin
100g Margarin berkualitas
2 butir Kuning telur ayam
150g Keju edam tua (parut halus, angin-anginkan agar kering renyah)
50g Keju parmesan bubuk (untuk aroma gurih umami khas)
300g Tepung terigu protein rendah (diayak)
50g Tepung maizena
30g Susu bubuk full cream
Bahan Olesan & Topping:
2 butir Kuning telur ayam
1 sdm Minyak sayur
100g Keju cheddar parut panjang untuk taburan atas
Langkah-Langkah Pembuatan:
Mengocok Mentega dan Telur: Kocok mentega butter dingin dan margarin menggunakan mixer kecepatan rendah selama 1 menit hingga lembut tercampur. Masukkan kuning telur, kocok rata sebentar saja.
Memasukkan Keju Tua: Masukkan keju edam parut kering dan keju parmesan bubuk ke dalam adonan mentega. Aduk rata menggunakan spatula karet hingga butiran keju tersebar merata.
Memasukkan Tepung: Masukkan tepung terigu, tepung maizena, dan susu bubuk yang sudah diayak. Aduk balik perlahan menggunakan spatula hingga adonan kalis dan bisa dipulung atau digilas (jangan diuleni dengan tangan hangat agar adonan tidak keras).
Mencetak Kastengel: Gilas adonan di antara dua lembar plastik dengan ketebalan sekitar 0.8 cm. Potong-potong adonan memanjang dengan ukuran 1x3 cm menggunakan pemotong kue kastengel atau pisau tajam. Tata potongan adonan di atas loyang kue kering bersemir tipis margarin.
Mengoles dan Menaburi Keju: Campurkan kuning telur dengan minyak sayur. Olesi seluruh permukaan adonan dengan kuas. Taburi keju cheddar parut panjang secara melimpah di atasnya, tekan sedikit agar keju menempel erat.
Memanggang: Panaskan oven hingga suhu 140-150°C. Panggang kastengel selama 30-35 menit hingga kue berwarna kuning keemasan, keju taburan kering renyah, dan bagian bawah kue matang sempurna.
Penyajian: Angkat loyang dari oven dan biarkan kastengel dingin sempurna di suhu ruang hingga teksturnya menjadi sangat renyah dan gurih sebelum dimasukkan ke dalam toples kaca kedap udara.
Nutrisi (Per 3 Batang Kue): Kalori 160 kkal | Protein 4g | Lemak 10g | Karbohidrat 14g. Sumber kalsium dan protein susu yang melimpah dari fermentasi keju edam asli, menghadirkan kerenyahan gurih otentik kue hari raya.""",
        "ingredientGroups": [
            {
                "name": "Bahan Adonan Kastengel",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "175g Mentega butter dingin", "amount": 175.0, "unit": "g", "name": "Mentega butter", "notes": "dingin", "orderIndex": 1},
                    {"rawText": "100g Margarin berkualitas", "amount": 100.0, "unit": "g", "name": "Margarin", "notes": "berkualitas", "orderIndex": 2},
                    {"rawText": "2 butir Kuning telur ayam", "amount": 2.0, "unit": "butir", "name": "Kuning telur ayam", "notes": None, "orderIndex": 3},
                    {"rawText": "150g Keju edam tua (parut halus, anginkan)", "amount": 150.0, "unit": "g", "name": "Keju edam tua", "notes": "parut halus", "orderIndex": 4},
                    {"rawText": "50g Keju parmesan bubuk", "amount": 50.0, "unit": "g", "name": "Keju parmesan bubuk", "notes": None, "orderIndex": 5},
                    {"rawText": "300g Tepung terigu protein rendah", "amount": 300.0, "unit": "g", "name": "Tepung terigu protein rendah", "notes": "ayak", "orderIndex": 6},
                    {"rawText": "50g Tepung maizena", "amount": 50.0, "unit": "g", "name": "Tepung maizena", "notes": None, "orderIndex": 7},
                    {"rawText": "30g Susu bubuk full cream", "amount": 30.0, "unit": "g", "name": "Susu bubuk full cream", "notes": None, "orderIndex": 8}
                ]
            },
            {
                "name": "Bahan Olesan & Topping",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "2 butir Kuning telur ayam", "amount": 2.0, "unit": "butir", "name": "Kuning telur ayam", "notes": None, "orderIndex": 1},
                    {"rawText": "1 sdm Minyak sayur", "amount": 1.0, "unit": "sdm", "name": "Minyak sayur", "notes": None, "orderIndex": 2},
                    {"rawText": "100g Keju cheddar parut panjang", "amount": 100.0, "unit": "g", "name": "Keju cheddar", "notes": "parut panjang untuk taburan", "orderIndex": 3}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Mengocok Mentega dan Telur", "instruction": "Kocok mentega butter dingin dan margarin menggunakan mixer kecepatan rendah selama 1 menit hingga lembut tercampur. Masukkan kuning telur, kocok rata sebentar saja.", "rawText": "Mengocok Mentega dan Telur: Kocok mentega butter dingin dan margarin menggunakan mixer kecepatan rendah selama 1 menit hingga lembut tercampur. Masukkan kuning telur, kocok rata sebentar saja."},
            {"stepNumber": 2, "title": "Memasukkan Keju Tua", "instruction": "Masukkan keju edam parut kering dan keju parmesan bubuk ke dalam adonan mentega. Aduk rata menggunakan spatula karet hingga butiran keju tersebar merata.", "rawText": "Memasukkan Keju Tua: Masukkan keju edam parut kering dan keju parmesan bubuk ke dalam adonan mentega. Aduk rata menggunakan spatula karet hingga butiran keju tersebar merata."},
            {"stepNumber": 3, "title": "Memasukkan Tepung", "instruction": "Masukkan tepung terigu, tepung maizena, dan susu bubuk yang sudah diayak. Aduk balik perlahan menggunakan spatula hingga adonan kalis dan bisa dipulung atau digilas.", "rawText": "Memasukkan Tepung: Masukkan tepung terigu, tepung maizena, dan susu bubuk yang sudah diayak. Aduk balik perlahan menggunakan spatula hingga adonan kalis dan bisa dipulung atau digilas."},
            {"stepNumber": 4, "title": "Mencetak Kastengel", "instruction": "Gilas adonan di antara dua lembar plastik dengan ketebalan sekitar 0.8 cm. Potong-potong adonan memanjang dengan ukuran 1x3 cm menggunakan pemotong kue kastengel atau pisau tajam. Tata potongan adonan di atas loyang.", "rawText": "Mencetak Kastengel: Gilas adonan di antara dua lembar plastik dengan ketebalan sekitar 0.8 cm. Potong-potong adonan memanjang dengan ukuran 1x3 cm menggunakan pemotong kue kastengel atau pisau tajam. Tata potongan adonan di atas loyang."},
            {"stepNumber": 5, "title": "Mengoles dan Menaburi Keju", "instruction": "Campurkan kuning telur dengan minyak sayur. Olesi seluruh permukaan adonan dengan kuas. Taburi keju cheddar parut panjang secara melimpah di atasnya, tekan sedikit agar menempel erat.", "rawText": "Mengoles dan Menaburi Keju: Campurkan kuning telur dengan minyak sayur. Olesi seluruh permukaan adonan dengan kuas. Taburi keju cheddar parut panjang secara melimpah di atasnya, tekan sedikit agar menempel erat."},
            {"stepNumber": 6, "title": "Memanggang", "instruction": "Panaskan oven hingga suhu 140-150°C. Panggang kastengel selama 30-35 menit hingga kue berwarna kuning keemasan, keju taburan kering renyah, dan bagian bawah matang sempurna.", "rawText": "Memanggang: Panaskan oven hingga suhu 140-150°C. Panggang kastengel selama 30-35 menit hingga kue berwarna kuning keemasan, keju taburan kering renyah, dan bagian bawah matang sempurna."},
            {"stepNumber": 7, "title": "Penyajian", "instruction": "Angkat loyang dari oven dan biarkan kastengel dingin sempurna di suhu ruang hingga teksturnya menjadi sangat renyah dan gurih sebelum dimasukkan ke dalam toples kedap udara.", "rawText": "Penyajian: Angkat loyang dari oven dan biarkan kastengel dingin sempurna di suhu ruang hingga teksturnya menjadi sangat renyah dan gurih sebelum dimasukkan ke dalam toples kedap udara."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per 3 Batang Kue): Kalori 160 kkal | Protein 4g | Lemak 10g | Karbohidrat 14g. Sumber kalsium dan protein susu yang melimpah dari fermentasi keju edam asli, menghadirkan kerenyahan gurih otentik kue hari raya.",
            "serving": "Per 3 Batang Kue",
            "calories": 160,
            "protein": 4.0,
            "fat": 10.0,
            "carbohydrates": 14.0,
            "notes": "Sumber kalsium dan protein susu yang melimpah dari fermentasi keju edam asli, menghadirkan kerenyahan gurih otentik kue hari raya."
        }
    },
    {
        "recipeNumber": 195,
        "title": "195. Kue Putri Salju Pandan Mede (Nusantara)",
        "name": "Kue Putri Salju Pandan Mede",
        "slug": "kue-putri-salju",
        "scope": "INDONESIA",
        "origin": "Jawa Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 40,
        "cookTimeMinutes": 30,
        "servings": 8,
        "difficulty": "MEDIUM",
        "spicinessLevel": 0,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """195. Kue Putri Salju Pandan Mede (Nusantara)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Adonan Putri Salju:
150g Kacang mete (sangrai hingga matang harum kecokelatan, haluskan/blender halus)
150g Mentega butter berkualitas
100g Margarin
80g Gula halus (ayak)
2 butir Kuning telur ayam
300g Tepung terigu protein rendah (diayak)
50g Tepung maizena
30g Susu bubuk vanili
1 sdm Pasta pandan suji murni (memberi warna hijau lembut dan wangi alami)
1/4 sdt Garam halus
Bahan Taburan Salju Dingin:
150g Gula donat dingin (gula halus salju icing dingin)
50g Susu bubuk full cream vanili (aduk rata bersama gula dingin)
Langkah-Langkah Pembuatan:
Menyiapkan Kacang Mete: Sangrai kacang mete hingga matang harum keemasan. Dinginkan, lalu blender atau giling hingga bertekstur bubuk halus berminyak.
Mengocok Mentega dan Telur: Kocok mentega butter, margarin, gula halus, dan garam menggunakan mixer kecepatan rendah selama 1.5 menit hingga lembut. Masukkan kuning telur dan pasta pandan suji, kocok kembali hingga tercampur rata dan berwarna hijau muda harum.
Memasukkan Bubuk Mete dan Tepung: Masukkan kacang mete bubuk, aduk rata dengan spatula. Tambahkan tepung terigu, tepung maizena, dan susu bubuk yang telah diayak. Aduk balik menggunakan spatula hingga adonan menyatu lembut dan mudah dibentuk.
Mencetak Bentuk Bulan Sabit: Gilas adonan di antara dua plastik dengan ketebalan 0.7 cm. Cetak menggunakan cetakan kue putri salju berbentuk bulan sabit. Tata di atas loyang yang telah beralaskan baking paper.
Memanggang: Panaskan oven hingga suhu 140°C. Panggang kue selama 25-30 menit hingga matang renyah (permukaan tidak gosong dan bagian dasar mulai kecokelatan).
Menyelimuti dengan Salju: Angkat kue dari oven. Saat kue masih dalam kondisi hangat suam-suam kuku, gulingkan segera ke dalam campuran gula donat dingin dan susu bubuk (kondisi hangat membuat gula menempel sempurna dan membentuk lapisan salju tebal).
Penyajian: Tata kue putri salju pandan mede di dalam toples, lalu taburi lagi sedikit sisa gula salju di atasnya. Tutup rapat toples.
Nutrisi (Per 3 Butir Kue): Kalori 150 kkal | Protein 3g | Lemak 9g | Karbohidrat 15g. Gurih lezat lemak tak jenuh dari kacang mete alami dipadukan aroma daun pandan dan sensasi dingin manis gula salju di lidah.""",
        "ingredientGroups": [
            {
                "name": "Bahan Adonan Putri Salju",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "150g Kacang mete (sangrai, blender halus)", "amount": 150.0, "unit": "g", "name": "Kacang mete", "notes": "sangrai, blender halus", "orderIndex": 1},
                    {"rawText": "150g Mentega butter berkualitas", "amount": 150.0, "unit": "g", "name": "Mentega butter", "notes": "berkualitas", "orderIndex": 2},
                    {"rawText": "100g Margarin", "amount": 100.0, "unit": "g", "name": "Margarin", "notes": None, "orderIndex": 3},
                    {"rawText": "80g Gula halus (ayak)", "amount": 80.0, "unit": "g", "name": "Gula halus", "notes": "ayak", "orderIndex": 4},
                    {"rawText": "2 butir Kuning telur ayam", "amount": 2.0, "unit": "butir", "name": "Kuning telur ayam", "notes": None, "orderIndex": 5},
                    {"rawText": "300g Tepung terigu protein rendah", "amount": 300.0, "unit": "g", "name": "Tepung terigu protein rendah", "notes": "ayak", "orderIndex": 6},
                    {"rawText": "50g Tepung maizena", "amount": 50.0, "unit": "g", "name": "Tepung maizena", "notes": None, "orderIndex": 7},
                    {"rawText": "30g Susu bubuk vanili", "amount": 30.0, "unit": "g", "name": "Susu bubuk vanili", "notes": None, "orderIndex": 8},
                    {"rawText": "1 sdm Pasta pandan suji murni", "amount": 1.0, "unit": "sdm", "name": "Pasta pandan suji", "notes": "murni alami", "orderIndex": 9},
                    {"rawText": "1/4 sdt Garam halus", "amount": 0.25, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 10}
                ]
            },
            {
                "name": "Bahan Taburan Salju Dingin",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "150g Gula donat dingin (icing salju dingin)", "amount": 150.0, "unit": "g", "name": "Gula donat dingin", "notes": "icing salju dingin", "orderIndex": 1},
                    {"rawText": "50g Susu bubuk full cream vanili", "amount": 50.0, "unit": "g", "name": "Susu bubuk full cream vanili", "notes": None, "orderIndex": 2}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menyiapkan Kacang Mete", "instruction": "Sangrai kacang mete hingga matang harum keemasan. Dinginkan, lalu blender atau giling hingga bertekstur bubuk halus berminyak.", "rawText": "Menyiapkan Kacang Mete: Sangrai kacang mete hingga matang harum keemasan. Dinginkan, lalu blender atau giling hingga bertekstur bubuk halus berminyak."},
            {"stepNumber": 2, "title": "Mengocok Mentega dan Telur", "instruction": "Kocok mentega butter, margarin, gula halus, dan garam menggunakan mixer kecepatan rendah selama 1.5 menit hingga lembut. Masukkan kuning telur dan pasta pandan suji, kocok kembali hingga tercampur rata.", "rawText": "Mengocok Mentega dan Telur: Kocok mentega butter, margarin, gula halus, dan garam menggunakan mixer kecepatan rendah selama 1.5 menit hingga lembut. Masukkan kuning telur dan pasta pandan suji, kocok kembali hingga tercampur rata."},
            {"stepNumber": 3, "title": "Memasukkan Bubuk Mete dan Tepung", "instruction": "Masukkan kacang mete bubuk, aduk rata dengan spatula. Tambahkan tepung terigu, tepung maizena, dan susu bubuk yang telah diayak. Aduk balik menggunakan spatula hingga adonan menyatu lembut dan mudah dibentuk.", "rawText": "Memasukkan Bubuk Mete dan Tepung: Masukkan kacang mete bubuk, aduk rata dengan spatula. Tambahkan tepung terigu, tepung maizena, dan susu bubuk yang telah diayak. Aduk balik menggunakan spatula hingga adonan menyatu lembut dan mudah dibentuk."},
            {"stepNumber": 4, "title": "Mencetak Bentuk Bulan Sabit", "instruction": "Gilas adonan di antara dua plastik dengan ketebalan 0.7 cm. Cetak menggunakan cetakan kue putri salju berbentuk bulan sabit. Tata di atas loyang yang beralaskan baking paper.", "rawText": "Mencetak Bentuk Bulan Sabit: Gilas adonan di antara dua plastik dengan ketebalan 0.7 cm. Cetak menggunakan cetakan kue putri salju berbentuk bulan sabit. Tata di atas loyang yang beralaskan baking paper."},
            {"stepNumber": 5, "title": "Memanggang", "instruction": "Panaskan oven hingga suhu 140°C. Panggang kue selama 25-30 menit hingga matang renyah, permukaan tidak gosong dan dasar kue mulai kecokelatan.", "rawText": "Memanggang: Panaskan oven hingga suhu 140°C. Panggang kue selama 25-30 menit hingga matang renyah, permukaan tidak gosong dan dasar kue mulai kecokelatan."},
            {"stepNumber": 6, "title": "Menyelimuti dengan Salju", "instruction": "Angkat kue dari oven. Saat kue masih dalam kondisi hangat suam kuku, gulingkan segera ke dalam campuran gula donat dingin dan susu bubuk agar menempel sempurna membentuk lapisan salju tebal.", "rawText": "Menyelimuti dengan Salju: Angkat kue dari oven. Saat kue masih dalam kondisi hangat suam kuku, gulingkan segera ke dalam campuran gula donat dingin dan susu bubuk agar menempel sempurna membentuk lapisan salju tebal."},
            {"stepNumber": 7, "title": "Penyajian", "instruction": "Tata kue putri salju pandan mede di dalam toples, lalu taburi lagi sedikit sisa gula salju di atasnya. Tutup rapat toples kedap udara.", "rawText": "Penyajian: Tata kue putri salju pandan mede di dalam toples, lalu taburi lagi sedikit sisa gula salju di atasnya. Tutup rapat toples kedap udara."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per 3 Butir Kue): Kalori 150 kkal | Protein 3g | Lemak 9g | Karbohidrat 15g. Gurih lezat lemak tak jenuh dari kacang mete alami dipadukan aroma daun pandan dan sensasi dingin manis gula salju di lidah.",
            "serving": "Per 3 Butir Kue",
            "calories": 150,
            "protein": 3.0,
            "fat": 9.0,
            "carbohydrates": 15.0,
            "notes": "Gurih lezat lemak tak jenuh dari kacang mete alami dipadukan aroma daun pandan dan sensasi dingin manis gula salju di lidah."
        }
    },
    {
        "recipeNumber": 196,
        "title": "196. Bubur Kampiun Khas Minang (Sumatera Barat)",
        "name": "Bubur Kampiun Minang",
        "slug": "bubur-kampiun-minang",
        "scope": "INDONESIA",
        "origin": "Sumatera Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 45,
        "cookTimeMinutes": 40,
        "servings": 5,
        "difficulty": "HARD",
        "spicinessLevel": 0,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """196. Bubur Kampiun Khas Minang (Sumatera Barat)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Bubur Ketan Hitam:
150g Beras ketan hitam (rendam air minimal 4 jam)
800 ml Air bersih
80g Gula pasir / gula merah aren
1 lembar Daun pandan (ikat simpul)
1/4 sdt Garam
Bahan Kolak Pisang Ubi:
3 buah Pisang kepok kuning (potong serong)
1 buah Ubi jalar merah (kupas, potong dadu)
400 ml Santan sedang
100g Gula merah aren (sisir)
1 lembar Daun pandan
1/4 sdt Garam
Bahan Bubur Sumsum Lembut:
100g Tepung beras
700 ml Santan sedang
2 lembar Daun pandan
1/2 sdt Garam halus
Bahan Bubur Candil Ketan:
100g Tepung ketan putih
75 ml Air hangat suam kuku
1/4 sdt Garam
Kuah Candil: 250 ml air, 70g gula merah aren, 1 sdm tepung tapioka (larutkan air)
Bahan Ketan Putih Kukus:
150g Beras ketan putih (kukus matang bersama 100 ml santan dan sedikit garam)
Langkah-Langkah Pembuatan:
Memasak Bubur Ketan Hitam: Rebus beras ketan hitam yang telah direndam bersama air dan daun pandan hingga merekah dan empuk kental. Masukkan gula pasir dan garam, aduk rata hingga matang legit. Sisihkan.
Membuat Kolak Pisang Ubi: Rebus ubi jalar dan pisang dalam santan sedang bersama gula merah aren, daun pandan, dan garam hingga ubi empuk dan kuah meresap wangi manis. Angkat dan sisihkan.
Membuat Bubur Candil Ketan: Campurkan tepung ketan, garam, dan air hangat, uleni hingga kalis lalu bentuk bulatan kecil sebesar kelereng. Didihkan air kuah gula merah dan daun pandan, masukkan bulatan ketan. Masak hingga mengapung. Masukkan larutan tapioka, aduk hingga kuah kinca mengental pekat.
Membuat Bubur Sumsum: Campurkan tepung beras, santan, daun pandan, dan garam dalam panci. Aduk larut tanpa gerindil. Masak di atas api sedang cenderung kecil sambil terus diaduk cepat hingga mengental lembut meletup-letup.
Mengukus Ketan Putih: Pastikan ketan putih gurih kukus telah matang pulen beralaskan daun pandan.
Penyajian: Siapkan mangkuk saji saji. Sendokkan sedikit ketan putih kukus di dasar mangkuk. Beri sesendok bubur sumsum lembut, sesendok bubur ketan hitam legit, sesendok bubur candil kenyal, dan sesendok kolak pisang ubi. Siram dengan sedikit kuah santan kental gurih dan kuah kinca gula merah. Sajikan hangat atau dingin sebagai takjil legendaris buka puasa.
Nutrisi (Per Porsi Komplit): Kalori 380 kkal | Protein 6g | Lemak 11g | Karbohidrat 68g. Paduan karbohidrat kompleks kaya serat antosianin dari ketan hitam, kalium pisang, serta asam lemak sehat santan murni sebagai pemulih energi tubuh seketika saat berbuka puasa.""",
        "ingredientGroups": [
            {
                "name": "Bahan Bubur Ketan Hitam",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "150g Beras ketan hitam (rendam 4 jam)", "amount": 150.0, "unit": "g", "name": "Beras ketan hitam", "notes": "rendam 4 jam", "orderIndex": 1},
                    {"rawText": "800 ml Air bersih", "amount": 800.0, "unit": "ml", "name": "Air bersih", "notes": None, "orderIndex": 2},
                    {"rawText": "80g Gula pasir atau aren", "amount": 80.0, "unit": "g", "name": "Gula pasir atau aren", "notes": None, "orderIndex": 3},
                    {"rawText": "1 lembar Daun pandan", "amount": 1.0, "unit": "lembar", "name": "Daun pandan", "notes": "ikat simpul", "orderIndex": 4},
                    {"rawText": "1/4 sdt Garam", "amount": 0.25, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 5}
                ]
            },
            {
                "name": "Bahan Kolak Pisang Ubi",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "3 buah Pisang kepok kuning (potong serong)", "amount": 3.0, "unit": "buah", "name": "Pisang kepok kuning", "notes": "potong serong", "orderIndex": 1},
                    {"rawText": "1 buah Ubi jalar merah (potong dadu)", "amount": 1.0, "unit": "buah", "name": "Ubi jalar merah", "notes": "potong dadu", "orderIndex": 2},
                    {"rawText": "400 ml Santan sedang", "amount": 400.0, "unit": "ml", "name": "Santan sedang", "notes": None, "orderIndex": 3},
                    {"rawText": "100g Gula merah aren (sisir)", "amount": 100.0, "unit": "g", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 4},
                    {"rawText": "1 lembar Daun pandan", "amount": 1.0, "unit": "lembar", "name": "Daun pandan", "notes": None, "orderIndex": 5},
                    {"rawText": "1/4 sdt Garam", "amount": 0.25, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 6}
                ]
            },
            {
                "name": "Bahan Bubur Sumsum Lembut",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "100g Tepung beras", "amount": 100.0, "unit": "g", "name": "Tepung beras", "notes": None, "orderIndex": 1},
                    {"rawText": "700 ml Santan sedang", "amount": 700.0, "unit": "ml", "name": "Santan sedang", "notes": None, "orderIndex": 2},
                    {"rawText": "2 lembar Daun pandan", "amount": 2.0, "unit": "lembar", "name": "Daun pandan", "notes": None, "orderIndex": 3},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 4}
                ]
            },
            {
                "name": "Bahan Candil Ketan & Ketan Putih Kukus",
                "orderIndex": 4,
                "ingredients": [
                    {"rawText": "100g Tepung ketan putih", "amount": 100.0, "unit": "g", "name": "Tepung ketan putih", "notes": None, "orderIndex": 1},
                    {"rawText": "75 ml Air hangat", "amount": 75.0, "unit": "ml", "name": "Air hangat", "notes": None, "orderIndex": 2},
                    {"rawText": "70g Gula merah aren", "amount": 70.0, "unit": "g", "name": "Gula merah aren", "notes": "untuk kuah kinca", "orderIndex": 3},
                    {"rawText": "1 sdm Tepung tapioka", "amount": 1.0, "unit": "sdm", "name": "Tepung tapioka", "notes": "pengental kinca", "orderIndex": 4},
                    {"rawText": "150g Beras ketan putih (kukus)", "amount": 150.0, "unit": "g", "name": "Beras ketan putih", "notes": "kukus matang gurih", "orderIndex": 5}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Memasak Bubur Ketan Hitam", "instruction": "Rebus beras ketan hitam yang telah direndam bersama air dan daun pandan hingga merekah dan empuk kental. Masukkan gula pasir dan garam, aduk rata hingga matang legit. Sisihkan.", "rawText": "Memasak Bubur Ketan Hitam: Rebus beras ketan hitam yang telah direndam bersama air dan daun pandan hingga merekah dan empuk kental. Masukkan gula pasir dan garam, aduk rata hingga matang legit. Sisihkan."},
            {"stepNumber": 2, "title": "Membuat Kolak Pisang Ubi", "instruction": "Rebus ubi jalar dan pisang dalam santan sedang bersama gula merah aren, daun pandan, dan garam hingga ubi empuk dan kuah meresap wangi manis. Angkat dan sisihkan.", "rawText": "Membuat Kolak Pisang Ubi: Rebus ubi jalar dan pisang dalam santan sedang bersama gula merah aren, daun pandan, dan garam hingga ubi empuk dan kuah meresap wangi manis. Angkat dan sisihkan."},
            {"stepNumber": 3, "title": "Membuat Bubur Candil Ketan", "instruction": "Campurkan tepung ketan, garam, dan air hangat, uleni hingga kalis lalu bentuk bulatan kecil sebesar kelereng. Didihkan air kuah gula merah dan daun pandan, masukkan bulatan ketan. Masak hingga mengapung. Masukkan larutan tapioka, aduk hingga kuah kinca mengental pekat.", "rawText": "Membuat Bubur Candil Ketan: Campurkan tepung ketan, garam, dan air hangat, uleni hingga kalis lalu bentuk bulatan kecil sebesar kelereng. Didihkan air kuah gula merah dan daun pandan, masukkan bulatan ketan. Masak hingga mengapung. Masukkan larutan tapioka, aduk hingga kuah kinca mengental pekat."},
            {"stepNumber": 4, "title": "Membuat Bubur Sumsum", "instruction": "Campurkan tepung beras, santan, daun pandan, dan garam dalam panci. Aduk larut tanpa gerindil. Masak di atas api sedang cenderung kecil sambil terus diaduk cepat hingga mengental lembut meletup-letup.", "rawText": "Membuat Bubur Sumsum: Campurkan tepung beras, santan, daun pandan, dan garam dalam panci. Aduk larut tanpa gerindil. Masak di atas api sedang cenderung kecil sambil terus diaduk cepat hingga mengental lembut meletup-letup."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Tata ketan putih kukus, bubur sumsum, bubur ketan hitam, bubur candil, dan kolak pisang ubi dalam satu mangkuk saji. Siram dengan kuah santan dan kinca gula merah. Sajikan hangat atau dingin.", "rawText": "Penyajian: Tata ketan putih kukus, bubur sumsum, bubur ketan hitam, bubur candil, dan kolak pisang ubi dalam satu mangkuk saji. Siram dengan kuah santan dan kinca gula merah. Sajikan hangat atau dingin."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi Komplit): Kalori 380 kkal | Protein 6g | Lemak 11g | Karbohidrat 68g. Paduan karbohidrat kompleks kaya serat antosianin dari ketan hitam, kalium pisang, serta asam lemak sehat santan murni sebagai pemulih energi tubuh seketika saat berbuka puasa.",
            "serving": "Per Porsi Komplit",
            "calories": 380,
            "protein": 6.0,
            "fat": 11.0,
            "carbohydrates": 68.0,
            "notes": "Paduan karbohidrat kompleks kaya serat antosianin dari ketan hitam, kalium pisang, serta asam lemak sehat santan murni sebagai pemulih energi tubuh seketika saat berbuka puasa."
        }
    },
    {
        "recipeNumber": 197,
        "title": "197. Kolak Biji Salak Ubi Manis Khas Buka Puasa (DKI Jakarta)",
        "name": "Kolak Biji Salak Ubi Manis",
        "slug": "kolak-biji-salak",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 30,
        "cookTimeMinutes": 25,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 0,
        "categorySlug": "kudapan-jajanan-pasar",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """197. Kolak Biji Salak Ubi Manis Khas Buka Puasa (DKI Jakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Bola Biji Salak:
500g Ubi jalar kuning / oranye (kupas, kukus matang empuk, haluskan selagi hangat)
150g Tepung tapioka / sagu tani berkualitas
1 sdm Gula pasir halus
1/2 sdt Garam halus
Bahan Kuah Kinca Gula Aren:
200g Gula merah aren berkualitas (sisir halus)
30g Gula pasir
800 ml Air bersih
2 lembar Daun pandan wangi (ikat simpul)
2 sdm Tepung tapioka (larutkan dengan 3 sdm air dingin untuk mengentalkan kuah)
1/4 sdt Garam
Bahan Kuah Santan Gurih:
300 ml Santan kelapa kental segar
1 lembar Daun pandan
1/2 sdt Garam halus
Langkah-Langkah Pembuatan:
Membuat Adonan Biji Salak: Haluskan ubi jalar kukus selagi masih panas hingga lembut bebas serat kasar. Masukkan tepung tapioka, gula pasir, dan garam. Uleni perlahan dengan tangan hingga adonan kalis, elastis, dan mudah dipulung (jika ubi terlalu kering, bisa ditambah 1-2 sendok makan air matang).
Membentuk Bola Biji Salak: Ambil sedikit adonan, pulung dan bentuk menjadi bulatan lonjong kecil menyerupai biji salak alami (diameter sekitar 1.5 - 2 cm). Tata di atas nampan yang telah ditaburi tipis tepung tapioka agar tidak saling menempel.
Membuat Kuah Gula Aren: Rebus air, gula merah aren sisir, gula pasir, garam, dan daun pandan simpul dalam panci hingga gula larut mendidih. Saring air gula agar terbebas dari kotoran ampas gula aren, lalu masak kembali hingga mendidih.
Merebus Biji Salak: Masukkan bulatan biji salak ke dalam kuah gula aren yang sedang mendidih perlahan. Masak hingga seluruh bola biji salak terapung ke permukaan air (tanda adonan ubi telah matang kenyal sempurna hingga ke tengah). Tuangkan larutan tepung tapioka pengental sambil diaduk cepat hingga kuah kinca berubah menjadi kental pekat dan mengilap. Angkat.
Membuat Kuah Santan: Rebus santan kental bersama garam dan daun pandan simpul di atas api kecil sambil terus diaduk perlahan agar santan tidak pecah. Masak hingga santan harum dan mendidih perlahan. Angkat.
Penyajian: Sendokkan bola biji salak beserta kuah kinca gula aren kental hangat ke dalam mangkuk saji saji. Siramkan 2-3 sendok makan kuah santan gurih putih di atasnya. Sajikan hangat mengepul untuk membatalkan puasa di waktu maghrib.
Nutrisi (Per Porsi): Kalori 260 kkal | Protein 2g | Lemak 6g | Karbohidrat 52g. Karbohidrat alami dan beta-karoten tinggi dari ubi jalar kuning sangat lembut untuk lambung yang kosong setelah berpuasa, memberikan energi instan dengan indeks glikemik seimbang.""",
        "ingredientGroups": [
            {
                "name": "Bahan Bola Biji Salak",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "500g Ubi jalar kuning / oranye (kukus, haluskan)", "amount": 500.0, "unit": "g", "name": "Ubi jalar kuning", "notes": "kukus, haluskan selagi hangat", "orderIndex": 1},
                    {"rawText": "150g Tepung tapioka / sagu tani", "amount": 150.0, "unit": "g", "name": "Tepung tapioka", "notes": "berkualitas", "orderIndex": 2},
                    {"rawText": "1 sdm Gula pasir halus", "amount": 1.0, "unit": "sdm", "name": "Gula pasir halus", "notes": None, "orderIndex": 3},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 4}
                ]
            },
            {
                "name": "Bahan Kuah Kinca Gula Aren",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "200g Gula merah aren berkualitas (sisir)", "amount": 200.0, "unit": "g", "name": "Gula merah aren", "notes": "sisir", "orderIndex": 1},
                    {"rawText": "30g Gula pasir", "amount": 30.0, "unit": "g", "name": "Gula pasir", "notes": None, "orderIndex": 2},
                    {"rawText": "800 ml Air bersih", "amount": 800.0, "unit": "ml", "name": "Air bersih", "notes": None, "orderIndex": 3},
                    {"rawText": "2 lembar Daun pandan wangi", "amount": 2.0, "unit": "lembar", "name": "Daun pandan wangi", "notes": "ikat simpul", "orderIndex": 4},
                    {"rawText": "2 sdm Tepung tapioka (larutkan air)", "amount": 2.0, "unit": "sdm", "name": "Tepung tapioka", "notes": "pengental", "orderIndex": 5},
                    {"rawText": "1/4 sdt Garam", "amount": 0.25, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 6}
                ]
            },
            {
                "name": "Bahan Kuah Santan Gurih",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "300 ml Santan kelapa kental segar", "amount": 300.0, "unit": "ml", "name": "Santan kelapa kental segar", "notes": None, "orderIndex": 1},
                    {"rawText": "1 lembar Daun pandan", "amount": 1.0, "unit": "lembar", "name": "Daun pandan", "notes": None, "orderIndex": 2},
                    {"rawText": "1/2 sdt Garam halus", "amount": 0.5, "unit": "sdt", "name": "Garam halus", "notes": None, "orderIndex": 3}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Membuat Adonan Biji Salak", "instruction": "Haluskan ubi jalar kukus selagi masih panas hingga lembut bebas serat kasar. Masukkan tepung tapioka, gula pasir, dan garam. Uleni perlahan dengan tangan hingga adonan kalis, elastis, dan mudah dipulung.", "rawText": "Membuat Adonan Biji Salak: Haluskan ubi jalar kukus selagi masih panas hingga lembut bebas serat kasar. Masukkan tepung tapioka, gula pasir, dan garam. Uleni perlahan dengan tangan hingga adonan kalis, elastis, dan mudah dipulung."},
            {"stepNumber": 2, "title": "Membentuk Bola Biji Salak", "instruction": "Ambil sedikit adonan, pulung dan bentuk menjadi bulatan lonjong kecil menyerupai biji salak alami. Tata di atas nampan yang telah ditaburi tipis tepung tapioka agar tidak saling menempel.", "rawText": "Membentuk Bola Biji Salak: Ambil sedikit adonan, pulung dan bentuk menjadi bulatan lonjong kecil menyerupai biji salak alami. Tata di atas nampan yang telah ditaburi tipis tepung tapioka agar tidak saling menempel."},
            {"stepNumber": 3, "title": "Membuat Kuah Gula Aren", "instruction": "Rebus air, gula merah aren sisir, gula pasir, garam, dan daun pandan simpul dalam panci hingga gula larut mendidih. Saring air gula agar bersih, lalu masak kembali hingga mendidih.", "rawText": "Membuat Kuah Gula Aren: Rebus air, gula merah aren sisir, gula pasir, garam, dan daun pandan simpul dalam panci hingga gula larut mendidih. Saring air gula agar bersih, lalu masak kembali hingga mendidih."},
            {"stepNumber": 4, "title": "Merebus Biji Salak", "instruction": "Masukkan bulatan biji salak ke dalam kuah gula aren yang sedang mendidih perlahan. Masak hingga seluruh bola biji salak terapung ke permukaan air. Tuangkan larutan tepung tapioka pengental sambil diaduk cepat hingga kuah kinca berubah menjadi kental pekat dan mengilap.", "rawText": "Merebus Biji Salak: Masukkan bulatan biji salak ke dalam kuah gula aren yang sedang mendidih perlahan. Masak hingga seluruh bola biji salak terapung ke permukaan air. Tuangkan larutan tepung tapioka pengental sambil diaduk cepat hingga kuah kinca berubah menjadi kental pekat dan mengilap."},
            {"stepNumber": 5, "title": "Membuat Kuah Santan", "instruction": "Rebus santan kental bersama garam dan daun pandan simpul di atas api kecil sambil terus diaduk perlahan agar santan tidak pecah. Masak hingga santan harum dan mendidih perlahan. Angkat.", "rawText": "Membuat Kuah Santan: Rebus santan kental bersama garam dan daun pandan simpul di atas api kecil sambil terus diaduk perlahan agar santan tidak pecah. Masak hingga santan harum dan mendidih perlahan. Angkat."},
            {"stepNumber": 6, "title": "Penyajian", "instruction": "Sendokkan bola biji salak beserta kuah kinca gula aren kental hangat ke dalam mangkuk saji. Siramkan 2-3 sendok makan kuah santan gurih putih di atasnya. Sajikan hangat mengepul.", "rawText": "Penyajian: Sendokkan bola biji salak beserta kuah kinca gula aren kental hangat ke dalam mangkuk saji. Siramkan 2-3 sendok makan kuah santan gurih putih di atasnya. Sajikan hangat mengepul."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 260 kkal | Protein 2g | Lemak 6g | Karbohidrat 52g. Karbohidrat alami dan beta-karoten tinggi dari ubi jalar kuning sangat lembut untuk lambung yang kosong setelah berpuasa, memberikan energi instan dengan indeks glikemik seimbang.",
            "serving": "Per Porsi",
            "calories": 260,
            "protein": 2.0,
            "fat": 6.0,
            "carbohydrates": 52.0,
            "notes": "Karbohidrat alami dan beta-karoten tinggi dari ubi jalar kuning sangat lembut untuk lambung yang kosong setelah berpuasa, memberikan energi instan dengan indeks glikemik seimbang."
        }
    },
    {
        "recipeNumber": 198,
        "title": "198. Es Timun Suri Selasih Khas Buka Puasa (DKI Jakarta)",
        "name": "Es Timun Suri Selasih",
        "slug": "es-timun-suri-selasih",
        "scope": "INDONESIA",
        "origin": "DKI Jakarta",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 15,
        "cookTimeMinutes": 10,
        "servings": 4,
        "difficulty": "EASY",
        "spicinessLevel": 0,
        "categorySlug": "minuman-segar",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """198. Es Timun Suri Selasih Khas Buka Puasa (DKI Jakarta)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
1 buah Timun suri matang harum (belah dua, buang bijinya, keruk daging buahnya dengan sendok)
1 sdm Biji selasih (rendam air hangat hingga mengembang selaput putih)
150g Nata de coco beserta airnya
Bahan Kuah Sirup Pandan:
150 ml Sirup cocopandan merah (atau sirup gula pandan buatan sendiri)
500 ml Air matang dingin
1 sdm Air perasan jeruk nipis (opsional, penyeimbang rasa segar)
Es batu kristal / es serut secukupnya
Langkah-Langkah Pembuatan:
Menyiapkan Timun Suri: Keruk daging buah timun suri matang yang telah empuk dan merekah harum secara hati-hati menggunakan sendok koktail agar menghasilkan serpihan daging buah yang lembut alami.
Menyiapkan Biji Selasih: Rendam biji selasih dalam 100 ml air hangat selama 5-10 menit hingga mekar membentuk selaput transparan kenyal. Tiriskan.
Meracik Kuah Sirup: Campurkan air matang dingin, sirup cocopandan, dan air perasan jeruk nipis ke dalam wadah mangkuk besar atau teko saji. Aduk hingga tingkat kemanisan larut merata.
Mencampurkan Bahan: Masukkan kerukan buah timun suri lembut, nata de coco kenyal, dan biji selasih mekar ke dalam larutan sirup cocopandan. Aduk perlahan agar serat timun suri tidak terlalu hancur.
Penyajian: Siapkan gelas saji tinggi. Isi gelas dengan es batu secukupnya, lalu tuangkan es timun suri selasih beserta kuah sirupnya. Sajikan segera selagi dingin menyegarkan di waktu berbuka puasa.
Nutrisi (Per Porsi): Kalori 130 kkal | Protein 1g | Lemak 0.5g | Karbohidrat 31g. Mengandung kadar air lebih dari 90% serta kalium dan glukosa alami buah untuk rehidrasi seluler cepat yang sangat dibutuhkan tubuh setelah berpuasa seharian.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "1 buah Timun suri matang harum (keruk dagingnya)", "amount": 1.0, "unit": "buah", "name": "Timun suri matang", "notes": "keruk dagingnya", "orderIndex": 1},
                    {"rawText": "1 sdm Biji selasih (rendam air hangat)", "amount": 1.0, "unit": "sdm", "name": "Biji selasih", "notes": "rendam air hangat hingga mekar", "orderIndex": 2},
                    {"rawText": "150g Nata de coco beserta airnya", "amount": 150.0, "unit": "g", "name": "Nata de coco", "notes": "beserta airnya", "orderIndex": 3}
                ]
            },
            {
                "name": "Bahan Kuah Sirup Pandan",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "150 ml Sirup cocopandan merah", "amount": 150.0, "unit": "ml", "name": "Sirup cocopandan merah", "notes": None, "orderIndex": 1},
                    {"rawText": "500 ml Air matang dingin", "amount": 500.0, "unit": "ml", "name": "Air matang dingin", "notes": None, "orderIndex": 2},
                    {"rawText": "1 sdm Air perasan jeruk nipis", "amount": 1.0, "unit": "sdm", "name": "Air perasan jeruk nipis", "notes": "opsional penyeimbang segar", "orderIndex": 3},
                    {"rawText": "Es batu kristal / es serut secukupnya", "amount": None, "unit": "secukupnya", "name": "Es batu kristal atau es serut", "notes": None, "orderIndex": 4}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Menyiapkan Timun Suri", "instruction": "Keruk daging buah timun suri matang yang telah empuk dan merekah harum secara hati-hati menggunakan sendok koktail agar menghasilkan serpihan daging buah yang lembut alami.", "rawText": "Menyiapkan Timun Suri: Keruk daging buah timun suri matang yang telah empuk dan merekah harum secara hati-hati menggunakan sendok koktail agar menghasilkan serpihan daging buah yang lembut alami."},
            {"stepNumber": 2, "title": "Menyiapkan Biji Selasih", "instruction": "Rendam biji selasih dalam 100 ml air hangat selama 5-10 menit hingga mekar membentuk selaput transparan kenyal. Tiriskan.", "rawText": "Menyiapkan Biji Selasih: Rendam biji selasih dalam 100 ml air hangat selama 5-10 menit hingga mekar membentuk selaput transparan kenyal. Tiriskan."},
            {"stepNumber": 3, "title": "Meracik Kuah Sirup", "instruction": "Campurkan air matang dingin, sirup cocopandan, dan air perasan jeruk nipis ke dalam wadah mangkuk besar atau teko saji. Aduk hingga tingkat kemanisan larut merata.", "rawText": "Meracik Kuah Sirup: Campurkan air matang dingin, sirup cocopandan, dan air perasan jeruk nipis ke dalam wadah mangkuk besar atau teko saji. Aduk hingga tingkat kemanisan larut merata."},
            {"stepNumber": 4, "title": "Mencampurkan Bahan", "instruction": "Masukkan kerukan buah timun suri lembut, nata de coco kenyal, dan biji selasih mekar ke dalam larutan sirup cocopandan. Aduk perlahan agar serat timun suri tidak terlalu hancur.", "rawText": "Mencampurkan Bahan: Masukkan kerukan buah timun suri lembut, nata de coco kenyal, dan biji selasih mekar ke dalam larutan sirup cocopandan. Aduk perlahan agar serat timun suri tidak terlalu hancur."},
            {"stepNumber": 5, "title": "Penyajian", "instruction": "Siapkan gelas saji tinggi. Isi gelas dengan es batu secukupnya, lalu tuangkan es timun suri selasih beserta kuah sirupnya. Sajikan segera selagi dingin menyegarkan di waktu berbuka puasa.", "rawText": "Penyajian: Siapkan gelas saji tinggi. Isi gelas dengan es batu secukupnya, lalu tuangkan es timun suri selasih beserta kuah sirupnya. Sajikan segera selagi dingin menyegarkan di waktu berbuka puasa."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 130 kkal | Protein 1g | Lemak 0.5g | Karbohidrat 31g. Mengandung kadar air lebih dari 90% serta kalium dan glukosa alami buah untuk rehidrasi seluler cepat yang sangat dibutuhkan tubuh setelah berpuasa seharian.",
            "serving": "Per Porsi",
            "calories": 130,
            "protein": 1.0,
            "fat": 0.5,
            "carbohydrates": 31.0,
            "notes": "Mengandung kadar air lebih dari 90% serta kalium dan glukosa alami buah untuk rehidrasi seluler cepat yang sangat dibutuhkan tubuh setelah berpuasa seharian."
        }
    },
    {
        "recipeNumber": 199,
        "title": "199. Kari Kambing Spesial Idul Adha (Aceh)",
        "name": "Kari Kambing Spesial Idul Adha",
        "slug": "kari-kambing-aceh",
        "scope": "INDONESIA",
        "origin": "Aceh",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 30,
        "cookTimeMinutes": 75,
        "servings": 6,
        "difficulty": "MEDIUM",
        "spicinessLevel": 3,
        "categorySlug": "daging-sapi-kambing",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """199. Kari Kambing Spesial Idul Adha (Aceh)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
800g Daging kambing campur iga (potong dadu 3-4 cm)
1 butir Jeruk nipis (peras airnya untuk melumuri daging)
100g Kelapa parut (sangrai hingga cokelat gelap harum, ulek halus hingga berminyak / U Neulheue khas Aceh)
500 ml Santan kental murni (dari 1 butir kelapa)
1 liter Santan encer
4 sdm Minyak samin atau minyak kelapa untuk menumis
Rempah Daun & Rempah Utuh Khas Aceh:
3 tangkai Daun kari / daun temurui segar (petik daunnya)
2 lembar Daun pandan (ikat simpul)
2 batang Serai (memarkan)
3 buah Bunga lawang / pekak
5 butir Kapulaga putih
4 butir Cengkih
4 cm Kayu manis batangan
Bumbu Halus Rempah:
12 butir Bawang merah
6 siung Bawang putih
10 buah Cabai merah keriting
5 buah Cabai kering merah
1 sdm Ketumbar butiran (sangrai)
1 sdt Jintan (sangrai)
1/2 sdt Adas manis (sangrai)
1 sdt Merica butiran
3 cm Kunyit segar (bakar)
3 cm Jahe
4 butir Kemiri (sangrai)
2 sdt Garam
1 sdt Gula merah
Langkah-Langkah Pembuatan:
Persiapan Daging Kambing: Cuci bersih potongan daging dan iga kambing, tiriskan. Lumuri dengan perasan air jeruk nipis dan 1 sendok teh garam, diamkan selama 15 menit agar bau prengus hilang.
Menyiapkan Kelapa Sangrai (U Neulheue): Sangrai kelapa parut di atas api kecil tanpa minyak sambil diaduk terus hingga berwarna cokelat tua keemasan yang harum. Ulek kelapa sangrai selagi panas di atas cobek hingga benar-benar lumat halus dan mengeluarkan minyak alaminya.
Menumis Bumbu Rempah: Panaskan minyak samin dalam kuali atau panci tebal. Masukkan bumbu halus bersama daun temurui (daun kari), serai, daun pandan, bunga lawang, kapulaga, cengkih, dan kayu manis. Tumis dengan api sedang hingga bumbu benar-benar tanak, harum rempah semerbak, dan berminyak.
Memasak Daging Kambing: Masukkan potongan daging kambing dan kelapa sangrai ulek halus (u neulheue) ke dalam tumisan bumbu. Aduk rata hingga daging berubah warna dan terbalut bumbu pekat (sekitar 7-10 menit).
Memasak dengan Santan Encer: Tuangkan santan encer ke dalam panci. Aduk rata, tutup panci, dan masak dengan api sedang cenderung kecil selama 45 menit hingga daging kambing menjadi empuk dan bumbu meresap ke serat daging.
Menuangkan Santan Kental: Buka tutup panci, tuangkan santan kental murni secara bertahap sambil diaduk perlahan agar santan tidak pecah. Bumbui dengan garam dan gula merah. Masak kembali selama 20 menit dengan api kecil hingga kuah kari mengental pekat, berminyak merah kecokelatan, dan kuah meresap sempurna.
Penyajian: Angkat kari kambing Aceh dan tuangkan ke dalam mangkuk saji saji. Sajikan panas-panas bersama roti jala, roti canai, atau nasi putih hangat pada perayaan Hari Raya Idul Adha.
Nutrisi (Per Porsi): Kalori 410 kkal | Protein 32g | Lemak 28g | Karbohidrat 10g. Kaya akan protein hewani berkualitas tinggi, zat besi, seng, dan senyawa antioksidan dari rempah kari lengkap (jintan, ketumbar, daun temurui) yang menghangatkan tubuh.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama & Olahan Kelapa",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "800g Daging kambing campur iga (potong 3-4 cm)", "amount": 800.0, "unit": "g", "name": "Daging kambing campur iga", "notes": "potong 3-4 cm", "orderIndex": 1},
                    {"rawText": "1 butir Jeruk nipis (peras airnya)", "amount": 1.0, "unit": "butir", "name": "Jeruk nipis", "notes": "peras airnya", "orderIndex": 2},
                    {"rawText": "100g Kelapa parut (sangrai ulek halus berminyak / U Neulheue)", "amount": 100.0, "unit": "g", "name": "Kelapa parut", "notes": "sangrai ulek halus berminyak", "orderIndex": 3},
                    {"rawText": "500 ml Santan kental murni", "amount": 500.0, "unit": "ml", "name": "Santan kental murni", "notes": None, "orderIndex": 4},
                    {"rawText": "1 liter Santan encer", "amount": 1.0, "unit": "liter", "name": "Santan encer", "notes": None, "orderIndex": 5},
                    {"rawText": "4 sdm Minyak samin untuk menumis", "amount": 4.0, "unit": "sdm", "name": "Minyak samin", "notes": "untuk menumis", "orderIndex": 6}
                ]
            },
            {
                "name": "Rempah Daun & Rempah Utuh Khas Aceh",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "3 tangkai Daun kari / temurui segar", "amount": 3.0, "unit": "tangkai", "name": "Daun kari", "notes": "petik daunnya", "orderIndex": 1},
                    {"rawText": "2 lembar Daun pandan (ikat simpul)", "amount": 2.0, "unit": "lembar", "name": "Daun pandan", "notes": "ikat simpul", "orderIndex": 2},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 3},
                    {"rawText": "3 buah Bunga lawang / pekak", "amount": 3.0, "unit": "buah", "name": "Bunga lawang", "notes": None, "orderIndex": 4},
                    {"rawText": "5 butir Kapulaga putih", "amount": 5.0, "unit": "butir", "name": "Kapulaga putih", "notes": None, "orderIndex": 5},
                    {"rawText": "4 butir Cengkih", "amount": 4.0, "unit": "butir", "name": "Cengkih", "notes": None, "orderIndex": 6},
                    {"rawText": "4 cm Kayu manis batangan", "amount": 4.0, "unit": "cm", "name": "Kayu manis batangan", "notes": None, "orderIndex": 7}
                ]
            },
            {
                "name": "Bumbu Halus Rempah",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "12 butir Bawang merah", "amount": 12.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "6 siung Bawang putih", "amount": 6.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "10 buah Cabai merah keriting", "amount": 10.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 3},
                    {"rawText": "5 buah Cabai kering merah", "amount": 5.0, "unit": "buah", "name": "Cabai kering merah", "notes": None, "orderIndex": 4},
                    {"rawText": "1 sdm Ketumbar butiran (sangrai)", "amount": 1.0, "unit": "sdm", "name": "Ketumbar butiran", "notes": "sangrai", "orderIndex": 5},
                    {"rawText": "1 sdt Jintan (sangrai)", "amount": 1.0, "unit": "sdt", "name": "Jintan", "notes": "sangrai", "orderIndex": 6},
                    {"rawText": "1/2 sdt Adas manis (sangrai)", "amount": 0.5, "unit": "sdt", "name": "Adas manis", "notes": "sangrai", "orderIndex": 7},
                    {"rawText": "1 sdt Merica butiran", "amount": 1.0, "unit": "sdt", "name": "Merica butiran", "notes": None, "orderIndex": 8},
                    {"rawText": "3 cm Kunyit segar (bakar)", "amount": 3.0, "unit": "cm", "name": "Kunyit segar", "notes": "bakar", "orderIndex": 9},
                    {"rawText": "3 cm Jahe", "amount": 3.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 10},
                    {"rawText": "4 butir Kemiri (sangrai)", "amount": 4.0, "unit": "butir", "name": "Kemiri", "notes": "sangrai", "orderIndex": 11},
                    {"rawText": "2 sdt Garam", "amount": 2.0, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 12},
                    {"rawText": "1 sdt Gula merah", "amount": 1.0, "unit": "sdt", "name": "Gula merah", "notes": None, "orderIndex": 13}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Persiapan Daging Kambing", "instruction": "Cuci bersih potongan daging dan iga kambing, tiriskan. Lumuri dengan perasan air jeruk nipis dan garam, diamkan selama 15 menit agar aroma segar dan tidak amis.", "rawText": "Persiapan Daging Kambing: Cuci bersih potongan daging dan iga kambing, tiriskan. Lumuri dengan perasan air jeruk nipis dan garam, diamkan selama 15 menit agar aroma segar dan tidak amis."},
            {"stepNumber": 2, "title": "Menyiapkan Kelapa Sangrai (U Neulheue)", "instruction": "Sangrai kelapa parut di atas api kecil tanpa minyak sambil diaduk terus hingga berwarna cokelat tua keemasan yang harum. Ulek kelapa sangrai selagi panas di atas cobek hingga benar-benar lumat halus dan mengeluarkan minyak alaminya.", "rawText": "Menyiapkan Kelapa Sangrai (U Neulheue): Sangrai kelapa parut di atas api kecil tanpa minyak sambil diaduk terus hingga berwarna cokelat tua keemasan yang harum. Ulek kelapa sangrai selagi panas di atas cobek hingga benar-benar lumat halus dan mengeluarkan minyak alaminya."},
            {"stepNumber": 3, "title": "Menumis Bumbu Rempah", "instruction": "Panaskan minyak samin dalam kuali. Masukkan bumbu halus bersama daun temurui, serai, daun pandan, bunga lawang, kapulaga, cengkih, dan kayu manis. Tumis dengan api sedang hingga bumbu benar-benar tanak, harum rempah semerbak, dan berminyak.", "rawText": "Menumis Bumbu Rempah: Panaskan minyak samin dalam kuali. Masukkan bumbu halus bersama daun temurui, serai, daun pandan, bunga lawang, kapulaga, cengkih, dan kayu manis. Tumis dengan api sedang hingga bumbu benar-benar tanak, harum rempah semerbak, dan berminyak."},
            {"stepNumber": 4, "title": "Memasak Daging Kambing", "instruction": "Masukkan potongan daging kambing dan kelapa sangrai ulek halus (u neulheue) ke dalam tumisan bumbu. Aduk rata hingga daging berubah warna dan terbalut bumbu pekat sekitar 7-10 menit.", "rawText": "Memasak Daging Kambing: Masukkan potongan daging kambing dan kelapa sangrai ulek halus (u neulheue) ke dalam tumisan bumbu. Aduk rata hingga daging berubah warna dan terbalut bumbu pekat sekitar 7-10 menit."},
            {"stepNumber": 5, "title": "Memasak dengan Santan Encer", "instruction": "Tuangkan santan encer ke dalam panci. Aduk rata, tutup panci, dan masak dengan api sedang cenderung kecil selama 45 menit hingga daging kambing menjadi empuk dan bumbu meresap ke serat daging.", "rawText": "Memasak dengan Santan Encer: Tuangkan santan encer ke dalam panci. Aduk rata, tutup panci, dan masak dengan api sedang cenderung kecil selama 45 menit hingga daging kambing menjadi empuk dan bumbu meresap ke serat daging."},
            {"stepNumber": 6, "title": "Menuangkan Santan Kental", "instruction": "Buka tutup panci, tuangkan santan kental murni secara bertahap sambil diaduk perlahan agar santan tidak pecah. Bumbui dengan garam dan gula merah. Masak kembali selama 20 menit dengan api kecil hingga kuah kari mengental pekat, berminyak merah kecokelatan, dan kuah meresap sempurna.", "rawText": "Menuangkan Santan Kental: Buka tutup panci, tuangkan santan kental murni secara bertahap sambil diaduk perlahan agar santan tidak pecah. Bumbui dengan garam dan gula merah. Masak kembali selama 20 menit dengan api kecil hingga kuah kari mengental pekat, berminyak merah kecokelatan, dan kuah meresap sempurna."},
            {"stepNumber": 7, "title": "Penyajian", "instruction": "Angkat kari kambing Aceh dan tuangkan ke dalam mangkuk saji. Sajikan panas-panas bersama roti jala atau nasi putih hangat pada perayaan Hari Raya Idul Adha.", "rawText": "Penyajian: Angkat kari kambing Aceh dan tuangkan ke dalam mangkuk saji. Sajikan panas-panas bersama roti jala atau nasi putih hangat pada perayaan Hari Raya Idul Adha."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 410 kkal | Protein 32g | Lemak 28g | Karbohidrat 10g. Kaya akan protein hewani berkualitas tinggi, zat besi, seng, dan senyawa antioksidan dari rempah kari lengkap (jintan, ketumbar, daun temurui) yang menghangatkan tubuh.",
            "serving": "Per Porsi",
            "calories": 410,
            "protein": 32.0,
            "fat": 28.0,
            "carbohydrates": 10.0,
            "notes": "Kaya akan protein hewani berkualitas tinggi, zat besi, seng, dan senyawa antioksidan dari rempah kari lengkap (jintan, ketumbar, daun temurui) yang menghangatkan tubuh."
        }
    },
    {
        "recipeNumber": 200,
        "title": "200. Gulai Nangka Daging Tetelan Khas Minang (Sumatera Barat)",
        "name": "Gulai Nangka Tetelan Minang",
        "slug": "gulai-nangka-tetelan",
        "scope": "INDONESIA",
        "origin": "Sumatera Barat",
        "visualRef": "Lihat Ilustrasi Masakan",
        "imageUrl": None,
        "prepTimeMinutes": 25,
        "cookTimeMinutes": 50,
        "servings": 6,
        "difficulty": "MEDIUM",
        "spicinessLevel": 2,
        "categorySlug": "sayuran-tumisan",
        "cuisineTypeSlug": "hari-raya-perayaan",
        "rawContent": """200. Gulai Nangka Daging Tetelan Khas Minang (Sumatera Barat)
Referensi Visual: Lihat Ilustrasi Masakan
Deskripsi Bahan Baku:
Bahan Utama:
500g Nangka muda sayur (potong-potong tebal 3 cm, rebus setengah matang buang getahnya, tiriskan)
300g Daging sapi tetelan / sandung lamur (rebus hingga empuk, potong dadu)
1 liter Santan encer (dari rebusan daging dan kelapa)
400 ml Santan kental murni
3 sdm Minyak goreng untuk menumis
Bumbu Rempah Daun Khas Minang:
1 lembar Daun kunyit (ikat simpul)
2 batang Serai (memarkan)
4 lembar Daun jeruk purut (buang tulang daun)
2 lembar Daun salam kering
2 buah Asam kandis kering
Bumbu Halus Gulai:
10 butir Bawang merah
5 siung Bawang putih
10 buah Cabai merah keriting
3 cm Kunyit bakar
3 cm Jahe
4 cm Lengkuas
1 sdm Ketumbar sangrai
4 butir Kemiri sangrai
1.5 sdt Garam
1 sdt Kaldu sapi bubuk
Langkah-Langkah Pembuatan:
Merebus Nangka Muda dan Tetelan: Rebus potongan nangka muda dalam air mendidih selama 10 menit untuk melarutkan getah alaminya, lalu tiriskan dan bilas bersih. Di panci terpisah, rebus daging tetelan sapi hingga empuk, ambil dagingnya dan potong dadu (simpan air kaldunya untuk campuran santan encer).
Menumis Bumbu Halus Minang: Panaskan 3 sendok makan minyak dalam wajan cekung. Masukkan bumbu halus kuning kemerahan bersama daun kunyit simpul, serai memarkan, daun jeruk, dan daun salam. Tumis dengan api sedang hingga bumbu benar-benar harum tanak dan tidak langu.
Memasak dengan Santan Encer: Masukkan potongan daging tetelan dan nangka muda rebus ke dalam wajan. Aduk rata dengan bumbu. Tuangkan 1 liter santan encer. Masak sambil terus diaduk perlahan dari bawah ke atas agar santan menyatu dan mendidih.
Mematangkan Serat Nangka: Masukkan asam kandis kering, garam, dan kaldu sapi bubuk. Kecilkan api kompor, tutup sebagian wajan, dan biarkan mendidih perlahan selama 25-30 menit hingga nangka muda menjadi sangat empuk, lembut kemerahan, dan bumbu meresap ke rongga serat nangka.
Memasukkan Santan Kental: Tuangkan santan kental murni. Aduk perlahan dan masak terus dengan api kecil hingga kuah gulai mengental, mengeluarkan minyak kemerahan gurih alami khas Minang (*keluar pati minyak kelapa*), dan bumbu meresap sempurna. Cicipi dan angkat.
Penyajian Lebaran: Sajikan gulai nangka tetelan Minang selagi panas di mangkuk saji saji. Hidangan gulai nangka ini adalah lauk sayur legendaris nomor satu pendamping lontong gulai dan ketupat lebaran di ranah Minangkabau.
Nutrisi (Per Porsi): Kalori 270 kkal | Protein 14g | Lemak 18g | Karbohidrat 16g. Serat pangan tinggi dari nangka muda sangat baik untuk sistem pencernaan, dipadukan protein kolagen dari daging sapi tetelan dan asam lemak rantai sedang dari santan kelapa murni.""",
        "ingredientGroups": [
            {
                "name": "Bahan Utama",
                "orderIndex": 1,
                "ingredients": [
                    {"rawText": "500g Nangka muda sayur (potong tebal 3 cm, rebus)", "amount": 500.0, "unit": "g", "name": "Nangka muda sayur", "notes": "rebus setengah matang buang getah", "orderIndex": 1},
                    {"rawText": "300g Daging sapi tetelan (rebus, potong dadu)", "amount": 300.0, "unit": "g", "name": "Daging sapi tetelan", "notes": "rebus empuk, potong dadu", "orderIndex": 2},
                    {"rawText": "1 liter Santan encer", "amount": 1.0, "unit": "liter", "name": "Santan encer", "notes": None, "orderIndex": 3},
                    {"rawText": "400 ml Santan kental murni", "amount": 400.0, "unit": "ml", "name": "Santan kental murni", "notes": None, "orderIndex": 4},
                    {"rawText": "3 sdm Minyak goreng untuk menumis", "amount": 3.0, "unit": "sdm", "name": "Minyak goreng", "notes": "untuk menumis", "orderIndex": 5}
                ]
            },
            {
                "name": "Bumbu Rempah Daun Khas Minang",
                "orderIndex": 2,
                "ingredients": [
                    {"rawText": "1 lembar Daun kunyit (ikat simpul)", "amount": 1.0, "unit": "lembar", "name": "Daun kunyit", "notes": "ikat simpul", "orderIndex": 1},
                    {"rawText": "2 batang Serai (memarkan)", "amount": 2.0, "unit": "batang", "name": "Serai", "notes": "memarkan", "orderIndex": 2},
                    {"rawText": "4 lembar Daun jeruk purut", "amount": 4.0, "unit": "lembar", "name": "Daun jeruk purut", "notes": "buang tulang", "orderIndex": 3},
                    {"rawText": "2 lembar Daun salam kering", "amount": 2.0, "unit": "lembar", "name": "Daun salam kering", "notes": None, "orderIndex": 4},
                    {"rawText": "2 buah Asam kandis kering", "amount": 2.0, "unit": "buah", "name": "Asam kandis kering", "notes": None, "orderIndex": 5}
                ]
            },
            {
                "name": "Bumbu Halus Gulai",
                "orderIndex": 3,
                "ingredients": [
                    {"rawText": "10 butir Bawang merah", "amount": 10.0, "unit": "butir", "name": "Bawang merah", "notes": None, "orderIndex": 1},
                    {"rawText": "5 siung Bawang putih", "amount": 5.0, "unit": "siung", "name": "Bawang putih", "notes": None, "orderIndex": 2},
                    {"rawText": "10 buah Cabai merah keriting", "amount": 10.0, "unit": "buah", "name": "Cabai merah keriting", "notes": None, "orderIndex": 3},
                    {"rawText": "3 cm Kunyit bakar", "amount": 3.0, "unit": "cm", "name": "Kunyit bakar", "notes": None, "orderIndex": 4},
                    {"rawText": "3 cm Jahe", "amount": 3.0, "unit": "cm", "name": "Jahe", "notes": None, "orderIndex": 5},
                    {"rawText": "4 cm Lengkuas", "amount": 4.0, "unit": "cm", "name": "Lengkuas", "notes": None, "orderIndex": 6},
                    {"rawText": "1 sdm Ketumbar sangrai", "amount": 1.0, "unit": "sdm", "name": "Ketumbar sangrai", "notes": None, "orderIndex": 7},
                    {"rawText": "4 butir Kemiri sangrai", "amount": 4.0, "unit": "butir", "name": "Kemiri sangrai", "notes": None, "orderIndex": 8},
                    {"rawText": "1.5 sdt Garam", "amount": 1.5, "unit": "sdt", "name": "Garam", "notes": None, "orderIndex": 9},
                    {"rawText": "1 sdt Kaldu sapi bubuk", "amount": 1.0, "unit": "sdt", "name": "Kaldu sapi bubuk", "notes": None, "orderIndex": 10}
                ]
            }
        ],
        "steps": [
            {"stepNumber": 1, "title": "Merebus Nangka Muda dan Tetelan", "instruction": "Rebus potongan nangka muda dalam air mendidih selama 10 menit untuk melarutkan getah alaminya, lalu tiriskan dan bilas bersih. Di panci terpisah, rebus daging tetelan sapi hingga empuk, ambil dagingnya dan potong dadu.", "rawText": "Merebus Nangka Muda dan Tetelan: Rebus potongan nangka muda dalam air mendidih selama 10 menit untuk melarutkan getah alaminya, lalu tiriskan dan bilas bersih. Di panci terpisah, rebus daging tetelan sapi hingga empuk, ambil dagingnya dan potong dadu."},
            {"stepNumber": 2, "title": "Menumis Bumbu Halus Minang", "instruction": "Panaskan 3 sendok makan minyak dalam wajan cekung. Masukkan bumbu halus kuning kemerahan bersama daun kunyit simpul, serai memarkan, daun jeruk, dan daun salam. Tumis dengan api sedang hingga bumbu benar-benar harum tanak dan tidak langu.", "rawText": "Menumis Bumbu Halus Minang: Panaskan 3 sendok makan minyak dalam wajan cekung. Masukkan bumbu halus kuning kemerahan bersama daun kunyit simpul, serai memarkan, daun jeruk, dan daun salam. Tumis dengan api sedang hingga bumbu benar-benar harum tanak dan tidak langu."},
            {"stepNumber": 3, "title": "Memasak dengan Santan Encer", "instruction": "Masukkan potongan daging tetelan dan nangka muda rebus ke dalam wajan. Aduk rata dengan bumbu. Tuangkan 1 liter santan encer. Masak sambil terus diaduk perlahan dari bawah ke atas agar santan menyatu dan mendidih.", "rawText": "Memasak dengan Santan Encer: Masukkan potongan daging tetelan dan nangka muda rebus ke dalam wajan. Aduk rata dengan bumbu. Tuangkan 1 liter santan encer. Masak sambil terus diaduk perlahan dari bawah ke atas agar santan menyatu dan mendidih."},
            {"stepNumber": 4, "title": "Mematangkan Serat Nangka", "instruction": "Masukkan asam kandis kering, garam, dan kaldu sapi bubuk. Kecilkan api kompor, tutup sebagian wajan, dan biarkan mendidih perlahan selama 25-30 menit hingga nangka muda menjadi sangat empuk, lembut kemerahan, dan bumbu meresap ke rongga serat nangka.", "rawText": "Mematangkan Serat Nangka: Masukkan asam kandis kering, garam, dan kaldu sapi bubuk. Kecilkan api kompor, tutup sebagian wajan, dan biarkan mendidih perlahan selama 25-30 menit hingga nangka muda menjadi sangat empuk, lembut kemerahan, dan bumbu meresap ke rongga serat nangka."},
            {"stepNumber": 5, "title": "Memasukkan Santan Kental", "instruction": "Tuangkan santan kental murni. Aduk perlahan dan masak terus dengan api kecil hingga kuah gulai mengental, mengeluarkan minyak kemerahan gurih alami khas Minang, dan bumbu meresap sempurna. Cicipi dan angkat.", "rawText": "Memasukkan Santan Kental: Tuangkan santan kental murni. Aduk perlahan dan masak terus dengan api kecil hingga kuah gulai mengental, mengeluarkan minyak kemerahan gurih alami khas Minang, dan bumbu meresap sempurna. Cicipi dan angkat."},
            {"stepNumber": 6, "title": "Penyajian Lebaran", "instruction": "Sajikan gulai nangka tetelan Minang selagi panas di mangkuk saji sebagai lauk sayur legendaris nomor satu pendamping lontong gulai dan ketupat lebaran di ranah Minangkabau.", "rawText": "Penyajian Lebaran: Sajikan gulai nangka tetelan Minang selagi panas di mangkuk saji sebagai lauk sayur legendaris nomor satu pendamping lontong gulai dan ketupat lebaran di ranah Minangkabau."}
        ],
        "nutrition": {
            "rawText": "Nutrisi (Per Porsi): Kalori 270 kkal | Protein 14g | Lemak 18g | Karbohidrat 16g. Serat pangan tinggi dari nangka muda sangat baik untuk sistem pencernaan, dipadukan protein kolagen dari daging sapi tetelan dan asam lemak rantai sedang dari santan kelapa murni.",
            "serving": "Per Porsi",
            "calories": 270,
            "protein": 14.0,
            "fat": 18.0,
            "carbohydrates": 16.0,
            "notes": "Serat pangan tinggi dari nangka muda sangat baik untuk sistem pencernaan, dipadukan protein kolagen dari daging sapi tetelan dan asam lemak rantai sedang dari santan kelapa murni."
        }
    }
]

file_path = os.path.join(os.path.dirname(__file__), '../src/seeder/recipes-data.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter out if any 191-200 already exist to be idempotent
data['recipes'] = [r for r in data['recipes'] if r['recipeNumber'] < 191]

# Append new recipes
data['recipes'].extend(new_recipes)

# Save back to JSON
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total_count = len(data['recipes'])
print(f"Berhasil menambahkan 10 resep Hari Raya & Puasa! Total resep saat ini: {total_count}")

