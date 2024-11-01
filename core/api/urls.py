from home.views import index ,Person
from django.urls import path
# the floder name must and should be 'api' it self
# creating a seperate floder and file for urls for the views in app [home]
urlpatterns = [
    path('index/', index),
    path('person/', Person),
]
