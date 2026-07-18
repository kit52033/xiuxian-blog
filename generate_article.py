#!/usr/bin/env python3
"""
修仙研究院 - 自動文章生成器
黑洞 🌀 全能管家出品
"""

import os
import random
import json
from datetime import datetime, timedelta
import hashlib

# 文章話題庫
TOPICS_REVIEWS = [
    ("那些年一起追過的修仙神作", "從《凡人修仙傳》到《仙逆》，盤點最經典嘅修仙小說"),
    ("《我欲封天》開局分析：孟浩點樣一步步走上修仙路", "詳細分析主角孟浩嘅修煉之路同關鍵轉折點"),
    ("《凡人修仙傳》點解被稱為修仙天花板？", "全方位點評忘語呢部神作嘅成功之道"),
    ("都市修真文的魅力：現實與幻想嘅完美結合", "分析都市修真類型點解咁受歡迎"),
    ("修仙戰鬥系統拆解：邊個設定最正？", "各大小說戰鬥系統橫向對比"),
    ("盤點修仙小說中令人印象深刻的女主", "盤點各類型女主角形象"),
    ("修仙小說嘅修煉境界設定邊個最合理？", "對比各大小說境界設定"),
    ("從煉氣到飛升：修仙升級之路完整解析", "詳細圖解修仙各階段"),
]

TOPICS_ANALYSIS = [
    ("修仙主角光環分析：點解佢地總係死唔去？", "分析主角點樣合理開掛"),
    ("修仙世界觀：法寶、丹藥、靈根設定潛規則", "揭秘修仙世界運作原理"),
    ("網文作者寫修仙容易犯的錯誤", "新手作者常見問題提醒"),
    ("修仙小說節奏把控：點樣先苦後甜", "寫作技巧分享"),
    ("都市修真和傳統修仙各有咩優劣？", "兩大類型深度對比"),
]

TOPICS_TIER = [
    ("修仙小說實力排行：你估下邊個最強？", "各路神仙實力評級"),
    ("十大最強法寶排行榜", "盤點各大小說終極法寶"),
    ("女主實力排行：邊個女主最強？", "女性角色戰力分析"),
    ("反派實力榜：邊個BOSS最令人印象深刻？", "經典反派實力評級"),
]

CATEGORIES = {
    "reviews": {"dir": "content/categories/reviews/", "emoji": "📝", "name": "小說點評"},
    "analysis": {"dir": "content/categories/analysis/", "emoji": "🔍", "name": "深度分析"},
    "tier": {"dir": "content/categories/tier/", "emoji": "🏆", "name": "角色排行"},
}

def generate_slug(title: str) -> str:
    """生成 URL-friendly slug"""
    slug = title.replace(" ", "-")
    slug = "".join(c if c.isalnum() or c in ",-?" else "" for c in slug)
    return slug[:50]

def generate_frontmatter(title: str, category: str, tags: list) -> str:
    """生成 Hugo markdown frontmatter"""
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    slug = generate_slug(title)
    return f'''---
title: "{title}"
date: {date}
draft: false
categories: ["{CATEGORIES[category]["name"]}"]
tags: {json.dumps(tags, ensure_ascii=False)}
slug: "{slug}"
author: "黑洞 🌀"
---

'''

