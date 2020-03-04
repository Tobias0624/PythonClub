from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('getresource/', views.getresource, name='source'),
    path('getmeeting/', views.getmeeting, name= 'meeting' ),
    path('meetid/<int:id>', views.meetid, name='meetdetails'),
    path('newMeeting/', views.newMeeting, name= 'newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]