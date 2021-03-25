from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa')
