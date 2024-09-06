"""
URL configuration for barbershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core.views import (
    MainView,
    ThanksTemplateView,
    ServicesByMasterView,
    VisitCreateView,
    VisitDetailView,
    VisitUpdateView,
    VisitDeleteView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainView.as_view(), name="main"),
    path("thanks/", ThanksTemplateView.as_view(), name="thanks"),
    path(
        "get_services_by_master/<int:master_id>/",
        ServicesByMasterView.as_view(),
        name="get_services_by_master",
    ),
    path("visit/add/", VisitCreateView.as_view(), name="create_view"),
    path("visit/<int:pk>/view/", VisitDetailView.as_view(), name="detial_view"),
    path("visit/<int:pk>/edit/", VisitUpdateView.as_view(), name="edit_view"),
    path("visit/<int:pk>/delete/", VisitDeleteView.as_view(), name="delete_view"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
