# Generated by Django 2.2.28 on 2022-11-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20221117_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulenotification',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Prime'), (1, 'Buddy')], default=0),
        ),
        migrations.AlterField(
            model_name='schedulenotification',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]