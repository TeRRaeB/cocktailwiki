# Generated by Django 5.1.2 on 2024-10-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0, verbose_name=((0, 'Created'), (1, 'Published'), (2, 'Denied'))),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=2500),
        ),
    ]
