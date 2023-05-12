from django.db import models

class UserInfo(models.Model):
    age =  models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    waist_circumference = models.IntegerField()
    gender = models.IntegerField()
    bmi = models.FloatField(null=True, blank=True)
    drink = models.IntegerField()
    tobacco = models.IntegerField()
    family_diabetes = models.BooleanField()
    gestational = models.BooleanField()
    exercise = models.IntegerField()
    hypertension = models.IntegerField()

    



