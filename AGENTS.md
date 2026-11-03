# BizAI Hub - AI 代理協作規範與員工守則 (AGENTS.md)

> **版本**：v1.0.0  
> **適用代理系統**：OpenAI Codex、Antigravity、Cursor、Devin 及遵循 AGENTS.md 協議之所有自主 AI 代理人。  
> **核心使命**：規範 AI 在本專案中之行為準則、架構守則、設計語彙與自動化擴充標準作業程序（SOP），使後續接手之任何 AI 員工皆能「零歧義、零偏誤、免反覆提示」地持續維護與擴充本專案。

---

## 📌 一、專案目的與核心願景 (Mission & Architecture)

1. **專案定位**：
   - 本專案名為 **【BizAI Hub】（政大企管 AI Agent 落地實戰知識庫與講義庫）**。
   - 專門為商管領域學生、企業數位轉型經理人與 AI 實踐者打造之互動教學與概念 Wiki 平台。
2. **與一般 Vibe Coding 的根本差異**：
   - **Vibe Coding** 的目標是「把這一個網頁湊出來」（單次拼裝、缺乏延展性）。
   - **BizAI Hub** 的核心目標是「建立一套長久演進的開發憲法」：制定出精確的元件規範、三層資料解耦架構與自動化驗收規準，讓未來的 AI 員工閱讀本文件後，能以完全相同的標準、程式碼慣例與視覺品質，自主擴充全新的互動簡報與知識詞條。
3. **架構參考標準**：
   - 互動簡報體系：全面借鑑並強化國立政治大學 TAICA / DiveAI「呆一布 AI 共學實驗室」之手帳互動風格。
   - 知識庫體系：嚴格遵循 Andrej Karpathy 提出之 **LLM Wiki 三層解耦架構**（`raw/` 原始數據層 → `wiki/` 知識詞條層 → `AGENTS.md` 規則手冊層）。

---

## 🎨 二、設計系統與視覺語彙標準 (Design System & Tokens)

所有頁面嚴禁自訂隨意色碼或破壞視覺統一性。必須嚴格引用 `styles/base.css` 所定義之 CSS 自訂屬性變數：

### 1. 嚴格色票規範 (Color Tokens)
| 變數名稱 | 色碼 HEX | 語意用途與限制 |
| :--- | :--- | :--- |
| `--cream` | `#FCF8F0` | 全域主要背景暖米色，搭配微點狀網格背景。 |
| `--paper` | `#FFFDF8` | 手帳紙張白底色，用於側邊欄、次要卡片與對帳表。 |
| `--navy` | `#1E3A5F` | 主題深藍色。所有大標題（H1~H4）、核心邊框（3px）與主要重要文字。 |
| `--blue` | `#5FA8C4` | 輔助亮藍色。用於副標題、次要按鈕、關聯超連結。 |
| `--sky-soft` | `#D6EEF6` | 柔天藍底色。用於標籤背景、重點螢光標記（`.u-highlight-blue`）。 |
| `--blush` | `#F4B3BE` | 腮紅粉。用於手繪虛線點、警告膠帶、強調戳記。 |
| `--teal` | `#7CCBC9` | 科技薄荷綠。用於商業案例框（`.biz-case-box`）、企管實務徽章。 |
| `--yellow` | `#F7E6A8` | 暖陽黃。用於主行動按鈕（`.btn-action`）、標題重點底線（`.u-highlight`）。 |
| `--ink` | `#2C3E50` | 內文標準閱讀深墨色（行距 1.7）。 |

### 2. 手帳風專屬裝飾元件類別
- **手帳紙膠帶（`.tape`）**：必須置於卡片或簡報頂端角落。可搭配樣式 `.tape-left`、`.tape-right`、`.tape-pink`、`.tape-yellow`、`.tape-teal`。
- **手繪圓形戳記（`.sticker`）**：用於步驟序號（1、2、3）或概念圖騰（腦、手、ROI、SOP）。
- **手繪虛線分隔線（`.hand-line`）**：置於每個大標題下方，提供溫暖人文質感。
- **撕紙便條卡（`.note-dash`）**：具備 3px 虛線邊框，用於重點提示與警語。
- **重點營造底線（`.u-highlight`）**：使用漸層背景模擬黃色螢光筆劃線。

---

