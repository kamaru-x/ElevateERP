# Generated by Django 4.2.4 on 2024-03-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry_categories',
            name='CATID',
            field=models.CharField(default='STOE', max_length=10),
            preserve_default=False,
        ),
    ]
