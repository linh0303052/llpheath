from django.db import models

# Create your models here.
class User(models.Model):
    password = models.TextField(null=False, max_length=128)
    firstName = models.TextField(null=False, max_length=128)
    lastName = models.TextField(null=False, max_length=128)
    dob = models.DateField(null=False)
    gender = models.BooleanField(null=False) #True: male, False: female
    email = models.EmailField(null=False, primary_key=True)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)

    def __str__(self):
        return "{} {} {}".format(self.firstName, self.lastName, self.password)
