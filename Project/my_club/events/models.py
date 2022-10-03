from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Venue(models.Model):          #SO IT IS FOREIGNKEY OF EVENT SO WE CAN CALL EVENT.VENUE.NAME TO GET VENUE'S NAME
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=20, blank=True) #YOU DONT NECESSARILY GIVE THIS INTEGERFIELD
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Website Address', blank=True)            #THIS URLField and EmailField validates automatically, checks if theyre appropriate url or email form.
    email_address = models.EmailField('Email Address', blank=True)
    owner = models.IntegerField('Venue Owner', blank=False, default=1)  #INTEGERFIELD, BECAUSE WE WILL ASSIGN USER IDS WHERE DJANGO HAS BEEN CREATING FOR US WHENEVER WE CREATE A NEW USER WITH OWNER.
                                                                        #WHY IntegerField? BECAUSE OUR USERS HAVE UNIQUE IDS(PRIMARY KEYS)
                                                                        #WE CAN ASSOCIATE WITH THEM. WHEN SOMEONE ADDS VENUE, WHATEVER ID OF THAT
                                                                        #SOMEONE IS THATS WHO THE OWNER IS.
                                                                        #THAT WAY WE CAN TIE IT TO USER, TIE IT TO EVENT, TO EVERYTHING
    def __str__(self):
        return self.name 


class MyClubUser(models.Model):                     #SO NOW THE USER CAN GO TO MANY EVENTS AS POSSIBLE RIGHT?
                                                    #BUT THIS ISN'T CONNECTED TO ANY TABLE YET.
    first_name = models.CharField(max_length=30)    #WE DO THIS IN EVENT BECAUSE USERS GO TO EVENTS.
    last_name = models.CharField(max_length=30)     #WE NEED MANYTOMANY FIELD
    email = models.EmailField('User Email') 

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Event(models.Model):
    name = models.CharField('Event Name', max_length=120) #NAMING WITH THE ' NAME ' AS FIRST ARG
    date = models.DateTimeField('Event Date')             #YOU DONT NEED TO NAME THESE THO
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)       #FOREIGNKEY CONNECTS TWO TABLES, VENUE AND EVENT IN THIS CASE.
                                                                                            #WHEN WE DELETE EVENT, BUT THAT EVENT ALSO HAS A VENUE SO VENUE ALSO NEED TO BE DELETED, on_delete MEANS DELETE EVERYTHIN CONNECTED TO IT
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)     #SET_NULL MEANS, IF THE MANAGER OF THIS EVENT DELETES HIS PROFILE, LEAVE THE WEBPAGE, WE DON'T WANT TO DELETE ALL OF THE OTHER WHERE HE IS MANAGER AS WELL. WE JUST SET NULL, ALL OF THE MANAGER FIELD, INSTEAD OF DELETING IT. #BLANK=TRUE IT MEANS IF THERES ONE YET, NULL=TRUE IS COMMON, IN CASE THERE ISNT ONE YET 
    description = models.TextField(blank=True)                      #BLANK=TRUE MEANS YOU CAN LEAVE THIS BLANK ON THE WEBPAGE
    attendees = models.ManyToManyField(MyClubUser, blank=True)    #BLANK=TRUE BECAUSE USER MIGHT NOT GO TO EVENT.    
                                                            #EVERYTIME YOU MAKE CHANGE IN MODELS.PY YOU 
                                                            #NEED TO MAKEMIGRATION THEN MIGRATE !!!
    def __str__(self):
        return self.name            #THIS ALLOWS US TO USE OUR MODEL IN THE ADMIN AREA, THIS POPS UP ON THAT PAGE
                                    #AND WILL LIST THE NAME FOR EACH EVENT BECASUE; name


                                    #AFTER FINISHING THE TABLES WE NEED TO ADD THESE INTO ADMIN AREA
                                    #GO TO ADMIN.PY

    @property
    def days_until(self):
        today = date.today()
        until = self.date.date() - today #self.date refers to field in Event's model. date = models.DateTimeField('Event Date') THIS ONE, 
                                         #THEN WE ARE GETTING THE DATE OF IT WITH .date() function WE DIDN'T USE JUST self.date BECAUSE DATETIMEFIELD IN THE FIELDS RETURNS DATE AND TIME, WE
                                         #ONLY WANT DATE SO .date()
        until_stripped = str(until).split(",", 1)[0] #THIS IS BECAUSE IT RETURNS 00:00:00
                                                     #SO WHAT THIS WILL DO IS; RIGHT NOW IT SHOWS LIKE; ------------ 3 days, 0:00:00 ------------ SO
                                                     #THAT COMMA IS THE COMMA IN SPLIT. AND WE GET THE FIRST ELEMENT WITH[0] AFTER SPLITTING BECAUSE IT RETURNS LIST(SPLIT RETURNS LIST)
                                                     #["3 days until:", "0:00:00" ]
                                                     #AND THAT 1 IS SAYING ONLY SPLIT FROM THE FIRST COMMA, IF SAY THERE WERE TWO COMMAS IT WOULDNT SPLIT THE SECOND ONE      
        days = until_stripped.split(" ", 1)[0]      #COULDNT USE UNTIL_STRIPPED BECAUSE IT IS NUMBER SPACE DAYS LIKE 118 days. SO WE NEED TO SPLIT AGAIN FROM THE SPACE BETWEEN THEN TAKE THE
        if int(days) < 0:                           #FIRST ELEMENT, WHICH IS THE NUMBER WE WANT BUT IT IS A STRING, SO WE NEED TO MAKE IT INTEGER.
            return "This Event Took Place!"
        else:
            return until_stripped
