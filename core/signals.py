from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Visit
from .telegram_bot import send_telegram_message
from barbershop.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
import asyncio


@receiver(m2m_changed, sender=Visit.services.through)
def send_telegram_notification(sender, instance, action, **kwargs):
    """
    Обработчик сигнала m2m_changed для модели Visit.
    Он обрабатывает добавление КАЖДОЙ услуги в запись на консультацию.
    Отправка ОДНОГО сообщения в телеграмм выполняется в первом условии
    """
    if action == "post_add" and kwargs.get("pk_set"):
        services = [service.name for service in instance.services.all()]
        print(f"УСЛУГИ: {services}")
        message = f"""
*Новая запись на консультацию* 

*Имя:* {instance.name} 
*Телефон:* {instance.phone or 'не указан'} 
*Мастер:* {instance.master or 'не указан'}
*Услуги:* {', '.join(services) or 'не указаны'}
-------------------------------------------------------------
"""
        asyncio.run(
            send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message)
        )
