# Generated by Django 2.1 on 2018-09-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_program_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='vote_question',
            field=models.TextField(default='Desctiption'),
        ),
    ]
