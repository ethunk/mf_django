# Generated by Django 2.2.16 on 2021-01-30 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fool', '0003_auto_20210128_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='publish_at',
            field=models.DateTimeField(null=True),
        ),
    ]
