# Project Django_tdd

## 1. 목표

- Django + TDD 적용으로 개인 블로그를 대체할 홈페이지를 구축
- Codelab : 주제별로 글을 작성
- Toy : 여러가지 소규모 프로젝트 작성한다.
- Til : 간편하게 TIL 작성 
- 지속적으로 개발을 연습하는 토대가 되고, 새로운 기능을 붙여나간다.


## 2. 구현 기능

1. 가입 및 로그인 기능 구현
    - 권한 체계
        - Admin: 
            - 숨겨진 글 보기(흐릿하게 표시)
            - 모든 글 수정 가능
        - Writer:
            - 작성권한
            - 자신의 글 수정가능
        - 모든 사람은 공개글을 볼 수 있다.
    - 소셜 로그인 구현(Facebook, Google, Github)
    - 로그아웃 구현
    - 테스트 코드 작성
    
2. Codelab 
    - 글 작성
    - 글 목록
    - 글 검색
    - 글 수정
    - 글 삭제
    - 좋아요
    - 테스트 코드 작성
    
3. Til
    - Til 작성
    - Til 목록 
    - Til 통계
    - Til 수정
    - Til 삭제
    - 테스트 코드 작성

4. 메인 화면
    - React or Vue로 구현

5. Google Anlytics 붙이기

6. 기타

    - RSS
    - SITEMAP
    - error 카카오톡 또는 slack 알림
    - Firebase 기반 채팅기능 외부 가입자<->나 사이
    - 피드백 기능
    - 뉴스레터 기능
    - 번역기능 + 국제화 
    - 개발퀴즈
    - 중고물품 나눔
    - 프로젝트 파티원 구하기
    - 팝업 노티
    - PWA + 웹푸시
    
## 3. TODO

- ~~sentry 적용~~
- MEDIA FILE 설정 실서버 Nginx 설정 바꿔주기
- django_allauth 테스팅 작성해보기