# BizAI Hub - Claude Code 專案指南與員工手冊 (CLAUDE.md)

> 本文件為 Anthropic Claude Code 及 Claude 代理專用規約，與根目錄 `AGENTS.md` 嚴格同步對齊。Claude 開工前請務必遵循本文件之規範。

---

## 🎯 一、專案目的與核心願景 (Mission & Architecture)
- **專案名稱**：BizAI Hub・中原企管 AI Agent 落地實戰講義庫與知識 Wiki
- **專案目的**：
  1. 純靜態、零依賴、GitHub Pages 友善架構（純 HTML5 + Modern CSS + Vanilla JS）。
  2. 借鑑國立政治大學 TAICA / DiveAI「呆一布講義庫」手帳風互動設計。
  3. 實踐 Andrej Karpathy 的 LLM Wiki 三層解耦架構（`raw/` -> `wiki/` -> `AGENTS.md` / `CLAUDE.md`）。
  4. 讓 AI 能以同一套規範持續擴充新頁面，達成可延展、可維護的系統目標。

---

## 🎨 二、視覺風格與色票速查 (Visual Style & Tokens)

整體視覺風格嚴格採用手帳插畫風格，所有頁面必須使用 `styles/base.css` 的設計代碼：

```css
--cream: #FCF8F0;       /* 主背景暖米色 */
--paper: #FFFDF8;       /* 紙張白 */
--navy: #1E3A5F;        /* 標題與主邊框 3px solid */
--blue: #5FA8C4;        /* 強調亮藍 */
--sky-soft: #D6EEF6;    /* 標籤底色 */
--blush: #F4B3BE;       /* 腮紅粉手帳虛線點與紙膠帶 */
--teal: #7CCBC9;        /* 企管商業案例卡片邊框 */
--yellow: #F7E6A8;      /* 行動按鈕與螢光底線 */
--ink: #2C3E50;         /* 內文主要文字 */
```

### 裝飾語意類別速查：
- `.tape` / `.tape-pink` / `.tape-yellow` / `.tape-teal`：手帳紙膠帶裝飾
- `.sticker`：手繪序號圓戳記
- `.hand-line`：大標題下方的圓點虛線
- `.note-dash`：撕紙便條卡
- `.u-highlight`：黃色螢光筆底線
- `.biz-case-box`：企管商業落地實例卡片
- `.wiki-link`：雙向互連超連結

---

## 📂 三、頁面結構與檔案命名規範 (Page Structure & File Naming)

### 1. 頁面結構原型 (Archetypes)
- **原型 A：講義簡報頁 (Slide Deck)**：位於 `lessons/<id>/index.html`，具備鍵盤翻頁與全螢幕控制器。
- **原型 B：LLM Wiki 詞條頁**：位於 `wiki/<id>/index.html`，具備側邊欄目錄與 `raw/` 原始資料對照。
- **原型 C：大廳總覽頁**：位於根目錄 `index.html`，具備即時搜尋與計數器。

### 2. 檔案命名與放置標準 (File Placement & Naming)
- 檔案命名一律使用小寫英數字與連字號（`kebab-case`）。
- 原始資料存放於 `raw/`，檔名採數字前綴，例如 `raw/01_agent_basics.md`。

---

## 🛠️ 四、開發常用指令 (Common Development Commands)

Claude 在操作本專案時，可直接在終端機執行下列指令：

### 1. 執行全站健全度與測試驗收（每次修改後必跑）
```pwsh
python tools/validate_site.py
```
> 測試包含：核心檔案存在性、內部所有鏈結與資源是否 404、簡報控制器相容性、Wiki 詞條與 `raw/` 原始資料對應性、手冊完整度。

### 2. 新增互動講義簡報 (Lesson)
```pwsh
python tools/new_content.py lesson --id <kebab-case-id> --title "<課程標題>" --desc "<課程簡介>"
```

### 3. 新增 LLM Wiki 知識詞條 (Wiki Entry)
```pwsh
python tools/new_content.py wiki --id <kebab-case-id> --title "<詞條名稱>" --desc "<概念摘要>" --raw "<raw/對應檔名.md>"
```

### 4. 本地啟動即時預覽伺服器
```pwsh
python -m http.server 8000
```
> 於瀏覽器開啟 `http://localhost:8000` 即可預覽全站。

---

## 📋 五、AI 擴充標準作業程序 (AI Development SOP)
1. **事實檢查**：檢查 `raw/` 目錄中是否有客觀事實源。
2. **生成腳手架**：調用 `python tools/new_content.py`。
3. **編寫內容**：繁體中文（zh-TW）、全形標點符號、嵌入企管實務案例與雙向連結。
4. **登錄大廳**：在 `index.html` 的卡片網格中加入新卡片，標註 `data-tags`。
5. **主動驗證**：執行 `python tools/validate_site.py`，確保 0 報錯。

---

## ⚠️ 六、Claude 核心禁止事項 (Strict Inviolables)
- 禁止引入 Node.js / NPM 打包工具，保持原生純靜態。
- 禁止修改或刪除 `raw/` 目錄下的客觀事實筆記。
- 禁止隨意覆蓋全域 CSS 變數，維護風格一致性。
- 禁止提交未通過 `validate_site.py` 測試的程式碼。
