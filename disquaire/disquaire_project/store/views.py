# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking
from django.template import loader
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage

#from .models import ALBUMS

# Create your views here.

def index(request):
    #message="Hello Bro"
    # request albums
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    template = loader.get_template('store/index.html')
    context={'albums':albums}
    print(context)
    return render(request, 'store/index.html', context)

def listing(request):
    albums = Album.objects.filter(available=True)
    paginator = Paginator(albums_list, 9)
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        albums = paginator.page(paginator.num_pages)
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    context={'albums':albums,
            'paginate':True}
    return render(request, 'store/listing.html', context)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists= [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    context={'albums_tiltle':albums_tiltle,'albums_name':albums_name,'albums_id':albums_id}
    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }
    return render(request, 'store/search.html', context)

