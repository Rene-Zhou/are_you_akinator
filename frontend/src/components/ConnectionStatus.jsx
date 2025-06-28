import { useState, useEffect } from 'react';
import axios from 'axios';

const ConnectionStatus = () => {
  const [status, setStatus] = useState('checking'); // checking, connected, disconnected
  const [lastCheck, setLastCheck] = useState(null);

  const checkConnection = async () => {
    setStatus('checking');
    try {
      await axios.get('/health', { timeout: 5000 });
      setStatus('connected');
    } catch (error) {
      setStatus('disconnected');
    }
    setLastCheck(new Date());
  };

  useEffect(() => {
    checkConnection();
    const interval = setInterval(checkConnection, 30000); // Check every 30 seconds
    return () => clearInterval(interval);
  }, []);

  const getStatusColor = () => {
    switch (status) {
      case 'connected':
        return 'bg-green-100 text-green-800 border-green-200';
      case 'disconnected':
        return 'bg-red-100 text-red-800 border-red-200';
      case 'checking':
        return 'bg-yellow-100 text-yellow-800 border-yellow-200';
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200';
    }
  };

  const getStatusIcon = () => {
    switch (status) {
      case 'connected':
        return '✅';
      case 'disconnected':
        return '❌';
      case 'checking':
        return '🔄';
      default:
        return '❓';
    }
  };

  const getStatusText = () => {
    switch (status) {
      case 'connected':
        return '后端已连接';
      case 'disconnected':
        return '后端未连接';
      case 'checking':
        return '检查连接中...';
      default:
        return '未知状态';
    }
  };

  if (status === 'connected') {
    return null; // Don't show anything when connected
  }

  return (
    <div className="fixed top-4 right-4 z-50">
      <div className={`inline-flex items-center gap-2 px-3 py-2 rounded-lg border text-sm font-medium ${getStatusColor()}`}>
        <span>{getStatusIcon()}</span>
        <span>{getStatusText()}</span>
        {status === 'disconnected' && (
          <button
            onClick={checkConnection}
            className="ml-2 text-xs underline hover:no-underline"
          >
            重试
          </button>
        )}
      </div>
      
      {status === 'disconnected' && (
        <div className="mt-2 p-3 bg-white border border-red-200 rounded-lg shadow-lg max-w-sm">
          <div className="text-sm text-gray-700">
            <div className="font-semibold mb-2">连接失败</div>
            <div className="text-xs space-y-1">
              <div>• 请确保后端服务器已启动</div>
              <div>• 运行命令: <code className="bg-gray-100 px-1 rounded">uv run python run_backend.py</code></div>
              <div>• 或选择主菜单选项2启动后端</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ConnectionStatus;