# Generated by Django 5.0.2 on 2024-04-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(default='9c58cc718f2a415ea548b8d7bbf9a445', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]