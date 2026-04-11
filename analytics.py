

import math

# ---------- BASIC STATISTICS ----------

def mean(data):

    """
    Average value.
    """

    if len(data) == 0:

        return 0

    return sum(data)/len(data)



def std_dev(data):

    """
    Standard deviation.
    Measures policy stability.
    """

    if len(data) < 2:

        return 0

    m = mean(data)

    variance = sum(

    (x-m)**2

    for x in data

    )/len(data)

    return math.sqrt(variance)



# ---------- CORRELATION ----------

def pearson_r(x,y):

    """
    Pearson correlation.

    Measures relationship between:
    Economy vs emissions
    Emissions vs temperature
    Public vs economy
    """

    if len(x) != len(y):

        return 0

    mean_x = mean(x)

    mean_y = mean(y)

    numerator = sum(

    (a-mean_x)*(b-mean_y)

    for a,b in zip(x,y)

    )

    denom_x = math.sqrt(

    sum((a-mean_x)**2 for a in x)

    )

    denom_y = math.sqrt(

    sum((b-mean_y)**2 for b in y)

    )

    if denom_x == 0 or denom_y == 0:

        return 0

    return numerator/(denom_x*denom_y)



# ---------- DECISION ANALYSIS ----------

def chi_square(choices):

    """
    Detect decision bias.

    Tests if player choices are balanced
    or strongly biased.
    """

    good = choices.count("good")

    neutral = choices.count("neutral")

    bad = choices.count("bad")

    observed = [good,neutral,bad]

    total = sum(observed)

    if total == 0:

        return 0

    expected = total/3

    chi = sum(

    (o-expected)**2/expected

    for o in observed

    )

    return chi



# ---------- TREND DETECTION ----------

def trend_direction(data):

    """
    Detects if values trend upward or downward.
    """

    if len(data) < 3:

        return "stable"

    first = data[0]

    last = data[-1]

    change = last-first

    if change > 50:

        return "rising"

    if change < -50:

        return "falling"

    return "stable"



# ---------- POLICY EFFECTIVENESS ----------

def policy_effectiveness(state):

    """
    Measures if policies reduced emissions.
    """

    if len(state["co2_history"]) < 5:

        return 0

    start = state["co2_history"][0]

    end = state["co2_history"][-1]

    reduction = start-end

    return reduction



# ---------- CLIMATE RISK SCORE ----------

def climate_risk(state):

    """
    Composite climate danger metric.
    """

    risk = 0

    risk += state["temp"] * 20

    risk += state["co2_tons"] * 0.05

    risk -= state["public"] * 0.1

    return int(risk)



# ---------- LEADERSHIP PROFILE ----------

def leadership_style(choices):

    """
    Determines player leadership type.
    """

    good = choices.count("good")

    neutral = choices.count("neutral")

    bad = choices.count("bad")

    total = len(choices)

    if total == 0:

        return "Unknown"

    if good/total > 0.5:

        return "Environmentalist"

    if bad/total > 0.5:

        return "Industrialist"

    if neutral/total > 0.5:

        return "Pragmatist"

    return "Balanced"



# ---------- INTERPRETATION ENGINE ----------

def interpret_statistics(state):

    """
    Converts numbers into narrative analysis.
    """

    sd = std_dev(state["co2_history"])

    r = pearson_r(

    state["co2_history"],
    state["eco_history"]

    )

    chi = chi_square(state["choices"])

    style = leadership_style(state["choices"])

    print("\n--- ADVANCED ANALYSIS ---\n")

    print("Leadership style:",style)

    print("Carbon stability:",round(sd,2))

    print("Economy vs emissions:",round(r,2))

    print("Decision bias:",round(chi,2))

    # Interpret stability

    if sd > 200:

        print(
        "Policy direction was highly unstable."
        )

    elif sd > 100:

        print(
        "Moderate policy volatility detected."
        )

    else:

        print(
        "Stable environmental direction."
        )

    # Interpret correlation

    if r > 0.4:

        print(
        "Economic growth strongly linked to emissions."
        )

    elif r < -0.4:

        print(
        "Green growth achieved."
        )

    else:

        print(
        "Weak economic-emission link."
        )

    # Interpret decision bias

    if chi > 5:

        print(
        "Strong ideological bias detected."
        )

    else:
        print(
        "Balanced decision behaviour."
        )

def generate_analysis_text(state):
    
    """
    Returns full analysis as a string (for web display)
    """

    sd = std_dev(state["co2_history"])

    r = pearson_r(
        state["co2_history"],
        state["eco_history"]
    )

    chi = chi_square(state["choices"])

    style = leadership_style(state["choices"])

    result = []

    result.append(f"Leadership style: {style}")
    result.append(f"Carbon stability: {round(sd,2)}")
    result.append(f"Economy vs emissions: {round(r,2)}")
    result.append(f"Decision bias: {round(chi,2)}")

    # Stability
    if sd > 200:
        result.append("Policy direction was highly unstable.")
    elif sd > 100:
        result.append("Moderate policy volatility detected.")
    else:
        result.append("Stable environmental direction.")

    # Correlation
    if r > 0.4:
        result.append("Economic growth strongly linked to emissions.")
    elif r < -0.4:
        result.append("Green growth achieved.")
    else:
        result.append("Weak economic-emission link.")

    # Bias
    if chi > 5:
        result.append("Strong ideological bias detected.")
    else:
        result.append("Balanced decision behaviour.")

    return "\n".join(result)