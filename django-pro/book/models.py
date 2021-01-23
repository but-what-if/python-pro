from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.CharField(max_length=64)
    date_of_death = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    native_language = models.CharField(max_length=64)

# 2 показать список всех авторов по path /books/author/list/