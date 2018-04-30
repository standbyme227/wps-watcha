# Watcha(Remastering)

[Watcha](https://watcha.net/) 를 카피하는 프로젝트 입니다.
'.secrets'폴더내의 json파일로(ex. base.json, local.json....)
비밀 키를 관리합니다.

Dev(개발환경)이나 Production(배포)의 DB로 = PostgreSQL을 사용하고,
Local(로컬)에서는 = SQLite를 사용합니다.

local에서는 locahost의 DB를 활용하지만
Dev와 Production에서는 AWS의 RDS를 이용합니다.





## 환경 구분

### local

외부 서비스 접근 없이 개발 환경만을 사용 (DB, Storage 전부 로컬환경)



### dev

DB, Storage에 외부 서비스 (AWS RDS, S3)를 사용함



### production

실제 배포환경임.





## Requirements

### 로켈 테스트

- Python (3.6)



### AWS 환경 테스트

- Python (3.6)
- S3 Bucket, 해당 Bucket을 사용할 수있는 IAM User의 AWS ACCESS KEY, SECRET ACCESS KET
- RDS Database(보안그룹 허용 필요), 해당 Database를 사용할 수 있는 RDS의 user name, password





## Installation

```
pip install -r .requirements/dev.txt
python manage.py runserver
```





## Secrets

**`.secrets/base.json`**

```json

{
  "SECRET_KEY":"<Django settings SECRET_KEY value>",
  "RAVEN_CONFIG":{
    "dsn": "<RAVEN SECRET TOKEN>",
    "release": "raven.fetch_git_sha(os.path.abspath(os.pardir))"
  },
  "SUPERUSER_USERNAME": "<SUPERUSER's username>",
  "SUPERUSER_PASSWORD": "<SUPERUSER's password>",
  "SUPERUSER_EMAIL": "<SUPERUSER's email>"

  "AWS_ACCESS_KEY_ID": "AWS의 액세스키 .aws/credentials 참조",
  "AWS_SECRET_ACCESS_KEY": "AWS 비밀 액세스 키 .aws/credentials 참조",
  "AWS_STORAGE_BUCKET_NAME": "S3의 버킷 네임",

  "AWS_DEFAULT_ACL" : "private",
  "AWS_S3_REGION_NAME" : "지역",
  "AWS_S3_SIGNATURE_VERSION" : "s3v4"

  "FACEBOOK_APP_ID" : "사용하는 facebook_app ID",
  "FACEBOOK_SECRET_CODE" : "사용하는 facebook_app Secret"
}
```

**`.secrets/dev.json & production.json`**

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "rds 앤드포인트",
      "NAME": "DB Name",
      "USER": "DB의 사용자",
      "PASSWORD": "비밀번호",
      "PORT": 5432
    }
  }
}
```




## 목표(여기부턴 개인적인 프로젝트에 대한 감상)

### MVP

1차적으로 우리가 목표해야하는 기준점이 필요해서 3가지를 MVP로 정했다.

1. 검색
2. 평점주기
3. 유저프로필(마이페이지)



### 세부적인 페이지 구성

* 메인페이지
    1. 박스오피스관련 부분
    2. 장르/태그별로 카테고리가 나눠진 부분

* 마이페이지
    1. 통계 페이지
    2. 보고싶어요 페이지
    3. 봤어요 페이지
    4. 코멘트 페이지

* 영화 검색 페이지
    1. User 검색
    2. Movie 검색

* 박스오피스 페이지
    1. 간략히 랭킹만 표시하는 부분
    2. 상세히 영화 정보를 표시하는 부분

* 평가늘리기 페이지
    1. 장르/태그별로 카테고리가 나눠져서 표시됨.

* 영화 상세페이지
    1. 상세페이지 메인
    2. 영화의 배우/감독 상세페이지
    3. 코멘트 리스트



### 계획

1. User관련된 API 완성
2. Modeling과 기본적으로 있어야하는 영화Data를 위한 크롤러 구현
3. 메인, 박스오피스, 평가늘리기 등 커다란 부분 구현
4. 마이페이지, 영화상세 페이지등 디테일한 부분 구현



### 현실

1. Git이라는 문제에 부딫힘
2. User관련 API를 구현하고 나니 Test를 구현해야함
3. Modeling과 크롤러로 한 주를 다 보냄.
4. 페이지들을 꾸역꾸역 구현해냄.


### 첫 프로젝트의 문제점

1. 목표의식의 불투명
2. 만들고 API만 던져주면 된다라고 생각하는 부분.

