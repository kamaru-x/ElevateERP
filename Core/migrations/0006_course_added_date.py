# Generated by Django 4.2.4 on 2024-02-27 06:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Added_Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
