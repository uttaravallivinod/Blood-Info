# Generated by Django 2.2.10 on 2020-03-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Binfo', '0003_blood_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood',
            name='Age',
        ),
        migrations.AddField(
            model_name='blood',
            name='DOB',
            field=models.DateField(default='1990-01-01'),
            preserve_default=False,
        ),
    ]
