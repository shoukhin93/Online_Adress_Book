# Generated by Django 2.0.1 on 2018-02-17 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adress_book', '0003_auto_20180217_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adress_book.UserData')),
            ],
        ),
    ]
