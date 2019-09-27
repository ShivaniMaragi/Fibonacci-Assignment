from django.db import models

# Create your models here.
class Fibinfo(models.Model):
    inp_digit=models.CharField(max_length=10)
    out_result=models.CharField(max_length=225)
    time_taken=models.CharField(max_length=225,default=0.0)

    def __str__(self):
        return self.inp_digit
