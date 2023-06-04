# Generated by Django 4.2 on 2023-05-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgallery', '0002_genre_artwork_author_artwork_date_artwork_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='date',
            field=models.DateField(blank=True, help_text='Enter the date of the artwork in the format <em>YYYY-MM-DD</em>.', null=True, verbose_name='Artwork date'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a description of the artwork.', null=True, verbose_name='Artwork description'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre of the artwork.', to='artgallery.genre'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload an image of the artwork.', null=True, upload_to='img/', verbose_name='Artwork image'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='title',
            field=models.CharField(help_text='Enter a title of the artwork.', max_length=50, verbose_name='Artwork title'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a name of the genre.', max_length=50, verbose_name='Genre name'),
        ),
    ]
