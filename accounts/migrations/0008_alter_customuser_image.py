# Generated by Django 4.0 on 2022-01-05 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='../uploads/image/profile_p.jpg', null=True, upload_to='image'),
        ),
    ]
