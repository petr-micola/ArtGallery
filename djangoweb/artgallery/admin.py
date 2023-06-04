from django.contrib import admin

from artgallery.models import Artwork, Genre, Author

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Artwork)
