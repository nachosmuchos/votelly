# Generated by Django 2.0.2 on 2018-07-27 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_program_description'),
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='related_program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programs.Program'),
        ),
    ]
