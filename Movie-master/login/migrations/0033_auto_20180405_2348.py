# Generated by Django 2.0.2 on 2018-04-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0032_auto_20180405_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='phoneno',
            field=models.CharField(max_length=30),
        ),
    ]
