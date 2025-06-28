import { useState } from 'react';
import QuestionInput from './QuestionInput';
import QuestionHistory from './QuestionHistory';
import WinScreen from './WinScreen';
import useGame from '../hooks/useGame';

const GameBoard = () => {
  const { gameState, startNewGame, askQuestion, endGame, resetGame } = useGame();
  const [showHistory, setShowHistory] = useState(false);

  const handleStartGame = async () => {
    try {
      await startNewGame();
      setShowHistory(false);
    } catch (error) {
      console.error('Failed to start game:', error);
    }
  };

  const handleAskQuestion = async (question) => {
    try {
      await askQuestion(question);
    } catch (error) {
      console.error('Failed to ask question:', error);
    }
  };

  const handleEndGame = async () => {
    await endGame();
    setShowHistory(false);
  };

  const handleNewGame = async () => {
    await endGame();
    await handleStartGame();
  };

  const renderGameHeader = () => (
    <div className="text-center mb-8">
      <h1 className="text-4xl font-bold text-gray-800 mb-2">
        反向天才 🧠
      </h1>
      <p className="text-lg text-gray-600">
        我想了一个知名人物，你能猜出来吗？
      </p>
    </div>
  );

  const renderGameControls = () => {
    if (gameState.status === 'idle') {
      return (
        <div className="text-center">
          <div className="mb-6 flex justify-center">
            <img 
              src="https://raw.githubusercontent.com/Rene-Zhou/are_you_akinator/refs/heads/master/img/akinaotr-t.png" 
              alt="Akinator" 
              className="w-96 h-96 object-contain"
            />
          </div>
          <h2 className="text-2xl font-semibold text-gray-700 mb-4">
            准备开始新游戏
          </h2>
          <p className="text-gray-500 mb-8 max-w-md mx-auto">
            点击开始游戏，我会想一个知名人物，你通过提问来猜测这个人物是谁！
          </p>
          <button
            onClick={handleStartGame}
            className="btn-primary text-xl py-4 px-8"
            disabled={gameState.isLoading}
          >
            {gameState.isLoading ? '准备中...' : '🚀 开始游戏'}
          </button>
        </div>
      );
    }

    if (gameState.status === 'won') {
      return showHistory ? (
        <div>
          <div className="flex justify-between items-center mb-6">
            <button
              onClick={() => setShowHistory(false)}
              className="btn-secondary"
            >
              ← 返回结果
            </button>
            <button
              onClick={handleNewGame}
              className="btn-primary"
            >
              🚀 再来一局
            </button>
          </div>
          <QuestionHistory questions={gameState.questions} />
        </div>
      ) : (
        <WinScreen
          questionsCount={gameState.questions.length}
          onNewGame={handleNewGame}
          onViewHistory={() => setShowHistory(true)}
        />
      );
    }

    if (gameState.status === 'active') {
      return (
        <div className="space-y-8">
          {/* 游戏控制栏 */}
          <div className="flex flex-col sm:flex-row justify-between items-center gap-4 p-4 bg-white rounded-lg shadow-sm border">
            <div className="flex items-center gap-4">
              <div className="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-medium">
                🎮 游戏进行中
              </div>
              <div className="text-gray-600">
                已问 {gameState.questions.length} 个问题
              </div>
            </div>
            <button
              onClick={handleEndGame}
              className="btn-secondary text-red-600 border-red-200 hover:bg-red-50"
            >
              结束游戏
            </button>
          </div>

          {/* 问答历史 */}
          <QuestionHistory questions={gameState.questions} />

          {/* 输入区域 */}
          <div className="sticky bottom-0 bg-white border-t border-gray-100 p-6 -mx-6 -mb-6">
            <QuestionInput
              onSubmit={handleAskQuestion}
              isLoading={gameState.isLoading}
              disabled={gameState.status !== 'active'}
            />
          </div>
        </div>
      );
    }

    if (gameState.status === 'error') {
      return (
        <div className="text-center py-12">
          <div className="text-6xl mb-4">❌</div>
          <h3 className="text-xl font-semibold text-red-700 mb-2">出现错误</h3>
          <p className="text-red-600 mb-6">{gameState.error}</p>
          <button
            onClick={resetGame}
            className="btn-primary"
          >
            重新开始
          </button>
        </div>
      );
    }

    return null;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          {renderGameHeader()}
          
          <div className="card min-h-[600px]">
            {renderGameControls()}
          </div>
        </div>
      </div>
    </div>
  );
};

export default GameBoard;