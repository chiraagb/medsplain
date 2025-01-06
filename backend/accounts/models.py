from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)


class Report(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
