from django.shortcuts import render, redirect
from .forms import VisitModelForm
from .models import Service, Master
import asyncio


def mainPageView(request):
    if request.method == "POST":
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")
    else:
        form = VisitModelForm()

    masters = Master.objects.all()

    return render(request, "main.html", {"form": form, "masters": masters})


def thanks(request):
    return render(request, "thanks.html")
