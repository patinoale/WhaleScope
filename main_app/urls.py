from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('about/', views.about, name='about'),
    path('sightings/', views.SightingList.as_view(), name='index'),
    path('sightings/<int:pk>/', views.SightingDetail.as_view(), name='detail')
]