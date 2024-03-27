# Generated by Django 4.2.4 on 2024-03-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0017_alter_student_email_alter_student_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='Image',
            field=models.ImageField(null=True, upload_to='Places'),
        ),
        migrations.AddField(
            model_name='place',
            name='Type',
            field=models.CharField(choices=[('India', 'India'), ('Abroad', 'Abroad')], default='India', max_length=25),
        ),
    ]