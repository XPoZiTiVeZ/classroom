# Generated by Django 5.0.2 on 2024-04-13 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_remove_course_lessons_remove_lesson_solutions_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lesson',
            new_name='Task',
        ),
    ]