## 📐 三、三大頁面原型架構規範 (Page Archetypes)

任何新增或修改的網頁，必須嚴格符合以下三種原型之一：

### 原型 A：互動講義簡報頁 (Interactive Slide Deck)
- **目錄定位**：`lessons/<lesson-id>/index.html`
- **DOM 層級規範**：
  ```html
  <main class="slide-viewport">
    <header class="slide-topbar"> ... </header>
    <div class="deck-stage">
      <div class="deck-container">
        <!-- 每一頁簡報必須是一個 section.slide -->
        <section class="slide active" id="slide-1">
          <div class="tape tape-left"></div>
          <div class="slide-content-pad">
            <span class="slide-category">章節類別</span>
            <h1 class="slide-title">簡報主標題</h1>
            <div class="hand-line"></div>
            <p class="slide-lead">導引段落</p>
            <!-- 核心圖表、cards 或 data-table -->
            <div class="slide-oneline">一言以蔽之的洞察結論</div>
            <div class="slide-pageno">01</div>
          </div>
        </section>
        <!-- 接續 slide 2, slide 3 ... -->
      </div>
    </div>
    <!-- 浮動導覽控制器（必須具備） -->
    <nav class="slide-controls">
      <button id="prevSlideBtn">‹ 上一頁</button>
      <div class="slide-progress-track"><div class="slide-progress-fill" id="slideProgressFill"></div></div>
      <span class="control-counter" id="slideCounter">01 / 06</span>
      <button id="nextSlideBtn">下一頁 ›</button>
      <button id="fullscreenBtn">⛶</button>
    </nav>
  </main>
  <script src="../../scripts/slide.js"></script>
  ```
- **互動機制**：必須引入 `scripts/slide.js`，支援鍵盤方向鍵（`←` / `→`）、空白鍵、行動裝置左右滑動、全螢幕切換（`F`）及 URL Hash 路由（如 `#3`）。

### 原型 B：LLM Wiki 知識庫詞條頁 (Knowledge Entry)
- **目錄定位**：`wiki/<entry-id>/index.html`
- **Karpathy 架構規範**：
  1. 必須在頁尾透過 `.wiki-raw-source` 明確指向 `raw/` 中的對應事實源頭檔案（例如 `raw/01_agent_basics.md`）。
  2. 必須包含麵包屑導覽（`.wiki-breadcrumbs`）：`首頁 › LLM Wiki 知識庫 › 詞條標題`。
  3. 必須包含側邊欄 TOC（`<aside class="wiki-sidebar">` 搭配 `<ul id="tocList">`），並引入 `scripts/wiki.js` 實現自動標題抓取與 ScrollSpy 滾動追蹤。
  4. 必須具備【企管商務落地案例】區塊（`.biz-case-box`），體現商管決策價值。
  5. 必須具備【雙向互連超連結】（`<a class="wiki-link" href="...">`），形成網狀知識圖譜。

### 原型 C：知識大廳總覽頁 (Portal Hub Index)
- **目錄定位**：根目錄 `index.html`
- **功能規範**：
  - 具備 Hero 介紹、評分規準對應區塊與即時搜尋列（`#hubSearchInput`）。
  - 具備分類篩選標籤（全部、講義簡報、知識庫詞條）。
  - 具備即時項目計數器（`#contentCountDisplay`）與查無結果狀態提示（`#emptySearchState`）。
  - 具備 `AGENTS.md` 彈窗預覽功能（`#openAgentsModalBtn`），方便批改與展示。

---

## 📂 四、目錄結構與命名規約 (File Placement & Naming)

