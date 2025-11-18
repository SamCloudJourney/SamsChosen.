import { extractMentions } from '../modules/posts/service.js';

describe('extractMentions', () => {
  it('deduplicates and sanitizes mentions', () => {
    const result = extractMentions('Hello @alex and @alex plus @sam.');
    expect(result).toEqual(['alex', 'sam']);
  });

  it('handles absence of mentions', () => {
    expect(extractMentions('no mentions here')).toEqual([]);
  });
});
