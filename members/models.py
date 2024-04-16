from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname + ' ' + self.lastname