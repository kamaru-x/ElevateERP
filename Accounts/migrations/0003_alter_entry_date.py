# Generated by Django 4.2.4 on 2024-03-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_entry_categories_catid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
