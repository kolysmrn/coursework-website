# Generated by Django 2.1.3 on 2018-12-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_auto_20181218_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
