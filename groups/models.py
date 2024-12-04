from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=30)
    group_type = models.CharField(max_length=10)
