# Generated by Django 2.0.1 on 2018-02-17 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adress_book', '0008_auto_20180217_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='user_id',
        ),
    ]
