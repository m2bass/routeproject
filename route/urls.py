from django.urls import path
from . import views

urlpatterns = [
    path('', views.route_list, name='route_list'),  # This will be accessed via /routes/
    path('new/', views.route_create, name='route_create'),
    path('<str:route_id>/edit/', views.route_update, name='route_update'),
    path('<str:route_id>/delete/', views.route_delete, name='route_delete'),
]
