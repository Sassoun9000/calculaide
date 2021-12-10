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
        label="Isolation des combles",
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
    power = forms.ChoiceField(choices=PV_POWER_LEVEL, label="Dimensionnement de l'installation (kWc)", widget=MyRadioSelect)
    pv_type = forms.ChoiceField(choices=PV_TYPE, label="Type de panneaux", widget=MyRadioSelect)


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
    power = forms.ChoiceField(choices=PAC_POWER_LEVEL, label="Dimensionnement de l'installation (kWc)", widget=MyRadioSelect)
    pv_type = forms.ChoiceField(choices=PAC_TYPE, label="Type de panneaux", widget=MyRadioSelect)


class SurfaceIso(forms.Form):
    surface_rampants = forms.IntegerField(label="Sous rampants")
    surface_perdus = forms.IntegerField(label="Combles perdus")


INMATES_NUMBER = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6+"),
]


COLOR_CODES = [
    ("blue", "14 879 €"),
    ("yellow", "19 074 €"),
    ("purple", "29 148 €"),
    ("rose", "> 29 148 €"),
]


class ColorCategory(forms.Form):
    family_members = forms.ChoiceField(
        choices=INMATES_NUMBER,
        label="Nombre de personnes composant le foyer fiscal",
        widget=MyRadioSelect
    )
    income_color = forms.ChoiceField(choices=COLOR_CODES, label="Catégorie", widget=MyRadioSelect)
