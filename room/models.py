from django.db import models

class Branch(models.Model):
    name     = models.CharField(max_length = 20, null = True)
    address  = models.CharField(max_length = 100, null = True)
    phone    = models.CharField(max_length = 30, null = True)

    class Meta:
        db_table = 'branches'

class Neighbour(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'neighbours'

class Dining(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'dinings'

class Transport(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'transports'

class Service(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'services'

class Entry(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'entries'

class Facility(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'facilities'

class Language(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'languages'

class Date(models.Model):
    date         = models.DateField(null = True)
    is_weekend   = models.BooleanField(null = True)
    is_holiday   = models.BooleanField(null = True)
    is_season    = models.BooleanField(null = True)
    custom_price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)

    class Meta:
        db_table = 'dates'

class Package(models.Model):
    name  = models.CharField(max_length = 50, null = True)
    offer = models.CharField(max_length = 300, null = True)

    class Meta:
        db_table = 'packages'

class Room(models.Model):
    branch               = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True)
    name                 = models.CharField(max_length = 100, null = True)
    price                = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    package              = models.ManyToManyField(Package, through = 'RoomPackagePrice', null = True)
    date                 = models.ManyToManyField(Date, through = 'RoomDatePrice', null = True)
    free_parking         = models.BooleanField(null = True)
    free_wifi            = models.BooleanField(null = True)
    non_smoking          = models.BooleanField(null = True)
    room_square_meter    = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)
    bed                  = models.ManyToManyField('Bed', through = 'RoomBed', null = True)
    room_square_meter_py = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)
    tv                   = models.BooleanField(null = True)
    refrigerator         = models.BooleanField(null = True)

    class Meta:
        db_table = 'rooms'

class RoomDatePrice(models.Model):
    room  = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    date  = models.ForeignKey(Date, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'room_date_prices'

class RoomPackagePrice(models.Model):
    room     = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    package  = models.ForeignKey(Package, on_delete = models.SET_NULL, null = True)
    discount = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)

    class Meta:
        db_table = 'room_package_prices'


class Bed(models.Model):
    name = models. CharField(max_length = 30)

    class Meta:
        db_table = 'beds'

class RoomBed(models.Model):
    room        = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    bed         = models.ForeignKey(Bed, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'room_beds'

class RoomImage(models.Model):
    room      = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    image     = models.CharField(max_length = 500)

    class Meta:
        db_table = 'room_images'

class View(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)


    class Meta:
        db_table = 'views'

class Comfort(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'comforts'

class Bathroom(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'bathrooms'

class Entertainment(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'entertainments'

class Bedding(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'beddings'

class Furnishing(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'furnishings'

class FnBService(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'fnb_services'

class Laundry(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'laundries'

class Safety(models.Model):
    name   = models.CharField(max_length = 50, null = True)
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null =True)

    class Meta:
        db_table = 'safeties'
