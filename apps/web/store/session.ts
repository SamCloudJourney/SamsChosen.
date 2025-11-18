import { create } from 'zustand';

interface SessionState {
  user?: {
    id: string;
    username: string;
    areaCode: string;
    role: string;
  };
  setUser: (user?: SessionState['user']) => void;
}

export const useSession = create<SessionState>((set) => ({
  user: undefined,
  setUser: (user) => set({ user }),
}));
