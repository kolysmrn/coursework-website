# Generated by Django 2.1.3 on 2018-12-15 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
