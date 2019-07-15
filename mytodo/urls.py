
from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('/#todo',views.homepage,name='homepagetodo'),
    path('add',views.addtask,name="add"),
    path('delete',views.deletetask,name="delete"),
    path('macomp',views.completetask,name="macomp"),
    path('activate',views.activatetask,name="activate"),
    path('suspend',views.suspendtask,name="suspend")
]
