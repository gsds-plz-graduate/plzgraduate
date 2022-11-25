# Generated by Django 4.1.3 on 2022-11-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelupload', '0008_alter_document_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'document',
            name = 'degree',
            field = models.CharField(choices = [('석사', 'Master'), ('박사', 'Combined'), ('통합', 'Ph.D')], default = '석사', max_length = 10),
        ),
    ]