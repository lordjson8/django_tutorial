from django.urls import path
from .views import *

urlpatterns = [
    path('post/',post_view,name='hello'),
    path('cb/',TestView.as_view(),name='hello'),
]
