# Generated by Django 2.0.1 on 2018-02-17 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adress_book', '0007_contactinfo_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='user_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='adress_book.UserData'),
        ),
    ]