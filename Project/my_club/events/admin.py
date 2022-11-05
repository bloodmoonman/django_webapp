from django.contrib import admin
from .models import Venue, Event, MyClubUser

admin.site.register(MyClubUser)  

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('address',)     
    search_fields = ('name', 'address') 

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'date', 'description', 'manager')
    list_display = ('name', 'date', 'venue')
    list_filter = ('date', 'venue')
    ordering = ('-date',)  
