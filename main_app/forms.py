from django.forms import ModelForm
from .models import Watch

class WatchForm(ModelForm):
    class Meta:
        model = Watch
        fields = ['date']