from django.urls import path,include
from .views import main,projects


urlpatterns = [
    path('',main,name='home-main'),
    path('',main,name='homepage'),
    path('projects-tab/',projects,name='projects-page'),
    
]
