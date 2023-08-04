from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from app_telegram.models import TGUser, CallRequest


class TGUserAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'username', 'phone_number', 'fullname', 'created']
    list_filter = ['created',]
    search_fields = ['username', 'fullname', 'tg_id', 'phone_number']
    save_on_top = True


class CallRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_tg_id', 'get_user_phone', 'created', 'status']
    list_filter = ['created', 'status']
    search_fields = ['from_user__tg_id', 'from_user__username', 'from_user__phone_number']
    save_on_top = True

    def get_user_phone(self, obj):
        if obj.from_user:
            return f'{obj.from_user.phone_number}'
        return _('пользователь удалён')
    get_user_phone.short_description = _('номер телефона')

    def get_user_tg_id(self, obj):
        if obj.from_user:
            return f'{obj.from_user.tg_id}'
        return _('пользователь удалён')
    get_user_tg_id.short_description = _('id Telegram')


admin.site.register(TGUser, TGUserAdmin)
admin.site.register(CallRequest, CallRequestAdmin)
