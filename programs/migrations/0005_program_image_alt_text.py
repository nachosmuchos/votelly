# Generated by Django 2.1 on 2018-09-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_program_vote_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image_alt_text',
            field=models.CharField(default='alt_text', max_length=200),
            preserve_default=False,
        ),
    ]
