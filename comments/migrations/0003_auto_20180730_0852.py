# Generated by Django 2.0.2 on 2018-07-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180727_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='related_program',
            new_name='related_character',
        ),
    ]
