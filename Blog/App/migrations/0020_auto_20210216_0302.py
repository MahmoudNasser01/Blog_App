# Generated by Django 3.1.6 on 2021-02-16 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_auto_20210216_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
