

import random

from stats import std_dev
from variables import (BASE_RISK, CO2_RISK_FACTOR, GOOD_ENDING_SCORE,
                       TEMP_RISK_FACTOR)

# ---------- WORLD SCORE ----------

def update_world_view(state):

    """
    Calculates global perception score.
    """

    score = 0

    # Economy strength

    score += state["economy"] * 0.4

    # Public stability

    score += state["public"] * 0.3

    # Human wellbeing

    score += state["human"] * 0.2

    # Climate damage penalty

    score -= state["temp"] * 25

    # Emission penalty

    score -= state["co2_tons"] * 0.05

    state["world_score"] = round(score)

    return state["world_score"]



# ---------- SUSTAINABILITY INDEX ----------

def sustainability_index(state):

    """
    Combined sustainability measure.
    """

    index = (

    state["economy"] * 0.3 +

    state["public"] * 0.25 +

    state["human"] * 0.25 -

    state["temp"] * 20 -

    state["co2_tons"] * 0.04

    )

    return round(index,2)



# ---------- GLOBAL RISK ----------

def global_risk(state):

    """
    Calculates risk probability.
    """

    risk = BASE_RISK

    risk += state["temp"] * TEMP_RISK_FACTOR

    risk += state["co2_tons"] * CO2_RISK_FACTOR

    risk -= state["economy"] * 0.05

    risk -= state["public"] * 0.03

    if risk < 0:

        risk = 0

    if risk > 100:

        risk = 100

    return round(risk)



# ---------- CLIMATE CRISIS ----------

def climate_crisis(state):

    """
    Returns crisis messages.
    """

    crises=[]

    if state["temp"]>1.8:

        crises.append(
        "Heat waves increasing"
        )

    if state["temp"]>2.2:

        crises.append(
        "Food systems destabilizing"
        )

    if state["temp"]>2.6:

        crises.append(
        "Migration pressures rising"
        )

    if state["temp"]>3:

        crises.append(
        "Global systems failure risk"
        )

    return crises



# ---------- WORLD STAT DISPLAY ----------

def show_world_stats(state):

    print("\n--- GLOBAL ANALYSIS ---\n")

    print(

    "World score:",
    state["world_score"]

    )

    print(

    "Sustainability index:",
    sustainability_index(state)

    )

    print(

    "Risk probability:",
    global_risk(state),
    "%"

    )

    # Stability analysis

    if len(state["co2_history"])>3:

        stability = std_dev(
        state["co2_history"]
        )

        print(

        "Policy stability:",
        round(stability,2)

        )



# ---------- WORLD REACTION ----------

def world_reaction(score):

    """
    Narrative world reaction.
    """

    if score>GOOD_ENDING_SCORE:

        return (
        "Global leader of sustainability."
        )

    if score>60:

        return (
        "Respected but questioned."
        )

    if score>20:

        return (
        "Mixed global perception."
        )

    if score>-20:

        return (
        "International concern rising."
        )

    return (
    "Global criticism and instability."
    )



# ---------- INTERNATIONAL PRESSURE ----------

def international_pressure(state):

    """
    Global diplomatic pressure increases.
    """

    if state["temp"]>2:

        state["public"]-=1

    if state["temp"]>2.5:

        state["economy"]-=2

        state["public"]-=2



# ---------- STOCHASTIC GLOBAL EVENTS ----------

def global_random_events(state):

    """
    Random world reactions.
    """

    roll=random.randint(1,100)

    if roll>92:

        print(
        "\nGLOBAL MARKET SHOCK"
        )

        state["economy"]-=8

    if roll<8:

        print(
        "\nGREEN TECH BREAKTHROUGH"
        )

        state["co2_tons"]-=10

        state["economy"]+=5