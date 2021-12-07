from django.shortcuts import render

from .forms import *

from .utils import QPATH_FORMS


def index(request):
    return render(request, "index.html")


def general_infos(request):
    context = {
        "infos": ColorCategory(),
        "project_type": ProjectChoices(),
        "pv_characteristics": PVCharacteristics()
    }
    return render(request, "general_infos.html", context=context)


def questions(request):
    context = dict()
    if request.method == "POST":
        r = request.POST
        print(r)
        if "previous" in r:
            request.session["index"] -= 2
            print("YOOOOP")
        current_index = request.session["index"]
        if current_index == 0:
            request.session["QPath"] = ["start",]
            if "pv" in r:
                request.session["QPath"].append(QPATH_FORMS["pv"])
            if "pac" in r:
                request.session["QPath"].append(QPATH_FORMS["pac"])
            if "iso" in r:
                request.session["QPath"].append(QPATH_FORMS["iso"])
            request.session["QPath"].append("ColorCategory()")

        request.session["index"] += 1
        i = request.session["index"]

        context["form"] = eval(request.session["QPath"][i])
        if i == 1:
            context["2nd_question"] = True
        if i == len(request.session["QPath"]) - 1:
            return render(request, "results.html")

    else:
        request.session["index"] = 0
        context["form"] = ProjectChoices()
        context["first_question"] = True
        print("Première itération")

    return render(request, "questions.html", context=context)
