# Generated by Django 2.0.2 on 2018-04-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20180403_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='offer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