```
W9作業/
├── AGENTS.md                  <-- AI 代理通用員工手冊（本文件）
├── CLAUDE.md                  <-- Claude Code 專用映射手冊
├── README.md                  <-- 專案 GitHub 介紹首頁與公開連結
├── 作業說明與繳交報告.md      <-- 完整作業繳交報告（含標題、連結、申論）
├── index.html                 <-- 知識庫大廳入口
├── styles/
│   ├── base.css               <-- 全域設計代碼（Tokens）與基礎排版
│   ├── slide.css              <-- 簡報專屬樣式與動畫
│   └── wiki.css               <-- Wiki 專屬樣式與側邊欄排版
├── scripts/
│   ├── portal.js              <-- 大廳即時搜尋與分類過濾器
│   ├── slide.js               <-- 簡報鍵盤/觸控控制器
│   └── wiki.js                <-- Wiki TOC 生成與程式碼複製器
├── templates/
│   ├── lesson_template.html   <-- 簡報擴充標準範本
│   └── wiki_template.html     <-- 詞條擴充標準範本
├── lessons/
│   ├── agent-harness/         <-- 第一單元：Model ＋ Harness
│   └── prompt-to-agent/       <-- 第二單元：Prompt 到 Agentic
├── wiki/
│   ├── agentic-workflow/      <-- 概念 1：代理式工作流
│   ├── context-engineering/   <-- 概念 2：上下文工程
│   └── llm-wiki-architecture/ <-- 概念 3：Karpathy 三層架構
├── raw/
│   ├── 01_agent_basics.md     <-- 事實數據來源 01
│   ├── 02_context_design.md   <-- 事實數據來源 02
│   └── 03_karpathy_concept.md <-- 事實數據來源 03
└── tools/
    ├── new_content.py         <-- AI 自動化生成頁面工具
    └── validate_site.py       <-- 全站自動化測試與健全驗證套件
```

### 命名硬性限制：
1. 目錄與 HTML 檔名一律使用小寫英數字與連字號（`kebab-case`），例如 `lessons/agent-harness/index.html`。
2. 原始事實筆記一律存放於 `raw/`，檔名採雙位數序號加底線，例如 `raw/01_agent_basics.md`。

---

## 🚀 五、AI 擴充與維護作業標準程序 (AI Development SOP)

當人類使用者向 AI 發出交辦：「幫我新增一個關於 [...] 的講義簡報」或「幫我新增一個 [...] 的 Wiki 詞條」時，AI **必須嚴格依序執行以下 5 個步驟**：

### 步驟 1：檢驗事實來源 (Ground Truth Check)
- 檢查 `raw/` 目錄中是否存在對應的事實筆記。若無，先在 `raw/` 建立客觀事實來源（如 `raw/04_multi_agent.md`），杜絕幻覺捏造。

### 步驟 2：調用生成工具或範本 (Scaffold)
- 優先使用內建生成命令建立骨架：
  - 新增講義：`python tools/new_content.py lesson --id <id> --title "<標題>" --desc "<簡介>"`
  - 新增詞條：`python tools/new_content.py wiki --id <id> --title "<標題>" --desc "<簡介>" --raw "<raw檔名>"`

### 步驟 3：填寫結構化語意內容 (Fill Content)
- 必須遵循第二章之色票與裝飾元素。
- 中文文案**一律使用繁體中文（台灣，zh-TW）與全形標點符號**（`，`、`。`、`！`、`？`、`：`）。
- 詞條必須包含【企管商務落地案例】與至少 2 個連往既有詞條或講義的 `class="wiki-link"` 雙向連結。

### 步驟 4：登錄回首頁總覽 (Register in index.html)
- 在 `index.html` 中的 `#lessons-section` 或 `#wiki-section` 增加對應的卡片，填入 `data-tags` 與標題簡介，確保即時搜尋能索引到新頁面。

### 步驟 5：執行主動防禦驗證 (Automated Verification)
- 終端機執行：
  ```pwsh
  python tools/validate_site.py
  ```
- 驗收指標：必須達到 **0 個錯誤（0 Errors）**。若出現任何 Broken link、缺少標籤或未對應之 raw 檔案，必須立即修復直到全數通過。

---

## ⛔ 六、不可違反之地雷紅線 (Strict Inviolables)

1. **嚴禁引入重型建置依賴**：不准引入 Webpack、Vite、Node.js build step 或肥大 npm 套件，確保純靜態檔案隨推即呈現在 GitHub Pages。
2. **嚴禁篡改 `raw/` 內容**：Wiki 詞條是合成層，`raw/` 是真實基準，AI 只能讀取 `raw/`，不可任意刪減。
3. **嚴禁破壞向後相容性**：修改 CSS 時不可移除既有變數名稱或破壞簡報控制器 `slide.js` 的事件綁定。
4. **嚴禁提交未經驗證之代碼**：任何改動必須在本地經過 `validate_site.py` 測試通過，絕不交付破碎或死鏈之代碼。
