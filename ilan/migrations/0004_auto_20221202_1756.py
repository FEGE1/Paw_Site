# Generated by Django 3.1.6 on 2022-12-02 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0003_auto_20221130_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ilan',
            options={'ordering': ['-created_date']},
        ),
    ]