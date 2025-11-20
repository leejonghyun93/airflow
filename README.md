# Airflow 학습 저장소

## 소개

인프런 **김현진님의 [Airflow 마스터 클래스](강의링크)** 강의를 수강하며 작성한 실습 코드 저장소입니다.

데이터 엔지니어로 성장하기 위해 Airflow를 처음부터 학습하고 있습니다.

## 학습 목표

- [ ] Airflow 기본 개념 이해
- [ ] DAG 작성 능력 향상
- [ ] 다양한 Operator 활용
- [ ] 실전 데이터 파이프라인 구축
- [ ] 스케줄링 및 모니터링

## 기술 스택

- **Orchestration**: Apache Airflow 2.8.1
- **Container**: Docker & Docker Compose
- **Language**: Python 3.11
- **Database**: PostgreSQL 13
- **Message Broker**: Redis

## 빠른 시작

### 1. 저장소 클론

```bash
git clone [이 저장소 주소]
cd airflow
```

### 2. Airflow 실행

```bash
docker-compose up -d
```

### 3. 웹 UI 접속

- URL: http://localhost:8080
- ID: airflow
- PW: airflow

## 프로젝트 구조

```
airflow/
├── dags/                      # DAG 정의 파일
│   ├── dags_bash_operator.py
│   ├── dags_python_operator.py
│   └── ...
├── logs/                      # Airflow 로그
├── plugins/                   # 커스텀 플러그인
├── config/                    # 설정 파일
├── docker-compose.yaml        # Docker 설정
├── .env                       # 환경 변수
└── README.md
```

## 주요 학습 포인트

### Airflow 기본 개념 정리

#### Airflow란?

Apache Airflow는 데이터 작업을 자동화·스케줄링·관리하는 오픈소스 오케스트레이션 도구입니다.
ETL, API 파이프라인, 크롤링, 머신러닝 파이프라인 등 다양한 데이터 작업을 순서대로 실행하고 모니터링할 수 있습니다.

데이터 엔지니어링, 머신러닝 엔지니어링 분야에서 가장 널리 사용되는 워크플로우 관리 도구입니다.

Airflow 핵심 구성요소

1. DAG (Directed Acyclic Graph)

Airflow에서 실행되는 모든 워크플로우는 DAG 형태로 표현됩니다.

특징:

Directed: 실행 순서가 명확함

Acyclic: 순환 구조가 없음

Graph: Task들의 관계를 그래프 형태로 표현

예시:

from airflow import DAG
from datetime import datetime

with DAG(
dag_id="example_dag",
schedule="@daily",
start_date=datetime(2025, 1, 1)
) as dag:
...

2. Task

DAG 안에서 실제 실행되는 작업 단위입니다.

예시:

Bash 명령 실행

Python 함수 실행

SQL 실행

API 호출

Spark Job 실행

데이터 적재

3. Operator

Task를 생성하기 위한 템플릿 역할을 합니다.

주요 Operator 종류
Operator 설명
BashOperator Bash 명령 실행
PythonOperator Python 함수 실행
PythonVirtualenvOperator 가상환경에서 Python 실행
BranchPythonOperator 조건 분기 처리
EmailOperator 이메일 발송
SimpleHttpOperator 외부 API 호출
MySqlOperator / PostgresOperator SQL 실행
S3/GCS 관련 Operator 클라우드 스토리지 작업
DockerOperator Docker 컨테이너 실행
SparkSubmitOperator Spark Job 실행

BashOperator 예시:

from airflow.operators.bash import BashOperator

task = BashOperator(
task_id="run_echo",
bash_command="echo 'Hello Airflow'"
)

PythonOperator 예시:

from airflow.operators.python import PythonOperator

def run():
print("Airflow Python Task")

task = PythonOperator(
task_id="python_task",
python_callable=run
)

4. XCom (Cross Communication)

Task 간 데이터를 공유할 수 있는 기능입니다.

key/value 구조

push/pull 방식으로 전송

예시:

def send(ti):
ti.xcom_push(key="result", value=100)

def receive(ti):
print(ti.xcom_pull(key="result"))

5. Airflow 주요 컴포넌트
   컴포넌트 역할
   Scheduler DAG 실행 스케줄링 담당
   Webserver UI 제공
   Worker Task 실제 실행
   Metadata DB Task 실행 기록 저장
   Triggerer Deferrable Operator 실행
   DAG 작성 기본 패턴
   from airflow import DAG
   from airflow.operators.bash import BashOperator
   from datetime import datetime

with DAG(
dag_id="example_basic_dag",
start_date=datetime(2025, 1, 1),
schedule="@daily",
catchup=False
) as dag:

    task1 = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello'"
    )

    task2 = BashOperator(
        task_id="print_world",
        bash_command="echo 'World'"
    )

    task1 >> task2

```

## 🔗 참고 자료

- [Airflow 공식 문서](https://airflow.apache.org/)
```
