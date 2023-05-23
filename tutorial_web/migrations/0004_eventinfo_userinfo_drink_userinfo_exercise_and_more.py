# Generated by Django 4.2.1 on 2023-05-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_web', '0003_remove_userinfo_drink_remove_userinfo_exercise_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='drink',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='exercise',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='family_diabetes',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gestational',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='hypertension',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='tobacco',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='waist_circumference',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]