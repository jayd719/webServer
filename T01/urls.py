from django.urls import path,include
from .views import main,projects


urlpatterns = [
    path('',main,name='home-main'),
    path('',main,name='homepage'),
    path('check-out-work',projects,name='projects-page'),
    
]
