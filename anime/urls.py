from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime, name='anime'),
    path('galeria/', views.galeria, name='galeria'),
    path('anime/<str:pk>', views.AnimeDetailView.as_view(), name='anime-detail'),
    path('galeria/<str:pk>', views.GaleriaDetailView.as_view(),
         name='galeria-detail'),
]
urlpatterns += [
    path('anime/create/', views.AnimeCreate.as_view(), name='anime_create'),
    path('anime/<str:pk>/update', views.AnimeUpdate.as_view(), name='anime_update'),
    path('anime/<str:pk>/delete', views.AnimeDelete.as_view(), name='anime_delete'),
    path('galeria/create/', views.GaleriaCreate.as_view(), name='galeria_create'),
    path('galeria/<str:pk>/update',
         views.GaleriaUpdate.as_view(), name='galeria_update'),
    path('galeria/<str:pk>/delete',
         views.GaleriaDelete.as_view(), name='galeria_delete')
]
