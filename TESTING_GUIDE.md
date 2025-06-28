# 🧪 测试指南

## 完整系统测试

### 1. 环境准备

确保你有以下环境：
- Python 3.13+
- uv 包管理器
- Node.js 18+ 和 npm
- 有效的 OpenAI API 密钥

### 2. 依赖安装

```bash
# 安装 Python 依赖
uv sync

# 安装前端依赖 (首次运行时会自动安装)
cd frontend && npm install && cd ..
```

### 3. 环境配置

创建 `.env` 文件：
```bash
cp .env.example .env
```

编辑 `.env` 文件，添加你的 API 密钥：
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_actual_api_key_here
MODEL_NAME=gpt-4o-mini
```

## 🎯 测试场景

### 场景1：CLI 界面测试

1. **启动系统**
   ```bash
   uv run python main.py
   ```

2. **选择选项1** - 启动 CLI 游戏

3. **测试游戏流程**
   - 提问："这个人是男性吗？"
   - 提问："他是科学家吗？"
   - 猜测："是爱因斯坦吗？"
   - 使用命令：`history`、`help`、`quit`

### 场景2：Web 界面测试

1. **启动后端**
   ```bash
   # 终端1
   uv run python run_backend.py
   ```

2. **启动前端**
   ```bash
   # 终端2
   uv run python start_frontend.py
   ```

3. **访问 Web 界面**
   - 打开浏览器访问 http://localhost:3000
   - 测试响应式设计（调整浏览器窗口大小）
   - 测试移动端界面

4. **测试游戏功能**
   - 点击"开始游戏"
   - 输入问题并提交
   - 查看问答历史
   - 完成游戏并查看胜利界面

### 场景3：API 测试

1. **启动后端**
   ```bash
   uv run python run_backend.py
   ```

2. **访问 API 文档**
   - 打开 http://localhost:8000/docs
   - 测试各个端点

3. **手动 API 测试**
   ```bash
   # 健康检查
   curl http://localhost:8000/health
   
   # 开始游戏
   curl -X POST http://localhost:8000/api/game/start
   
   # 提问 (替换 SESSION_ID)
   curl -X POST http://localhost:8000/api/game/SESSION_ID/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "这个人是男性吗？"}'
   ```

## 🔍 错误排查

### 常见问题

#### 1. 前端无法连接后端
- **症状**: 前端显示连接错误
- **解决**: 
  - 确保后端在 http://localhost:8000 运行
  - 检查防火墙设置
  - 查看浏览器控制台错误

#### 2. API 密钥错误
- **症状**: "Failed to start game" 错误
- **解决**: 
  - 检查 `.env` 文件中的 API 密钥
  - 确认 API 密钥有效且有余额

#### 3. 人物信息获取失败
- **症状**: 游戏开始但 AI 回答异常
- **解决**: 
  - 检查网络连接
  - 确认可以访问 Wikipedia
  - 查看后端日志

#### 4. 前端编译错误
- **症状**: Tailwind CSS 类不存在
- **解决**: 
  - 确保 Tailwind 配置正确
  - 重新安装依赖: `npm install`
  - 清理缓存: `npm run build`

### 性能测试

1. **并发游戏测试**
   - 同时启动多个游戏会话
   - 测试内存使用情况

2. **长时间运行测试**
   - 让系统运行几小时
   - 监控内存泄漏

3. **响应时间测试**
   - 测量 API 响应时间
   - 测试不同问题的处理速度

## 📊 测试检查清单

### 基础功能
- [ ] 后端成功启动 (端口 8000)
- [ ] 前端成功启动 (端口 3000)
- [ ] API 文档可访问
- [ ] 健康检查端点工作正常

### 游戏功能
- [ ] 可以开始新游戏
- [ ] AI 能正确回答问题
- [ ] 问答历史正确显示
- [ ] 胜利检测工作正常
- [ ] 游戏可以正常结束

### 用户界面
- [ ] CLI 界面操作流畅
- [ ] Web 界面加载正常
- [ ] 响应式设计工作正常
- [ ] 加载动画显示正确
- [ ] 错误信息显示清晰

### 错误处理
- [ ] 后端不可用时显示连接状态
- [ ] API 错误有友好提示
- [ ] 网络错误处理正确
- [ ] 无效输入处理正确

### 兼容性
- [ ] Chrome 浏览器正常
- [ ] Firefox 浏览器正常
- [ ] Safari 浏览器正常
- [ ] 移动端浏览器正常

## 🚀 部署测试

### 生产构建测试
```bash
# 构建前端
cd frontend
npm run build

# 预览生产版本
npm run preview
```

### Docker 测试 (可选)
如果你有 Docker 环境，可以测试容器化部署：

```bash
# 构建 Docker 镜像
docker build -t are-you-akinator .

# 运行容器
docker run -p 8000:8000 -p 3000:3000 are-you-akinator
```

## 📝 测试报告

完成测试后，记录以下信息：

- 测试日期：
- 测试环境：
- 发现的问题：
- 性能表现：
- 建议改进：

---

**祝测试顺利！🎮**