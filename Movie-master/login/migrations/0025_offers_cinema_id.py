# Generated by Django 2.0.2 on 2018-04-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_cinema_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='cinema_id',
            field=models.ForeignKey(default='pvrndd', on_delete='true', to='login.Cinema'),
            preserve_default=False,
        ),
    ]