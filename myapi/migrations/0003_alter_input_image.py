# Generated by Django 3.2.6 on 2021-08-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20210827_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='image',
            field=models.CharField(max_length=20),
        ),
    ]