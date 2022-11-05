
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>', views.home, name='home'), 
    path('event_list', views.all_events, name='list-events'),
    path('add_venue', views.add_venue, name='add-venue'),      
    path('list_venue', views.list_venue, name='list-venue'),    #v
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('results', views.results, name='search-results'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('add_event', views.add_event, name='add-event'),
    path('update_event/<event_id>', views.update_event, name='update-event'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),
    path('events_mine', views.events_mine, name='events_mine'),

]                                                         
                                                                #name='add-venue' WE USE THE NAME IN HTML FILES TO CONNECT THE HTML AND URL. LIKE THIS IN NAVBAR.HTML;
                                                          #          <li class="nav-item">
                                                          #              <a class="nav-link" href="{% url 'add-venue' %}">Add Venue</a>
                                                          #          </li>                                                THIS Add Venue WILL BE DISPLAYED IN NAVBAR.
                                #COMMENT FOR 6TH LINE AND SO ON; 
                                #SO THIS '' MEANS;  WWW.AYKAN.COM/'' --- NOTHING IN THIS CASE BECAUSE IT IS EMPTY STRING; IF IT WERE TO BE path('aykan', ...
                                #IT WOULD BE WWW.AYKAN.COM/aykan
                                #AND NOW WE SET VIEWS.HOME, THAT MEANS IN VIEWS MODULE OR IN OTHER WORDS IN VIEWS.PY WE NEED TO CREATE home FUNCTION. BECAUSE WE ARE
                                #IMPORTING THE VIEWS SO VIEWS.SOMETHING MEANS USING A METHOD OR FUNCTION FROM VIEWS.PY
                                #home='name'
                                #WE ADDED PATH CONVERTERS INTO OUR PATH ' ' these are path converters <>/<>
                                #THIS WILL SET www.aykan.com/year/month    AS HOME PAGE YEAR IS INTEGER, MONTH IS STRING BECAUSE WE SET THEM TO BE SO. <int:year>/ etc.
                                #NOW WE NEED TO ADD THESE PATHS TO VIEWS.PY
                                #WHEN USER ENTERS THE URL AND HITS ENTER, IT REQUESTS INFO FROM VIEWS.PY
                                #SO LETS SAY WE CLICKED THE HOME PAGE, WE SET THIS PATH CORRECTLY TO HOME PAGE IN URLS.PY, BY POINTING THE CORRECT METHOD IN 
                                #OUR VIEWS.PY SO IN THIS CASE views.home POINTS OUT THE home METHOD(FUNCTION) IN VIEWS.PY
                                #AND THAT HOME FUNCTION IS RENDERS THE REQUEST. BECAUSE IT HAS ALL THE VALUES, HTML FILES ETC. IT IS THE BRIDGE BETWEEN DATABASE, HTML, AND WEBPAGE
                                #FOR INSTANCE WHEN USER ENTERS THE FOLLOWING URL; www.aykan.com/2022/June THESE 2022 AND JUNE ARE VALUES THAT WILL BE PASSED
                                # AS PARAMETERS IN VIEWS.HOME FUNCTION SO THAT FUNCTION WILL USE THOSE AS ARGUMENTS INSIDE OF THE CONTEXT DICT.
                                
