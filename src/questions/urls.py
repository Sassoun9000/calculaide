from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from questions.views import *

app_name = "questions"


urlpatterns = [
    path("", questions, name="questions-index")
]
