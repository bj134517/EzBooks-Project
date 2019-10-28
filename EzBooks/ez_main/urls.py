###############################################################################
#                      Url Patterns for the ez_main app                       #
###############################################################################

from django.urls import path

from . import views

# Url patterns for the ez_main app
app_name = 'ez_main'
urlpatterns = [
    # Home page path
    path('', views.home_page, name='home_page'),
]