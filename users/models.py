from django.db import models

class User(models.Model):
    grade                = models.ForeignKey('Grade', on_delete = models.CASCADE, blank = True, null = True)
    account_number       = models.CharField(max_length = 20, unique = True,  blank = True, null = True)
    account              = models.CharField(max_length = 30, unique = True,  blank = True, null = True)
    password             = models.CharField(max_length = 200, blank = True, null = True)
    name_kr              = models.CharField(max_length = 50, blank = True, null = True)
    name_eng             = models.CharField(max_length = 50, blank = True, null = True)
    birth                = models.DateField(blank = True, null = True)
    gender               = models.ForeignKey('Gender', on_delete = models.CASCADE , blank = True, null = True)
    mobile               = models.CharField(max_length = 15, blank = True, null = True)
    telephone            = models.CharField(max_length = 15, blank = True, null = True)
    zip_code             = models.CharField(max_length = 10, blank = True, null = True)
    address              = models.CharField(max_length = 50, blank = True, null = True)
    detailed_address     = models.CharField(max_length = 50, blank = True, null = True)
    email                = models.EmailField(max_length = 50, unique = True)
    job                  = models.ForeignKey('Job',  on_delete = models.CASCADE, blank = True, null = True)
    marketing_agree      = models.BooleanField(default = False, blank = True, null = True)
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