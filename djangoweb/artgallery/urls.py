from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artworks/', views.ArtworkListView.as_view(), name='artworks')
]
