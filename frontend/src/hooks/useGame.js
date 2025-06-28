import { useState, useCallback } from 'react';
import { gameAPI } from '../services/api';

const useGame = () => {
  const [gameState, setGameState] = useState({
    sessionId: null,
    status: 'idle', // idle, loading, active, won, error
    questions: [],
    isLoading: false,
    error: null,
  });

  const startNewGame = useCallback(async () => {
    setGameState(prev => ({ ...prev, isLoading: true, error: null }));
    
    try {
      const response = await gameAPI.startGame();
      setGameState({
        sessionId: response.session_id,
        status: 'active',
        questions: [],
        isLoading: false,
        error: null,
      });
      return response;
    } catch (error) {
      console.error('Failed to start game:', error);
      setGameState(prev => ({
        ...prev,
        status: 'error',
        isLoading: false,
        error: error.message || '启动游戏失败',
      }));
      throw error;
    }
  }, []);

  const askQuestion = useCallback(async (question) => {
    if (!gameState.sessionId) {
      throw new Error('No active game session');
    }

    setGameState(prev => ({ ...prev, isLoading: true, error: null }));

    try {
      const response = await gameAPI.askQuestion(gameState.sessionId, question);
      
      const newQuestion = {
        question: response.question,
        answer: response.answer,
        timestamp: new Date(),
      };

      setGameState(prev => ({
        ...prev,
        questions: [...prev.questions, newQuestion],
        status: response.answer === '你猜对了' ? 'won' : 'active',
        isLoading: false,
      }));

      return response;
    } catch (error) {
      console.error('Failed to ask question:', error);
      setGameState(prev => ({
        ...prev,
        isLoading: false,
        error: error.message || '提问失败',
      }));
      throw error;
    }
  }, [gameState.sessionId]);

  const endGame = useCallback(async () => {
    if (!gameState.sessionId) return;

    try {
      await gameAPI.endGame(gameState.sessionId);
    } catch (error) {
      console.error('Failed to end game:', error);
    } finally {
      setGameState({
        sessionId: null,
        status: 'idle',
        questions: [],
        isLoading: false,
        error: null,
      });
    }
  }, [gameState.sessionId]);

  const resetGame = useCallback(() => {
    setGameState({
      sessionId: null,
      status: 'idle',
      questions: [],
      isLoading: false,
      error: null,
    });
  }, []);

  return {
    gameState,
    startNewGame,
    askQuestion,
    endGame,
    resetGame,
  };
};

export default useGame;