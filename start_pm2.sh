#!/bin/bash

set -e

# 创建日志目录
mkdir -p logs

# 检查并安装 PM2
if ! command -v pm2 &> /dev/null; then
    npm install -g pm2
fi

# 安装前端依赖
cd frontend
if [ ! -d "node_modules" ]; then
    npm install
fi
cd ..

# 启动服务
pm2 start ecosystem.config.js

# 显示状态
pm2 status
pm2 save

echo "前端: http://localhost:3000"
echo "后端: http://localhost:8000"