# Generated by Django 2.1.3 on 2018-12-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]