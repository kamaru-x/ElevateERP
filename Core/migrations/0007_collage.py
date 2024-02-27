# Generated by Django 4.2.4 on 2024-02-27 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_course_added_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.IntegerField(default=1)),
                ('Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Core.agents')),
                ('Place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Core.place')),
            ],
        ),
    ]
