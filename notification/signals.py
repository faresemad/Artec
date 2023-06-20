from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify

from students.models import Student

User = get_user_model()


@receiver(post_save, sender=User)
def send_welcome_notification(sender, instance, created, **kwargs):
    if created:
        notify.send(
            sender=instance,
            recipient=instance,
            verb=f"مرحبا {instance.name}",
            description="مرحبا بك في منصنتنا الجديدة",
            level="success",
        )
