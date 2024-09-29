from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Visit, Master, Service
from django.http import JsonResponse
from django.views.generic import (
    View,
    TemplateView,
)
from django.urls import reverse_lazy
from django.db.models import Q


class MainView(View):
    
    def get(self, request):
        form = AppointmentForm()
        masters = Master.objects.all()

        return render(request, "main.html", {"form": form, "masters": masters})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")

        if form.errors:
            return render(
                request,
                "main.html",
                {"form": form, "masters": Master.objects.all()},
            )


class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"


class ServicesByMasterView(View):

    def get(self, request, master_id):
        services = Master.objects.get(id=master_id).services.all()
        services_data = [
            {"id": service.id, "name": service.name} for service in services
        ]
        return JsonResponse({"services": services_data})
