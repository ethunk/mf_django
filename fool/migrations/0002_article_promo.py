# Generated by Django 2.2.16 on 2021-01-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='promo',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
