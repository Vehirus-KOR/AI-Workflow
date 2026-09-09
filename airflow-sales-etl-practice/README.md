# Airflow Sales ETL Practice

Apache Airflow 3.3.1, Docker Compose, TaskFlow API를 이용한 입문용 ETL 실습입니다.

## 준비물

- Docker Desktop
- Docker Compose 2.14 이상
- 메모리 최소 4GB, 권장 8GB

## 1. 실행

프로젝트 폴더에서 다음 명령을 실행합니다.

```bash
docker compose up -d
```

첫 실행은 이미지를 내려받고 Airflow를 초기화하므로 시간이 걸릴 수 있습니다.

## 2. 로그인 비밀번호 확인

```bash
docker compose logs airflow
```

로그에서 생성된 `admin` 계정의 비밀번호를 확인합니다. 브라우저에서 `http://localhost:8080`을 열고 로그인합니다.

## 3. DAG 실행

1. DAG 목록에서 `daily_sales_etl`을 찾습니다.
2. DAG를 활성화합니다.
3. Trigger 버튼으로 수동 실행합니다.
4. Graph 화면에서 Task 흐름과 로그를 확인합니다.

## 4. 결과 확인

성공하면 로컬 `output` 폴더에 다음 파일이 생성됩니다.

- `cleaned_sales.csv`
- `sales.db`
- `summary.json`

## 5. 테스트

로컬 Python 환경에서는 다음 명령을 사용할 수 있습니다.

```bash
pip install pytest
pytest -q
```

GitHub에 Push하면 `.github/workflows/ci.yml`이 문법 검사, 단위 테스트, Docker Compose 설정 검사를 자동 실행합니다.

## 6. 종료

```bash
docker compose down
```

Airflow 메타데이터까지 초기화하려면 아래 명령을 사용합니다. 기존 실행 기록이 삭제되므로 필요할 때만 실행하세요.

```bash
docker compose down --volumes
```

자세한 실습 요구사항은 `ASSIGNMENT.md`를 확인하세요.
