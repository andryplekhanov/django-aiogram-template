import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_ac.settings")
os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
django.setup()

import logging

from asgiref.sync import sync_to_async

from app_telegram.models import TGUser

logger = logging.getLogger(__name__)


@sync_to_async
def add_user(user_id, full_name, username):
    try:
        user = TGUser(tg_id=int(user_id), fullname=full_name, username=username).save()
        logger.info(f"user {user_id} was added to DB")
        return TGUser.objects.filter(tg_id=user_id).first()
    except Exception as ex:
        logger.error(f"FAIL. User {user_id} was NOT added to DB: {ex}")
        return TGUser.objects.filter(tg_id=user_id).first()
