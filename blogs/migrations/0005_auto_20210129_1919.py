# Generated by Django 2.2.16 on 2021-01-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20210129_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='disclosure',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=8000, unique=True),
        ),
    ]
