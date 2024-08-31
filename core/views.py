from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Service, Master
import asyncio
from django.http import JsonResponse

def main_page_view(request):
    masters = Master.objects.all()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")

        if form.errors:
            return render(request, "main.html", {"form": form, "masters": masters})

    else:
        form = AppointmentForm()

    return render(request, "main.html", {"form": form, "masters": masters})


def thanks(request):
    return render(request, "thanks.html")


def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})