# 原始筆記 02：從 Prompt Engineering 到 Context Engineering

- 來源：商管企管數位轉型實戰專題筆記
- 整理者：Simon (中原 企管系)
- 原始建檔日期：2026-11-03

---

## 1. 概念演化：Prompt vs Context
- **Prompt Engineering（提示詞工程）**：聚焦於單次提問的措辭優化（例如 Few-Shot、角色扮演、思考鏈 CoT）。但一旦對話刷新，模型失去記憶，下次又得重複輸入大量前提。
- **Context Engineering（上下文工程）**：聚焦於「系統性環境脈絡配置」。將專案背景、業務邏輯、命名規範、設計規範以靜態檔案（`AGENTS.md` / `CLAUDE.md`）常駐於專案根目錄，使每一次啟動的 Agent 都能自動載入完整上下文。

## 2. 解決 AI「每天第一天上班」的失憶症
- 痛點：AI 每次開啟新工作階段（Session），都是失憶狀態。
- 解決方案：專案規則檔（Handbook）。
- 四大要素：
  1. **專案是什麼（What is this）**：目標、客群、架構定位。
  2. **工程與業務習慣（Conventions）**：命名標準、技術棧、CSS 變數、版型結構。
  3. **絕對禁令（Inviolables）**：不可刪改的根檔案、不能破壞的向後相容性、中文標點規定。
  4. **驗收驗證標準（Verification）**：完成後的確認指令（語法檢核、單元測試、連結查驗）。
