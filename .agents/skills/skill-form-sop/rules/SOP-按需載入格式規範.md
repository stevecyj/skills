# Rule 1 - SOP 只保留必要步驟

- 每個 Phase 必須對完成任務有直接作用。
- 每個步驟必須產生後續步驟或完成條件會使用的結果。
- SOP 不得重複已由參考檔定義的規則內容。

## Good Example

- SOP 只保留載入規範、寫入與驗證所需的步驟。

```markdown
1. `READ` `rules/example.md` 的所有規則，建立完成檢查清單。
2. `WRITE` 依已載入的完成檢查清單修改目標檔案。
3. `CHECK` 逐條驗證完成檢查清單。
```

## Bad Example

- 寫入前重複整理同一份規則，沒有產生新的工作結果。

```markdown
1. `READ` 規範檔的所有規則。
2. `THINK` 重新整理已讀取的所有規則。
3. `WRITE` 依規則修改目標檔案。
```

# Rule 2 - 參考檔只能在載入步驟中提名

- 參考檔的路徑必須只出現在實際讀取該檔案的 `READ` 步驟。
- 多個參考檔可以在同一個 `READ` 步驟中載入。
- 載入參考檔的 `READ` 步驟必須與第一個依賴載入結果的步驟位於同一個 Phase，並緊接在該步驟之前。
- SOP 不得為載入參考檔建立獨立 Phase。
- `WRITE`、`CHECK` 與完成條件不得重複參考檔的路徑。

## Good Example

- `READ` 與第一個依賴步驟位於同一個 Phase 且前後相鄰，參考檔路徑只出現一次。

```markdown
## Phase 1 -- 理解與設計

1. `READ` 使用者需求與目標檔案。
2. `THINK` 確認任務需要的參考檔。
3. `READ` `rules/example.md` 的所有 Rule，建立完成檢查清單。
4. `THINK` 依已載入的完成檢查清單設計內容。

完成條件：已完成符合檢查清單的內容設計。
```

## Bad Example

- 載入參考檔被拆成獨立 Phase，且路徑在後續 Phase 重複出現。

```markdown
## Phase 1 -- 載入規則

1. `READ` `rules/example.md` 的所有 Rule。

完成條件：已載入所有 Rule。

## Phase 2 -- 設計內容

1. `THINK` 依 `rules/example.md` 設計內容。

完成條件：已完成內容設計。
```

# Rule 3 - 後續步驟必須使用載入結果

- `READ` 步驟必須為載入結果指定明確名稱。
- 後續步驟必須使用該名稱引用載入結果。
- 載入結果名稱必須表明其用途，例如「完成檢查清單」。

## Good Example

- `READ` 步驟產生「完成檢查清單」，後續步驟持續使用同一名稱。

```markdown
1. `READ` `rules/example.md` 的所有 Rule，建立完成檢查清單。
2. `WRITE` 依已載入的完成檢查清單修改內容。
3. `CHECK` 逐條驗證完成檢查清單。
```

## Bad Example

- `READ` 步驟沒有命名載入結果，後續步驟也沒有可追蹤的輸入。

```markdown
1. `READ` 規範檔。
2. `WRITE` 修改內容。
3. `CHECK` 內容是否正確。
```

# Rule 4 - 讀取輸入必須明確

- `READ` 步驟必須明確指定要讀取的輸入。
- 只在特定條件下存在的輸入，必須在步驟中說明適用條件。
- 輸入名稱必須使用可辨識的名稱，不得使用「它」或「該檔案」等無法從同一步驟確定指涉對象的代名詞。

## Good Example

- 步驟分別指定必讀輸入與只在修改情境存在的輸入。

```markdown
1. `READ` 使用者需求、目標 Skill 的 `SKILL.md`，以及待修改的既有 RuleFile。
```

## Bad Example

- 「它」的指涉對象不明，新建 RuleFile 時也沒有可讀取的目標檔案。

```markdown
1. `READ` 使用者需求、目標 RuleFile 與擁有它的 `SKILL.md`。
```
