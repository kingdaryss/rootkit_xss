from django.db import models
from django.utils import timezone


class Logs(models.Model):
    domain = models.TextField(null=True, blank=True)
    localstorage = models.TextField(null=True, blank=True)
    cookies = models.TextField(null=True, blank=True)
    insert_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager()



class Scripts(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    script = models.TextField(null=True, blank=True)

    objects = models.Manager()

