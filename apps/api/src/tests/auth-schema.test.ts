import { registerSchema } from '../modules/auth/schema.js';

describe('registerSchema', () => {
  it('fails for invalid area', () => {
    expect(() =>
      registerSchema.parse({
        email: 'test@example.com',
        username: 'user123',
        name: 'Test User',
        password: 'password123',
        areaCode: 'NW1',
      })
    ).toThrow();
  });

  it('passes for SE22', () => {
    expect(
      registerSchema.parse({
        email: 'test@example.com',
        username: 'user123',
        name: 'Test User',
        password: 'password123',
        areaCode: 'SE22',
      })
    ).toBeTruthy();
  });
});
