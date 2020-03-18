import json
from .models import (
    Branch,
    Neighbour,
    Dining,
    Transport,
    Service,
    Entry,
    Facility,
    Language,
    Room,
    Branch,
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
    RoomBed,
    RoomImage
)

from django.test import TestCase, Client

class DetailViewTest(TestCase):
    client = Client()

    def setUp(self):
        Branch.objects.create(
            name = '경주',
            address = '경상북도 경주시 보문로 338 (신평동)',
            phone = '054.748.2233'
        )

        Room.objects.create(
            name = 'HILL SIDE DELUXE DOUBLE',
            price = 500000,
            branch = Branch.objects.get(id =1),
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

        RoomBed.objects.create(
            bed  = Bed.objects.get(id = 1),
            room = Room.objects.get(id = 1)
        )

        Bathroom.objects.create(
            name = '타월/린넨',
            room = Room.objects.get(id = 1)
        )

        Bedding.objects.create(
            name = '깃털 베게',
            room = Room.objects.get(id = 1)
        )

        Comfort.objects.create(
            name = '에어컨',
            room = Room.objects.get(id = 1)
        )

        Entertainment.objects.create(
            name = '위성방송/케이블',
            room = Room.objects.get(id = 1)
        )

        FnBService.objects.create(
            name = '냉장고',
            room = Room.objects.get(id = 1)
        )

        Furnishing.objects.create(
            name = '책상',
            room = Room.objects.get(id = 1)
        )

        Laundry.objects.create(
            name = '옷장',
            room = Room.objects.get(id = 1)
        )

        Safety.objects.create(
            name = '객실내 안전금고',
            room = Room.objects.get(id = 1)
        )

        View.objects.create(
            name = '발코니 /테라스',
            room = Room.objects.get(id = 1)
        )

        RoomImage.objects.create(
            room = Room.objects.get(id = 1),
            image = 'img'
        )

        Dining.objects.create(
            name = '조식 뷔페',
            branch = Branch.objects.get(id =1)
        )
        Entry.objects.create(
            name = '24시간 경비서비스',
            branch = Branch.objects.get(id =1)
        )
        Facility.objects.create(
            name = '실외 수영장',
            branch = Branch.objects.get(id =1)
        )
        Language.objects.create(
            name = '영어',
            branch = Branch.objects.get(id =1)
        )
        Neighbour.objects.create(
            name = '가까운 공항 34km',
            branch = Branch.objects.get(id =1)
        )
        Safety.objects.create(
            name = '객실내 안전금고',
            room = Room.objects.get(id =1)
        )
        Service.objects.create(
            name = '드라이클리닝',
            branch = Branch.objects.get(id =1)
        )
        View.objects.create(
            name = '가든전망',
            room = Room.objects.get(id =1)
        )

    def tearDown(self):
        Facility.objects.all().delete()
        Branch.objects.all().delete()
        Room.objects.all().delete()
        Neighbour.objects.all().delete()
        Dining.objects.all().delete()
        Transport.objects.all().delete()
        Service.objects.all().delete()
        Entry.objects.all().delete()
        Language.objects.all().delete()
        Bathroom.objects.all().delete()
        Bedding.objects.all().delete()
        Comfort.objects.all().delete()
        Entertainment.objects.all().delete()
        FnBService.objects.all().delete()
        Furnishing.objects.all().delete()
        Laundry.objects.all().delete()
        Safety.objects.all().delete()
        View.objects.all().delete()
        Bed.objects.all().delete()
        RoomBed.objects.all().delete()
        RoomImage.objects.all().delete()

    def test_detail_view_get_success(self):
        client =Client()
        response = client.get('/room/detail/1')
        print(response.json())
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
                                     'room_square_meter_py': '11.20', 
                                     'tv': True, 
                                     'refrigerator': True, 
                                     'bed_type': ['라지더블']}, 
                                 'room_info': {
                                     'view': ['발코니 /테라스', '가든전망'], 
                                     'comfort': ['에어컨'], 
                                     'bathroom': ['타월/린넨'], 
                                     'entertainment': ['위성방송/케이블'], 
                                     'bedding': ['깃털 베게'], 
                                     'furnishing': ['책상'], 
                                     'fnbservice': ['냉장고'], 
                                     'laundry': ['옷장'], 
                                     'safety': ['객실내 안전금고', '객실내 안전금고']}, 
                                 'facility_info': {
                                     'neighbour': ['가까운 공항 34km'], 
                                     'dining': ['조식 뷔페'], 
                                     'transport': [], 
                                     'service': ['드라이클리닝'], 
                                     'entry': ['24시간 경비서비스'], 
                                     'facility': ['실외 수영장'], 
                                     'language': ['영어']}}
                         }
        )
