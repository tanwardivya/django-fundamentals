from django.contrib import admin
from meetingplaner.models import Meetings, Room
from django.contrib.admin import ModelAdmin


# Register your models here.
# admin.site.register(Meetings)
admin.site.register(Room)

@admin.register(Meetings)
class MeetingAdmin(ModelAdmin):
    model = Meetings
    list_display = ['id', 'title', 'date', 'start_time', 'room']
    search_fields = ("title",)
    list_filter = ("date",)