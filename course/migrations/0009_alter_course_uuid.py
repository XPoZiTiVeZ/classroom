# Generated by Django 5.0.2 on 2024-04-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_course_owners_alter_course_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(default='cb86b983d982499daa9fe01dcf5630ed', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
