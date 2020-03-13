from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length = 500, null = True)

    class Meta:
        db_table = 'facilities'

class Branch(models.Model):
    name     = models.CharField(max_length = 20, null = True)
    facility = models.ForeignKey(Facility, on_delete = models.SET_NULL, null = True)
    address  = models.CharField(max_length = 100, null = True)
    phone    = models.CharField(max_length = 30, null = True)

    class Meta:
        db_table = 'branches'

class Room(models.Model):
    branch    = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)
    room_type = models.ForeignKey('RoomType', on_delete = models.SET_NULL, null = True)
    name      = models.CharField(max_length = 100, null = True)
    price     = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    package   = models.ManyToManyField('Package', through = 'RoomPackagePrice', null = True)

    class Meta:
        db_table = 'rooms'

class Package(models.Model):
    name  = models.CharField(max_length = 50, null = True)
    offer = models.CharField(max_length = 300, null = True)

    class Meta:
        db_table = 'packages'

class RoomPackagePrice(models.Model):
    room     = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    package  = models.ForeignKey(Package, on_delete = models.SET_NULL, null = True)
    discount = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)

    class Meta:
        db_table = 'room_package_prices'

class Date(models.Model):
    date         = models.DateField(null = True)
    is_weekend   = models.BooleanField(null = True)
    is_holiday   = models.BooleanField(null = True)
    is_season    = models.BooleanField(null = True)
    custom_price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)

    class Meta:
        db_table = 'dates'

class RoomDatePrice(models.Model):
    room  = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    date  = models.ForeignKey(Date, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'room_date_prices'

class RoomType(models.Model):
    iconic_info      = models.ForeignKey('RoomIconicInfo', on_delete = models.SET_NULL, null = True)
    image            = models.ForeignKey('RoomImage', on_delete = models.SET_NULL, null = True)
    room_information = models.ForeignKey('RoomInformation', on_delete = models.SET_NULL, null = True)
    name             = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'room_types'

class RoomIconicInfo(models.Model):
    free_parking         = models.BooleanField(null = True)
    free_wifi            = models.BooleanField(null = True)
    non_smoking          = models.BooleanField(null = True)
    room_square_meter    = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)
    bed_type             = models.ManyToManyField('Bed', through = 'BedType', null = True)
    room_square_meter_py = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)
    tv                   = models.BooleanField(null = True)
    refrigerator         = models.BooleanField(null = True)

    class Meta:
        db_table = 'room_iconic_infos'

class Bed(models.Model):
    name = models. CharField(max_length = 30)

    class Meta:
        db_table = 'beds'

class BedType(models.Model):
    iconic_info = models.ForeignKey(RoomIconicInfo, on_delete = models.SET_NULL, null = True)
    bed         = models.ForeignKey(Bed, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'bed_types'

class RoomImage(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete = models.SET_NULL, null = True)
    image     = models.CharField(max_length = 500)

    class Meta:
        db_table = 'room_images'

class View(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'views'

class Comfort(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'comforts'

class Bathroom(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'bathrooms'

class Entertainment(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'entertainments'

class Bedding(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'beddings'

class Furnishing(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'furnishings'

class FnBService(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'fnb_services'

class Laundry(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'laundries'

class Safety(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'safeties'

class RoomInformation(models.Model):
    view          = models.ForeignKey(View, on_delete = models.SET_NULL, null = True)
    comfort       = models.ForeignKey(Comfort, on_delete = models.SET_NULL, null = True)
    bathroom      = models.ForeignKey(Bathroom, on_delete = models.SET_NULL, null = True)
    entertainment = models.ForeignKey(Entertainment, on_delete = models.SET_NULL, null = True)
    bedding       = models.ForeignKey(Bedding, on_delete = models.SET_NULL, null = True)
    furnishing    = models.ForeignKey(Furnishing, on_delete = models.SET_NULL, null = True)
    fnb_service   = models.ForeignKey(FnBService, on_delete = models.SET_NULL, null = True)
    laundry       = models.ForeignKey(Laundry, on_delete = models.SET_NULL, null = True)
    safety        = models.ForeignKey(Safety, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'room_informations'
