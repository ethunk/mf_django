from typing import Text
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.related import ForeignKey
from django_extensions.db.fields import AutoSlugField

class Author(models.Model):
    username = models.CharField(max_length=36)
    email = models.EmailField(max_length=254, primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    small_img = models.URLField(max_length=255, default='http://g.foolcdn.com/avatar/1593347483/small.ashx')
    large_img = models.URLField(max_length=255, default='http://g.foolcdn.com/avatar/1593347483/large.ashx')
    short_bio = models.CharField(max_length=500, null=True)
    articles = models.Many
    class Meta:
        unique_together = ('username', 'email')


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(max_length=36, populate_from='name', overwrite=True)


class Article(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    body = models.TextField(max_length=8000)

    @property
    def by_line(self):
        return f'{self.author.first_name} {self.author.last_name}'

class Image(models.Model):
    name = CharField(max_length=255)
    url = models.URLField(max_length=255)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
