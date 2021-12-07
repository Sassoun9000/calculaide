from django.shortcuts import render

from .forms import *


def index(request):
    return render(request, "index.html")


def general_infos(request):
    context = {
        "color": ColorCategory(),
        "project_type": ProjectChoices(),
        "pv_characteristics": CharacteristicsPv()
    }
    return render(request, "general_infos.html", context=context)
