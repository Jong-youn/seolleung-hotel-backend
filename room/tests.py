import json
from .models import (
    Room,
    Facility,
    Branch,
    RoomIconicInfo,
    RoomInformation,
    RoomType,
    Room,
    Bathroom,
    Bedding,
    Comfort,
    Entertainment,
    FnBService,
    Furnishing,
    Laundry,
    Safety,
    View,
    Bed,
    BedType,
    RoomImage
)

from django.test import TestCase, Client

class DetailViewTest(TestCase):
    client = Client()

    def setUp(self):
        Facility.objects.create(
            name = '시설정보, 무료wi-fi 수영장 피트니스 장애인 편의 레스토랑 대중교통편리,  호텔 주변시설, 가까운 공항 34Km, 버스 및 기차역 25Km, 병. 의원 9.5Km, 약국 8Km, 편의점 0.6Km, 호텔내 편의시설, 실외 수영장, 실내 수영장, 피트니스 센터, 정원, 레스토랑, 커피숍, 바, 얼음기계, 연회장, 라운지, 기프트 샵, 사우나, 키즈카페,  서비스, 드라이클리닝, 룸서비스(이용제한), 일일 청소 서비스, 여행 가방보관, 환전, 팩스, 현금인출기, 아동용 시설 서비스,  식사정보, 조식 뷔페, 석식 뷔페,  출입/접근 서비스, 24시간 경비서비스, 장애인용 편의시설, 24시간 프런트, 엘리베이터, 휠체어 접근방식,  이동 편의 시설 서비스, 숙소 내 주차장, 휠체어 접근 가능, 택시 서비스,  숙소 내 사용 가능한 언어, 영어, 일본어, 중국어(북경어)'
        )

        Branch.objects.create(
            name = '경주',
            address = '경상북도 경주시',
            phone = '054.748.2223',
            facility = Facility.objects.get(id = 1)
        )

        RoomIconicInfo.objects.create(
            free_parking = 1,
            free_wifi = 1,
            non_smoking = 1,
            room_square_meter = 37,
            room_square_meter_py = 11.2,
            tv = 1,
            refrigerator = 1
        )

        Bed.objects.create(
            name = '라지더블'
        )

        BedType.objects.create(
            bed = Bed.objects.get(id = 1),
            iconic_info = RoomIconicInfo.objects.get(id = 1)
        )

        Bathroom.objects.create(
            name = '타월/린넨, 샤워실, 세면도구, 헤어 드라이기, 욕실가운'
        )

        Bedding.objects.create(
            name = '깃털 베게, 고급 침구'
        )

        Comfort.objects.create(
            name = '에어컨, 모닝콜서비스, 암막커튼, 알람시계, 슬리퍼, 난방'
        )

        Entertainment.objects.create(
            name = '위성방송/케이블, 전화기, 라디오'
        )

        FnBService.objects.create(
            name = '냉장고, 무료생수, 무료 인스턴트 커피, 무료 차'
        )

        Furnishing.objects.create(
            name = '책상, 목조 바닥, 테이블, 소파'
        )

        Laundry.objects.create(
            name = '옷장, 옷걸이'
        )

        Safety.objects.create(
            name = '객실내 안전금고, 화재 탐지기'
        )

        View.objects.create(
            name = '발코니 /테라스, 가든전망'
        )

        RoomInformation.objects.create(
            bathroom = Bathroom.objects.get(id = 1),
            bedding = Bedding.objects.get(id = 1),
            comfort = Comfort.objects.get(id =1),
            entertainment = Entertainment.objects.get(id = 1),
            fnb_service = FnBService.objects.get(id = 1),
            furnishing = Furnishing.objects.get(id = 1),
            laundry = Laundry.objects.get(id = 1),
            safety = Safety.objects.get(id = 1),
            view = View.objects.get(id = 1)
        )

        RoomType.objects.create(
            name = 'HILL SIDE DELUXE DOUBLE',
            iconic_info = RoomIconicInfo.objects.get(id = 1),
            room_information = RoomInformation.objects.get(id = 1)
        )

        RoomImage.objects.create(
            room_type = RoomType.objects.get(id = 1),
            image = 'img'
        )

        Room.objects.create(
            name = 'HILL SIDE DELUXE DOUBLE',
            price = 500000,
            branch = Branch.objects.get(id =1),
            room_type = RoomType.objects.get(id = 1)
        )

    def tearDown(self):
        Facility.objects.all().delete()
        Branch.objects.all().delete()
        RoomIconicInfo.objects.all().delete()
        RoomInformation.objects.all().delete()
        RoomType.objects.all().delete()
        Room.objects.all().delete()

    def test_detail_view_get_success(self):
        client =Client()
        response = client.get('/room/detail/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
        {
            'details': {
                'images': ['img'], 
                'iconic_info': {
                    'free_parking': True, 
                    'free_wifi': True, 
                    'non_smoking': True, 
                    'room_square_meter': '37.00', 
                    'bed_type': '라지더블', 
                    'room_square_meter_py': '11.20', 
                    'tv': True, 
                    'refrigerator': True}, 
                'room_info': {
                    'view': '발코니 /테라스, 가든전망', 
                    'comfort': '에어컨, 모닝콜서비스, 암막커튼, 알람시계, 슬리퍼, 난방', 
                    'bathroom': '타월/린넨, 샤워실, 세면도구, 헤어 드라이기, 욕실가운', 
                    'entertainment': '위성방송/케이블, 전화기, 라디오', 
                    'bedding': '깃털 베게, 고급 침구', 
                    'furnishing': '책상, 목조 바닥, 테이블, 소파', 
                    'fnb_service': '냉장고, 무료생수, 무료 인스턴트 커피, 무료 차', 
                    'laundry': '옷장, 옷걸이', 
                    'safety': '객실내 안전금고, 화재 탐지기'}, 
                'facility_info': '시설정보, 무료wi-fi 수영장 피트니스 장애인 편의 레스토랑 대중교통편리,  호텔 주변시설, 가까운 공항 34Km, 버스 및 기차역 25Km, 병. 의원 9.5Km, 약국 8Km, 편의점 0.6Km, 호텔내 편의시설, 실외 수영장, 실내 수영장, 피트니스 센터, 정원, 레스토랑, 커피숍, 바, 얼음기계, 연회장, 라운지, 기프트 샵, 사우나, 키즈카페,  서비스, 드라이클리닝, 룸서비스(이용제한), 일일 청소 서비스, 여행 가방보관, 환전, 팩스, 현금인출기, 아동용 시설 서비스,  식사정보, 조식 뷔페, 석식 뷔페,  출입/접근 서비스, 24시간 경비서비스, 장애인용 편의시설, 24시간 프런트, 엘리베이터, 휠체어 접근방식,  이동 편의 시설 서비스, 숙소 내 주차장, 휠체어 접근 가능, 택시 서비스,  숙소 내 사용 가능한 언어, 영어, 일본어, 중국어(북경어)'
            }
        }
    )
