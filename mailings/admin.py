from django.contrib import admin

from mailings.models import Mailing, Client, Message


@admin.register(Mailing)
class AdminMailing(admin.ModelAdmin):
    list_display = ('id', 'first_send_datetime', 'periodicity', 'status')
    list_filter = ('first_send_datetime', 'periodicity', 'status')


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ('subject', 'text')
