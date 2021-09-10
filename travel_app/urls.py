from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('/', views.index),
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout),

    path('travels', views.index),
    path('view/<int:travel_id>', views.detail), 
    path('addtrip', views.addtrip),
]
