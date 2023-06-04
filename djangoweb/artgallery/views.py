from django.shortcuts import render

from .models import Artwork


def index(request):
    newest_art = Artwork.objects.order_by('-created_at')[0]
    featured_art = Artwork.objects.order_by('-title')[:3]

    context = {
        'newest_art': newest_art,
        'featured_art': featured_art,
    }
    return render(request, 'base.html', context=context)
