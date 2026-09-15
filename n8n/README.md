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

---

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

---

### (3) Submission Workflow

**File:** `(3)submission-workflow-public.json`

n8n Form으로 이름, 이메일, 문의내용을 입력받아 Google Sheets에 저장하고, Google Gemini가 문의에 대한 답변을 자동 생성합니다. 생성된 답변은 Google Sheets에 기록된 후 Gmail을 통해 문의자에게 자동 발송됩니다.

**Workflow**

`Form Trigger` → `Google Sheets (Append)` → `Gemini LLM` → `Google Sheets (Update)` → `Gmail (Send)` → `Google Sheets (Update Status)`

**구현 순서**

1. n8n Form을 통한 문의 데이터 수집
2. 이름 / 이메일 / 문의내용을 Google Sheets에 저장
3. Google Gemini를 이용한 문의 답변 자동 생성
4. 생성된 답변을 Google Sheets에 업데이트
5. Gmail을 통해 문의자 이메일로 답변 자동 발송
6. 발송 완료 후 Google Sheets의 발송 상태 업데이트

---

### (4) n8n Getting Started

**File:** `(4)n8n-getting-started.json`

Google Sheets의 데이터를 불러와 조건에 맞는 Row를 필터링하고, 필요한 필드를 가공한 뒤 조건에 따라 워크플로우를 분기합니다.

**Workflow**

`Manual / Schedule Trigger` → `Google Sheets (Get Rows)` → `Filter` → `Edit Fields / If` → `No Operation`

**구현 순서**

1. Manual Trigger 및 Schedule Trigger 구성
2. Google Sheets에서 Row 데이터 조회
3. Filter를 사용하여 조건에 맞는 데이터 필터링
4. Edit Fields를 사용하여 필요한 필드 가공
5. If를 사용하여 조건에 따라 True / False 분기
6. No Operation으로 처리 흐름 종료

---

**Reference**

▶ [YouTube - n8n Google Credentials Setup](https://www.youtube.com/watch?v=lXNIteL16Z0)

[![n8n Google Credentials Setup](https://img.youtube.com/vi/lXNIteL16Z0/maxresdefault.jpg)](https://www.youtube.com/watch?v=lXNIteL16Z0)
