# Generated by Django 4.2.1 on 2023-05-23 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_web', '0004_eventinfo_userinfo_drink_userinfo_exercise_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventinfo',
            options={'verbose_name': '예측한 가격 리스트'},
        ),
        migrations.AlterModelTable(
            name='eventinfo',
            table='estimated_price',
        ),
    ]
