# Generated by Django 3.2.5 on 2021-07-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='version',
            field=models.CharField(max_length=10, verbose_name='Version Number'),
        ),
    ]
