const { PrismaClient } = require('@prisma/client');
const fs = require('fs');
const prisma = new PrismaClient();

const updates = [
  {
    slug: 'rendang-daging-khas-minang',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Rendang_daging_sapi_asli_Padang.JPG/800px-Rendang_daging_sapi_asli_Padang.JPG'
  },
  {
    slug: 'soto-betawi',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Soto_Betawi_Jakarta_Street_Side_Food.JPG/800px-Soto_Betawi_Jakarta_Street_Side_Food.JPG'
  },
  {
    slug: 'tempe-mendoan-banyumas',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Mendoan.jpg/800px-Mendoan.jpg'
  },
  {
    slug: 'es-pisang-ijo-makassar',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Es_pisang_ijo.jpg/800px-Es_pisang_ijo.jpg'
  },
  {
    slug: 'ayam-goreng-lengkuas',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Ayam_goreng_in_Jakarta.JPG/800px-Ayam_goreng_in_Jakarta.JPG'
  }
];

async function main() {
  console.log('Updating database for 5 sample recipes...');
  for (const item of updates) {
    const res = await prisma.recipe.updateMany({
      where: { slug: item.slug },
      data: { imageUrl: item.imageUrl }
    });
    console.log(`Updated DB slug: ${item.slug}, count: ${res.count}`);
  }

  console.log('Updating recipes-data.json...');
  const jsonPath = 'src/seeder/recipes-data.json';
  const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  for (const item of updates) {
    const r = data.recipes.find(r => r.slug === item.slug);
    if (r) {
      r.imageUrl = item.imageUrl;
    }
  }
  fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2), 'utf8');
  console.log('recipes-data.json updated successfully.');

  const verified = await prisma.recipe.findMany({
    where: { slug: { in: updates.map(u => u.slug) } },
    select: { id: true, title: true, slug: true, imageUrl: true }
  });
  console.log('Verified from DB:');
  console.dir(verified, { depth: null });
}

main()
  .catch(err => {
    console.error(err);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

