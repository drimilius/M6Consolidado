
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('add/', views.add_vehiculo, name='add_vehiculo'),  
    path('listar/', views.listar_vehiculos, name='listar_vehiculos'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
