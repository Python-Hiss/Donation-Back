# Generated by Django 4.0 on 2022-01-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='../uploads/image/profile_p.jpg', upload_to='image'),
        ),
    ]
