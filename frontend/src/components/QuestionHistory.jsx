import AnswerDisplay from './AnswerDisplay';

const QuestionHistory = ({ questions }) => {
  if (!questions || questions.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-6xl mb-4">🤖</div>
        <h3 className="text-xl font-semibold text-gray-700 mb-2">开始您的探索</h3>
        <p className="text-gray-500">
          我已经想好了一个知名人物，请开始提问来猜测这个人物是谁！
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-xl font-semibold text-gray-800">问答记录</h2>
        <div className="bg-primary-100 text-primary-800 px-3 py-1 rounded-full text-sm font-medium">
          共 {questions.length} 个问题
        </div>
      </div>
      
      <div className="space-y-4 max-h-96 overflow-y-auto">
        {questions.map((qa, index) => (
          <AnswerDisplay
            key={index}
            question={qa.question}
            answer={qa.answer}
            timestamp={qa.timestamp}
            isLatest={index === questions.length - 1}
          />
        ))}
      </div>
    </div>
  );
};

export default QuestionHistory;