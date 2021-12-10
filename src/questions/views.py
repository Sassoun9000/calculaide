from django.shortcuts import render

from .forms import *

from .utils import QPATH_FORMS, COLOR_AMOUNTS, result_process


def index(request):
    return render(request, "index.html")


def questions(request):
    context = dict()
    print(f"request.method {request.method} ")
    if request.method == "POST":
        r = request.POST.dict()
        r.pop("csrfmiddlewaretoken", None)
        print(r)
        current_index = request.session["index"]
        if current_index == 0:
            request.session["QPath"] = ["start",]
            request.session["answers"] = {}
            if "pv" in r:
                request.session["QPath"].append(QPATH_FORMS["pv"])
            if "pac" in r:
                request.session["QPath"].append(QPATH_FORMS["pac"])
            if "iso" in r:
                request.session["QPath"].append(QPATH_FORMS["iso"])
            request.session["QPath"].append("ColorCategory()")

        if "previous" in r:
            request.session["index"] -= 1
        else:
            request.session["index"] += 1
        i = request.session["index"]
        if i == 1:
            context["first_question"] = True

        r.pop("next", None)
        r.pop("previous", None)
        request.session["answers"].update(r)
        print(f"answers {request.session['answers']}")
        if i == len(request.session["QPath"]):
            context['results'] = result_process(request.session['answers'])
            context['answers'] = request.session['answers']
            return render(request, "results.html", context=context)

        step_name = request.session["QPath"][i]
        context["form"] = eval(step_name)
        context["form_id"] = f"form_{step_name}".replace("()", "")

        if context["form_id"] == "form_ColorCategory":
            context["color_amounts"] = COLOR_AMOUNTS

    else:
        request.session["index"] = 0
        context["form"] = ProjectChoices()
        context["form_id"] = "form_product"
        context["first_question"] = True
        print("Première itération")

    return render(request, "questions.html", context=context)
