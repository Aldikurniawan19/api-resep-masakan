const fs = require('fs');
const path = require('path');
const { PrismaClient } = require('@prisma/client');
require('dotenv').config();

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY) {
  console.error('Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY in .env');
  process.exit(1);
}

const dbUrl = process.env.DIRECT_URL || process.env.DATABASE_URL;
const prisma = new PrismaClient({
  datasources: {
    db: {
      url: dbUrl
    }
  }
});

const batchImages = [
  {
    slug: 'soto-ayam-lamongan',
    localFile: 'C:/Users/Vstor/.gemini/antigravity/brain/11b6c7ef-165d-4b53-8bbe-6a65d11c9456/soto_ayam_lamongan_1793267222173.jpg',
    storageName: 'soto-ayam-lamongan.jpg'
  },
  {
    slug: 'gado-gado-betawi',
    localFile: 'C:/Users/Vstor/.gemini/antigravity/brain/11b6c7ef-165d-4b53-8bbe-6a65d11c9456/gado_gado_betawi_1793267224286.jpg',
    storageName: 'gado-gado-betawi.jpg'
  },
  {
    slug: 'sate-lilit-ikan-tenggiri',
    localFile: 'C:/Users/Vstor/.gemini/antigravity/brain/11b6c7ef-165d-4b53-8bbe-6a65d11c9456/sate_lilit_ikan_tenggiri_1793267228414.jpg',
    storageName: 'sate-lilit-ikan-tenggiri.jpg'
  },
  {
    slug: 'pempek-kapal-selam',
    localFile: 'C:/Users/Vstor/.gemini/antigravity/brain/11b6c7ef-165d-4b53-8bbe-6a65d11c9456/pempek_kapal_selam_1793267239092.jpg',
    storageName: 'pempek-kapal-selam.jpg'
  },
  {
    slug: 'nasi-goreng-kampung',
    localFile: 'C:/Users/Vstor/.gemini/antigravity/brain/11b6c7ef-165d-4b53-8bbe-6a65d11c9456/nasi_goreng_kampung_1793267244799.jpg',
    storageName: 'nasi-goreng-kampung.jpg'
  }
];

async function uploadToSupabaseStorage(filePath, storageName) {
  const fileBuffer = fs.readFileSync(filePath);
  const uploadUrl = `${SUPABASE_URL}/storage/v1/object/recipes/${storageName}`;

  const response = await fetch(uploadUrl, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`,
      'apikey': SUPABASE_SERVICE_ROLE_KEY,
      'Content-Type': 'image/jpeg',
      'x-upsert': 'true',
      'cache-control': '31536000'
    },
    body: fileBuffer
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Upload failed for ${storageName} (${response.status}): ${errorText}`);
  }

  const publicUrl = `${SUPABASE_URL}/storage/v1/object/public/recipes/${storageName}`;
  return publicUrl;
}

async function main() {
  console.log(`Starting upload of ${batchImages.length} AI images to Supabase Storage bucket [recipes]...`);

  // Ensure local assets directory exists to keep an archive copy
  const projectAssetsDir = path.join(__dirname, '..', 'assets', 'images', 'recipes');
  if (!fs.existsSync(projectAssetsDir)) {
    fs.mkdirSync(projectAssetsDir, { recursive: true });
  }

  const results = [];

  for (const item of batchImages) {
    console.log(`\nProcessing: ${item.slug}`);

    // Verify local file exists
    if (!fs.existsSync(item.localFile)) {
      throw new Error(`Local file not found: ${item.localFile}`);
    }

    // Copy to project assets
    const destPath = path.join(projectAssetsDir, item.storageName);
    fs.copyFileSync(item.localFile, destPath);
    console.log(`  Archived locally to: assets/images/recipes/${item.storageName}`);

    // Upload to Supabase Storage
    const publicUrl = await uploadToSupabaseStorage(item.localFile, item.storageName);
    console.log(`  Uploaded to Supabase: ${publicUrl}`);

    // Update in database
    const updateResult = await prisma.recipe.updateMany({
      where: { slug: item.slug },
      data: { imageUrl: publicUrl }
    });
    console.log(`  Database updated for slug [${item.slug}], rows affected: ${updateResult.count}`);

    results.push({
      slug: item.slug,
      publicUrl
    });
  }

  // Update recipes-data.json
  console.log('\nUpdating src/seeder/recipes-data.json...');
  const jsonPath = path.join(__dirname, '..', 'src', 'seeder', 'recipes-data.json');
  const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  for (const res of results) {
    const r = data.recipes.find(r => r.slug === res.slug);
    if (r) {
      r.imageUrl = res.publicUrl;
    }
  }
  fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2), 'utf8');
  console.log('src/seeder/recipes-data.json updated successfully.');

  // Verify by querying database
  console.log('\nVerifying updated recipes from database:');
  const verified = await prisma.recipe.findMany({
    where: { slug: { in: batchImages.map(s => s.slug) } },
    select: { id: true, title: true, slug: true, imageUrl: true }
  });
  console.dir(verified, { depth: null });
}

main()
  .catch(err => {
    console.error('Error during execution:', err);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
