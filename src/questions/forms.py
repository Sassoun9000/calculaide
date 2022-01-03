from django import forms


class MyRadioSelect(forms.RadioSelect):
    option_template_name = "widgets/radio_option.html"


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseForm, self).__init__(*args, **kwargs)


forms.Form = BaseForm


class ProjectChoices(forms.Form):
    pv = forms.BooleanField(
        required=False,
        label="Panneaux photovoltaïques",
        widget=forms.CheckboxInput(attrs={'class': 'zob'})
    )
    pac = forms.BooleanField(
        required=False,
        label="Pompe à chaleur",
        widget=forms.CheckboxInput(attrs={'class': 'zob'})
    )
    iso = forms.BooleanField(
        required=False,
        label="Isolation",
        widget=forms.CheckboxInput(attrs={'class': 'zob'})
    )
    btd = forms.BooleanField(
        required=False,
        label="Ballon thermodynamique",
        widget=forms.CheckboxInput(attrs={'class': 'zob'})
    )
    cesol = forms.BooleanField(
        required=False,
        label="Chauffe-eau solaire",
        widget=forms.CheckboxInput(attrs={'class': 'zob'})
    )


PV_POWER_LEVEL = [
    ("3", "3"),
    ("4.5", "4,5"),
    ("6", "6"),
    ("9", "9"),
    ("12", "12"),
    ("15", "15"),
]
PV_TYPE = [("classic", "Classiques"), ("hybrides", "Hybrides")]


class PVCharacteristics(forms.Form):
    pv_power = forms.ChoiceField(choices=PV_POWER_LEVEL, label="Dimensionnement des panneaux photovoltaïques (kWc)", widget=MyRadioSelect)
    pv_type = forms.ChoiceField(choices=PV_TYPE, label="Type de panneaux", widget=MyRadioSelect)


PAC_POWER_LEVEL = [
    ("4", "4"),
    ("6", "6"),
    ("8", "8"),
    ("11", "11"),
    ("14", "14"),
    ("16", "16")
]
PAC_TYPE = [("pac_air", "Air-Air"), ("pac_eau", "Air-Eau")]


class PACCharacteristics(forms.Form):
    power = forms.ChoiceField(choices=PAC_POWER_LEVEL, label="Dimensionnement de la pompe à chaleur (kW)", widget=MyRadioSelect)
    pac_type = forms.ChoiceField(choices=PAC_TYPE, label="Type de pompe à chaleur", widget=MyRadioSelect)


class SurfaceIso(forms.Form):
    surface_rampants = forms.IntegerField(label="Sous rampants (m²)", initial=0)
    surface_perdus = forms.IntegerField(label="Combles perdus (m²)", initial=0)


INMATES_NUMBER = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8")
]


COLOR_CODES = [
    ("blue", "< 14 879 €"),
    ("yellow", "< 19 074 €"),
    ("purple", "< 29 148 €"),
    ("pink", "> 29 148 €"),
]


class ColorCategory(forms.Form):
    family_members = forms.ChoiceField(
        choices=INMATES_NUMBER,
        label="Nombre de personnes composant le foyer fiscal",
        widget=MyRadioSelect
    )
    income_color = forms.ChoiceField(choices=COLOR_CODES, label="Revenu Fiscal de Référence", widget=MyRadioSelect)
