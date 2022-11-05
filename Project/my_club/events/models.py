from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Venue(models.Model):          
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=20, blank=True) 
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Website Address', blank=True)            #THIS URLField and EmailField validates automatically, checks if theyre appropriate url or email form.
    email_address = models.EmailField('Email Address', blank=True)
    owner = models.IntegerField('Venue Owner', blank=False, default=1)  

                                                                        
                                                                        
    def __str__(self):
        return self.name 


class MyClubUser(models.Model):                     
                                                    
    first_name = models.CharField(max_length=30)    
    last_name = models.CharField(max_length=30)     
    email = models.EmailField('User Email') 

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Event(models.Model):
    name = models.CharField('Event Name', max_length=120) 
    date = models.DateTimeField('Event Date')             
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)       
                                                                                            #WHEN WE DELETE EVENT, BUT THAT EVENT ALSO HAS A VENUE SO VENUE ALSO NEED TO BE DELETED, on_delete MEANS DELETE EVERYTHIN CONNECTED TO IT
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)     
    description = models.TextField(blank=True)                     
    attendees = models.ManyToManyField(MyClubUser, blank=True)    
                                                            
                                                           
    def __str__(self):
        return self.name            #THIS ALLOWS US TO USE OUR MODEL IN THE ADMIN AREA, THIS POPS UP ON THAT PAGE
                                    #AND WILL LIST THE NAME FOR EACH EVENT BECASUE; name

    @property
    def days_until(self):
        today = date.today()
        until = self.date.date() - today #self.date refers to field in Event's model. date = models.DateTimeField('Event Date') THIS ONE, 
                                         
                                        
        until_stripped = str(until).split(",", 1)[0] 

                                                     
        days = until_stripped.split(" ", 1)[0]      
        if int(days) < 0:                          
            return "This Event Took Place!"
        else:
            return until_stripped
