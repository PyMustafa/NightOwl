from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    """
    A signal receiver function that creates a Profile instance for a newly created
    User instance.
    Parameters:
        sender (class): The class of the model that sent the signal.
        instance (object): The actual instance of the sender that was saved.
        created (bool): A boolean indicating whether a new instance was created or an existing instance was updated.
        **kwargs: Any additional keyword arguments that may be passed to the signal.
    """
    #after this u should import the this signals.py in the ready method of the apps.py in this app