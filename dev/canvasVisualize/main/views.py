from django.shortcuts import render
from django.views import View


from .models import Visualization
from .forms import VisualizationForm
from .upload import open

bucket_name = "cvisualize-code"

def renderMainPage(request):
    return render(request, "main/home.html" )

def renderVisualizations(request):
    if request.method == "GET":
        visualizations = Visualization.objects.all()[:16]
        for v in visualizations:
            v.imgPreview  = open(bucket_name, f"images/visualizationPreviews/{v.title}.txt")

        return render(request, "main/visualizations.html", {
            "visualizations":visualizations
        })


class CreateVisualization(View):
    def get(self, request): 
        return render(request, "main/createVisualization.html", {
            "form":VisualizationForm()
        })

    def post(self, request):

        form = VisualizationForm(request.POST)
        if form.is_valid():
            code = request.POST['code']
            imgPreview = request.POST['imgPreview']
            form = form.cleaned_data



            v = Visualization(title = form['title'],  creator = request.user )
            v.save()
            v.upload(code, imgPreview)

            return renderMainPage(request)
        else: 
            return render(request, "main/createVisualization.html", {
                "form":form
                }, status=400)


def individualVisualization(request, pk): 
    if request.method == 'GET':
        v = Visualization.objects.get(pk = pk)
        v = v.get()
        return render(request, "main/visualization.html", {
        "visualization":v
        })

def viewCode(request, pk):
        v = Visualization.objects.get(pk = pk)
        v = v.get()
        return render(request, "main/viewCode.html", {
            "visualization":v
        })