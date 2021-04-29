# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import ALBUMS

# Create your views here.

def index(request):
    message="Hello Bro"
    return HttpResponse(message)

def listing(request):
    albums= ["<li>{}</li>".format(albumn['name']) for albumn in ALBUMS]
    messages="""<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(messages)

def getAlbum(request,album_id):
    id= int (album_id)
    album=ALBUMS[id]
    artists=" ".join([artist['name'] for artist in album['artists']])
    message= "l\'album {} à pour artiste {}".format(album['name'],artists)
    return HttpResponse(message)