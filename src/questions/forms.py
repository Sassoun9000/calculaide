from django import forms


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseForm, self).__init__(*args, **kwargs)


forms.Form = BaseForm


class GeneralInfos(forms.Form):
    last_name = forms.CharField(label="Nom")
    first_name = forms.CharField(label="Prénom")
    email = forms.EmailField(label="Adresse e-mail")


class ProjectChoices(forms.Form):
    pv = forms.BooleanField(label="Photovoltaïque")
    pac = forms.BooleanField(label="Pompe à chaleur")
    iso = forms.BooleanField(label="Isolation des combles")

POWER_LEVEL = [("three", "3 kWc"), ("four_five", "4,5 kWc")]
PV_TYPE = [("classic", "Classique"), ("hybrid", "Hybrides")]

class CharacteristicsPv(forms.Form):
    power = forms.ChoiceField(choices=POWER_LEVEL, label="Dimensionnement de l'installation (kWc)", widget=forms.RadioSelect)
    pv_type = forms.ChoiceField(choices=PV_TYPE, label="Type de panneaux", widget=forms.RadioSelect)