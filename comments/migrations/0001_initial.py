# Generated by Django 2.0.2 on 2018-07-27 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0002_character_related_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('comment_time', models.DateTimeField()),
                ('related_program', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
    ]
