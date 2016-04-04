from django.db import models

class HumanProfile(models.ModeL):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=512)
    Country = models.CharField(max_length=46)
    