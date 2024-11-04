from django.db import models

from users.models import NULLABLE


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    preview = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='preview')
    desc = models.TextField(verbose_name='description')

class Course(models.Model):
    title = models.CharField(max_length=50)
    preview = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='preview')
    desc = models.TextField(verbose_name='description')
    url=models.URLField(verbose_name='link')
