# Airflow 실습 과제: 일별 매출 ETL 파이프라인

## 시나리오

매일 오전 9시에 주문 CSV를 읽어 정상 매출만 정제하고, SQLite에 적재한 뒤 매출 요약 JSON을 생성합니다.

## 학습 목표

- DAG와 Task의 차이를 설명한다.
- TaskFlow API로 Task 의존성을 구성한다.
- 작은 메타데이터를 XCom으로 전달한다.
- 재시도, 스케줄, catchup을 설정한다.
- 멱등성 있는 적재 작업을 구현한다.
- GitHub Actions에서 비즈니스 로직을 자동 테스트한다.

## 기본 과제

1. Docker Compose로 Airflow를 실행한다.
2. `daily_sales_etl` DAG를 수동 실행한다.
3. Graph 화면에서 `extract → transform → load → report` 순서를 확인한다.
4. 각 Task 로그와 XCom 반환값을 확인한다.
5. `output/cleaned_sales.csv`, `output/sales.db`, `output/summary.json`을 확인한다.
6. 같은 DAG를 다시 실행하고 SQLite 행이 중복되지 않는지 확인한다.

## 코드 수정 과제

### 과제 A — 고액 매출 필터

`clean_sales()`에 최소 매출액 조건을 추가해 `revenue >= 20000`인 주문만 남기세요.

### 과제 B — 검증 Task 추가

`transform`과 `load` 사이에 `validate` Task를 추가하세요. 정제 행이 0개이면 `ValueError`를 발생시키고, 그렇지 않으면 원래 transform 결과를 반환해야 합니다.

목표 흐름:

```text
extract → transform → validate → load → report
```

### 과제 C — 실패와 재시도 관찰

`data/sales.csv`의 파일명을 잠시 변경한 뒤 DAG를 실행하세요. `extract` 또는 `transform`이 실패하고 10초 후 재시도되는지 로그에서 확인한 다음 파일명을 복구하고 Task를 다시 실행하세요.

### 과제 D — 테스트 추가

`tests/test_sales_etl.py`에 다음 테스트를 추가하세요.

- 고액 매출 필터 테스트
- 입력 CSV가 비어 있을 때의 테스트
- 같은 데이터를 SQLite에 두 번 적재해도 행 수가 늘지 않는 테스트

## 제출물

- GitHub 저장소 URL
- Airflow Graph 화면 캡처
- 성공한 DAG Run 화면 캡처
- 생성된 `summary.json`
- 성공한 GitHub Actions 화면 캡처
- `DAG`, `Task`, `XCom`, `멱등성`에 대한 각 1~2문장 설명

## 평가 기준

| 항목 | 배점 |
|---|---:|
| Airflow 실행 및 DAG 등록 | 20 |
| Task 의존성 구성 | 20 |
| ETL 결과 정확성 | 25 |
| 예외 처리·재시도·멱등성 | 15 |
| pytest 및 GitHub Actions | 10 |
| 문서화와 실행 화면 | 10 |
| 합계 | 100 |
