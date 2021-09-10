from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout),

    path('travels', views.index),
    path('view/<int:travel_id>', views.detail), 
    path('add', views.add), 
    path('join/<int:travel_id>', views.join),  
    path('remove/<int:travel_id>', views.remove),
    path('delete/<int:travel_id>', views.delete),
    
]
