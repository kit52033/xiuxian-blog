# 🌀 修仙研究院

全自動化運營嘅修仙/都市修真小說內容網站

## 📌 網站功能

- ✅ 每日自動生成新文章
- ✅ 自動部署到 GitHub Pages
- ✅ 小說點評、深度分析、角色排行三大分類
- ✅ SEO 優化
- ✅ 比特幣/以太坊打賞功能

## 🚀 快速開始

### 本地開發

```bash
# 克隆項目
git clone https://github.com/YOUR_USERNAME/xiuxian-blog.git
cd xiuxian-blog

# 安裝 Hugo 擴展版
brew install hugo

# 初始化主題
git submodule update --init --recursive

# 本地預覽
hugo server
```

### 自動生成文章

```bash
# 生成單篇文章
python3 generate_article.py

# 生成多篇文章
python3 -c "
import generate_article
for _ in range(5):
    import random
    cats = list(generate_article.CATEGORIES.keys())
    generate_article.create_article(random.choice(cats))
"
```

## 🔄 自動化流程

1. **GitHub Actions** 每日香港時間 09:00 自動運行
2. 自動生成一篇新文章
3. 自動編譯 Hugo 網站
4. 自動部署到 GitHub Pages

## 📁 目錄結構

```
xiuxian-blog/
├── content/
│   └── categories/
│       ├── reviews/      # 小說點評
│       ├── analysis/     # 深度分析
│       └── tier/         # 角色排行
├── layouts/
│   └── index.html        # 首頁範本
├── scripts/
│   └── daily_article.py  # 每日生成腳本
├── themes/
│   └── PaperMod/         # Hugo 主題
├── generate_article.py  # 文章生成器
└── hugo.toml            # 站點配置
```

## 💰 變現方式

- 聯盟行銷（推廣小說網站）
- 比特幣/以太坊打賞
- Google AdSense
- 付費訂閱（未來）

## 🛠️ 自定義

### 修改網站名稱

編輯 `hugo.toml`:

```toml
title = "你的網站名稱"
```

### 添加新分類

1. 在 `hugo.toml` 的 `[menu]` 添加新項目
2. 在 `content/categories/` 添加新目錄
3. 在 `generate_article.py` 添加新話題

## 📝 文章模板

文章使用 Markdown + Hugo Frontmatter 格式:

```markdown
---
title: "文章標題"
date: 2026-07-18T00:00:00+08:00
categories: ["小說點評"]
tags: ["修仙", "推薦"]
---

文章內容...
```

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📜 許可

MIT License

---

*🌀 黑洞出品 | 全能管家*
