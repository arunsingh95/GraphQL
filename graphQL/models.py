from django.db import models


class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=(('M', 'Male'), ('F', 'Female')))
    age = models.IntegerField()

    def __str__(self):
        return self.name
