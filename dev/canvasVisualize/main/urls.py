from .views import *
from django.urls import path, include

urlpatterns = [
    path('', renderMainPage, name = "main"), 
    path('visualization/create/', CreateVisualization.as_view(), name = "createVisualization"), 
    path('visualizations/', renderVisualizations, name = "visualizations" ), 
    path('visualization/<int:pk>', individualVisualization, name = "visualization"), 
    path('code/<int:pk>', viewCode, name = "code"),
]