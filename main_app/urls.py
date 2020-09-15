from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('about/', views.about, name='about'),
    path('sightings/', views.SightingList.as_view(), name='index'),
    path('sightings/<int:pk>/', views.SightingDetail.as_view(), name='detail'),
    path('sightings/create/', views.SightingCreate.as_view(), name='sightings_create'),
    path('sightings/<int:pk>/update', views.SightingUpdate.as_view(), name='sightings_update'),
    path('sightings/<int:pk>/delete', views.SightingDelete.as_view(), name='sightings_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('sightings/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('sightings/<int:pk>/comments_update/', views.comments_update, name='comments_update'),
    path('sightings/<int:pk>/comments_delete/', views.CommentDelete.as_view(), name='comments_delete'),
]