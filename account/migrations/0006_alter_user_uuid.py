# Generated by Django 5.0.2 on 2024-04-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default='62b20f3af38311eea60d645d868f2c89', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID'),
        ),
    ]
