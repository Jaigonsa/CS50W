# Generated by Django 4.2 on 2023-06-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_register_enddate_alter_register_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
