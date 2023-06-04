from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='Author name',
                            help_text='Enter a name of the author.')
    born_year = models.IntegerField(blank=True, null=True, verbose_name='Author born year',
                                    help_text='Enter a born year of the author.')
    biography = models.TextField(blank=True, null=True, verbose_name='Author biography',
                                 help_text='Enter a biography of the author.')
    image = models.ImageField(upload_to='images/authors/', blank=True, null=True, verbose_name='Author image',
                              help_text='Upload an image of the author.')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Genre name',
                            help_text='Enter a name of the genre.')

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.CharField(max_length=50, verbose_name='Artwork title', help_text='Enter a title of the artwork.')
    author = models.ManyToManyField(Author, help_text='Select an author of the artwork.')
    year = models.IntegerField(blank=True, null=True, verbose_name='Artwork year',
                               help_text='Enter a year of the artwork.')
    description = models.TextField(blank=True, null=True, verbose_name='Artwork description',
                                   help_text='Enter a description of the artwork.')
    image = models.ImageField(upload_to='images/artworks/', blank=True, null=True, verbose_name='Artwork image',
                              help_text='Upload an image of the artwork.')
    genre = models.ManyToManyField(Genre, help_text='Select a genre of the artwork.')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Artwork'
        verbose_name_plural = 'Artworks'
        ordering = ['-title']

    def __str__(self):
        return self.title
