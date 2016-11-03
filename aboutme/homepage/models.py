from django.db import models
import datetime

# Create your models here.
class Me(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    photo = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.second_name

class Education(models.Model):
    man = models.ForeignKey(Me, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    YEAR_CHOICES = [(r,r) for r in range(1992, datetime.date.today().year+10)]
    year_of_the_beginning = models.IntegerField(choices=YEAR_CHOICES)
    year_of_graduation = models.IntegerField(choices=YEAR_CHOICES, null=True)
    specialization = models.CharField(max_length=200)
    site = models.URLField(default='')

    def __str__(self):
        return self.place

class PlaceOfWork(models.Model):
    man = models.ForeignKey(Me, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    YEAR_CHOICES = [(r,r) for r in range(1992, datetime.date.today().year+10)]
    started_in = models.IntegerField(choices=YEAR_CHOICES)
    end_date = models.IntegerField(choices=YEAR_CHOICES, null=True)
    position = models.CharField(max_length=50)
    site = models.URLField(default='')

    def __str__(self):
        return self.company

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/hobby/')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
