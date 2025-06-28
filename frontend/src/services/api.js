import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    console.error('API Error:', error);
    
    // Handle network errors
    if (!error.response) {
      if (error.code === 'ECONNREFUSED' || error.message.includes('Network Error')) {
        error.message = '无法连接到后端服务器，请确保后端服务器已启动 (http://localhost:8000)';
      } else {
        error.message = '网络连接错误，请检查网络连接';
      }
    } else {
      // Handle HTTP errors
      const status = error.response.status;
      switch (status) {
        case 404:
          error.message = '请求的资源不存在';
          break;
        case 500:
          error.message = '服务器内部错误';
          break;
        default:
          error.message = error.response.data?.detail || `请求失败 (${status})`;
      }
    }
    
    throw error;
  }
);

export const gameAPI = {
  async startGame() {
    return await api.post('/api/game/start');
  },

  async getGameStatus(sessionId) {
    return await api.get(`/api/game/${sessionId}`);
  },

  async askQuestion(sessionId, question) {
    return await api.post(`/api/game/${sessionId}/ask`, { question });
  },

  async endGame(sessionId) {
    return await api.delete(`/api/game/${sessionId}`);
  },

  async getStats() {
    return await api.get('/api/game/stats/overview');
  },
};

export default api;