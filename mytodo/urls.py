from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
    
    url(r'^add$',views.addtask,name="add"),
    url(r'^delete$',views.deletetask,name="delete"),
    url(r'^macomp$',views.completetask,name="macomp"),
    url(r'^activate$',views.activatetask,name="activate"),
    url(r'^suspend$',views.suspendtask,name="suspend")
]
