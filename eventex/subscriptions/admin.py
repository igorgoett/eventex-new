from datetime import date
from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscripitonModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'phone', 'cpf', 'created_at',
                    'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid','created_at')


    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()


    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscripitonModelAdmin)