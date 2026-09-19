---
name: plan-with-class-diagram
description: Before implementing a feature or refactor that introduces or changes classes, propose a Mermaid class diagram, obtain explicit user confirmation, then implement according to the approved diagram and dependency order.
---

# Plan With Class Diagram

先提出 Mermaid 類別圖，再等待使用者明確確認；確認前不得修改程式碼。確認後依核准的類別圖與相依性順序開發。

# SOP

## Phase 1 -- 分析與提案

1. `READ` 使用者需求、相關程式碼與專案規範，確認功能範圍與現有類別。
2. `THINK` 設計必要的類別、責任、關係、相依性與開發順序。
3. `WRITE` 產出 Mermaid `classDiagram`、簡短設計說明與實作順序。
4. `CHECK` 確認類別圖涵蓋需求、關係一致，且 Mermaid 語法可渲染。

完成條件：已提出可評估的類別圖與實作順序，尚未修改程式碼。

## Phase 2 -- 確認提案

1. `CHECK` 向使用者展示類別圖與實作順序，詢問是否進入開發。
2. `CHECK` 等待使用者明確確認；若要求修改，返回 Phase 1；未確認前停止開發。

完成條件：使用者已明確確認目前版本的類別圖與實作方向。

## Phase 3 -- 按圖開發與驗證

1. `READ` 重新讀取已確認的類別圖與相關程式碼。
2. `THINK` 依類別相依性決定實作順序；若需要改變已確認的類別圖，先返回 Phase 2 重新確認。
3. `WRITE` 依確認的類別圖與實作順序完成程式開發。
4. `CHECK` 確認程式碼的類別組織符合類別圖，並執行適用的測試、型別檢查或 lint。

完成條件：程式已依核准的類別圖完成，且驗證結果已回報。
