###############################################################################
#                          Views for the ez_main app                          #
###############################################################################

from django.shortcuts import render

def home_page(request):
    """ Return the home page for ez_main """
    return render(request, 'ez_main/home_page.html')
