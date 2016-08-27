from django.db import models

# Create your models here.
class TripMain(models.Model):
    TripName = models.CharField(max_length=255)
    MainLocation = models.CharField(max_length=100)
    Description = models.CharField(max_length=512,blank=True)
    DateStart = models.DateField(blank=True)
    DateEnd = models.DateField(blank=True)
    TopPhoto = models.CharField(max_length=512,blank=True)
    TotalDay = models.IntegerField(blank=True, default=1)


class Plan(models.Model):
    TYPE_CHOICES = (('景點', '景點'),
                    ('購物', '購物'),
                    ('住宿', '住宿'),
                    ('用餐', '用餐'))

    PlanName = models.CharField(max_length=255)
    LocationName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100,blank=True)
    TimeStart = models.DateTimeField(blank=True)
    TimeEnd = models.DateTimeField(blank=True)
    Description = models.CharField(max_length=255,blank=True)
    PhotoPath = models.CharField(max_length=512,blank=True)
    Type = models.CharField(max_length=50,blank=True, choices=TYPE_CHOICES)
    dayCount = models.IntegerField(default=1,blank=True)
    trip = models.ForeignKey(TripMain)


