"""
STATISTICAL ANALYSIS ENGINE
"""

import math

from analytics import pearson_r
from stats import mean, std_dev

# =========================
# STANDARD DEVIATION REPORT
# =========================

def deviation_analysis(state):

    print("\n--- VARIABILITY ANALYSIS ---\n")

    co2_sd = std_dev(state["co2_history"])
    eco_sd = std_dev(state["eco_history"])
    pub_sd = std_dev(state["public_history"])
    temp_sd = std_dev(state["temp_history"])

    print("CO2 deviation:", round(co2_sd, 2))
    print("Economy deviation:", round(eco_sd, 2))
    print("Public deviation:", round(pub_sd, 2))
    print("Temperature deviation:", round(temp_sd, 3))

    if co2_sd < 10:
        print("Emissions are stable")
    else:
        print("Emissions are volatile")


# =========================
# CORRELATION ANALYSIS
# =========================

def correlation_analysis(state):

    print("\n--- CORRELATION ANALYSIS ---\n")

    r = pearson_r(state["co2_history"], state["eco_history"])

    print("Pearson r:", round(r, 3))

    if r > 0.6:
        print("Strong positive relationship")
    elif r > 0.3:
        print("Moderate relationship")
    elif r > -0.3:
        print("Weak relationship")
    else:
        print("Negative relationship")


# =========================
# CHI SQUARED TEST
# =========================

def chi_squared_test(state):

    print("\n--- STABILITY TEST (CHI²) ---\n")

    observed = state["co2_history"]
    expected = [mean(observed)] * len(observed)

    chi = 0

    for o, e in zip(observed, expected):
        if e != 0:
            chi += ((o - e) ** 2) / e

    print("Chi squared:", round(chi, 2))

    if chi < 50:
        print("System is stable")
    else:
        print("System shows instability")


# =========================
# SCIENTIFIC CONCLUSION
# =========================

def research_conclusion(state):

    print("\n--- SCIENTIFIC CONCLUSION ---\n")

    if len(state["co2_history"]) > 1:
        co2_change = state["co2_history"][-1] - state["co2_history"][0]
    else:
        co2_change = 0

    if co2_change < 0:
        print("Policies reduced emissions.")
    else:
        print("Policies failed to reduce emissions.")

    if state["temperature"] < 1.6:
        print("Climate remained within Paris targets.")
    else:
        print("Paris targets exceeded.")


# =========================
# RELATIONSHIP ANALYSIS
# =========================

def relationship_analysis(state):

    print("\n--- RELATIONSHIP ANALYSIS ---\n")

    r = pearson_r(state["co2_history"], state["eco_history"])

    print("Correlation (r):", round(r, 3))

    if abs(r) >= 0.8:
        strength = "Very strong"
    elif abs(r) >= 0.6:
        strength = "Strong"
    elif abs(r) >= 0.4:
        strength = "Moderate"
    elif abs(r) >= 0.2:
        strength = "Weak"
    else:
        strength = "Very weak"

    direction = "positive" if r > 0 else "negative" if r < 0 else "no"

    print("Relationship strength:", strength)
    print("Relationship type:", direction)

    if r > 0.5:
        print("Economic growth is increasing emissions.")
    elif r < -0.5:
        print("Economic growth is becoming greener.")
    else:
        print("Economy and emissions weakly related.")


# =========================
# CO2 vs TEMPERATURE
# =========================

def co2_temperature_analysis(state):

    print("\n--- CO2 vs TEMPERATURE ANALYSIS ---\n")

    co2 = state["co2_history"]
    temp = state["temp_history"]

    if len(co2) < 2 or len(temp) < 2:
        print("Not enough data.")
        return

    r = pearson_r(co2, temp)

    print("Correlation (r):", round(r, 3))

    if abs(r) >= 0.8:
        strength = "Very strong"
    elif abs(r) >= 0.6:
        strength = "Strong"
    elif abs(r) >= 0.4:
        strength = "Moderate"
    elif abs(r) >= 0.2:
        strength = "Weak"
    else:
        strength = "Very weak"

    direction = "positive" if r > 0 else "negative" if r < 0 else "no"

    print("Relationship strength:", strength)
    print("Relationship type:", direction)

    if r > 0.6:
        print("Higher emissions are strongly increasing temperature.")
    elif r > 0.3:
        print("Emissions show moderate warming influence.")
    elif r > 0:
        print("Weak warming relationship detected.")
    else:
        print("Temperature not strongly linked to emissions.")

    if co2[-1] < co2[0]:
        print("Policies successfully reduced emissions.")
    else:
        print("Emissions increased during leadership.")


# =========================
# FULL ANALYSIS
# =========================

def full_analysis(state):

    print("\n==============================")
    print("FINAL SCIENTIFIC ANALYSIS")
    print("==============================")

    deviation_analysis(state)
    correlation_analysis(state)
    chi_squared_test(state)
    relationship_analysis(state)
    co2_temperature_analysis(state)
    research_conclusion(state)

    # ✅ FIX: define co2_change HERE
    if len(state["co2_history"]) > 1:
        co2_change = state["co2_history"][-1] - state["co2_history"][0]
    else:
        co2_change = 0

    result = []

    if co2_change < 0:
        result.append("Emissions decreased over time.")
    else:
        result.append("Emissions increased over time.")

    if state["temperature"] < 1.6:
        result.append("Climate stayed within safe limits.")
    else:
        result.append("Climate targets were exceeded.")

    r = pearson_r(state["co2_history"], state["eco_history"])

    if r > 0.5:
        result.append("Economic growth increased emissions.")
    elif r < -0.5:
        result.append("Green growth was achieved.")
    else:
        result.append("Weak link between economy and emissions.")

    return " ".join(result)