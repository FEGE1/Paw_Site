# Generated by Django 3.1.6 on 2022-11-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files/covers', verbose_name='fotograf'),
        ),
    ]
