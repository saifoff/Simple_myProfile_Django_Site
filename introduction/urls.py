from django.urls import path
from django.contrib import admin
from  .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('contact', views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('feedback',views.feedback,name='feedback'),
]
