# Generated by Django 3.1.6 on 2021-02-16 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
