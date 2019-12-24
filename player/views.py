from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from gameplay.models import Game
from .forms import InvitationForm
from .models import Invitation


@login_required
def home(request):
    all_my_games = Game.objects.games_for_user(request.user)
    return render(request, "player/home.html", {'games': all_my_games})


@login_required
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(data=request.POST, instance=invitation)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm
    return render(request, "player/new_invitation_form.html", {'form': form})
