from django import forms


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseForm, self).__init__(*args, **kwargs)


forms.Form = BaseForm


class ProjectChoices(forms.Form):
    pv = forms.BooleanField(required=False, label="Panneaux Photovoltaïques")
    pac = forms.BooleanField(required=False, label="Pompe à chaleur")
    iso = forms.BooleanField(required=False, label="Isolation des combles")
    btd = forms.BooleanField(required=False, label="Ballon Thermodynamique")
    cesol = forms.BooleanField(required=False, label="Chauffe-eau solaire")


PV_POWER_LEVEL = [
    ("three", "3"),
    ("four_five", "4,5"),
    ("six", "6"),
    ("seven_five", "7,5"),
    ("nine", "9"),
    ("ten_five", "10,5"),
    ("twelve", "12")
]
PV_TYPE = [("classic", ""), ("hybrid", "")]


class PVCharacteristics(forms.Form):
    power = forms.ChoiceField(choices=PV_POWER_LEVEL, label="Dimensionnement de l'installation (kWc)", widget=forms.RadioSelect)
    pv_type = forms.ChoiceField(choices=PV_TYPE, label="Type de panneaux", widget=forms.RadioSelect)


PAC_POWER_LEVEL = [
    ("four", "4"),
    ("six", "6"),
    ("eight", "8"),
    ("eleven", "11"),
    ("fourteen", "14"),
    ("sixteen", "16")
]
PAC_TYPE = [("airair", ""), ("aireau", "")]


class PACCharacteristics(forms.Form):
    power = forms.ChoiceField(choices=PAC_POWER_LEVEL, label="Dimensionnement de l'installation (kWc)", widget=forms.RadioSelect)
    pv_type = forms.ChoiceField(choices=PAC_TYPE, label="Type de panneaux", widget=forms.RadioSelect)


class SurfaceIso(forms.Form):
    surface_rampants = forms.IntegerField(label="Sous rampants")
    surface_perdus = forms.IntegerField(label="Combles perdus")


INMATES_NUMBER = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
]


COLOR_CODES = [
    ("blue", "Bleu"),
    ("yellow", "Jaune"),
    ("purple", "Violet"),
    ("rose", "Rose"),
]


class ColorCategory(forms.Form):
    family_members = forms.ChoiceField(
        choices=INMATES_NUMBER,
        label="Nombre de personnes composant le foyer fiscal",
        widget=forms.RadioSelect
    )
    income_color = forms.ChoiceField(choices=COLOR_CODES, label="Type de panneaux", widget=forms.RadioSelect)
