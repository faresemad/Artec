from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
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


@receiver(post_save, sender=Student)
def send_notification(sender, instance, created, **kwargs):
    if created:
        notify.send(
            sender=instance.user,
            recipient=instance.user,
            verb=f"تهانينا علي انضمامك الي كلية '{instance.college}'",
            description=f"تم انشاء طالب جديد بإسم '{instance.full_name}'",
            level="success",
        )
    elif instance.up_to_level:
        notify.send(
            sender=instance.user,
            recipient=instance.user,
            verb=f"تهانينا{instance.full_name}",
            description="انت الآن لائق للترقي لهذه الكلية",
            level="success",
        )
    elif not instance.up_to_level:
        notify.send(
            sender=instance.user,
            recipient=instance.user,
            verb="مازلت غير لائق",
            description="انت غير لائق للترقي لهذه الكلية",
            level="warning",
        )
