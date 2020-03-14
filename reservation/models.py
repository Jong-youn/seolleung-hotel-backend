from users.models import User
from room.models  import Room, Date

from django.db    import models

class Reservation(models.Model):
    user              = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    room              = models.ForeignKey(Room, on_delete = models.SET_NULL, null = True)
    check_in_date     = models.DateField(null = True)
    stay_night        = models.IntegerField(null = True)
    how_many_adults   = models.IntegerField(null = True)
    first_name        = models.CharField(max_length = 30, null = True)
    last_name         = models.CharField(max_length = 30, null= True)
    email             = models.EmailField(max_length = 100)
    mobile            = models.CharField(max_length = 50)
    request           = models.CharField(max_length = 500)
    option            = models.CharField(max_length = 100)
    confirmation_code = models.CharField(max_length = 30)
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
