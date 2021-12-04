from django import forms


class GeneralInfos(forms.Form):
    last_name = forms.CharField(label="Nom")
    first_name = forms.CharField(label="Prénom")
    email = forms.EmailField(label="Adresse mail")


class ProjectChoices(forms.Form):
    pv = forms.BooleanField(label="Photovoltaïque")
    pac = forms.BooleanField(label="Pompe à chaleur")
    iso = forms.BooleanField(label="Isolation des combles")
