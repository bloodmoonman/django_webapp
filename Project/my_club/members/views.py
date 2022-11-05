from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, try again.")) 
            return redirect('login_user')
    else:
        return render(request, 'members/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out!")) 
    return redirect('home') 
    

def register_user(request):
    if request.method == "POST": 
        form = RegisterUserForm(request.POST)
                                            
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  
                                                       
            user = authenticate(username=username, password=password) #WE AUTHENTICATE THE USER
            login(request, user)  #LOGS IN THE USER
            messages.success(request, ('Registered!'))
            return redirect('home')
    else:   #THIS MEANS, THEY DIDN'T FILL OUT THE FORM SO WE WANT TO SHOW THEM THE FORM ITSELF.
        form = RegisterUserForm() #WE JUST WANT THE PLAIN FORM, NOT FILLED OUT FORM. SO () IS EMPTY

    return render(request, 'members/register_user.html', {'form': form, })




