# Generated by Django 5.1.2 on 2024-11-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]
