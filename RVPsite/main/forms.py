from django import forms
from .models import GameId


class GameIdInput(forms.ModelForm):

    class Meta:
        model = GameId
        fields = '__all__'
