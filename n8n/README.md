# n8n Workflow Examples

### (1) Google Sheets Example

**File:** `(1)google-sheets-example.json`

Google OAuth 2.0으로 n8n과 Google Sheets API를 연결하고,
워크플로우 실행 시 지정한 데이터를 새로운 행(Row)으로 추가합니다.

**Workflow**

`Manual Trigger` → `Google Sheets (Append Row)` → `Google Sheets API`

**구현 순서**
1. Google Sheets / Drive API 활성화
2. OAuth 2.0 Credential 생성 및 n8n 연결
3. Google Sheets 컬럼 매핑
4. Manual Trigger 실행
5. Google Sheets에 새로운 Row 추가

### (2) Gmail Example

**File:** `(2)gmail-example.json`

Google OAuth 2.0으로 n8n과 Gmail API를 연결하고, 워크플로우 실행 시 지정한 수신자에게 이메일을 자동으로 발송합니다.

**Workflow**

`Manual Trigger` → `Gmail (Send a Message)` → `Gmail API`

**구현 순서**

1. Gmail API 활성화
2. OAuth 2.0 Credential 생성 및 n8n 연결
3. 수신자, 제목, 메시지 설정
4. Manual Trigger 실행
5. Gmail을 통해 이메일 자동 발송

**Reference**

▶ [YouTube - n8n Google Credentials Setup](https://www.youtube.com/watch?v=lXNIteL16Z0)

[![n8n Google Credentials Setup](https://img.youtube.com/vi/lXNIteL16Z0/maxresdefault.jpg)](https://www.youtube.com/watch?v=lXNIteL16Z0)
