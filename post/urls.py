from django.urls import path
from .views import *

urlpatterns = [
    path('',post_view,name='post'),
    path('post/create/',create_post_view,name='create_post'),
    path('post/<int:id>/',detail_view,name='post_detail'),
    path('post/delete/<int:id>/',delete_view,name='post_delete')
]



