# Generated by Django 2.2.10 on 2020-03-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Binfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood',
            name='Phone',
            field=models.CharField(default='Null', max_length=10),
            preserve_default=False,
        ),
    ]
