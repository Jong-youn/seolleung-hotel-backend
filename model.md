### Database Modeling
![image](https://user-images.githubusercontent.com/58175076/76593982-249d8400-653b-11ea-892b-68ce733c67b5.png)


#### User
<details>
	<summary>users</summary>
  서비스 이용에 필요한 유저 정보를 저장합니다.
</details>

<details>
	<summary>user_jobs</summary>
  유저가 선택할 수 있는 직업 정보를 저장합니다.
</details>

<details>
	<summary>user_genders</summary>
  유저가 선택할 수 있는 성별 정보를 저장합니다.
</details>

<details>
	<summary>user_grades</summary>
  유저의 등급과, 등급에 따른 포인트 적립율을 저장합니다.
</details>

<details>
	<summary>inquiries</summary>
  유저가 작성한 QnA 관련 정보를 저장합니다.
</details>

<details>
	<summary>inquiry_types</summary>
  유저가 선택할 수 있는 문의유형을 저장합니다.
</details>

#### Room
<details>
	<summary>facilites</summary>
  지점에 따른 시설정보를 저장합니다.
</details>

<details>
	<summary>branches</summary>
  호텔 지점 정보를 저장합니다.
</details>

<details>
	<summary>rooms</summary>
  지점에 따른 룸 타입, 이름, 가격 및 패키지 정보를 저장합니다.
</details>

<details>
	<summary>packages</summary>
  패키지 정보를 저장합니다.
</details>

<details>
	<summary>room_package_prices</summary>
  Room 과 Package의 중간테이블로 룸에 따른 Package 정보를 저장합니다.
</details>

<details>
	<summary>dates</summary>
  날짜, 주말 여부, 공휴일 여부, 성수기 여부에 따른 가격 정보를 저장합니다.
</details>

<details>
	<summary>room_date_prices</summary>
  Room 과 Date의 중간테이블로 날짜에 따른 룸의 가격정보를 저장합니다.
</details>

<details>
	<summary>room_types</summary>
  각각의 룸 타입이 가지는 아이콘 정보, 이미지, 룸 상세정보를 저장합니다.
</details>

<details>
	<summary>room_iconic_infos</summary>
  아이콘에 담기는 룸의 주요 정보를 저장합니다.
</details>

<details>
	<summary>beds</summary>
  유저가 선택할 수 있는 침대 유형을 저장합니다.
</details>

<details>
	<summary>bed_types</summary>
  RoomIconicInfo와 Bed의 중간테이블로, 룸에 따른 침대 유형을 저장합니다.
</details>

<details>
	<summary>room_images</summary>
  룸 이미지를 저장합니다.
</details>

<details>
	<summary>views</summary>
  룸의 객실 구성을 저장합니다.
</details>

<details>
	<summary>comforts</summary>
  룸의 객실 편의용품을 저장합니다.
</details>

<details>
	<summary>bathrooms</summary>
  룸의 욕실 구성을 저장합니다.
</details>

<details>
	<summary>entertainments</summary>
  룸의 엔터테인먼트를 저장합니다.
</details>

<details>
	<summary>beddings</summary>
  룸의 침구정보를 저장합니다.
</details>

<details>
	<summary>furnishings</summary>
  룸의 레이아웃 및 가구를 저장합니다.
</details>

<details>
	<summary>fnb_services</summary>
  룸의 식음료 시설 및 서비스를 저장합니다.
</details>

<details>
	<summary>laundries</summary>
  룸의 세탁 편의 용품 및 시설을 저장합니다.
</details>

<details>
	<summary>safeties</summary>
  룸의 안전 및 보안시설을 저장합니다.
</details>

<details>
	<summary>room_informations</summary>
  룸에 따른 객실 구성, 객실 편의용품, 욕실 구성, 엔터테인먼트, 침구 정보, 레이아웃 및 가구, 식음료 시설 및 서비스, 세탁 편의 용품 및 시설, 안전 및 보안시설 정보를 저장합니다.
</details>

#### Reservation

<details>
	<summary></summary>
  업데이트 예정😜
</details>
