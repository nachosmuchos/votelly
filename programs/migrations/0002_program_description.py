# Generated by Django 2.0.2 on 2018-07-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='description',
            field=models.TextField(default='Desctiption'),
        ),
    ]
