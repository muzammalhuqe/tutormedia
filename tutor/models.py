from django.db import models

# Create your models here.
class TutorAccount(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=13)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="tutors/images")

    def __str__(self):
        return self.full_name