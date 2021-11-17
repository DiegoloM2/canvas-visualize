from django.forms import ModelForm
from .models import Visualization


class VisualizationForm(ModelForm):
    class Meta: 
        model = Visualization
        fields = ["title", ]