from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify

from students.models import (
    DigitalDrawingAnswer,
    HandDrawingAnswer,
    McqAnswer,
    PracticeDrawingAnswer,
    Student,
    StudentResults,
)

User = get_user_model()


@receiver(post_save, sender=McqAnswer, dispatch_uid="mcq_result")
def mcq_result(sender, instance, created, **kwargs):
    student_result, _ = StudentResults.objects.get_or_create(user=instance.student)
    student_result.mcq_result += instance.score
    student_result.save()


@receiver(post_save, sender=HandDrawingAnswer, dispatch_uid="hand_drawing_result")
def hand_drawing_result(sender, instance, created, **kwargs):
    student_result, _ = StudentResults.objects.get_or_create(user=instance.student)
    student_result.hand_drawing_result = instance.score
    student_result.save()


@receiver(post_save, sender=DigitalDrawingAnswer, dispatch_uid="digital_drawing_result")
def digital_drawing_result(sender, instance, created, **kwargs):
    student_result, _ = StudentResults.objects.get_or_create(user=instance.student)
    student_result.digital_art_result = instance.score
    student_result.save()


@receiver(
    post_save, sender=PracticeDrawingAnswer, dispatch_uid="practice_drawing_result"
)
def practice_drawing_result(sender, instance, created, **kwargs):
    student_result, _ = StudentResults.objects.get_or_create(user=instance.student)
    student_result.trial_result = instance.score
    student_result.save()


@receiver(post_save, sender=Student)
def student_result(sender, instance, created, **kwargs):
    notify.send(
        sender=instance.user,
        recipient=instance.user,
        verb=f"تهانينا علي انضمامك الي كلية '{instance.college}'",
        description=f"تم انشاء طالب جديد بإسم '{instance.full_name}'",
        level="success",
    )


@receiver(post_save, sender=Student, dispatch_uid="update_up_to_level")
def update_up_to_level(sender, instance, created, **kwargs):
    student_result, _ = StudentResults.objects.get_or_create(user=instance)
    student_result.up_to_level = instance.up_to_level
    student_result.save()

    if student_result.up_to_level:
        notify.send(
            sender=instance.user,
            recipient=instance.user,
            verb=f"تهانينا{instance.full_name}",
            description="انت الآن لائق للترقي لهذه الكلية",
            level="success",
        )
    elif not student_result.up_to_level:
        notify.send(
            sender=instance.user,
            recipient=instance.user,
            verb=f"عذرا{instance.full_name}",
            description="انت لست لائق للترقي لهذه الكلية",
            level="error",
        )
