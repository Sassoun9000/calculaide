from django.shortcuts import render

from .forms import *


def index(request):
    return render(request, "index.html")


def general_infos(request):
    context = {
        "infos": GeneralInfos(),
        "project_type": ProjectChoices(),
    }
    return render(request, "general_infos.html", context=context)
