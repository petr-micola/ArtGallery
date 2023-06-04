from django.shortcuts import render
from django.views.generic import ListView

from .models import Artwork


class ArtworkListView(ListView):
    model = Artwork
    context_object_name = 'artworks_list'
    template_name = 'artworks.html'


def index(request):
    newest_art = Artwork.objects.order_by('-created_at')[0]
    featured_art = Artwork.objects.order_by('-title')[:3]

    context = {
        'newest_art': newest_art,
        'featured_art': featured_art,
    }
    return render(request, 'index.html', context=context)
