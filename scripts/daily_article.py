#!/usr/bin/env python3
"""
修仙研究院 - 每日文章生成器
用於 GitHub Actions 自動化
"""

import os
import sys
import random
import json
from datetime import datetime

# 添加父目錄到路徑以便導入
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generate_article import create_article, CATEGORIES

def main():
    """每日生成一篇文章"""
    print(f"🌀 修仙研究院 - 每日文章生成器")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 40)
    
    # 隨機選擇分類
    categories = list(CATEGORIES.keys())
    weights = [0.5, 0.3, 0.2]  # reviews 50%, analysis 30%, tier 20%
    category = random.choices(categories, weights=weights)[0]
    
    print(f"📝 正在生成文章 (分類: {CATEGORIES[category]['name']})...")
    
    try:
        filepath = create_article(category)
        print(f"\n✅ 當日文章生成完成!")
        return 0
    except Exception as e:
        print(f"\n❌ 生成失敗: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
