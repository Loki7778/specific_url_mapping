from csk.views import *
from django.urls import path

app_name='csk'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('buvi/',buvi,name='buvi'),

]
