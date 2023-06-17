# Generated by Django 3.2 on 2023-06-16 13:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0002_auto_20230503_0836'),
        ('colleges', '0002_auto_20230403_2235'),
        ('students', '0005_auto_20230425_1057'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='digitaldrawinganswer',
            unique_together={('student', 'digital_draw', 'answer')},
        ),
        migrations.AlterUniqueTogether(
            name='handdrawinganswer',
            unique_together={('student', 'hand_draw', 'answer')},
        ),
        migrations.AlterUniqueTogether(
            name='mcqanswer',
            unique_together={('student', 'question', 'answer')},
        ),
        migrations.AlterUniqueTogether(
            name='practicedrawinganswer',
            unique_together={('student', 'practice_draw', 'answer')},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('seat_number', 'national_id', 'phone_number', 'user', 'college')},
        ),
    ]