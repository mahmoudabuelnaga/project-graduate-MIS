# Generated by Django 2.2.11 on 2020-05-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_remove_contactusinformation_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact us'},
        ),
        migrations.AlterField(
            model_name='contactusinformation',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
