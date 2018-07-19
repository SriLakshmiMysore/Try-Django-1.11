import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import RestuarantLocation

def restuarant_listview(request):
    template_name = 'restuarants/restuarants_list.html'
    queryset = RestuarantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name,context)
