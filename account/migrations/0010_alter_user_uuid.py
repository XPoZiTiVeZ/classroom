# Generated by Django 5.0.2 on 2024-04-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default='87b352ddf38611eeb971645d868f2c89', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID'),
        ),
    ]
