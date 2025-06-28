const AnswerDisplay = ({ question, answer, timestamp, isLatest = false }) => {
  const getAnswerEmoji = (answer) => {
    switch (answer) {
      case '是':
        return '✅';
      case '否':
        return '❌';
      case '不知道':
        return '🤷‍♂️';
      case '或许是':
        return '🤔';
      case '或许不是':
        return '😐';
      case '你猜对了':
        return '🎉';
      default:
        return '🤖';
    }
  };

  const getAnswerColor = (answer) => {
    switch (answer) {
      case '是':
        return 'text-green-600 bg-green-50 border-green-200';
      case '否':
        return 'text-red-600 bg-red-50 border-red-200';
      case '不知道':
        return 'text-gray-600 bg-gray-50 border-gray-200';
      case '或许是':
        return 'text-yellow-600 bg-yellow-50 border-yellow-200';
      case '或许不是':
        return 'text-orange-600 bg-orange-50 border-orange-200';
      case '你猜对了':
        return 'text-purple-600 bg-purple-50 border-purple-200';
      default:
        return 'text-blue-600 bg-blue-50 border-blue-200';
    }
  };

  return (
    <div className={`card transition-all duration-300 ${isLatest ? 'animate-slide-in ring-2 ring-primary-200' : ''}`}>
      <div className="flex flex-col sm:flex-row gap-4">
        {/* 问题部分 */}
        <div className="flex-1">
          <div className="flex items-start gap-3">
            <div className="flex-shrink-0 w-8 h-8 bg-primary-100 rounded-full flex items-center justify-center">
              <span className="text-primary-600 font-semibold text-sm">Q</span>
            </div>
            <div className="flex-1">
              <p className="text-gray-800 font-medium">{question}</p>
              {timestamp && (
                <p className="text-xs text-gray-500 mt-1">
                  {new Date(timestamp).toLocaleTimeString('zh-CN')}
                </p>
              )}
            </div>
          </div>
        </div>

        {/* 答案部分 */}
        <div className="flex-shrink-0">
          <div className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg border font-semibold ${getAnswerColor(answer)}`}>
            <span className="text-lg">{getAnswerEmoji(answer)}</span>
            <span>{answer}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AnswerDisplay;