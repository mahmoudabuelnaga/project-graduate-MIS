# Generated by Django 2.2.11 on 2020-05-09 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20200509_0404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='postal_code',
            new_name='zip',
        ),
    ]
