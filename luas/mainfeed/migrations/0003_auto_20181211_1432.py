# Generated by Django 2.1.3 on 2018-12-11 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeed', '0002_headline_hit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headline',
            options={'ordering': ['hit']},
        ),
    ]