from django.urls import path, re_path
from . import views
from .feeds import LatestPostsFeed

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
    path('sightings/<int:pk>/<int:comment_id>/', views.comments_update, name='comments_update'),
    path('sightings/<int:sighting_id>/<int:comment_id>/comments_delete/', views.comments_delete, name='comments_delete'),
    path('sightings/<int:sighting_id>/<int:comment_id>/<int:reply_id>/replies_delete/', views.replies_delete, name='replies_delete'),
    path('sightings/<int:sighting_id>/<int:comment_id>/add_reply', views.add_reply, name='add_reply'),
    path('sightings/<int:sighting_id>/add_photo/', views.add_photo, name='add_photo'),
    path('sightings/<int:sighting_id>/<int:photo_id>/photos_delete/', views.photos_delete, name='photos_delete'),
    path('map/', views.map, name='map'),
    path('likes/<int:pk>/', views.like_sighting, name='like_sighting'),
    ### path('likecomment/<int:pk>/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('feed/rss', LatestPostsFeed(), name="post_feed"),
    re_path(r'^map/generate', views.generate, name="generate")
]