# Generated by Django 2.2.17 on 2020-12-10 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='transfers',
            new_name='Transfer',
        ),
    ]
