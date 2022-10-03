from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  #THIS IS ALREADY EXIST, I DIDN'T CREATE THAT MODEL
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'})) #THIS EMAILINPUT IS FUNCTION, WE ARE GONNA PASS ATTRIBUTES.
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs={'class': 'form-control', 'placeholder':'Username'} 
        self.fields['password1'].widget.attrs={'class': 'form-control', 'placeholder':'Password'}               #YEY FOUND IT.
        self.fields['password2'].widget.attrs={'class': 'form-control', 'placeholder':'Confirm Password'}     #NOW FIGURE OUT HOW TO REMOVE TITLES FROM USERCREATIONFORM.
        #self.fields['username'].widget.attrs['placeholder'] = 'Username'
#THERE IS A class="form-control" in html, SINCE THIS REGISTRATION
#IS BUILT IN DJANGO MODULE, WE CAN'T STYLE OUR REGISTER_USER PAGE
#LIKE WE DO USUALLY
#SO WE NEED TO ADD THIS class="form-control" SOMEHOW INTO FORMS.PY
#FORM IN HTML FILE IS JUST {{ form.as_p }} THERE IS NOW HTML TO
#ADD THIS class="form-control"   SO WE NEED TO ADD THAT CLASS INTO
#OUR FORMS.PY FILE

#WE'LL USE WIDGET, WIDGET LETS US TO PLAY AROUND WITH FORMS.