from django.urls import path
from  valeo.views import  *


urlpatterns = [
    path('', print, name='valeo'),

]
