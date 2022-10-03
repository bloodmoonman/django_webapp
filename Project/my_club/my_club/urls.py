
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('members.urls')), #AS WE DID FOR THE FIRST APP, EVENTS, WE WANT THIS ORIGINAL URLS.PY TO POINT TO MEMBERS APP TOO.
    path('members/', include('django.contrib.auth.urls')), #THIS IS FOR, REFERENCING THE AUTHENTICATION, THIS WILL ALLOW US TO USE BUNCH OF URLS THAT COMES WITH THE AUTHENTICATION    
]
