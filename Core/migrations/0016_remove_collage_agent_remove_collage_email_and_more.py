# Generated by Django 4.2.4 on 2024-03-02 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_student_agent_commission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collage',
            name='Agent',
        ),
        migrations.RemoveField(
            model_name='collage',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='collage',
            name='Mobile',
        ),
    ]
