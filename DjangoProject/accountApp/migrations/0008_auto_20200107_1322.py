# Generated by Django 2.2.7 on 2020-01-07 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0007_merge_20200107_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age_range',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '10대'), (20, '20대'), (30, '30대'), (40, '40대'), (50, '50대'), (60, '60대 이상')], null=True),
        ),
    ]
