# Generated by Django 2.1 on 2019-07-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0007_auto_20190703_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
