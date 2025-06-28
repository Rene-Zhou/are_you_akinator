# 反向天才（Reverse Akinator）开发文档

## 项目概述

反向天才是一个基于AI的猜人物游戏，与传统的Akinator相反：
- AI预设一个网络知名人物
- 人类通过提问来猜测这个人物
- AI只能回答："是"、"否"、"不知道"、"或许是"、"或许不是"、"你猜对了"

## 技术架构

### 后端架构
```
FastAPI Backend
├── API层：通过OpenAI SDK实现与LLM的交互
├── AI服务层：LLM集成与回答生成
├── 事实获取层：在选定人物后，从维基百科信息获取人物资料，提供给LLM
├── 游戏状态管理：会话管理
└── 配置管理：环境变量与LLM提供商配置
```

### 前端架构
```
阶段1：CLI界面（Python Prompt Toolkit）✅
├── 命令行交互界面
├── 游戏流程控制
├── API客户端
└── 用户输入处理

阶段2：Web界面（React）✅
├── 现代化UI组件 - React + Tailwind CSS
├── 实时交互 - 游戏状态管理和动画
├── 游戏历史记录 - 问答历史展示
├── 响应式设计 - 移动端和桌面端适配
├── 错误处理 - 连接状态监控和错误边界
└── 用户体验 - 加载动画和友好提示
```

## 技术栈选择

### 后端技术栈
- **Web框架**: FastAPI
  - 原因：高性能、自动API文档、类型提示支持
- **AI服务**: OpenAI SDK
  - 支持多个LLM提供商（OpenAI、Azure OpenAI、本地模型等）
- **事实验证**: 
  - Wikipedia API (wikipedia-api库)
  - BeautifulSoup4（网页解析）
- **依赖管理**: uv（符合用户偏好）
- **环境管理**: python-dotenv
- **HTTP客户端**: httpx

### 前端技术栈
#### CLI界面
- **CLI框架**: Python Prompt Toolkit
  - 原因：丰富的交互功能、自动补全、历史记录
- **HTTP客户端**: httpx
- **配置管理**: python-dotenv

#### Web界面（React）
- **前端框架**: React 18
  - 原因：组件化开发、生态丰富、社区活跃
- **构建工具**: Vite 5
  - 原因：快速开发服务器、热重载、优化构建
- **样式框架**: Tailwind CSS 3.4
  - 原因：原子化CSS、响应式设计、自定义主题
- **HTTP客户端**: Axios
  - 原因：拦截器支持、错误处理、请求配置
- **状态管理**: React Hooks (useState, useEffect, custom hooks)
  - 原因：轻量级、符合React最佳实践
- **开发工具**: ESLint + PostCSS + Autoprefixer

### 数据存储
- **会话存储**: 内存存储（Redis可选，用于扩展）
- **人物信息缓存**: 本地JSON文件 + 内存缓存

## 项目结构

```
are_you_akinator/
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── main.py              # FastAPI应用入口
│       ├── api/
│       │   ├── __init__.py
│       │   ├── game.py          # 游戏API端点
│       │   └── health.py        # 健康检查
│       ├── services/
│       │   ├── __init__.py
│       │   ├── ai_service.py    # AI服务集成
│       │   └── game_manager.py  # 游戏状态管理
│       ├── models/
│       │   ├── __init__.py
│       │   ├── game.py          # 游戏数据模型
│       │   └── person.py        # 人物信息模型
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py      # 配置管理
│       └── utils/
│           ├── __init__.py
│           └── wikipedia.py     # 维基百科工具
├── cli/
│   ├── __init__.py
│   ├── main.py                  # CLI应用入口
│   ├── client.py                # API客户端
│   ├── ui.py                    # 用户界面
│   └── config.py                # CLI配置
├── frontend/                    # React前端
│   ├── src/
│   │   ├── components/          # React组件
│   │   │   ├── GameBoard.jsx    # 主游戏界面
│   │   │   ├── QuestionInput.jsx # 问题输入组件
│   │   │   ├── AnswerDisplay.jsx # 答案显示组件
│   │   │   ├── QuestionHistory.jsx # 问答历史
│   │   │   ├── WinScreen.jsx    # 胜利界面
│   │   │   ├── ConnectionStatus.jsx # 连接状态
│   │   │   ├── ErrorBoundary.jsx # 错误边界
│   │   │   └── Loading.jsx      # 加载组件
│   │   ├── hooks/               # 自定义Hooks
│   │   │   └── useGame.js       # 游戏状态管理Hook
│   │   ├── services/            # API服务
│   │   │   └── api.js           # 后端API接口
│   │   ├── styles/              # 样式文件
│   │   │   └── index.css        # 主样式和Tailwind配置
│   │   ├── App.jsx              # 主应用组件
│   │   └── main.jsx             # 应用入口点
│   ├── public/                  # 静态资源
│   ├── index.html               # HTML模板
│   ├── package.json             # 前端依赖
│   ├── vite.config.js           # Vite配置
│   ├── tailwind.config.js       # Tailwind CSS配置
│   ├── postcss.config.js        # PostCSS配置
│   ├── .eslintrc.cjs            # ESLint配置
│   ├── .gitignore               # Git忽略文件
│   ├── .env.example             # 前端环境变量示例
│   └── README.md                # 前端文档
├── famous_people.txt            # 人物列表文件
├── .env.example                 # 环境变量示例
├── .env                         # 环境变量（不提交）
├── main.py                      # 主入口程序
├── run_backend.py               # 后端启动脚本
├── start_cli.py                 # CLI启动脚本
├── start_frontend.py            # 前端启动脚本
├── pyproject.toml               # 项目配置
├── README.md                    # 项目说明
├── DEVELOPMENT.md               # 开发文档
└── TESTING_GUIDE.md             # 测试指南
```

