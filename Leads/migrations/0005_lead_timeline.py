# Generated by Django 4.2.4 on 2024-03-28 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0004_leads_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead_Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Title', models.TextField()),
                ('Color', models.CharField(max_length=15)),
            ],
        ),
    ]
