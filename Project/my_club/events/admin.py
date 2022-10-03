from django.contrib import admin
from .models import Venue, Event, MyClubUser

#admin.site.register(Venue)   #REGISTERED THE TABLES.
#admin.site.register(Event)   #NOW WE NEED TO MAKE A MIGRATIONS WITH MAKEMIGRATIONS
admin.site.register(MyClubUser)     #THEN MIGRATE

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone') #THESE ARE THE FIELDS FROM MODELS.PY, WHEN WE PASS THIS INTO TUPLE, IT DISPLAYS THESE FIELDS IN ADMIN AREA.
    ordering = ('address',)      #A TO Z FOR ADDRESS FIELDS. IF I CHANGE IT TO 'name' IT WILL LIST A TO Z OF NAMES. YOU CAN USE ANY FIELD.
    search_fields = ('name', 'address')  #THIS TAKES INTO ACCOUNT THE NAMES AND ADDRESS, IF YOU PUT PHONE NUMBER OR ANY OTHER CHAR THAT NAME AND ADDRESS DOESNT INCLUDE, IT WONT SHOW.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'date', 'description', 'manager')
    list_display = ('name', 'date', 'venue')
    list_filter = ('date', 'venue')
    ordering = ('-date',)  #SO LIST DISPLAY WILL DISPLAY THE NAME, DATE, VENUE AS COLUMNS. AND ORDERING WILL DETERMINE WHICH ONE FIRST AND NOT. SO SEPTEMBER WILL BE ON TOP OF JUNE
                           #BECAUSE IT IS -DATE. IF THERE IS DECEMBER IT WILL BE ON TOP.