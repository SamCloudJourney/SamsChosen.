import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f7ff',
          100: '#dbeefe',
          200: '#b3dbfd',
          500: '#1c5dd8',
          600: '#1349ad',
        },
      },
    },
  },
  plugins: [],
};

export default config;
