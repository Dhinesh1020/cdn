from . import views
from django.urls import path

urlpatterns = [
    path('members/', views.members, name='members'),
    path('edit/<str:firstName>/', views.edit_item, name='edit_item'),
    path('delete/<str:firstName>/', views.delete_item, name='delete_item'),
    path('inventory/', views.inventory, name='inventory'),
    path('dns/', views.dns, name='dns'),
    path('distribution/', views.DistributionView.as_view(), name='distribution'),
    path('dashboard/', views.dashboard, name='dashboard'),
]