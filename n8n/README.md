# n8n Workflow Examples

n8n을 활용한 Workflow 및 API Integration 실습 예제입니다.

## Examples

### (1) Google Sheets Example

**File:** `(1)google-sheets-example.json`

Google OAuth 2.0으로 n8n과 Google Sheets API를 연결하고,
워크플로우 실행 시 지정한 데이터를 새로운 행(Row)으로 추가합니다.

**Workflow**

`Manual Trigger` → `Google Sheets (Append Row)` → `Google Sheets API`

**구현 순서**
1. Google Sheets / Drive API 활성화
2. OAuth 2.0 Credential 생성 및 n8n 연결
3. Google Sheets의 `name`, `product`, `price` 컬럼 매핑
4. Manual Trigger 실행
5. Google Sheets에 새로운 Row 추가

**기능**
- Google OAuth 2.0 인증
- Google Sheets API 연동
- 컬럼 데이터 Mapping
- Spreadsheet Row 자동 추가
