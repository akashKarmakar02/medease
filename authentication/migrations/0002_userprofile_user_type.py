# Generated by Django 5.0.3 on 2024-03-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')], default='patient', max_length=20),
        ),
    ]
