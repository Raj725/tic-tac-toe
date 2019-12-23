from django.shortcuts import render

from gameplay.models import Game


def home(request):
    all_my_games = Game.objects.games_for_user(request.user)
    return render(request, "player/home.html", {'games': all_my_games})

