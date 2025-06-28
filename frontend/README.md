# 反向天才 - React 前端

这是反向天才（Reverse Akinator）游戏的 React 前端界面。

## 功能特性

- 🎮 现代化的游戏界面
- 📱 响应式设计，支持移动端和桌面端
- 🎨 基于 Tailwind CSS 的精美 UI
- ⚡ 基于 Vite 的快速开发体验
- 🔄 实时游戏状态管理
- 📝 完整的问答历史记录
- 🎉 胜利庆祝界面

## 技术栈

- **框架**: React 18
- **构建工具**: Vite
- **样式**: Tailwind CSS
- **HTTP 客户端**: Axios
- **开发语言**: JavaScript

## 快速开始

### 1. 安装依赖

```bash
cd frontend
npm install
```

### 2. 环境配置

复制环境变量示例文件：

```bash
cp .env.example .env
```

根据需要修改 `.env` 文件中的配置。

### 3. 启动开发服务器

```bash
npm run dev
```

前端将在 http://localhost:3000 启动。

### 4. 构建生产版本

```bash
npm run build
```

## 项目结构

```
frontend/
├── src/
│   ├── components/          # React 组件
│   │   ├── GameBoard.jsx    # 主游戏界面
│   │   ├── QuestionInput.jsx # 问题输入组件
│   │   ├── AnswerDisplay.jsx # 答案显示组件
│   │   ├── QuestionHistory.jsx # 问答历史
│   │   └── WinScreen.jsx    # 胜利界面
│   ├── hooks/              # 自定义 React Hooks
│   │   └── useGame.js      # 游戏状态管理 Hook
│   ├── services/           # API 服务
│   │   └── api.js          # 后端 API 接口
│   ├── styles/             # 样式文件
│   │   └── index.css       # 主样式文件
│   ├── App.jsx             # 主应用组件
│   └── main.jsx            # 应用入口点
├── public/                 # 静态资源
├── index.html              # HTML 模板
├── vite.config.js          # Vite 配置
├── tailwind.config.js      # Tailwind CSS 配置
└── package.json            # 项目依赖
```

## 组件说明

### GameBoard
主游戏界面组件，管理整个游戏的状态和流程。

### QuestionInput
问题输入组件，提供用户输入问题的界面。

### AnswerDisplay
答案显示组件，展示 AI 的回答和相应的视觉提示。

### QuestionHistory
问答历史组件，显示所有的问答记录。

### WinScreen
胜利界面组件，在用户猜对时显示庆祝界面。

## API 集成

前端通过 `/src/services/api.js` 与后端 FastAPI 服务器通信，支持以下功能：

- 开始新游戏
- 提问和获取回答
- 获取游戏状态
- 结束游戏
- 获取统计信息

## 响应式设计

使用 Tailwind CSS 的响应式工具类，确保在不同设备上的良好体验：

- 移动设备优先设计
- 平板和桌面端适配
- 灵活的布局系统

## 开发命令

```bash
# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview

# 代码检查
npm run lint

# 自动修复代码
npm run lint:fix
```