from datetime import datetime

from django.test import TestCase

from fool.models import Article, Author, StockTicker


class ArticleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Setup data once for all tests in class."""
        cls.author = Author.objects.create(
            username='jondoe',
            email='jodoe@alias.com',
            first_name='John',
            last_name='Doe',
            short_bio='I exist ephemerally, for testing only.',
        )
        cls.article = Article.objects.create(
            author=cls.author,
            body=(
                '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam in neque'''
                ''' sed arcu dapibus ultricies vitae placerat sem. Sed orci urna, euismod'''
                ''' vel odio non, porta facilisis nunc. Nunc quis eros nec metus egestas'''
                ''' blandit id sit amet lacus.'''
            ),
            promo='Only the financially prudent will know how to save.',
            headline='Read this if you want to get rich!',
            publish_at=datetime.now(),
            disclosure='The views expressed in this article are fictitious.',
        )


    def test_article_by_line_attribute(self):
        """Article has a by line if author is identiifed."""
        self.assertEqual(self.article.by_line, 'John Doe')


class StockTickerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Setup StockTicker test data."""
        exchange = StockTicker.Exchange._member_map_.values()[0]
        sector = StockTicker.Sector._value2member_map_.values()[0]
        cls.stock_ticker = StockTicker.objects.create(
                company_name='Motley Fool',
                symbol='MF',
                current_price='100.00',
                change=100.00,
                exchange=exchange,
                sector=sector,
            )
