# Generated by Django 2.2.28 on 2022-05-31 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotification',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
