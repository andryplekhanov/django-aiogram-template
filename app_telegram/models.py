from django.contrib.auth.models import User
from django.db import models


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('-created',)

    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата обновления')


class TGUser(TimeBasedModel):
    # Раскомментировать, если нужна связка с аккаунтами с сайта
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='пользователь')
    tg_id = models.BigIntegerField(unique=True, db_index=True, verbose_name='id Telegram')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.tg_id}'
