# 反向天才 (Reverse Akinator)

一个基于AI的猜人物游戏，与传统的Akinator相反：AI预设一个知名人物，人类通过提问来猜测这个人物是谁。

## 🎮 游戏规则

- AI已经想好了一个网络知名人物（从人物列表中随机选择）
- 你需要通过提问来猜测这个人物是谁  
- AI只能回答：**是**、**否**、**不知道**、**或许是**、**或许不是**、**你猜对了**
- 尽量用最少的问题猜出答案！

## 🚀 快速开始

### 1. 环境配置

确保你有Python 3.13+和uv包管理器：

```bash
# 安装依赖
uv sync
```

### 2. 配置环境变量

创建`.env`文件并配置你的LLM API密钥：

```env
# LLM配置
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini

# 其他配置
DEBUG=True
LOG_LEVEL=INFO
PORT=8000
WIKIPEDIA_LANGUAGE=en
```

### 3. 自定义人物列表（可选）

项目包含一个`famous_people.txt`文件，里面预设了各类知名人物。你可以编辑这个文件来：

- **添加新的人物**：每行一个名字
- **删除不想要的人物**：直接删除对应行
- **分类组织**：使用注释（以`#`开头的行）

文件格式示例：
```
# 科学家
Albert Einstein
Stephen Hawking
Marie Curie

# 企业家  
Steve Jobs
Bill Gates
Elon Musk

# 你自己添加的人物
Your Custom Person
```

### 4. 启动游戏

#### 方式一：使用主菜单（推荐）
```bash
uv run python main.py
```
选择：
- **选项1**：启动CLI游戏（命令行界面）
- **选项2**：启动后端服务器
- **选项3**：启动React前端界面（现代Web界面）🆕

#### 方式二：分别启动

**CLI游戏:**
```bash
# 1. 启动后端服务器
uv run python run_backend.py

# 2. 在另一个终端启动CLI客户端
uv run python start_cli.py
```

**Web界面游戏:**
```bash
# 1. 启动后端服务器
uv run python run_backend.py

# 2. 在另一个终端启动前端
uv run python start_frontend.py
```

**注意**：
- 首次启动前端需要安装Node.js和npm
- Web前端将在 http://localhost:3000 启动
- 支持移动端和桌面端浏览器
- 提供现代化的用户界面和交互体验

## 🎯 游戏界面

### CLI界面命令
在命令行界面中，你可以使用以下方式：

- **直接提问**：`这个人是男性吗？`
- **直接猜测**：`是爱因斯坦吗？`
- **查看历史**：`history`
- **获取帮助**：`help`
- **退出游戏**：`quit`

### Web界面特性 🆕
在React Web界面中，你可以享受：

- **🎨 现代化UI**：精美的界面设计和动画效果
- **📱 响应式设计**：完美适配手机、平板、桌面端
- **⚡ 实时交互**：即时显示AI回答和游戏状态
- **📝 问答历史**：自动记录所有问答对话
- **🎉 胜利庆祝**：游戏胜利时的庆祝动画和统计
- **🔄 连接监控**：实时显示后端连接状态
- **🛡️ 错误处理**：友好的错误提示和恢复机制
- **🎨 UX优化**：自动滚动到最新消息，输入框焦点保持

## 🔧 技术架构

### 后端 (FastAPI)
- **AI服务**：OpenAI SDK集成，支持多LLM提供商
- **人物选择**：从`famous_people.txt`文件随机选择
- **事实验证**：Wikipedia API获取人物信息
- **游戏管理**：会话状态管理
- **REST API**：提供游戏接口

### 前端
#### CLI界面 (Python)
- **交互界面**：Python Prompt Toolkit + Rich
- **游戏流程**：问答历史记录、命令处理
- **API客户端**：与后端通信

#### Web界面 (React)
- **现代化UI**：React + Tailwind CSS
- **响应式设计**：支持移动端和桌面端
- **实时交互**：游戏状态管理和动画效果
- **完整功能**：问答历史、胜利界面、统计信息

## 📚 API文档

启动后端服务器后，访问 http://localhost:8000/docs 查看完整的API文档。

### 主要端点

- `POST /api/game/start` - 开始新游戏
- `POST /api/game/{session_id}/ask` - 提问
- `GET /api/game/{session_id}` - 获取游戏状态
- `GET /api/game/stats/overview` - 获取游戏统计（包含人物总数）
- `DELETE /api/game/{session_id}` - 结束游戏

## 🎪 提问技巧

1. **从大范围开始**：性别、年龄段、国籍、职业领域
2. **逐步缩小范围**：具体行业、时代、成就类型
3. **注意AI回答**：
   - "或许是"/"或许不是" = 不确定，可以换个角度问
   - "不知道" = 信息不足，尝试更具体的问题

## 🔍 示例游戏流程

```
❓ 问题 #1: 这个人是男性吗？
🤖 AI回答: 是

❓ 问题 #2: 他是科学家吗？
🤖 AI回答: 是

❓ 问题 #3: 他获得过诺贝尔奖吗？
🤖 AI回答: 是

🎯 你的问题或命令: 是爱因斯坦吗？
🤖 AI回答: 你猜对了

🎉 恭喜！你猜对了！
💡 你的猜测：是爱因斯坦吗？
📊 总共用了 3 个问题
🎯 游戏结束，感谢游玩！
```

## 🛠️ 开发

### 项目结构

```
are_you_akinator/
├── backend/           # FastAPI后端
│   └── app/
│       ├── api/       # API端点
│       ├── services/  # 业务逻辑
│       ├── models/    # 数据模型
│       ├── config/    # 配置管理
│       └── utils/     # 工具函数
├── cli/               # CLI客户端
├── frontend/          # React前端
│   ├── src/
│   │   ├── components/ # React组件
│   │   ├── hooks/     # 自定义Hooks
│   │   ├── services/  # API服务
│   │   └── styles/    # 样式文件
│   ├── package.json   # 前端依赖
│   └── vite.config.js # Vite配置
├── famous_people.txt  # 人物列表文件
├── main.py            # 主入口
├── run_backend.py     # 后端启动脚本
└── start_frontend.py  # 前端启动脚本
```

### 人物管理

- 编辑`famous_people.txt`添加或删除人物
- 重启后端服务器以加载新的人物列表
- 查看`/api/game/stats/overview`端点获取当前人物总数

### 运行测试

```bash
# 安装开发依赖
uv sync --dev

# 运行测试
uv run pytest

# 代码格式化
uv run black .
uv run isort .
```

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

---

**享受游戏吧！🎮**