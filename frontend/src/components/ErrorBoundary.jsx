import { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo
    });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen bg-gradient-to-br from-red-50 via-orange-50 to-yellow-50 flex items-center justify-center p-4">
          <div className="card max-w-lg mx-auto text-center">
            <div className="text-6xl mb-4">😵</div>
            <h2 className="text-2xl font-bold text-red-700 mb-4">
              哎呀，出现了错误！
            </h2>
            <p className="text-gray-600 mb-6">
              应用遇到了一个意外错误，请刷新页面重试。
            </p>
            <div className="space-y-4">
              <button
                onClick={() => window.location.reload()}
                className="btn-primary w-full"
              >
                🔄 刷新页面
              </button>
              <details className="text-left">
                <summary className="cursor-pointer text-sm text-gray-500 hover:text-gray-700">
                  技术详情 (点击展开)
                </summary>
                <div className="mt-2 p-3 bg-gray-100 rounded text-xs text-gray-700 overflow-auto">
                  <div className="font-semibold mb-2">错误信息:</div>
                  <div className="mb-3">{this.state.error && this.state.error.toString()}</div>
                  <div className="font-semibold mb-2">错误栈:</div>
                  <pre className="whitespace-pre-wrap">
                    {this.state.errorInfo.componentStack}
                  </pre>
                </div>
              </details>
            </div>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;