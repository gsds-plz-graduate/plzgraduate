# Generated by Django 4.1.3 on 2022-11-28 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_enrollment_delete_recenrollment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name = 'enrollment',
            options = {'managed': True},
        ),
    ]
