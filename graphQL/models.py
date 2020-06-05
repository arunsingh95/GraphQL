from django.db import models


class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=(('M', 'Male'), ('F', 'Female')))
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Location(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='user')
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name}_{self.city}_{self.state}"


