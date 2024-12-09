from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_customer_group(sender, instance, created, **kwargs):
    if created:
        try:
            customer=Group.objects.get(name="cliente")
        except:
            customer=Group.objects.create(name="cliente")
            customer=Group.objects.create(name="encargadodepizzas")
            customer=Group.objects.create(name="administrador")

        instance.user.groups.add(customer)