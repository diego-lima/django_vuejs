from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Games

def index(request):
    games = Games.objects.all()
    return render(request, "homepage/index.html", { 'games': games })

def games(request):
    games = serialize("json", Games.objects.all())
    return HttpResponse(games, content_type="application/json")
