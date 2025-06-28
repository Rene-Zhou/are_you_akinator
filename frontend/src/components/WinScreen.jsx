const WinScreen = ({ questionsCount, onNewGame, onViewHistory }) => {
  return (
    <div className="text-center py-12 animate-fade-in">
      <div className="text-8xl mb-6 animate-bounce-subtle">🎉</div>
      
      <h2 className="text-3xl font-bold text-gray-800 mb-4">
        恭喜您猜对了！
      </h2>
      
      <div className="bg-gradient-to-r from-purple-50 to-blue-50 rounded-xl p-6 mb-8 max-w-md mx-auto">
        <div className="flex items-center justify-center gap-4 text-lg">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🎯</span>
            <span className="font-semibold text-gray-700">总共用了</span>
          </div>
          <div className="bg-white rounded-lg px-4 py-2 shadow-sm">
            <span className="text-2xl font-bold text-primary-600">{questionsCount}</span>
            <span className="text-gray-600 ml-1">个问题</span>
          </div>
        </div>
      </div>

      <div className="space-y-4 mb-8">
        <p className="text-lg text-gray-600">
          您的推理能力真是令人印象深刻！
        </p>
        <p className="text-gray-500">
          想要挑战另一个人物吗？
        </p>
      </div>

      <div className="flex flex-col sm:flex-row gap-4 justify-center max-w-md mx-auto">
        <button
          onClick={onNewGame}
          className="btn-primary flex-1 text-lg py-3"
        >
          🚀 再来一局
        </button>
        <button
          onClick={onViewHistory}
          className="btn-secondary flex-1 text-lg py-3"
        >
          📝 查看记录
        </button>
      </div>
    </div>
  );
};

export default WinScreen;