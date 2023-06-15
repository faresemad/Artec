from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from students.models import Student
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=Student)
def send_notification(sender, instance, created, **kwargs):
    if created:
        # Send a notification using the notify function
        notify(
            actor=instance.user,
            recipient=instance.user,
            verb="created",
            target=instance,
            description="A new student has been created",
        )


@receiver(post_save, sender=Student)
def send_student_notification(sender, instance, created, **kwargs):
    if created:
        if instance.up_to_level:
            notify(
                actor=instance.user,
                recipient=instance.user,
                verb="became fit",
                target=instance,
                description="You have become fit to move up to the next level",
            )
        else:
            notify(
                actor=instance.user,
                recipient=instance.user,
                verb="became unfit",
                target=instance,
                description="You are still unfit to move up to the next level",
            )
