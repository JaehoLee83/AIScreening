from django.db import models

class UserInfo(models.Model):
    age =  models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    waist_circumference = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    drink = models.IntegerField(null=True, blank=True)
    tobacco = models.IntegerField(null=True, blank=True)
    family_diabetes = models.BooleanField(null=True, blank=True)
    gestational = models.BooleanField(null=True, blank=True)
    exercise = models.IntegerField(null=True, blank=True)
    hypertension = models.IntegerField(null=True, blank=True)

class EventInfo(models.Model):
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.price) 
    
    class Meta:
        db_table = "estimated_price"
        verbose_name = "예측한 가격 리스트"

    



