import { render, screen } from '@testing-library/react';
import { ThreadCard } from '../components/ThreadCard';
import type { Thread } from '../lib/types';

const mockThread: Thread = {
  id: 'thread-1',
  title: 'Lost cat on Barry Road',
  content: 'Please help find our cat near Goose Green.',
  category: { id: '1', name: 'Lost & Found', slug: 'lost', description: '' },
  author: { username: 'sam', areaCode: 'SE22' },
  _count: { posts: 3 },
  createdAt: new Date().toISOString(),
  updatedAt: new Date().toISOString(),
  location: 'Goose Green',
};

describe('ThreadCard', () => {
  it('renders title and author', () => {
    render(<ThreadCard thread={mockThread} />);
    expect(screen.getByText(mockThread.title)).toBeInTheDocument();
    expect(screen.getByText(/@sam/)).toBeInTheDocument();
  });
});
