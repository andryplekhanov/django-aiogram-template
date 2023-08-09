from django.contrib import admin

from app_telegram.models import TGUser


class TGUserAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'created']
    list_filter = ['created', ]
    search_fields = ['tg_id', ]
    save_on_top = True


admin.site.register(TGUser, TGUserAdmin)
