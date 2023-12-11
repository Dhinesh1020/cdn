from django.db import models

class DBTable(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)