# Generated by Django 4.1.3 on 2022-12-01 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('excelupload', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name = 'CheckCourse',
            fields = [
                ('cid_int', models.IntegerField(primary_key = True, serialize = False)),
                ('cid', models.CharField(max_length = 255)),
                ('cname', models.CharField(blank = True, max_length = 255, null = True)),
                ('crd', models.IntegerField(blank = True, null = True)),
                ('yr_20', models.CharField(blank = True, max_length = 255, null = True)),
                ('yr_21', models.CharField(blank = True, max_length = 255, null = True)),
                ('yr_22', models.CharField(blank = True, max_length = 255, null = True)),
            ],
            options = {
                'db_table': 'check_course',
                'managed' : False,
            },
        ),
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
            name = 'Enrollment',
            fields = [
                ('id', models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                ('year', models.IntegerField(blank = True, null = True)),
                ('cid', models.CharField(max_length = 255)),
                ('cname', models.CharField(blank = True, max_length = 255, null = True)),
                ('crd', models.IntegerField(blank = True, null = True)),
                ('gpa', models.CharField(blank = True, max_length = 50, null = True)),
                ('gbn', models.CharField(blank = True, max_length = 50, null = True)),
                ('re', models.BooleanField(default = False)),
                ('cid_int', models.ForeignKey(db_column = 'cid_int', on_delete = django.db.models.deletion.CASCADE, to = 'check.checkcourse')),
                ('up', models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = 'excelupload.document')),
                ('user', models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = settings.AUTH_USER_MODEL, verbose_name = 'user')),
            ],
            options = {
                'db_table': 'rec_enrollment',
                'managed' : True,
            },
        ),
    ]
