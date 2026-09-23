---
name: plan-with-class-diagram
description: Before implementing a feature or refactor that introduces or changes classes, propose a Mermaid class diagram, obtain explicit user confirmation, then implement according to the approved diagram and dependency order.
---

# SOP

## Phase 1 -- 分析與提案

1. `READ` 使用者需求、相關程式碼、專案規範，以及專案根目錄下既有的 `specs/plan/` 計畫目錄（若存在）。
2. `READ` 設計類別時，讀取 `rules/類別設計-格式規範.md` 的所有 Rule，建立類別設計檢查清單。
3. `THINK` 依已載入的類別設計檢查清單，設計必要的類別、責任、關係、相依性與開發順序；並決定本次計畫名稱及下一個可用的兩位數編號 `<NN>`（從既有最大編號加一，沒有既有計畫時從 `01` 開始）。
4. `CHECK` 逐條驗證類別設計檢查清單；未通過時修正設計。
5. `READ` 產生類別圖時，讀取 `rules/類別圖輸出-格式規範.md` 的所有 Rule，建立類別圖輸出檢查清單。
6. `READ` `templates/class-diagram-proposal.md` 與 `templates/class-diagram-proposal.example.md`，載入骨架與範例，命名載入結果為「類別圖提案樣板組」。
7. `WRITE` 依已載入的類別圖輸出檢查清單與「類別圖提案樣板組」，建立計畫目錄，將完整 Markdown 類別圖提案檔寫入專案根目錄下的 `specs/plan/<NN>-<本次計畫名稱>/class-diagram-proposal.md`；第一個頂層 Section 放置 Mermaid 類別圖，第二個頂層 Section 放置設計說明與實作順序。
8. `CHECK` 逐條驗證類別圖輸出檢查清單，並確認提案檔位於指定路徑、兩個頂層 Section 結構、Mermaid 類別圖、設計說明與實作順序彼此一致且涵蓋需求。

完成條件：類別設計與類別圖輸出檢查清單均已通過，完整 Markdown 類別圖提案檔可供使用者評估，且程式碼尚未修改。

## Phase 2 -- 確認提案

1. `WRITE` 向使用者展示完整 Markdown 類別圖提案檔（第一個頂層 Section 為 Mermaid 類別圖，第二個頂層 Section 為設計說明與實作順序），並請求明確確認。
2. `CHECK` 使用者回覆；要求修改時返回 Phase 1，未明確確認時停止執行。

完成條件：使用者已明確確認目前版本的 Markdown 類別圖提案檔與實作順序。

## Phase 3 -- 按圖開發與驗證

1. `READ` 已確認的 Markdown 類別圖提案檔、最新的相關程式碼與專案規範。
2. `THINK` 依已確認的 Markdown 類別圖提案檔中的類別圖與類別相依性確定實作順序；實際狀態需要改變類別圖時，返回 Phase 1 修訂並重新取得確認。
3. `WRITE` 依已確認的 Markdown 類別圖提案檔與實作順序修改程式碼。
4. `CHECK` 類別組織符合已確認的 Markdown 類別圖提案檔中的類別圖，並執行適用的測試、型別檢查與 lint。

完成條件：程式碼符合已確認的 Markdown 類別圖提案檔中的類別圖，且所有適用驗證結果已回報。
