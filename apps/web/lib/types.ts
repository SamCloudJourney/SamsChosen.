export interface Category {
  id: string;
  name: string;
  slug: string;
  description: string;
}

export interface Thread {
  id: string;
  title: string;
  content: string;
  category: Category;
  author: {
    username: string;
    areaCode: string;
  };
  _count: { posts: number };
  createdAt: string;
  updatedAt: string;
  price?: number;
  location?: string;
  pinned?: boolean;
}

export interface Post {
  id: string;
  content: string;
  author: { username: string; areaCode: string; avatarUrl?: string };
  createdAt: string;
}

export interface Notification {
  id: string;
  type: string;
  payload: Record<string, unknown>;
  readAt?: string;
  createdAt: string;
}
