import nextJest from 'next/jest.js';

const createJestConfig = nextJest({
  dir: './',
});

const config = createJestConfig({
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/tests/setup.ts'],
});

export default config;
