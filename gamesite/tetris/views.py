from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import WebGame# Create your views here.


def index(request):
    current_games = WebGame.objects.order_by('difficulty')[:5]
    context = {
        'current_games': current_games,
    }
    return render(request, 'tetris/index.html', context)

def game_select(request, difficulty):
    game = get_object_or_404(WebGame, difficulty=difficulty)
    return render(request, 'tetris/difficulty.html/', {'webgame': game})

def game_screen(request):
    return HttpResponse("This is the game screen")

