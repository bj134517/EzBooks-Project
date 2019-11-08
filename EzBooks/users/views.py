###############################################################################
#                           Views for the users app                           #
###############################################################################

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import User_profileForm
from ez_main.models import Class_schedule, User_profile
from users.models import User_profile
from django.contrib.auth.decorators import login_required


def logout(request):
    """ Log out the currently logged in user """
    auth_logout(request)
    return HttpResponseRedirect(reverse('ez_main:home_page'))

def register(request):
    """ Register a new user """
    if request.method != 'POST':
        # Display a blank registration form
        form = User_profileForm()
    else:
        # Process the complete form
        form = User_profileForm(data=request.POST)
    
    if form.is_valid():
        # Authenticate user and save into the model
        new_user = form.save()
        authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
        auth_login(request, authenticated_user)
        
        #Create class schedule for user based on major selection
        new_users_schedule = Class_schedule(user_id=authenticated_user)
        new_users_schedule.create_class(authenticated_user.major)
        new_users_schedule.save()
        return HttpResponseRedirect(reverse('ez_main:home_page'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
