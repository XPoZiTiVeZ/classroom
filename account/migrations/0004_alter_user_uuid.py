# Generated by Django 5.0.2 on 2024-04-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default='40b0a911f20411ee88cd645d868f2c89', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID'),
        ),
    ]
