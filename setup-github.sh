#!/bin/bash
# 修仙研究院 - GitHub 初始化腳本
# 黑洞 🌀

set -e

echo "🌀 修仙研究院 - GitHub 初始化"
echo "================================"
echo ""

# 檢查 Hugo
if ! command -v hugo &> /dev/null; then
    echo "❌ 請先安裝 Hugo: brew install hugo"
    exit 1
fi

# 提示用戶輸入 GitHub 用戶名
read -p "請輸入 GitHub 用戶名: " GH_USER

# 創建 GitHub 倉庫
echo ""
echo "📝 請手動創建 GitHub 倉庫:"
echo "   https://github.com/new"
echo "   - Repository name: xiuxian-blog"
echo "   - Public ✓"
echo ""
read -p "按 Enter 繼續..."

# 初始化 GitHub Pages 分支
echo "🚀 設置 GitHub Pages..."

git remote add origin "https://github.com/$GH_USER/xiuxian-blog.git" 2>/dev/null || \
    git remote set-url origin "https://github.com/$GH_USER/xiuxian-blog.git"

git branch -M main
git push -u origin main
git push origin gh-pages 2>/dev/null || true

echo ""
echo "✅ 初始化完成！"
echo ""
echo "📋 下一步:"
echo "1. 前往 https://github.com/$GH_USER/xiuxian-blog/settings/pages"
echo "2. Source 選擇 'gh-pages' 分支"
echo "3. 等待 2-3 分鐘後訪問: https://$GH_USER.github.io/xiuxian-blog"
echo ""
echo "💡 之後每日 09:00 (UTC) / 17:00 (HK) 會自動生成新文章並部署"
