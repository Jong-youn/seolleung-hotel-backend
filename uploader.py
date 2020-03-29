import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lahan.settings")

import django
django.setup()

import csv
from users.models import *
from room.models import *

#hand = open('./csv/user_job.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Job(name = row[0]))
#
#Job.objects.bulk_create(bulk_list)
#
#hand = open('./csv/user_grades.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Grade(name = row[0], point_rate = row[1]))
#
#Grade.objects.bulk_create(bulk_list)
#
#hand = open('./csv/user_genders.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Gender(name = row[0]))
#
#Gender.objects.bulk_create(bulk_list)
#
#hand = open('./csv/packages.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Package(name = row[0], offer = row[1]))
#
#Package.objects.bulk_create(bulk_list)
#
#hand = open('./csv/dates.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Date(date = row[0], is_weekend = row[1], is_holiday = row[2], is_season = row[3], custom_price = row[4]))
#
#Date.objects.bulk_create(bulk_list)
#
#hand = open('./csv/branches.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Branch(name = row[0], address = row[1], phone = row[2]))
#
#Branch.objects.bulk_create(bulk_list)
#
#
#hand = open('./csv/views.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(View(name = row[0]))
#
#
#hand = open('./csv/comforts.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Comfort(name = row[0]))
#
#Comfort.objects.bulk_create(bulk_list)
#
#
#import csv
#from room.models import *
#
#hand = open('./csv/bathrooms.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Bathroom(name = row[0]))
#
#Bathroom.objects.bulk_create(bulk_list)
#
#hand = open('./csv/entertains.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Entertainment(name = row[0]))
#
#Entertainment.objects.bulk_create(bulk_list)
#
#hand = open('./csv/beddings.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Bedding(name = row[0]))
#
#Bedding.objects.bulk_create(bulk_list)
#
#hand = open('./csv/furnishings.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Furnishing(name = row[0]))
#
#Furnishing.objects.bulk_create(bulk_list)
#
#hand = open('./csv/safeties.csv')
#reader = csv.reader(hand)
#bulk_list = []
#for row in reader:
#    bulk_list.append(Safety(name = row[0]))
#
#Safety.objects.bulk_create(bulk_list)

hand = open('./csv/laundries.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Laundry(name = row[0]))

Laundry.objects.bulk_create(bulk_list)


hand = open('./csv/fnbs.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(FnBService(name = row[0]))

FnBService.objects.bulk_create(bulk_list)

hand = open('./csv/room_images.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(RoomImage(image = row[1]))

RoomImage.objects.bulk_create(bulk_list)

hand = open('./csv/rooms.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Room(name = row[0], price = row[1], free_parking = row[3], free_wifi = row[4], non_smoking = row[5], refrigerator = row[6], room_square_meter = row[7], room_square_meter_py = row[8], tv = row [9]))

Room.objects.bulk_create(bulk_list)


hand = open('./csv/rooms_package_prices.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(RoomPackagePrice(room_id = row[0], package_id = row[1]))

RoomPackagePrice.objects.bulk_create(bulk_list)



hand = open('./csv/room_date_prices.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(RoomDatePrice(room_id = row[0], date_id = row[1]))

RoomDatePrice.objects.bulk_create(bulk_list)



hand = open('./csv/bed.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Bed(name = row[0]))

Bed.objects.bulk_create(bulk_list)

hand = open('./csv/room_beds.csv')

reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(RoomBed(room_id = row[0], bed_id = row[1]))

RoomBed.objects.bulk_create(bulk_list)

hand = open('./csv/LAHAN HOTEL - bathrooms.csv')
reader = csv.reader(hand)
for row in reader:
    a = Bathroom.objects.filter(id=row[0])
    a.update(room_id = row[1])
hand = open('./csv/LAHAN HOTEL - beddings.csv')
reader = csv.reader(hand)
for row in reader:
    a = Bedding.objects.filter(id=row[0])
    a.update(room_id = row[1])
#
hand = open('./csv/LAHAN HOTEL - safeties.csv')
reader = csv.reader(hand)
for row in reader:
    a = Safety.objects.filter(id=row[0])
    a.update(room_id = row[1])
#
hand = open('./csv/LAHAN HOTEL - views.csv')
reader = csv.reader(hand)
for row in reader:
    a = View.objects.filter(id=row[0])
    a.update(room_id = row[1])

hand = open('./csv/LAHAN HOTEL - comforts.csv')
reader = csv.reader(hand)
for row in reader:
    a = Comfort.objects.filter(id=row[0])
    a.update(room_id = row[1])

hand = open('./csv/LAHAN HOTEL - entertains.csv')
reader = csv.reader(hand)
for row in reader:
    a = Entertainment.objects.filter(id=row[0])
    a.update(room_id = row[1])

hand = open('./csv/LAHAN HOTEL - fnbs.csv')
reader = csv.reader(hand)
for row in reader:
    a = FnBService.objects.filter(id=row[0])
    a.update(room_id = row[1])

hand = open('./csv/LAHAN HOTEL - furnishings.csv')
reader = csv.reader(hand)
for row in reader:
    a = Furnishing.objects.filter(id=row[0])
    a.update(room_id = row[1])


hand = open('./csv/LAHAN HOTEL - laundries.csv')
reader = csv.reader(hand)
for row in reader:
    a = Laundry.objects.filter(id=row[0])
    a.update(room_id = row[1])

hand = open('./csv/room_dining.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Dining(name = row[0], branch_id = row[1]))

Dining.objects.bulk_create(bulk_list)


hand = open('./csv/room_entry.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Entry(name = row[0], branch_id = row[1]))

Entry.objects.bulk_create(bulk_list)

hand = open('./csv/room_facility.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Facility(name = row[0], branch_id = row[1]))

Facility.objects.bulk_create(bulk_list)

hand = open('./csv/room_language.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Language(name = row[0], branch_id = row[1]))

Language.objects.bulk_create(bulk_list)

hand = open('./csv/room_neighbour.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Neighbour(name = row[0], branch_id = row[1]))

Neighbour.objects.bulk_create(bulk_list)

hand = open('./csv/room_services.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Service(name = row[0], branch_id = row[1]))

Service.objects.bulk_create(bulk_list)

hand = open('./csv/room_transport.csv')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(Transport(name = row[0], branch_id = row[1]))

Transport.objects.bulk_create(bulk_list)
