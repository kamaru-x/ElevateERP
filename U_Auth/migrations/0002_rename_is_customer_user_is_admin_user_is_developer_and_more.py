# Generated by Django 5.0.2 on 2024-02-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_Auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_customer',
            new_name='is_admin',
        ),
        migrations.AddField(
            model_name='user',
            name='is_developer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_telecaller',
            field=models.BooleanField(default=False),
        ),
    ]