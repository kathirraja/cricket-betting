from django.forms import ModelForm
from .models import Player
from bedding_admin.models import Match, Team

class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = []

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        exclude =[]

class MatchForm(ModelForm):
    class Meta:
        model = Match
        exclude =[]