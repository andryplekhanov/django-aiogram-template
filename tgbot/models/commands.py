# Не оптимизировать импорты и не менять их порядок

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_ac.settings")
os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
django.setup()

import logging

from asgiref.sync import sync_to_async

from app_telegram.models import TGUser

logger = logging.getLogger(__name__)


@sync_to_async
def add_or_create_user(user_id: int) -> TGUser:
    user, created = TGUser.objects.get_or_create(tg_id=user_id)
    if created:
        logger.info(f"user {user.tg_id} was added to DB")
    else:
        logger.info(f"User {user.tg_id} is already exist")
    return user
