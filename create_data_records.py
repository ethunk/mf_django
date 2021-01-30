import json
from blogs.models import Author, Tag, Article, Image, StockTicker
from datetime import datetime


contents = json.load(open('content_api.json'))['results']

authors = []
for content in contents:
    author = content['authors'][0]
    authors.append(
        Author(
            username=author['username'],
            email=author['email'],
            first_name=author['first_name'],
            last_name=author['last_name'],
            small_img=author['small_avatar_url'],
            large_img=author['large_avatar_url'],
            short_bio=author['short_bio'],
        )
    )
tag_objects = []
for content in contents:
    tags = content['tags']
    tag_objects = []
    for tag in tags:
        tag_objects.append(Tag(name=tag['name']))

    Tag.objects.bulk_create(tag_objects)

article_objects = []
for content in contents:
    author = content['authors'][0]
    author = Author.objects.get(username=author['username'], email=author['email'])
    tags = [Tag.objects.get(name=tag['name']) for tag in content['tags']]
    body = content['body']
    promo = content['promo']
    publish_at = datetime.strptime(content['publish_at'], '%Y-%m-%dT%H:%M:%SZ')
    headline = content['headline']

    try:
        article = Article.objects.get(body=body)
    except Article.DoesNotExist:
        article_object = Article(
            author=author,
            body=body,
            promo=promo,
            headline=headline,
            publish_at=publish_at,
        )
        article_object.save()
        article_object.tags.set(tags)

image_objects = []
for content in contents:
    article = Article.objects.get(promo=content['promo'])
    for image in content['images']:
        image_objects.append(
            Image(
                name=image['name'],
                url=image['url'],
                article=article,
            )
        )

Image.objects.bulk_create(image_objects)



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
