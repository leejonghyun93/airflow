# 🚀 Airflow 학습 저장소

## 📖 소개

인프런 **김현진님의 [Airflow 마스터 클래스](강의링크)** 강의를 수강하며 작성한 실습 코드 저장소입니다.

데이터 엔지니어로 성장하기 위해 Airflow를 처음부터 학습하고 있습니다.

## 🎯 학습 목표

- [ ] Airflow 기본 개념 이해
- [ ] DAG 작성 능력 향상
- [ ] 다양한 Operator 활용
- [ ] 실전 데이터 파이프라인 구축
- [ ] 스케줄링 및 모니터링

## 🛠 기술 스택

- **Orchestration**: Apache Airflow 2.8.1
- **Container**: Docker & Docker Compose
- **Language**: Python 3.11
- **Database**: PostgreSQL 13
- **Message Broker**: Redis

## 🚀 빠른 시작

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

## 📁 프로젝트 구조
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

## 💡 주요 학습 포인트

### 1. DAG 작성 패턴
```python
from airflow import DAG
from datetime import datetime

with DAG(
    dag_id='my_dag',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
) as dag:
    # tasks...
```


## 🔗 참고 자료

- [Airflow 공식 문서](https://airflow.apache.org/)

## 📝 학습 일지

### 2025-11-07
- BashOperator 학습 완료
- 외부 쉘 스크립트 실행 방법 학습

### 2025-11-08
- PythonOperator 학습 시작
- 랜덤 과일 선택 DAG 작성

- Blog: 블로그

##
