from barbershop.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Visit
from .telegram_bot import send_telegram_message
import asyncio
from django.db.models.signals import m2m_changed


@receiver(m2m_changed, sender=Visit.services.through)
def send_telegram_notification(action, instance, **kwargs):
    if action == "post_add" and kwargs.get("pk_set"):
        services = [service.name for service in instance.services.all()]
        message = f"""
*Новая запись на консультацию* 

*Имя:* {instance.name} 
*Телефон:* {instance.phone or 'не указан'} 
*Мастер:* {instance.master}
*Услуги:* {', '.join(services) or 'не указаны'}
-------------------------------------------------------------
"""
        asyncio.run(
            send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message)
        )
