#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动前端开发服务器
"""
import subprocess
import sys
import os

def main():
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    
    if not os.path.exists(frontend_dir):
        print("❌ 前端目录不存在")
        return 1
    
    # 检查是否安装了依赖
    node_modules_dir = os.path.join(frontend_dir, "node_modules")
    if not os.path.exists(node_modules_dir):
        print("📦 正在安装前端依赖...")
        try:
            subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
        except subprocess.CalledProcessError:
            print("❌ 安装依赖失败")
            return 1
        except FileNotFoundError:
            print("❌ 未找到 npm，请先安装 Node.js")
            return 1
    
    print("🚀 启动前端开发服务器...")
    print("📍 前端地址: http://localhost:3000")
    print("🔗 后端 API: http://localhost:8000")
    print("👉 请确保后端服务器已启动")
    print()
    
    try:
        subprocess.run(["npm", "run", "dev"], cwd=frontend_dir)
    except subprocess.CalledProcessError:
        print("❌ 启动前端失败")
        return 1
    except KeyboardInterrupt:
        print("\n👋 前端服务器已停止")
        return 0

if __name__ == "__main__":
    sys.exit(main())