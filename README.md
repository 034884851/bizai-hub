# BizAI Hub・中原企管 AI Agent 落地實戰講義庫與知識 Wiki

[![Site Status](https://img.shields.io/badge/Status-Live%20Ready-brightgreen)](https://034884851.github.io/bizai-hub/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Design System](https://img.shields.io/badge/Design-DiveAI%20Style-orange)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Karpathy%20LLM%20Wiki-teal)](#)

> 本專案為中原大學企管系三丁 劉正祥（學號 11341461）之生成式 AI 實作成果：**建立一個自己的 AGENTS.md 或 CLAUDE.md**。  
> 告別單次拼湊的「Vibe Coding」，建立一套讓 AI 代理人（Claude / Codex / Antigravity / Cursor）能持續遵循、無限擴充新內容的企業級工程規準。

---

## 🌐 網頁成果與專案連結

- **線上瀏覽成果（GitHub Pages）**：[https://034884851.github.io/bizai-hub/](https://034884851.github.io/bizai-hub/) （或本機 `index.html`）
- **GitHub Repository**：[https://github.com/034884851/bizai-hub](https://github.com/034884851/bizai-hub)
- **專案核心規範文件**：[`AGENTS.md`](AGENTS.md) ｜ [`CLAUDE.md`](CLAUDE.md)
- **完整作業繳交報告**：[`作業說明與繳交報告.md`](作業說明與繳交報告.md)

---

## 🎯 專案核心特色

### 1. 雙核心架構交會：呆一布講義庫 ✕ Karpathy LLM Wiki
1. **互動式手帳講義庫（Slide Lessons）**：
   - 借鑑政大 TAICA / DiveAI「呆一布 AI 共學實驗室」的溫暖手帳風格（暖米色背景、深藍邊框、紙膠帶、戳記、黃色螢光底線）。
   - 具備純原生 JavaScript 簡報控制器，支援鍵盤方向鍵 `←` `→`、空白鍵、觸控滑動與全螢幕切換。
2. **Karpathy LLM Wiki 三層解耦知識庫**：
   - **Layer 1：`raw/`（事實源頭層）**：原始講義筆記，AI 嚴格唯讀。
   - **Layer 2：`wiki/`（知識詞條層）**：AI 依事實編纂概念頁，包含企管實例與高密度雙向互連。
   - **Layer 3：`AGENTS.md`（規範手冊層）**：定義 AI 的工作行為與代碼憲法。

### 2. 評分規準 9~10 分關鍵指標落實
- **專案規則清楚、具體**：根目錄維護了詳盡的 `AGENTS.md` 與 `CLAUDE.md`，定義色票、邊框、檔案放置、語意類別與禁止地雷。
- **AI 可以依照文件內容繼續新增或修改頁面**：提供 `templates/` 範本與 `tools/new_content.py` 生成指令，AI 接手時可一鍵生成標準頁面。
- **網頁內容與專案規則有良好對應**：全站頁面嚴格依循色彩代碼與手帳視覺語彙，杜絕硬編碼與拼裝感。
- **重複使用與延伸的可能性**：內建 `tools/validate_site.py` 自動化檢核套件，確保全站 0 死鏈、色票與元數據 100% 健全。

---

## 📂 專案目錄結構

```text
W9作業/
├── AGENTS.md                  # AI 代理通用員工手冊
├── CLAUDE.md                  # Claude Code 專案員工手冊
├── README.md                  # 專案公開說明文件（本檔）
├── 作業說明與繳交報告.md      # 完整作業繳交報告
├── index.html                 # 知識庫總覽大廳（即時搜尋、分類篩選、計數器）
├── styles/
│   ├── base.css               # 全域設計代碼（Tokens）、色票與版面底層
│   ├── slide.css              # 講義簡報專屬樣式與手帳裝飾
│   └── wiki.css               # Wiki 詞條專屬樣式與目錄排版
├── scripts/
│   ├── portal.js              # 大廳即時搜尋與分類過濾器
│   ├── slide.js               # 講義簡報鍵盤/觸控控制器
│   └── wiki.js                # Wiki 自動產生目錄與程式碼複製
├── templates/
│   ├── lesson_template.html   # 簡報擴充標準範本
│   └── wiki_template.html     # 詞條擴充標準範本
├── lessons/
│   ├── agent-harness/         # 第一單元：Model ＋ Harness 拆解與實作
│   └── prompt-to-agent/       # 第二單元：從 Prompt 提問到 Agentic 交辦
├── wiki/
│   ├── agentic-workflow/      # 概念 1：代理式工作流
│   ├── context-engineering/   # 概念 2：上下文工程
│   └── llm-wiki-architecture/ # 概念 3：Karpathy 三層架構
├── raw/
│   ├── 01_agent_basics.md     # 客觀事實源頭 01
│   ├── 02_context_design.md   # 客觀事實源頭 02
│   └── 03_karpathy_concept.md # 客觀事實源頭 03
└── tools/
    ├── new_content.py         # AI 擴充頁面自動生成工具
    └── validate_site.py       # 全站自動化測試與健全驗證套件
```

---

## 🚀 快速上手與本地測試

### 1. 運行全站自動化健全檢查 (CI 測試)
```pwsh
python tools/validate_site.py
```

### 2. 啟動本機即時預覽伺服器
```pwsh
python -m http.server 8000
```
於瀏覽器開啟 [http://localhost:8000](http://localhost:8000) 即可自由翻閱。

### 3. 命令列一鍵擴充新內容
- **新增互動講義**：
  ```pwsh
  python tools/new_content.py lesson --id multi-agent --title "Multi-Agent 團隊協作" --desc "解析 LangGraph 與 CrewAI 在企業流程中的多代理人協同實戰。"
  ```
- **新增 Wiki 詞條**：
  ```pwsh
  python tools/new_content.py wiki --id rag-vs-agent --title "RAG 與 Agent 決策矩陣" --desc "企業知識庫檢索與主動決策機制的深度對比。"
  ```

---

## 📜 授權與宣告
本專案為學術教學與實踐用途，視覺風格靈感源自國立政治大學 TAICA / DiveAI「呆一布 AI 共學實驗室」，架構理論引用自 Andrej Karpathy。
