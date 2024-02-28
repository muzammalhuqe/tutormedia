from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="accounts/images",null=True, blank=True)
    ssc_roll = models.IntegerField(null=True, blank=True)
    ssc_gpa = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)


    def __str__(self):
        return self.user.username

