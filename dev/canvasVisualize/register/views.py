from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import RegisterForm

from PIL import Image

def registerView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.cleaned_data.get('profileImg', False)
            if image: 
                image = Image.open(image)
                form.cleaned_data['profileImg'] = image.resize((400, 400))


            user = form.save()
            login(request, user)

            return render(request,"register/success.html")
        else:
            return render(request, "register/register.html", {"form": form})

    form = RegisterForm()
    return render(request,"register/register.html", {"form": form})
