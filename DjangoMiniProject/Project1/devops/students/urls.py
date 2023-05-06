from django.urls import path
from  students.views import  *


urlpatterns = [
    path('', printing, name='stud_info'),

]
