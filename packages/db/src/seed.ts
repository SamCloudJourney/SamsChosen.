import { prisma, Role } from './index.js';

const categories = [
  { name: 'General Chat', slug: 'general', description: 'Everyday life in SE22/SE15.' },
  { name: 'Recommendations', slug: 'recommendations', description: 'Local tips and services.' },
  { name: 'For Sale / Free', slug: 'for-sale', description: 'Pre-loved goods, swaps, and freebies.' },
  { name: 'Jobs & Gigs', slug: 'jobs', description: 'Help wanted and short-term gigs.' },
  { name: 'Housing / Rooms', slug: 'housing', description: 'Homes, flatshares, and movers.' },
  { name: 'Parenting & Families', slug: 'parenting', description: 'Family talk and support.' },
  { name: 'Nightlife & Events', slug: 'events', description: 'What’s on around SE22/SE15.' },
  { name: 'Lost & Found', slug: 'lost-and-found', description: 'Missing pets, keys, and treasures.' },
];

async function main() {
  await Promise.all(
    categories.map((category) =>
      prisma.category.upsert({
        where: { slug: category.slug },
        update: category,
        create: category,
      })
    )
  );

  const adminEmail = process.env.SEED_ADMIN_EMAIL;
  const adminPasswordHash = process.env.SEED_ADMIN_PASSWORD_HASH;

  if (adminEmail && adminPasswordHash) {
    await prisma.user.upsert({
      where: { email: adminEmail },
      update: {},
      create: {
        email: adminEmail,
        username: 'admin',
        name: 'Forum Admin',
        passwordHash: adminPasswordHash,
        areaCode: 'SE22',
        role: Role.ADMIN,
      },
    });
  }
}

main()
  .catch((error) => {
    console.error('Seed failed', error);
    process.exit(1);
  })
  .finally(async () => prisma.$disconnect());
