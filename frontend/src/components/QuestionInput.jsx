import { useState } from 'react';
import Loading from './Loading';

const QuestionInput = ({ onSubmit, isLoading, disabled }) => {
  const [question, setQuestion] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (question.trim() && !isLoading && !disabled) {
      onSubmit(question.trim());
      setQuestion('');
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto">
      <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-3">
        <div className="flex-1">
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="请输入您的问题..."
            className="input-field resize-none h-12 min-h-[3rem] focus:h-20 transition-all duration-200"
            disabled={disabled || isLoading}
            rows={1}
          />
        </div>
        <button
          type="submit"
          disabled={!question.trim() || isLoading || disabled}
          className="btn-primary sm:px-8 disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap"
        >
          {isLoading ? (
            <Loading message="思考中..." size="small" variant="light" />
          ) : (
            '提问'
          )}
        </button>
      </form>
      
      <div className="mt-3 text-sm text-gray-500 text-center">
        💡 提示：您可以问关于性别、职业、国籍、年龄等问题，也可以直接猜测人物姓名
      </div>
    </div>
  );
};

export default QuestionInput;