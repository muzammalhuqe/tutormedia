from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TutorAccount(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=13)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="tutors/images")

    def __str__(self):
        return self.user.username