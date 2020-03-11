from django.db import models

class User(models.Model):
    grade                = models.ForeignKey('Grade', on_delete = models.CASCADE)
    account_number       = models.CharField(max_length = 20, unique = True)
    account              = models.CharField(max_length = 30, unique = True)
    password             = models.CharField(max_length = 200)
    name_kr              = models.CharField(max_length = 50)
    name_eng             = models.CharField(max_length = 50)
    birth                = models.DateField()
    gender               = models.ForeignKey('Gender', on_delete = models.CASCADE )
    mobile               = models.CharField(max_length = 15)
    telephone            = models.CharField(max_length = 15)
    zip_code             = models.CharField(max_length = 10)
    address              = models.CharField(max_length = 50)
    detailed_address     = models.CharField(max_length = 50, blank = True, null = True)
    email                = models.EmailField(max_length = 50, unique = True)
    job                  = models.ForeignKey('Job',  on_delete = models.CASCADE, blank = True, null = True)
    marketing_agree      = models.BooleanField(default = False)
    created_at           = models.DateTimeField(auto_now_add = True)
    updated_at           = models.DateTimeField(auto_now = True)

    class Meta :
        db_table = 'users'

class Gender(models.Model):
    name         = models.CharField(max_length = 5)

    class Meta :
        db_table = 'genders'

class Grade(models.Model):
    name           = models.CharField(max_length = 20)
    point_rate   = models.DecimalField(max_digits = 5, decimal_places = 2) 

    class Meta :
        db_table = 'grades'

class Job(models.Model) :
    name         = models.CharField(max_length = 30)

    class Meta:
        db_table = 'jobs'


