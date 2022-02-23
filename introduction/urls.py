from django.urls import path
from .import views

urlpatterns = [
    path('home', views.index,name='home'),
    path('contact', views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('feedback',views.feedback,name='feedback'),
]
