# Generated by Django 4.0 on 2022-01-01 14:14

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0004_remove_account_age_remove_account_blood_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='blood_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='chronic_diseases',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='date',
            field=models.DateField(blank=True, default='2022-01-01', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='donate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='group',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='boes', to='auth.group'),
        ),
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(default='../uploads/image/320.png', upload_to='image'),
        ),
        migrations.AddField(
            model_name='account',
            name='isAuthenticated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
