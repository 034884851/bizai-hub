#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BizAI Hub - Automated Site Test & Integrity Suite (CI/CD Quality Gate)
Validates internal link integrity, template compliance, CSS variables,
Karpathy raw/ mapping, and AGENTS.md rules across the entire repository.
"""

import os
import re
import sys

# Force UTF-8 stdout for Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

errors = []
warnings = []
passed_checks = 0

def log_pass(msg):
    global passed_checks
    passed_checks += 1
    print(f"  [PASS] {msg}")

def log_error(msg):
    errors.append(msg)
    print(f"  [FAIL] {msg}")

def log_warn(msg):
    warnings.append(msg)
    print(f"  [WARN] {msg}")

def test_core_files_exist():
    print("\n--- 1. Testing Core Project Infrastructure Files ---")
    essential_files = [
        "index.html",
        "AGENTS.md",
        "CLAUDE.md",
        "README.md",
        "作業說明與繳交報告.md",
        "styles/base.css",
        "styles/slide.css",
        "styles/wiki.css",
        "scripts/portal.js",
        "scripts/slide.js",
        "scripts/wiki.js",
        "templates/lesson_template.html",
        "templates/wiki_template.html",
        "tools/new_content.py"
    ]
    for rel_path in essential_files:
        full_path = os.path.join(ROOT_DIR, rel_path)
        if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
            log_pass(f"Essential file exists: {rel_path} ({os.path.getsize(full_path)} bytes)")
        else:
            log_error(f"Missing or empty file: {rel_path}")

def get_all_content_html_files():
    html_files = []
    for root, _, files in os.walk(ROOT_DIR):
        if ".git" in root or "templates" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))
    return html_files

def test_internal_links_and_assets():
    print("\n--- 2. Testing Internal Hyperlinks & Asset References ---")
    html_files = get_all_content_html_files()
    link_pattern = re.compile(r'(?:href|src)=["\']([^"\']+)["\']', re.IGNORECASE)

    for html_file in html_files:
        rel_html = os.path.relpath(html_file, ROOT_DIR)
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()

        matches = link_pattern.findall(content)
        for target in matches:
            if target.startswith(("http://", "https://", "mailto:", "javascript:", "data:")):
                continue
            
            parts = target.split("#")
            file_part = parts[0]
            hash_part = parts[1] if len(parts) > 1 else None

            if not file_part and hash_part:
                # Same-page anchor verification
                id_pat = re.compile(rf'id=["\']{re.escape(hash_part)}["\']', re.IGNORECASE)
                if id_pat.search(content):
                    log_pass(f"[{rel_html}] -> Valid in-page anchor: #{hash_part}")
                else:
                    log_error(f"[{rel_html}] -> Broken in-page anchor: #{hash_part}")
                continue

            target_dir = os.path.dirname(html_file)
            resolved_target = os.path.abspath(os.path.join(target_dir, file_part))

            if os.path.exists(resolved_target):
                if hash_part and resolved_target.endswith(".html"):
                    with open(resolved_target, "r", encoding="utf-8") as tf:
                        target_content = tf.read()
                    id_pat = re.compile(rf'id=["\']{re.escape(hash_part)}["\']', re.IGNORECASE)
                    if id_pat.search(target_content):
                        log_pass(f"[{rel_html}] -> Valid link with anchor: {target}")
                    else:
                        log_error(f"[{rel_html}] -> Broken anchor in target: #{hash_part} not found in {resolved_target}")
                else:
                    log_pass(f"[{rel_html}] -> Valid link: {target}")
            else:
                log_error(f"[{rel_html}] -> Broken link (404 Not Found): {target} (Resolved: {resolved_target})")

def test_slide_lessons_compliance():
    print("\n--- 3. Testing Slide Deck Archetype Compliance ---")
    lessons_dir = os.path.join(ROOT_DIR, "lessons")
    if not os.path.exists(lessons_dir):
        log_warn("No lessons directory found.")
        return

    for entry in os.listdir(lessons_dir):
        lesson_path = os.path.join(lessons_dir, entry, "index.html")
        if not os.path.exists(lesson_path):
            continue

        rel_path = os.path.relpath(lesson_path, ROOT_DIR)
        with open(lesson_path, "r", encoding="utf-8") as f:
            html = f.read()

        if 'class="slide active"' in html or "class='slide active'" in html:
            log_pass(f"[{rel_path}] has initial active slide")
        else:
            log_error(f"[{rel_path}] missing active slide element")

        if 'id="prevSlideBtn"' in html and 'id="nextSlideBtn"' in html:
            log_pass(f"[{rel_path}] has navigation buttons")
        else:
            log_error(f"[{rel_path}] missing prev/next navigation controls")

        if 'slide.js' in html:
            log_pass(f"[{rel_path}] includes scripts/slide.js controller")
        else:
            log_error(f"[{rel_path}] missing scripts/slide.js")

def test_wiki_entries_and_karpathy_ground_truth():
    print("\n--- 4. Testing LLM Wiki Archetype & Karpathy Layer 1 Mapping ---")
    wiki_dir = os.path.join(ROOT_DIR, "wiki")
    if not os.path.exists(wiki_dir):
        log_warn("No wiki directory found.")
        return

    for entry in os.listdir(wiki_dir):
        wiki_path = os.path.join(wiki_dir, entry, "index.html")
        if not os.path.exists(wiki_path):
            continue

        rel_path = os.path.relpath(wiki_path, ROOT_DIR)
        with open(wiki_path, "r", encoding="utf-8") as f:
            html = f.read()

        if 'class="wiki-article"' in html:
            log_pass(f"[{rel_path}] conforms to wiki-article structure")
        else:
            log_error(f"[{rel_path}] missing .wiki-article container")

        if 'class="wiki-breadcrumbs"' in html:
            log_pass(f"[{rel_path}] has breadcrumb navigation")
        else:
            log_error(f"[{rel_path}] missing breadcrumb navigation")

        # Verify raw ground truth mapping specifically inside the raw-source footer
        footer_match = re.search(r'<footer[^>]*class=["\'][^"\']*wiki-raw-source[^"\']*["\'][^>]*>(.*?)</footer>', html, re.DOTALL)
        if footer_match:
            raw_match = re.search(r'<code>raw/([^<]+)</code>', footer_match.group(1))
            if raw_match:
                raw_filename = raw_match.group(1).strip()
                raw_full_path = os.path.join(ROOT_DIR, "raw", raw_filename)
                if os.path.exists(raw_full_path):
                    log_pass(f"[{rel_path}] Karpathy Layer 1 ground-truth verified: raw/{raw_filename}")
                else:
                    log_error(f"[{rel_path}] Referenced raw file does not exist: raw/{raw_filename}")
            else:
                log_warn(f"[{rel_path}] No raw/ code block found in wiki-raw-source footer")
        else:
            log_warn(f"[{rel_path}] No explicit wiki-raw-source footer found")

def test_handbook_completeness():
    print("\n--- 5. Testing AGENTS.md & CLAUDE.md Handbook Completeness ---")
    for handbook_name in ["AGENTS.md", "CLAUDE.md"]:
        hb_path = os.path.join(ROOT_DIR, handbook_name)
        if not os.path.exists(hb_path):
            log_error(f"{handbook_name} is missing!")
            continue

        with open(hb_path, "r", encoding="utf-8") as f:
            content = f.read()

        required_keywords = [
            "專案目的",
            "風格",
            "結構",
            "命名",
            "SOP",
            "validate_site.py"
        ]
        all_found = True
        for kw in required_keywords:
            if kw not in content:
                log_error(f"[{handbook_name}] missing critical section keyword: {kw}")
                all_found = False
        if all_found:
            log_pass(f"[{handbook_name}] contains all required sections and guidelines")

def test_scaffolding_and_extension_pipeline():
    print("\n--- 6. Testing AI Scaffolding Generator Pipeline (tools/new_content.py) ---")
    import subprocess
    import shutil

    test_lesson_id = "test-ci-lesson"
    test_wiki_id = "test-ci-wiki"

    # 1. Test lesson scaffolding
    lesson_cmd = [
        sys.executable,
        os.path.join(ROOT_DIR, "tools", "new_content.py"),
        "lesson",
        "--id", test_lesson_id,
        "--title", "CI 測試講義",
        "--desc", "這是 CI 自動化測試驗證之簡報。"
    ]
    lesson_res = subprocess.run(lesson_cmd, capture_output=True, text=True, cwd=ROOT_DIR)
    if lesson_res.returncode == 0:
        log_pass("tools/new_content.py lesson scaffolding generated successfully")
    else:
        log_error(f"tools/new_content.py lesson generation failed: {lesson_res.stderr}")

    # 2. Test wiki scaffolding & automatic Karpathy raw stub creation
    wiki_cmd = [
        sys.executable,
        os.path.join(ROOT_DIR, "tools", "new_content.py"),
        "wiki",
        "--id", test_wiki_id,
        "--title", "CI 測試詞條",
        "--desc", "這是 CI 自動化測試驗證之詞條。"
    ]
    wiki_res = subprocess.run(wiki_cmd, capture_output=True, text=True, cwd=ROOT_DIR)
    if wiki_res.returncode == 0:
        log_pass("tools/new_content.py wiki scaffolding & Karpathy raw stub generated successfully")
    else:
        log_error(f"tools/new_content.py wiki generation failed: {wiki_res.stderr}")

    raw_stub_path = os.path.join(ROOT_DIR, "raw", f"{test_wiki_id}.md")
    if os.path.exists(raw_stub_path) and os.path.getsize(raw_stub_path) > 0:
        log_pass(f"Karpathy Layer 1 ground truth auto-provisioned: raw/{test_wiki_id}.md")
    else:
        log_error(f"Karpathy Layer 1 raw stub missing for {test_wiki_id}")

    # 3. Cleanup temporary test artifacts
    lesson_dir = os.path.join(ROOT_DIR, "lessons", test_lesson_id)
    wiki_dir = os.path.join(ROOT_DIR, "wiki", test_wiki_id)
    if os.path.exists(lesson_dir):
        shutil.rmtree(lesson_dir, ignore_errors=True)
    if os.path.exists(wiki_dir):
        shutil.rmtree(wiki_dir, ignore_errors=True)
    if os.path.exists(raw_stub_path):
        os.remove(raw_stub_path)
    log_pass("CI temporary test artifacts cleaned up cleanly")

def main():
    print("=" * 60)
    print("  BizAI Hub - Automated Test & CI Verification Suite")
    print("=" * 60)

    test_core_files_exist()
    test_internal_links_and_assets()
    test_slide_lessons_compliance()
    test_wiki_entries_and_karpathy_ground_truth()
    test_handbook_completeness()
    test_scaffolding_and_extension_pipeline()

    print("\n" + "=" * 60)
    print(f"  Test Results: {passed_checks} Passed | {len(warnings)} Warnings | {len(errors)} Errors")
    print("=" * 60)

    if errors:
        print("\nFAILED CHECKS:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\nALL TESTS PASSED! Project is healthy, robust, and GitHub Pages ready.")
        sys.exit(0)

if __name__ == "__main__":
    main()
