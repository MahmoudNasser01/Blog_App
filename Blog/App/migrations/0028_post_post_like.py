# Generated by Django 3.1.6 on 2021-02-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_auto_20210217_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_like',
            field=models.ManyToManyField(related_name='likes', to='App.Post'),
        ),
    ]
