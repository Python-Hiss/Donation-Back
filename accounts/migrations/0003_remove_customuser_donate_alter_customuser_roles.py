# Generated by Django 4.0 on 2022-01-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='donate',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.CharField(blank=True, choices=[('Donater', 'Donater'), ('hospital', 'hospital'), ('Blood needer', 'Blood needer')], max_length=50, null=True),
        ),
    ]
