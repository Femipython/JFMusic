from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # /music/album_id/   -numbers represent id or pk (product key or )
    path('<int:pk>/', views.DetailView.as_view( ), name='detail'),

    # /music/album/add
    path('album/add/$', views.AlbumCreate.as_view(), name='add-album'),




]