def generate_article_content(title: str, description: str, category: str) -> str:
    """生成文章主體"""
    emoji = CATEGORIES[category]["emoji"]
    
    # 根據分類生成不同風格嘅內容
    if category == "reviews":
        content = f'''{emoji} **{title}**

{description}

## 📖 前言

修仙小說，作為中國網絡文學嘅重要類型，一直深受讀者喜愛。今日我哋就來深度分析一下呢個話題。

## 🔥 內容分析

### 為何吸引讀者？

修仙小說之所以長盛不衰，主要有以下幾個原因：

1. **升級快感** - 跟隨主角由弱者變強者，滿足讀者嘅代入感
2. **世界觀宏大** - 仙俠世界嘅設定令人著迷
3. **情感糾葛** - 修仙路上嘅愛恨情仇
4. **想象空間** - 法寶、丹藥、靈獸無限可能

### 經典元素

| 元素 | 特點 | 例子 |
|------|------|------|
| 修煉境界 | 由低到高層層遞進 | 煉氣→筑基→金丹→元嬰 |
| 法寶神器 | 主角標配 | 寶劍、盾牌、鐘塔 |
| 丹藥系統 | 加速修煉必備 | 筑基丹、破階丹 |
| 師門傳承 | 強大後台 | 各類宗門世家 |

## 💡 結論

修仙小說之所以吸引人，係因為佢完美結合咗幻想同現實。讀者可以喺書中體驗另一種人生，滿足對力量同自由嘅渴望。

---
*📝 本文由 黑洞 🌀 自動生成*
'''
    elif category == "analysis":
        content = f'''{emoji} **{title}**

{description}

## 🔍 深度解析

### 背景介紹

呢個話題喺修仙圈入面一直備受討論。今日我哋從多個角度嚟分析。

## 📊 核心要點

### 1. 設定邏輯

修仙世界觀嘅設定需要考慮以下因素：
- 世界觀嘅完整性
- 力量體系嘅平衡性
- 主角成長嘅合理性

### 2. 讀者心理

讀者喜歡修仙小說嘅深層次原因：
- 逃避現實嘅壓力
- 追求力量嘅夢想
- 情感共鳴嘅需求

### 3. 寫作技巧

高質量修仙小說嘅共同特點：

> "修仙唔只係寫飛劍法寶，更重要係寫人情世故。" —— 某資深書蟲

## 🎯 重點總結

| 面向 | 評價 |
|------|------|
| 世界觀 | ⭐⭐⭐⭐⭐ |
| 人物塑造 | ⭐⭐⭐⭐ |
| 戰鬥描寫 | ⭐⭐⭐ |
| 情感線 | ⭐⭐⭐⭐ |

---
*🔍 本文由 黑洞 🌀 自動生成*
'''
    else:  # tier
        content = f'''{emoji} **{title}**

{description}

## 🏆 排行榜

今次為大家帶來修仙界各方實力嘅詳細評級。

## 第一梯隊：天花板級別

呢個級別嘅角色已經接近修仙界嘅天花板，實力唔可以再用常規標準衡量。

### T0 超神級
- 擁有毀天滅地之力
- 已經超脫常規修仙體系
- 萬年難得一見嘅天才

### T1 頂尖級
- 各大宗門嘅頂梁柱
- 可以以一敵萬
- 擁有傳說級法寶

## 第二梯隊：強者級別

呢個級別已經係修仙界嘅精英：

| 等級 | 實力描述 | 代表人物 |
|------|----------|----------|
| A+ | 宗門長老級 | 各派長老 |
| A | 核心弟子級 | 天才師兄師姐 |
| A- | 普通精英 | 修煉有成人 |

## 第三梯隊：普通修仙者

呢個級別佔據修仙界大多數：

- 煉氣期修士（基層）
- 筑基期修士（小有所成）
- 金丹期修士（一方霸主）

## 💬 總結

修仙界實力為尊，但係實力唔係一切。有啲角色雖然實力唔係最強，但係人氣反而更高。

你認為邊個先係真正嘅最強？歡迎留言討論！

---
*🏆 本文由 黑洞 🌀 自動生成*
'''

    return content

def create_article(category: str) -> str:
    """創建一篇新文章"""
    # 根據分類選擇話題庫
    if category == "reviews":
        topic = random.choice(TOPICS_REVIEWS)
    elif category == "analysis":
        topic = random.choice(TOPICS_ANALYSIS)
    else:
        topic = random.choice(TOPICS_TIER)
    
    title, description = topic
    title = f"{CATEGORIES[category]['emoji']} {title}"
    
    # 生成文件名
    slug = generate_slug(title)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(CATEGORIES[category]["dir"], filename)
    
    # 確保目錄存在
    os.makedirs(CATEGORIES[category]["dir"], exist_ok=True)
    
    # 生成內容
    frontmatter = generate_frontmatter(title, category, tags=["修仙", "小說", "推薦"])
    article_content = generate_article_content(title, description, category)
    
    full_content = frontmatter + article_content
    
    # 寫入文件
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    print(f"✅ 文章已創建: {filepath}")
    return filepath

def main():
    """主函數"""
    os.chdir("/Users/kit99/xiuxian-blog")
    
    print("🌀 修仙研究院 - 文章生成器")
    print("=" * 40)
    
    # 隨機生成文章
    categories = list(CATEGORIES.keys())
    category = random.choice(categories)
    
    print(f"📝 正在生成文章...")
    filepath = create_article(category)
    
    print(f"\n✅ 完成！文章位置: {filepath}")
    print(f"💡 運行 'hugo server' 可以預覽網站")

if __name__ == "__main__":
    main()