## 核心功能设计

### 1. AI服务设计
```python
# AI提示词模板
SYSTEM_PROMPT = """
你是一个反向Akinator游戏的AI。你已经选择了一个网络知名人物：{person_name}

关于这个人物的信息：
{person_info}

游戏规则：
1. 用户会问你关于这个人物的问题
2. 你只能回答以下6种答案之一：
   - "是" - 确定答案为是
   - "否" - 确定答案为否  
   - "不知道" - 不确定或信息不足
   - "或许是" - 可能是，但不确定
   - "或许不是" - 可能不是，但不确定
   - "你猜对了" - 用户猜中了人物

3. 基于提供的人物信息准确回答
4. 如果用户直接猜测人物姓名且正确，回答"你猜对了"
"""
```

### 2. 人物管理系统
- 从famous_people.txt文件动态加载人物列表
- 支持注释和分类组织
- 备用默认列表机制
- 使用Wikipedia API获取人物详细信息
- 缓存机制避免重复请求
- 信息结构化存储（年龄、职业、国籍、成就等）

### 3. 游戏流程
1. **初始化阶段**：AI从famous_people.txt文件随机选择一个知名人物
2. **信息获取阶段**：从Wikipedia获取人物详细信息
3. **游戏进行阶段**：用户提问，AI根据信息回答
4. **自然猜测阶段**：用户可以通过自然语言猜测人物（如"是爱因斯坦吗？"）
5. **结束阶段**：AI回答"你猜对了"时自动结束游戏并显示胜利信息

## API设计

### 游戏API端点
```python
POST /api/game/start              # 开始新游戏
GET  /api/game/{session_id}       # 获取游戏状态
POST /api/game/{session_id}/ask   # 提问（包括猜测）
GET  /api/game/stats/overview     # 获取游戏统计信息
DELETE /api/game/{session_id}     # 结束游戏
```

### 数据模型
```python
class GameSession:
    session_id: str
    person_name: str
    person_info: dict
    questions_asked: list
    status: GameStatus  # ACTIVE, WON, ABANDONED
    created_at: datetime

class Question:
    question: str
    answer: str
    timestamp: datetime
```

## 环境配置

### .env文件配置
```env
# LLM配置
LLM_PROVIDER=openai  # openai, azure, local
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini

# 应用配置
DEBUG=True
LOG_LEVEL=INFO
PORT=8000

# Wikipedia配置
WIKIPEDIA_LANGUAGE LLM对对语言文本的理解能力较好，优先提供人物的英文文本和本人国籍的文本

CACHE_DURATION=3600    # 缓存时间（秒）
```

## 开发阶段规划

### 阶段1：基础后端开发 ✅
1. 搭建FastAPI项目结构
2. 实现AI服务集成  
3. 开发Wikipedia信息获取
4. 实现游戏状态管理
5. 编写API端点

### 阶段2：CLI前端开发 ✅
1. 设计CLI交互界面
2. 实现API客户端
3. 开发游戏流程控制
4. 添加用户体验优化

### 阶段3：功能优化 ✅
1. 人物列表文件管理
2. 自然语言猜测
3. 错误处理完善
4. 移除冗余功能

### 阶段4：Web界面开发 ✅
1. React + Vite 项目搭建
2. Tailwind CSS 响应式设计
3. 游戏组件开发 (GameBoard, QuestionInput, AnswerDisplay等)
4. 状态管理和API集成
5. 错误处理和用户体验优化
6. 连接状态监控和加载动画
7. 移动端适配和触摸友好交互

### 阶段5：扩展功能（可选）
1. 多语言支持
2. 难度级别设置
3. 人物类别筛选
4. 单元测试编写
5. Docker容器化部署
6. 数据库集成和用户系统

## 技术决策说明

### 为什么选择FastAPI？
- 高性能异步框架
- 自动生成OpenAPI文档
- 优秀的类型提示支持
- 活跃的社区和生态

### 为什么使用Wikipedia API？
- 免费且可靠的数据源
- 结构化的人物信息
- 多语言支持
- 实时更新的内容

### 为什么先开发CLI？
- 快速验证核心逻辑
- 降低开发复杂度
- 便于调试和测试
- 为Web版本奠定基础

### 为什么选择React + Tailwind CSS？
**React选择原因：**
- 组件化开发，代码复用性强
- 丰富的生态系统和社区支持
- 优秀的开发工具和调试体验
- React Hooks 提供简洁的状态管理

**Tailwind CSS选择原因：**
- 原子化CSS，快速开发
- 内置响应式设计系统
- 可定制的设计系统
- 优秀的性能和构建优化

**Vite选择原因：**
- 极快的开发服务器启动
- 热模块替换 (HMR) 性能优秀
- 内置 TypeScript/JSX 支持
- 现代化的构建工具

## 风险评估与缓解

### 技术风险
1. **LLM API限制**：实现多提供商支持，本地fallback
2. **Wikipedia访问限制**：添加请求频率控制，缓存机制
3. **信息准确性**：多源验证，用户反馈机制

### 产品风险
1. **人物信息不足**：建立人物数据库，人工筛选
2. **游戏难度平衡**：可调节的提示系统
3. **用户体验**：渐进式UI改进

## 后续扩展方向

1. **多人模式**：支持多用户同时游戏
2. **排行榜系统**：记录用户游戏成绩
3. **自定义人物**：允许用户添加人物
4. **社交功能**：分享游戏结果
5. **移动端应用**：React Native实现

这个开发文档为项目提供了清晰的技术路线和实现方案。请审阅并提出任何需要调整的地方。