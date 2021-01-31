import json

from datetime import datetime

from django.core.management.base import BaseCommand
from fool.models import Author, Tag, Article, Image, StockTicker


class Command(BaseCommand):
    help = 'Create initial data records from provided JSON files.'


    def handle(self, *args, **kwargs):
        contents = json.load(open('content_api.json'))['results']

        authors = []
        for content in contents:
            author = content['authors'][0]
            try:
                Author(
                    username=author['username'],
                    email=author['email'],
                    first_name=author['first_name'],
                    last_name=author['last_name'],
                    small_img=author['small_avatar_url'],
                    large_img=author['large_avatar_url'],
                    short_bio=author['short_bio'],
                ).save()
            except:
                pass

            # Tags
            tags = content['tags']
            for tag in tags:
                try:
                    Tag(name=tag['name']).save()
                except:
                    pass

        for content in contents:
            author = content['authors'][0]
            author = Author.objects.get(username=author['username'], email=author['email'])
            tags = [Tag.objects.get(name=tag['name']) for tag in content['tags']]
            body = content['body']
            promo = content['promo']
            publish_at = datetime.strptime(content['publish_at'], '%Y-%m-%dT%H:%M:%SZ')
            headline = content['headline']
            disclosure = content['disclosure']

            article, _ = Article.objects.get_or_create(
                    author=author,
                    body=body,
                    promo=promo,
                    headline=headline,
                    publish_at=publish_at,
                    disclosure=disclosure,

            )

            article.tags.set(tags)

            for image in content['images']:
                Image.objects.get_or_create(
                        name=image['name'],
                        url=image['url'],
                        article=article,
                        modified=datetime.strptime(image['modified'], '%Y-%m-%dT%H:%M:%S.%fZ')
                )


        quotes = json.load(open('quotes_api.json'))
        for quote in quotes:
            company_name = quote['CompanyName']
            symbol = quote['Symbol']
            current_price = quote['CurrentPrice']['Amount']
            change = quote['Change']['Amount']
            exchange = StockTicker.Exchange._member_map_[quote['Exchange']]
            sector = StockTicker.Sector._value2member_map_[quote['Sector']]
            try:
                StockTicker(
                    company_name=company_name,
                    symbol=symbol,
                    current_price=current_price,
                    change=change,
                    exchange=exchange,
                    sector=sector,
                ).save()
            except:
                continue
