# Generated by Django 3.1 on 2020-08-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='NFC_Tag',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
