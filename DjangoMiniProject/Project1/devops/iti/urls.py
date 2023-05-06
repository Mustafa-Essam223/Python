from django.urls import path
from iti.views import *

urlpatterns = [
    path('hello', hello_world, name='test'),

    path('courseList', getCourses, name='courses_test'),
    path('courseList/<int:idx>', getCourseByID, name='courses_id'),
    # <int:idx> control the input in the url

]
