# Generated by Django 4.1.3 on 2022-11-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name = 'CourseKey',
            fields = [
                ('cid_int', models.IntegerField()),
                ('cid', models.CharField(max_length = 255, primary_key = True, serialize = False)),
            ],
            options = {
                'db_table': 'course_key',
                'managed' : False,
            },
        ),
        migrations.CreateModel(
            name = 'RecEnrollment',
            fields = [
                ('id', models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                ('year', models.IntegerField(blank = True, null = True)),
                ('cid', models.CharField(max_length = 255)),
                ('cname', models.CharField(blank = True, max_length = 255, null = True)),
                ('crd', models.IntegerField(blank = True, null = True)),
                ('gpa', models.CharField(blank = True, max_length = 50, null = True)),
                ('gbn', models.CharField(blank = True, max_length = 50, null = True)),
                ('re', models.BooleanField(default = False)),
                ('user_id', models.IntegerField(blank = True, null = True)),
            ],
            options = {
                'db_table': 'rec_enrollment',
                'managed' : False,
            },
        ),
    ]
