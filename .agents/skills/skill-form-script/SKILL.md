---
name: skill-form-script
description: 建立或修改 Skill 的 scripts/ 目錄中的單檔 Python 腳本時使用；處理腳本的依賴宣告、命令列介面、跨平台執行與驗證。
---

# SOP

## Phase 1 -- 理解與設計

1. `READ` 使用者需求、目標 Skill 的 `SKILL.md`，以及待修改的既有 Python 腳本（若有）。
2. `READ` 撰寫 Python 腳本時，讀取 `rules/Python腳本-格式規範.md` 的所有 Rule，建立 Python 腳本完成檢查清單。
3. `THINK` 依已載入的 Python 腳本完成檢查清單，確定腳本的輸入、輸出、副作用、完成條件、命令列參數、Python 版本要求與第三方依賴。

完成條件：已確定符合 Python 腳本完成檢查清單的目標腳本路徑與可驗證的執行介面。

## Phase 2 -- 寫入與驗證

1. `WRITE` 依已載入的 Python 腳本完成檢查清單，在目標 Skill 的 `scripts/` 目錄建立或更新單檔 Python 腳本。
2. `DELEGATE` 執行 `uv --version`；未安裝時依 [uv 官方安裝說明](https://docs.astral.sh/uv/getting-started/installation/) 選擇目前平台的安裝方式，安裝後重新檢查，無法安裝時停止並回報原因。
3. `DELEGATE` 使用 `uv run --script` 與測試資料執行腳本，檢查命令列說明與代表性的成功、失敗情境，記錄輸出和退出狀態。
4. `CHECK` 逐條驗證 Python 腳本完成檢查清單與執行結果；未通過時修正後重新檢查。

完成條件：腳本已寫入，Python 腳本完成檢查清單、執行介面與所有適用驗證均已通過。
