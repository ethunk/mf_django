# Generated by Django 2.2.16 on 2021-02-02 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fool', '0010_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='promo',
            field=models.CharField(max_length=400, null=True, unique=True),
        ),
    ]
