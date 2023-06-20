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


@receiver(post_save, sender=Student, dispatch_uid="student_status")
def student_status(sender, instance, created, **kwargs):
    if created:
        instance.user.status = "student_review"
        instance.user.save()
        notify.send(
            instance.user,
            recipient=instance.user,
            verb=f"تم التسجيل بنجاح في كلية {instance.college}",
            description="يمكنك الآن تأدية الاختبارات الخاصة بالقبول في الكلية",
        )


@receiver(post_save, sender=Student, dispatch_uid="update_up_to_level")
def update_up_to_level(sender, instance, created, **kwargs):
    student_result, _ = StudentResults.objects.get_or_create(user=instance)
    student_result.up_to_level = instance.up_to_level
    student_result.save()
    if instance.up_to_level == True:
        instance.user.status = "student"
        instance.user.save()


@receiver(post_save, sender=User, dispatch_uid="user_approval")
def check_user_approval(sender, instance, created, **kwargs):
    if instance.status == "student":
        notify.send(
            instance,
            recipient=instance,
            verb="تهانينا تم قبولك في الكلية",
            description="تهانينا تم قبولك في الكلية و نتمنى لك التوفيق",
        )
