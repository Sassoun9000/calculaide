QPATH_FORMS = {
    "pv": "PVCharacteristics()",
    "pac": "PACCharacteristics()",
    "iso": "SurfaceIso()",
}

PR_AMOUNT = {
    "blue": {
        "pv3": 380,
        "pv9": 280,
        "pv36": 160,
        "pv100": 80,
        "pv_hybrid": 2500,
        "pac_eau": 4000,
        "pac_air": 0,
        "combles_perdus": 0,
        "sous_rampants": 25,
        "ce_solaire": 4000,
        "thermodynamique": 1200,
    },
    "yellow": {
        "pv3": 380,
        "pv9": 280,
        "pv36": 160,
        "pv100": 80,
        "pv_hybrid": 2000,
        "pac_eau": 3000,
        "pac_air": 0,
        "combles_perdus": 0,
        "sous_rampants": 20,
        "ce_solaire": 3000,
        "thermodynamique": 800,
    },
    "purple": {
        "pv3": 380,
        "pv9": 280,
        "pv36": 160,
        "pv100": 80,
        "pv_hybrid": 1000,
        "pac_eau": 2000,
        "pac_air": 0,
        "combles_perdus": 0,
        "sous_rampants": 15,
        "ce_solaire": 2000,
        "thermodynamique": 400,
    },
    "pink": {
        "pv3": 380,
        "pv9": 280,
        "pv36": 160,
        "pv100": 80,
        "pv_hybrid": 0,
        "pac_eau": 0,
        "pac_air": 0,
        "combles_perdus": 0,
        "sous_rampants": 7,
        "ce_solaire": 0,
        "thermodynamique": 0,
    },
}

CEE_AMOUNT = {
    "blue": {
        "pv3": 0,
        "pv9": 0,
        "pv36": 0,
        "pv100": 0,
        "pv_hybrid": 251,
        "pac_eau": 4364,
        "pac_air": 900,
        "combles_perdus": 22,
        "sous_rampants": 22,
        "ce_solaire": 275,
        "thermodynamique": 168,
    },
    "yellow": {
        "pv3": 0,
        "pv9": 0,
        "pv36": 0,
        "pv100": 0,
        "pv_hybrid": 125,
        "pac_eau": 4364,
        "pac_air": 450,
        "combles_perdus": 22,
        "sous_rampants": 22,
        "ce_solaire": 137,
        "thermodynamique": 84,
    },
    "purple": {
        "pv3": 0,
        "pv9": 0,
        "pv36": 0,
        "pv100": 0,
        "pv_hybrid": 125,
        "pac_eau": 2727,
        "pac_air": 450,
        "combles_perdus": 11,
        "sous_rampants": 11,
        "ce_solaire": 137,
        "thermodynamique": 84,
    },
    "pink": {
        "pv3": 0,
        "pv9": 0,
        "pv36": 0,
        "pv100": 0,
        "pv_hybrid": 125,
        "pac_eau": 2727,
        "pac_air": 450,
        "combles_perdus": 11,
        "sous_rampants": 11,
        "ce_solaire": 137,
        "thermodynamique": 84,
    },
}


def result_process(answers):
    total_sub = {}
    income = answers["income_color"]
    if "pv" in answers:
        pv_power = float(answers["pv_power"])
        if pv_power >= 3:
            kwc_amount = "pv3"
        elif 3 < pv_power <= 9:
            kwc_amount = "pv9"
        elif 9 < pv_power <= 36:
            kwc_amount = "pv36"
        else:
            kwc_amount = "pv100"
        total_sub["pv_pr_sub"] = pv_power * PR_AMOUNT[income][kwc_amount]
        if answers["pv_type"] == "hybrid":
            total_sub["pv_pr_sub"] += PR_AMOUNT[income]["pv_hybrid"]
            total_sub["pv_cee_sub"] = CEE_AMOUNT[income]["pv_hybrid"]
    if "pac" in answers:
        pac_type = answers["pac_type"]
        total_sub["pac_pr_sub"] = PR_AMOUNT[income][pac_type]
        total_sub["pac_cee_sub"] = CEE_AMOUNT[income][pac_type]
    if "iso" in answers:
        total_sub["pac_pr_sub"] = 0
        total_sub["pac_cee_sub"] = 0
        if answers["surface_rampants"]:
            total_sub["pac_pr_sub"] += PR_AMOUNT[income]["sous_rampants"]
            total_sub["pac_cee_sub"] += CEE_AMOUNT[income]["sous_rampants"]
        if answers["surface_perdus"]:
            total_sub["pac_pr_sub"] += PR_AMOUNT[income]["combles_perdus"]
            total_sub["pac_cee_sub"] += CEE_AMOUNT[income]["combles_perdus"]
    if "btd" in answers:
        total_sub["btd_pr_sub"] = PR_AMOUNT[income]["thermodynamique"]
        total_sub["btd_cee_sub"] = CEE_AMOUNT[income]["thermodynamique"]
    if "cesol" in answers:
        total_sub["cesol_pr_sub"] = PR_AMOUNT[income]["ce_solaire"]
        total_sub["cesol_cee_sub"] = CEE_AMOUNT[income]["ce_solaire"]

    return total_sub
