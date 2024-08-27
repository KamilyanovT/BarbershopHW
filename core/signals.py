from barbershop.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Visit
from .telegram_bot import send_telegram_message
import asyncio


@receiver(post_save, sender=Visit)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        message = f"""
*Новая запись на консультацию* 

*Имя:* {instance.name} 
*Телефон:* {instance.phone or 'не указан'} 
*Мастер:* {instance.master}
*Услуги:* {instance.service}
-------------------------------------------------------------
"""
        asyncio.run(
            send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message)
        )
