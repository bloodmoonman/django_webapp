from msilib.schema import ListView
from django.shortcuts import redirect, render
from datetime import datetime
import calendar
from calendar import HTMLCalendar
from .models import Event, Venue, MyClubUser
from .forms import VenueForm, EventForm, EventAdminForm
from django.http import HttpResponseRedirect, FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator
from django.contrib import messages


def events_mine(request):         #FIRST OF ALL WE ONLY WANT THIS PAGE TO BE SEEN BY USERS(WHEN THEY LOGGED IN)
    if request.user.is_authenticated:   #CHECKING IF THEY'RE LOGGED IN
        me = request.user.id    #ALL OF THE ATTENDEES HAVE UNIQUE ID, THERE CAN BE SAME NAME BUT NOT ID HENCE USE ID.
        events = Event.objects.filter(attendees=me) #ME IS EQUAL TO THAT LOGGED IN USER'S SPECIFIC ID, SO WE ARE PASSING THAT TO ATTENDEES AND FILTERING WITH IT.
        return render(request, 'events/events_mine', {'events': events})
    else:
        messages.success(request, ("You Are Not Authorized To View This Page!"))
        return redirect('home')



def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont('Helvetica', 14)

    venues = Venue.objects.all()
    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append('----------------')

    c.drawText(textobject)
    c.showPage
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venues.pdf')


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)      #GETTING THE VENUE_ID FROM EVENT MODEL, WHERE DJANGO AUTOMATICALLY CREATED FOR US, WHENEVER WE CREATED A VENUE.
    venue.delete()
    return redirect('list-venue')


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)      #GETTING THE EVENT_ID FROM EVENT MODEL, WHERE DJANGO AUTOMATICALLY CREATED FOR US, WHENEVER WE CREATED AN EVENT.
    if request.user == event.manager:           #CHECKS IF THE LOGGED IN USER MATCHES THE EVENT'S MANAGER
        event.delete()
        messages.success(request, ("Event Deleted!"))
        return redirect('list-events')
    else:
        messages.success(request, ("You are not authorized to delete this event!"))
        return redirect('list-events')


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)      #GETTING THE EVENT_ID FROM EVENT MODEL, WHERE DJANGO AUTOMATICALLY CREATED FOR US, WHENEVER WE CREATED AN EVENT.
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', {'form': form, 'event': event})


def add_event(request):
    submitted = False   #WE NEED THIS VARIABLE TO DETERMINE IF USER SUBMITTED THEIR FORM (OR POSTED IN OTHER WORD)
    if request.method == "POST":        #THIS DETERMINES IF THE USER POSTS THE FORM, IT MEANS THEY FILLED OUT THE FORM AND POSTED.
        if request.user.is_superuser:   #IF USER IS THE SUPERUSER THEN DO THIS;
            form = EventAdminForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:                           #IF NOT THEN WE WILL SHOW THE USER THE FORM THAT INCLUDES THE MANAGER FIELD, IN THIS CASE, IT CAN BE ANYTHING.
            form = EventForm(request.POST)
            if form.is_valid():                 #THIS WILL ASSIGN THE LOGGED IN USER AS A MANAGER, WHEN THEY CREATE AN EVENT.
                event = form.save(commit=False) #Saving with commit=False gets you a model object, then you can add your extra data and save it.
                event.manager = request.user    #ASSIGNING USERNAME TO MANAGER. NOT ID BECAUSE MANAGER IS A NAME
                event.save()                    #IT IS EVENT.MANAGER BECAUSE THE FORM USES THE EVENT MODEL. SO WE ARE ACCESSING THE EVENT CLASS MANAGER VARAIBLE WITH EVENT.MANAGER
                return HttpResponseRedirect('/add_event?submitted=True')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:                               #THIS IS WHEN USER JUST GETS TO THE PAGE, NOT SUBMITTING.
        if request.user.is_superuser:
            form = EventAdminForm
        else:
            form = EventForm #WHY ISN'T THERE REQUEST.POST PASSED IN?? BECAUSE WE WANT TO SHOW THE FORM, WHEN WE PASS REQUEST.POST IT MEANS USER FILLED OUT THE FORM AND 
                             #WE ARE PASSING THAT FORM(INFO, OR FILLED FIELDS WHATEVER YOU SAY) SO THROUGH THAT FORM WE CAN ADD IT INTO DATABASE. BUT IN THIS CASE (ELSE:) WE JUST WANT THEM TO FILL
                             #THE FORM BECAUSE WE KNOW THEY DIDN'T SUBMITTED THEIR FORM YET.
        if "submitted" in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue) 
                                              
    if form.is_valid():    #CHECKS IF THE USER INPUT IS VALID
        form.save()        #THEN WE SAVE IT TO DATABASE
        return redirect('list-venue') #WE USE name='' VAR IN URLS.PY WHEN WE USE REDIRECT
    return render(request, 'events/update_venue.html', {'venue': venue,'form': form, })

def results(request):
    if request.method == "POST": 
        searched = request.POST['searched']  
        results_ven = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search.html', {'searched': searched, 'results_ven': results_ven,})   
    else:                                                                         
        return render(request, 'events/search.html', {})                          
                                                        
                                                        


                                                                                  
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue,})
    

def list_venue(request):
    p = Paginator(Venue.objects.all().order_by('name'), 2)
    page = request.GET.get('page')       
    venues = p.get_page(page)
    return render(request, 'events/venue.html', {'venues': venues,})

def add_venue(request):
    submitted = False  
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():   

            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted, })

def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")): #WITH DATETIME MODULE WE ARE ABLE TO PASS TODAYS DATE IN HOME PAGE, BY DEFAULT.
    name = "Aykan"
    last_name = "Seper"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(
        year,
        month_number,
    )
    event_list = Event.objects.filter(date__year = year, date__month = month_number)  
    now = datetime.now()                                                             
    current_year = now.year

    return render(request, 'events/home.html', {"name": name, "last_name": last_name, "year": year, "month": month, "month_number": month_number, "cal": cal, "current_year": current_year, "event_list": event_list})




def all_events(request):
    event_list = Event.objects.all().order_by('-date')
    return render(request, 'events/event_list.html', {
        "event_list": event_list,
        })
