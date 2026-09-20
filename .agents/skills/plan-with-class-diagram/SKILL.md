---
name: plan-with-class-diagram
description: Before implementing a feature or refactor that introduces or changes classes, propose a Mermaid class diagram, obtain explicit user confirmation, then implement according to the approved diagram and dependency order.
---

# SOP

## Phase 1 -- 分析與提案

1. `READ` 使用者需求、相關程式碼與專案規範。
2. `THINK` 設計必要的類別、責任、關係、相依性與開發順序。
3. `READ` 產生類別圖時，讀取 `rules/類別圖輸出-格式規範.md` 的所有 Rule，建立類別圖輸出檢查清單。
4. `WRITE` 依已載入的類別圖輸出檢查清單產出 Mermaid `classDiagram`、簡短設計說明與實作順序。
5. `CHECK` 逐條驗證類別圖輸出檢查清單，並確認類別圖涵蓋需求且關係一致。

完成條件：類別圖輸出檢查清單均已通過，提案可供使用者評估，且程式碼尚未修改。

## Phase 2 -- 確認提案

1. `WRITE` 向使用者展示類別圖、設計說明與實作順序，並請求明確確認。
2. `CHECK` 使用者回覆；要求修改時返回 Phase 1，未明確確認時停止執行。

完成條件：使用者已明確確認目前版本的類別圖與實作順序。

## Phase 3 -- 按圖開發與驗證

1. `READ` 已確認的類別圖、最新的相關程式碼與專案規範。
2. `THINK` 依類別相依性確定實作順序；實際狀態需要改變類別圖時，返回 Phase 1 修訂並重新取得確認。
3. `WRITE` 依已確認的類別圖與實作順序修改程式碼。
4. `CHECK` 類別組織符合已確認的類別圖，並執行適用的測試、型別檢查與 lint。

完成條件：程式碼符合已確認的類別圖，且所有適用驗證結果已回報。
