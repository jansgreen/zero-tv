from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# THIS CODE DOES NOT COME EXACTLY FROM A TUTORIAL, THIS IS THE RESULT OF SEVERAL TUTORIALS TO BE ABLE TO UNDERSTAND HOW THE SIGNALS WORK.

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ update the order fields by signals """
    
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ update the order fields by signals """


