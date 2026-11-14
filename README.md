# RemindApi｜FastAPI 農務提醒資料 API 原型

RemindApi 是一個以 FastAPI、SQLAlchemy 與 SQLite 建立的農務提醒資料 API 原型，並附有 Streamlit 表單作為資料輸入端。

## 系統組成

- **FastAPI：** 提供栽植期提醒與預警報的 GET／POST 路由。
- **SQLAlchemy：** 定義 PlantMsg、AlerMsg ORM models，封裝 CRUD。
- **SQLite：** 保存提醒資料。
- **Streamlit：** 提供溫度、雨量及預警報輸入表單，透過 Requests 呼叫本機 API。

## 技術

- Python
- FastAPI
- Pydantic
- SQLAlchemy ORM
- SQLite
- Streamlit
- Requests

## API 路由

| Method | Path | 用途 |
|---|---|---|
| GET | `/Remind/plant` | 取得栽植期提醒 |
| POST | `/Remind/plant` | 新增栽植期提醒 |
| GET | `/Remind/aler` | 取得預警報 |
| POST | `/Remind/aler` | 新增預警報 |

## 重要限制

- 目前 API schema 的主鍵欄位名稱與 ORM model 不一致，POST request schema 也要求前端沒有提供的主鍵欄位；現有 Streamlit POST 流程可能無法通過驗證。
- Pydantic schema 使用小寫 `config`，不是 Pydantic 預期的 `Config`，ORM mode 設定可能不會生效。
- CORS 設定允許所有來源，且開啟 credentials，不應直接作為正式部署設定。
- Streamlit 表單沒有完整處理 API 連線失敗、HTTP status 或非 JSON 回應。
- Repository 追蹤 SQLite 資料庫檔案，本次沒有讀取或刪除。
- 本次未重新執行 API 或 Streamlit。

完整技術回顧請參閱 [PROJECT_RETROSPECTIVE.md](PROJECT_RETROSPECTIVE.md)。
