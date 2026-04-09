

import math

# ---------- CREATE SYSTEM ----------

def create_carbon():

    return {

    "transport":45,

    "energy":40,

    "industry":35,

    "buildings":25,

    "waste":15

    }



# ---------- TOTAL EMISSIONS ----------

def total_emissions(state):

    total = sum(
    state["carbon"].values()
    )

    return round(total,2)



# ---------- SECTOR MODIFICATION ----------

def change_sector(state,sector,value):

    if sector not in state["carbon"]:

        return

    state["carbon"][sector]+=value

    if state["carbon"][sector]<0:

        state["carbon"][sector]=0



# ---------- EMISSION INERTIA ----------

def emission_inertia(state):

    """
    Emissions do not instantly change.
    Some sectors resist change.
    """

    for sector in state["carbon"]:

        if state["carbon"][sector] > 50:

            state["carbon"][sector] *= 1.01

        if state["carbon"][sector] > 80:

            state["carbon"][sector] *= 1.02



# ---------- POLICY LAG EFFECT ----------

def policy_lag(state):

    """
    Policies take time to show effect.
    """

    if "carbon_memory" not in state:

        return

    for policy in state["carbon_memory"]:

        policy["duration"]-=1

        if policy["duration"]<=0:

            for sector,value in \
            policy["effect"].items():

                change_sector(
                state,
                sector,
                value
                )

    state["carbon_memory"]=[
    p for p in state["carbon_memory"]
    if p["duration"]>0
    ]



# ---------- APPLY CARBON POLICY ----------

def apply_carbon_policy(state,effects,duration):

    if "carbon_memory" not in state:

        state["carbon_memory"]=[]

    state["carbon_memory"].append({

    "effect":effects,

    "duration":duration

    })



# ---------- CARBON INTENSITY ----------

def carbon_intensity(state):

    """
    Emissions per economic unit.
    """

    eco = state["economy"]

    if eco<=0:

        return 0

    return round(
    total_emissions(state)/eco,
    3
    )



# ---------- SECTOR ANALYSIS ----------

def sector_percentages(state):

    total = total_emissions(state)

    data={}

    if total==0:

        return data

    for sector,value in state["carbon"].items():

        data[sector]=round(
        (value/total)*100,
        1
        )

    return data



# ---------- CARBON TREND ----------

def carbon_trend(state):

    if len(state["co2_history"])<3:

        return "Insufficient data"

    start=state["co2_history"][0]

    end=state["co2_history"][-1]

    change=end-start

    if change>25:

        return "Rapid increase"

    if change>8:

        return "Increasing"

    if change>-8:

        return "Stable"

    if change>-25:

        return "Decreasing"

    return "Rapid decrease"



# ---------- REDUCTION EFFICIENCY ----------

def reduction_efficiency(state):

    """
    Measures effectiveness of green decisions.
    """

    green = state["choices"].count("green")

    total = len(state["choices"])

    if total==0:

        return 0

    return round(
    (green/total)*100,
    1
    )



# ---------- CARBON RISK CONTRIBUTION ----------

def carbon_risk(state):

    total = total_emissions(state)

    risk = total * 0.12

    if total>150:

        risk+=10

    if total>250:

        risk+=25

    return round(risk)



# ---------- SUSTAINABILITY SCORE ----------

def carbon_sustainability(state):

    total=total_emissions(state)

    efficiency=reduction_efficiency(state)

    score = 100

    score -= total*0.25

    score += efficiency*0.4

    if score<0:

        score=0

    return round(score)



# ---------- CARBON REPORT ----------

def carbon_report(state):

    print("\n--- CITY CARBON REPORT ---\n")

    for sector,value in state["carbon"].items():

        print(
        sector,
        ":",
        round(value,1)
        )

    print(
    "\nTotal emissions:",
    total_emissions(state)
    )

    print(
    "Carbon intensity:",
    carbon_intensity(state)
    )

    print(
    "Carbon trend:",
    carbon_trend(state)
    )

    print(
    "Reduction efficiency:",
    reduction_efficiency(state),
    "%"
    )

    print(
    "Sustainability score:",
    carbon_sustainability(state)
    )