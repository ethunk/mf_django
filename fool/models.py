from builtins import property
from enum import Enum, IntEnum
from typing import Text

from django.db import models
from django.db.models.fields import CharField, DateTimeField, URLField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_extensions.db.fields import AutoSlugField


class Article(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    body = models.TextField(max_length=8000, unique=True)
    promo = models.CharField(max_length=400, null=True)
    headline = models.CharField(max_length=400, null=True)
    publish_at = models.DateTimeField(null=True)
    disclosure = models.CharField(max_length=800, null=True)

    @property
    def by_line(self):
        return f'{self.author.first_name} {self.author.last_name}'

    def __str__(self):
        return f'{self.by_line}: {self.promo[:16]}'

class Author(models.Model):
    username = models.CharField(max_length=36)
    email = models.EmailField(max_length=254, primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    small_img = models.URLField(max_length=255, default='http://g.foolcdn.com/avatar/1593347483/small.ashx')
    large_img = models.URLField(max_length=255, default='http://g.foolcdn.com/avatar/1593347483/large.ashx')
    short_bio = models.CharField(max_length=500, null=True)

    class Meta:
        unique_together = ('username', 'email')

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Image(models.Model):
    name = CharField(max_length=255)
    url = models.URLField(max_length=255)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    modified = DateTimeField(null=True)
    def __str__(self):
        return self.name

    class Meta:
        get_latest_by = ['modified']


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(max_length=36, populate_from='name', overwrite=True)

    class Meta:
        unique_together = ('name', 'slug')

    def __str__(self):
        return self.name


class StockTicker(models.Model):
    company_name = models.CharField(max_length=200, null=False)
    symbol = models.CharField(max_length=7, unique=True, null=False)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    change = models.DecimalField(max_digits=10, decimal_places=2, null=True)


    class Exchange(IntEnum):
        NASDAQ = 1
        NASDAQOTH = 2
        NYSE = 3
        NYSEMKT = 4
        UNKNOWN = 5

        @classmethod
        def choices(cls):
            return [(x.value, x.name) for x in cls]

    exchange = models.IntegerField(choices=Exchange.choices())
    class Sector(Enum):
        FINANCIALS = 'Financials'
        SERVICES = 'Services'
        UTILITIES = 'Utilities'
        BASIC_MATERIALS = 'Basic Materials'
        SECTOR_EQUITY = 'Sector Equity'
        TECHNOLOGY = 'Technology'
        CONSUMER_GOODS = 'Consumer Goods'
        NONE = ''

        @classmethod
        def choices(cls):
            return [(x.value, x.name) for x in cls]

    sector = CharField(choices=Sector.choices(), max_length=100)

    @property
    def percent_change(self):
        if self.change and self.current_price:
            return '{:.2%}'.format(self.change / self.current_price)
        else:

            return '{:.2%}'.format(0)

    @property
    def exchange_name(self):
        return self.Exchange._value2member_map_.get(self.exchange)._name_


@receiver(pre_save, sender=StockTicker)
def upper_case_symbol(sender, instance, *args, **kwargs):
    instance.symbol = instance.symbol.upper()


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=60, null=False, default='Untitled')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{}: {}'.format(self.name, self.body[0:30])
