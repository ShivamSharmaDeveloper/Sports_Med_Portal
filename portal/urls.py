from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('index', views.index, name='index'),
    path('sports', views.sports, name='sports'),
    # path('addsports', views.addsports, name='addsports'),
    path('medical', views.medical, name='medical'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('update/<int:id>', views.update, name='update'),
    path('update/update/<int:id>', views.update, name='updated'),
    path('update/logout', views.logout, name='logout'),
    path('logout', views.logout, name='logout'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
]
