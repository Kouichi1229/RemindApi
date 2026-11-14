# RemindApi：FastAPI 農務提醒 API 原型技術回顧

> 本文件依據 FastAPI routes、Pydantic schemas、SQLAlchemy models／CRUD、Streamlit 表單及資料庫設定整理。沒有重新執行或端到端測試。

## 1. 專案定位

RemindApi 是一個將農務提醒資料拆分為 API 後端與管理端表單的早期原型。管理者透過 Streamlit 輸入栽植期溫度／雨量注意事項或預警報，前端以 Requests 將 JSON 傳送至 FastAPI，再由 SQLAlchemy 寫入 SQLite。

## 2. 系統架構

主要檔案：

| 檔案 | 職責 |
|---|---|
| `app.py` | Streamlit 管理端表單 |
| `sql_app/main.py` | FastAPI app、CORS、GET／POST routes、DB dependency |
| `sql_app/models.py` | PlantMsg、AlerMsg ORM models |
| `sql_app/schemas.py` | Pydantic request／response schemas |
| `sql_app/crud.py` | 資料查詢與新增 |
| `sql_app/database.py` | SQLite engine、SessionLocal、Base |

## 3. 資料流程

### 栽植期提醒

1. Streamlit 輸入更新日期、溫度注意事項及雨量注意事項。
2. 將日期轉換為 ISO 8601 字串。
3. 使用 Requests POST JSON 至 `/Remind/plant`。
4. FastAPI 接收 schema，呼叫 CRUD function。
5. SQLAlchemy 建立 PlantMsg 並寫入 SQLite。

### 預警報

1. Streamlit 輸入更新日期與預警報文字。
2. 將日期轉換為 ISO 8601 字串。
3. 使用 Requests POST JSON 至 `/Remind/aler`。
4. FastAPI 呼叫 CRUD function，寫入 AlerMsg。

此原型已呈現前端管理表單、HTTP JSON API、資料驗證、ORM 與資料庫的基本分層概念。

## 4. 技術能力摘要

| 技術 | 程式證據 | 合理定位 |
|---|---|---|
| FastAPI | GET／POST endpoints、Depends | 有 REST API 開發接觸 |
| Pydantic | request／response schemas | 有 API 資料結構建模經驗 |
| SQLAlchemy | ORM models、CRUD、session | 有 ORM 資料存取經驗 |
| SQLite | database engine | 有輕量型關聯式資料庫經驗 |
| Streamlit | sidebar、form、date_input、text_area | 有內部資料輸入介面實作經驗 |
| Requests | POST JSON | 有 Python HTTP client 整合經驗 |

## 5. 已知限制

- **主鍵欄位不一致：** ORM models 使用 `id`，但 Pydantic response schemas 使用 `plant_id` 與 `aler_id`。
- **POST schema 不一致：** FastAPI POST routes 使用含主鍵欄位的 `Plant`／`Aler` schema 作為 request model；Streamlit payload 沒有提供這些主鍵欄位，可能在 Pydantic validation 階段回傳 422。
- **ORM mode 設定：** schema 內寫成 `class config`，而非 `class Config`，Pydantic ORM mode 設定可能無效。
- **CRUD 型別標註：** CRUD create functions 使用 response schema 作為輸入型別，未區分 Create schema 與 response schema。
- **CORS：** allow_origins 設為 `["*"]` 並啟用 credentials，不適合直接用於正式部署。
- **錯誤處理：** Streamlit 端沒有完整處理 timeout、連線錯誤、非 2xx status 及非 JSON 回應。
- **資料庫生命週期：** 應用匯入時呼叫 create_all；沒有看到版本化 migration 流程。
- **SQLite 檔案：** Repository 追蹤 `sql_app.db`，未確認其內容是否包含非公開資料，本次未讀取或刪除。

## 6. 履歷描述建議

以 Python、FastAPI、SQLAlchemy 與 SQLite 建立農務提醒資料 API，設計栽植期提醒及預警報的 GET／POST endpoints，並以 Streamlit 建立管理端輸入表單，透過 Requests 傳送 JSON 至後端，實作基本資料驗證與資料庫 CRUD 流程。

應描述為 API 原型或練習，不宜宣稱已完成可用的正式部署服務。

## 7. 驗證界線

- 未重新安裝 requirements 或啟動 FastAPI。
- 未執行 Streamlit 表單與 API 的端到端測試。
- 未檢查 SQLite 資料庫內容。
- 本文件依靜態程式碼指出可辨識的設計與 schema 不一致問題，不保證現有 POST 路徑可正常執行。
