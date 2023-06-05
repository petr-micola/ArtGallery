from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artworks/', views.ArtworkListView.as_view(), name='artworks'),
    path('artworks/<int:pk>/', views.ArtworkDetailView.as_view(), name='artwork')
]
