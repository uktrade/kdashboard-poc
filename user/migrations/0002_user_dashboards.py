# Generated by Django 3.0.3 on 2020-04-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kdashboard', '0002_remove_dashboards_user'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dashboards',
            field=models.ManyToManyField(to='kdashboard.Dashboards'),
        ),
    ]
