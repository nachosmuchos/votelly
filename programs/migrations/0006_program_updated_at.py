# Generated by Django 2.1 on 2019-07-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_program_image_alt_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]