###############################################################################
#                           Views for the users app                           #
###############################################################################

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import User_profileForm

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
        new_user = form.save()
        authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
        auth_login(request, authenticated_user)
        return HttpResponseRedirect(reverse('ez_main:home_page'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)