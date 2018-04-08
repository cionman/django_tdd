# Project Django_tdd

## 1. 목표

- Django + TDD 적용으로 개인 블로그를 대체할 홈페이지를 구축
- Codelab : 주제별로 글을 작성
- Toy : 여러가지 소규모 프로젝트 작성한다.
- Til : 간편하게 TIL 작성 
- 지속적으로 개발을 연습하는 토대가 되고, 새로운 기능을 붙여나간다.

## 2. Model

- 개략적인 모델

### 2.1 User

- 작성권한 : 시작은 작성자는 처음은 나로 한정하지만, 다른 유저가 작성할 수 있는 권한을 가질 수 있도록 한다.
- 읽기권한 : 모든이
- 등록일
- 이메일
- Password
- Firebase Authentication 도입 여부 고민 

### 2.2 Codelab

- 개요 : Codelab은 하나의 주제로 여러개의 포스팅이 묶여짐
- 작성자ID 
- 작성자명
- subject :
- title : 포스팅별 타이틀
- contents : 포스팅 내용
- parent : 부모페이지
- isView : 공개여부
- idate : 등록일
- mdate : 수정일
- favorite : 좋아요 카운트

### 2.3 Toy

### 2.4 Til



