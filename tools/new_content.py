#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BizAI Hub - New Content Generator Tool
Used by AI Agents and developers to create new lessons or wiki entries
following the strict architectural rules in AGENTS.md.
"""

import sys
import os
import argparse
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")

def create_lesson(lesson_id, title, desc, category="講義簡報"):
    target_dir = os.path.join(ROOT_DIR, "lessons", lesson_id)
    target_file = os.path.join(target_dir, "index.html")
    template_path = os.path.join(TEMPLATES_DIR, "lesson_template.html")

    if os.path.exists(target_file):
        print(f"[ERROR] Lesson already exists at {target_file}")
        sys.exit(1)

    os.makedirs(target_dir, exist_ok=True)
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace("{{LESSON_ID}}", lesson_id)
    content = content.replace("{{LESSON_TITLE}}", title)
    content = content.replace("{{LESSON_DESCRIPTION}}", desc)
    content = content.replace("{{CATEGORY}}", category)
    content = content.replace("{{SLIDE_2_TITLE}}", "核心架構拆解")
    content = content.replace("{{SLIDE_2_LEAD}}", f"針對 {title} 進行結構化層次解析：")

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[SUCCESS] Created new lesson at: lessons/{lesson_id}/index.html")
    print(f"[NEXT STEP] Remember to add a card link in index.html and run python tools/validate_site.py")

def create_wiki(entry_id, title, desc, category="知識工程", raw_file=""):
    target_dir = os.path.join(ROOT_DIR, "wiki", entry_id)
    target_file = os.path.join(target_dir, "index.html")
    template_path = os.path.join(TEMPLATES_DIR, "wiki_template.html")

    if os.path.exists(target_file):
        print(f"[ERROR] Wiki entry already exists at {target_file}")
        sys.exit(1)

    os.makedirs(target_dir, exist_ok=True)
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    today_str = datetime.today().strftime('%Y-%m-%d')
    raw_filename = raw_file if raw_file else f"{entry_id}.md"
    raw_filepath = os.path.join(ROOT_DIR, "raw", raw_filename)

    # Karpathy Layer 1 Auto-provision: Ensure ground-truth raw file exists
    if not os.path.exists(raw_filepath):
        os.makedirs(os.path.join(ROOT_DIR, "raw"), exist_ok=True)
        raw_stub = f"""# 原始筆記：{title}

- 來源：BizAI Hub 客觀事實庫記錄
- 整理者：BizAI AI Agent
- 原始建檔日期：{today_str}
- 知識類別：{category}

---

## 1. 概念背景與客觀事實
{desc}

## 2. 核心技術特徵與事實記錄
- 事實要點 1：系統化架構與狀態運作定義。
- 事實要點 2：環境 Harness、工具邊界與資料流轉標準。

## 3. 商管實務與決策情境
- 本詞條記錄企業經理人評估導入時之關鍵維度與組織效益。
"""
        with open(raw_filepath, "w", encoding="utf-8") as rf:
            rf.write(raw_stub)
        print(f"[SUCCESS] Auto-created Karpathy Layer 1 raw source: raw/{raw_filename}")
    else:
        print(f"[INFO] Verified existing Karpathy Layer 1 raw source: raw/{raw_filename}")

    content = content.replace("{{ENTRY_TITLE}}", title)
    content = content.replace("{{ENTRY_DESCRIPTION}}", desc)
    content = content.replace("{{CATEGORY}}", category)
    content = content.replace("{{UPDATED_DATE}}", today_str)
    content = content.replace("{{CONCEPT_OVERVIEW_CONTENT}}", f"{title} 的系統性定義與架構邊界解析。")
    content = content.replace("{{BIZ_CASE_TITLE}}", f"企業落地的 {title} 實戰策略")
    content = content.replace("{{BIZ_CASE_CONTENT}}", "本區塊展示企管經理人如何運用此概念提升組織決策品質與作業效率。")
    content = content.replace("{{RAW_FILENAME}}", raw_filename)

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[SUCCESS] Created new wiki entry at: wiki/{entry_id}/index.html")
    print(f"[NEXT STEP] Remember to add a card link in index.html and run python tools/validate_site.py")

def main():
    parser = argparse.ArgumentParser(description="BizAI Hub Content Generator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Lesson sub-command
    lesson_parser = subparsers.add_parser("lesson", help="Create a new interactive slide lesson")
    lesson_parser.add_argument("--id", required=True, help="Kebab-case ID for the lesson (e.g. multi-agent)")
    lesson_parser.add_argument("--title", required=True, help="Title of the lesson")
    lesson_parser.add_argument("--desc", default="這是一份依據 AGENTS.md 產生的互動式講義簡報。", help="Brief description")
    lesson_parser.add_argument("--category", default="講義簡報", help="Badge category")

    # Wiki sub-command
    wiki_parser = subparsers.add_parser("wiki", help="Create a new LLM Wiki concept entry")
    wiki_parser.add_argument("--id", required=True, help="Kebab-case ID for the wiki entry (e.g. langgraph)")
    wiki_parser.add_argument("--title", required=True, help="Title of the wiki concept")
    wiki_parser.add_argument("--desc", default="這是一份依據 Karpathy 三層架構產生的 Wiki 概念詞條。", help="Brief summary")
    wiki_parser.add_argument("--category", default="知識詞條", help="Category badge")
    wiki_parser.add_argument("--raw", default="", help="Corresponding filename in raw/ directory")

    args = parser.parse_args()

    if args.command == "lesson":
        create_lesson(args.id, args.title, args.desc, args.category)
    elif args.command == "wiki":
        create_wiki(args.id, args.title, args.desc, args.category, args.raw)

if __name__ == "__main__":
    main()
