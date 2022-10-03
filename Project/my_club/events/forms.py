from multiprocessing import Event
from select import select
from django import forms
from django.forms import ModelForm
from .models import Venue, Event


class VenueForm(ModelForm):
    class Meta:
        model = Venue            #MODEL IS THE VENUE 
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address',)  #THESE ARE THE FIELDS WE WANT USERS TO SEE ON THE WEB PAGE. WE COULD USE '__all__' FOR ALL FIELDS.
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
        'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
        'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
        'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
        'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web'}),
        'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),}
        labels = {                              #IF YOU DON'T ADD THESE '' OR THE labels DICTIONARY THEN THE LABELS WILL SHOW UP ON THE PAGE, TRY IT OUT. WE ARE LEFTING EMPTY BUT
                                                #WE USE PLACEHOLDERS IN WIDGETS SO IT LOOKS MUCH BETTER.
            'name': '',         
            'address': '',
            'zip_code': '',            
            'phone': '',                 
            'web': '',          
            'email_address': '',
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'venue', 'attendees', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 25, }),

        }

        labels = {
            'name': '',
            'date': '',
            'venue': '',
            'attendees': '',
            'description': '',
        }
#NOW WE HAVE OUR FORM, WE NEED TO CREATE A WEB FOR THIS FORM TO SHOW UP. AND HTML MEANS URL, VIEWS. WE'LL CREATE PATH IN URLS.PY AND METHOD IN VIEWS.PY FOR THIS WEB PAGE.

class EventAdminForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'venue', 'manager', 'attendees', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 25, }),

        }

        labels = {
            'name': '',
            'date': '',
            'venue': '',
            'manager': '',
            'attendees': '',
            'description': '',
        }
