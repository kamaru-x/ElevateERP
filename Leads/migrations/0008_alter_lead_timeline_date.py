# Generated by Django 4.2.4 on 2024-03-28 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0007_lead_timeline_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead_timeline',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
