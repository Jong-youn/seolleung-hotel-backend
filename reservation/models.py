from users.models import User
from room.models  import Room, Date

from django.db    import models

class Reservation(models.Model):
    user              = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    room              = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    room_name         = models.CharField(max_length = 100, null = True)
    price             = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    check_in          = models.DateField(null = True)
    stay_nights       = models.IntegerField(null = True)
    adult             = models.IntegerField(null = True)
    reservation_code  = models.CharField(max_length = 100)
    created_at        = models.DateTimeField(auto_now_add = True)
    updated_at        = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'reservations'

class Vacancy(models.Model):
    date        = models.ForeignKey(Date, on_delete = models.SET_NULL, null = True)
    room        = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    reservation = models.ForeignKey(Reservation, on_delete = models.SET_NULL, null = True)
    vacancy     = models.IntegerField(null = True)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'vacancies'

class Point(models.Model):
    user           = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    reservation    = models.ForeignKey(Reservation, on_delete = models.SET_NULL, null = True)
    saved_point    = models.IntegerField(null = True)
    used_point     = models.IntegerField(null = True)
    total_point    = models.IntegerField(null = True)
    is_accumulated = models.BooleanField(null = True)
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'points'
