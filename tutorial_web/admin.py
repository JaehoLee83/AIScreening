from django.contrib import admin
from .models import EventInfo, UserInfo


# Register your models here.
class Event_userAdmin(admin.ModelAdmin):
    list_display = ('price','price')

admin.site.register(EventInfo, Event_userAdmin)