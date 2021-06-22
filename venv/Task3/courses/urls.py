from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('courses/', CourseView.as_view(), name='courses_api'),
    path('courses/<int:pk>/', CourseDelete.as_view(), name='single_course')
]


urlpatterns = format_suffix_patterns(urlpatterns)