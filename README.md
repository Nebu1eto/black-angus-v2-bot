# 올 뉴 인공흑우

이 프로젝트는 [인공흑우](https://github.com/Hazealign/black-angus-bot) 디스코드 봇의 후속 프로젝트입니다. [yui](https://github.com/item4/yui) 로부터 많은 영감을 얻은 다용도 디스코드 봇입니다.

## 목표

### 설계

 - 인공흑우(줄여서 v1)에 이어 올 뉴 인공흑우(줄여서 v2) 또한 MongoDB를 데이터베이스로 사용합니다.
 - v2는 v1과 다르게, 모든 파일 저장소를 S3에 저장하며 메인 봇 서버를 Docker로 배포할 수 있습니다.
 - v2는 v1과 다르게, 봇 서버와 별개로 원격에서 Lambda로 다음 기능이 수행됩니다.
   - 이모티콘 다운로드
   - RSS / 웹 스크래핑 기반 구독
 - v2는 v1과 다르게, 이모티콘 호출을 제외하고 빗금 명령어를 이용해서 봇을 사용할 수 있게 지원합니다.
   - Pycord v2가 나와야 구현 가능
   - 나오긴 했지만... 아직 Pycord v2가 안정적이지 않음.

### 기능 제공

 - [ ] 이모티콘 기능
   - 이미지 업로드 및 삭제, 리사이징, 검색 등을 지원합니다.
 - [ ] 이모티콘 - 라인콘 기능
   - 한국 리전과 일본 리전에서 라인 이모티콘(음성 제외)를 제공합니다.
 - [ ] 이모티콘 - 디시콘 기능
   - 한국 리전에서 디시인사이드 디시콘을 제공합니다.
 - [ ] 리마인더 / 복약 알림 등을 겸하는 '알람' 기능
 - [ ] 경로 추적 기능
   - [x] 대중 교통 경로 안내 기능
   - [ ] 자동차 경로 안내 기능
 - [x] RSS 및 웹 스크래핑 기반 구독 기능
   - [x] RSS 기반 구독 기능
   - ~~[ ] 웹 스크래핑 기반 구독 기능 (어느 사이트 구독이 필요한지 요청을 받아야함.)~~
 - [x] 구글 이미지 검색
 - [x] 유튜브 영상 검색
 - [x] 날씨 조회 기능
   - [x] 공기 질 조회 기능
 - [x] 파파고 번역 기능
 - [x] 랜덤 뽑기 기능

## 개발

### 실행하기


### 개발 환경 구축하기


## 설정 파일
