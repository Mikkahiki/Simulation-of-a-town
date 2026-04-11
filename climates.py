

from data import (NATURAL_ABSORPTION, TEMP_PER_CO2, TIPPING_POINTS,
                  disaster_roll)

# =========================
# TEMPERATURE MODEL
# =========================

def update_temperature(state):

    """
    Temperature rises based on emissions.
    Includes natural absorption and feedback.
    """

    co2_effect = state["co2_tons"] * TEMP_PER_CO2

    absorption = NATURAL_ABSORPTION * 0.01

    state["temperature"] += co2_effect

    state["temperature"] -= absorption

    # Feedback acceleration

    if state["temperature"] > 2:

        state["temperature"] += 0.02

    if state["temperature"] > 2.5:

        state["temperature"] += 0.03



# =========================
# EMISSION MOMENTUM
# =========================

def emission_feedback(state):

    """
    High emissions cause future increases.
    Represents industrial inertia.
    """

    if state["co2_tons"] > 120:

        state["co2_tons"] += 2

    if state["co2_tons"] > 200:

        state["co2_tons"] += 5



# =========================
# TIPPING POINT SYSTEM
# =========================

def check_tipping_points(state):

    triggered=[]

    if "tipped" not in state:

        state["tipped"]=[]

    for tip in TIPPING_POINTS:

        if (

        state["temperature"] >= tip["temp"]

        and

        tip["name"] not in state["tipped"]

        ):

            trigger_tipping_point(
            state,
            tip
            )

            triggered.append(
            tip["name"]
            )

    state["tipped"].extend(triggered)

    return triggered



def trigger_tipping_point(state,tip):

    print("\nCLIMATE TIPPING POINT")

    print(tip["name"])

    print(tip["text"])

    # permanent emission increase

    state["co2_tons"] += tip["effect"]

    state["crisis_level"] += 1



# =========================
# STOCHASTIC DISASTERS
# =========================

def climate_disaster(state):

    """
    Random disasters based on temperature.
    """

    level,damage = disaster_roll(
        state["temperature"]
    )

    if not level:

        return False

    print("\nCLIMATE DISASTER")

    print(level)

    apply_disaster_damage(
        state,
        damage
    )

    return True



def apply_disaster_damage(state,damage):

    eco_damage = damage

    public_damage = damage//2

    carbon_spike = damage//3

    state["economy"] -= eco_damage

    state["public"] -= public_damage

    state["co2_tons"] += carbon_spike

    print("Economic loss:",eco_damage)

    print("Public impact:",public_damage)



# =========================
# ONGOING CLIMATE EFFECTS
# =========================

def apply_climate_effects(state):

    t = state["temperature"]

    # gradual damage

    if t > 1.7:

        state["economy"] -= 1

    if t > 2.2:

        state["economy"] -= 2

        state["public"] -= 1

    if t > 2.8:

        state["economy"] -= 4

        state["public"] -= 3

        state["crisis_level"] += 1

    # disasters

    climate_disaster(state)

    # tipping points

    check_tipping_points(state)



# =========================
# CLIMATE STATUS
# =========================

def climate_status(state):

    t = state["temperature"]

    if t < 1.5:

        return "Stable"

    if t < 2:

        return "Warming"

    if t < 2.5:

        return "Dangerous"

    if t < 3:

        return "Severe"

    return "Catastrophic"



# =========================
# CLIMATE REPORT
# =========================

def climate_report(state):

    print("\n--- CLIMATE REPORT ---\n")

    print(
    "Temperature:",
    round(state["temperature"],2)
    )

    print(
    "Status:",
    climate_status(state)
    )

    print(
    "Crisis level:",
    state["crisis_level"]
    )

    print(
    "Total emissions:",
    state["co2_tons"]
    )

    if "tipped" in state:

        print(
        "Tipping points:",
        len(state["tipped"])
        )



# =========================
# MAIN SYSTEM WRAPPERS
# =========================

def climate_update(state):

    co2 = state["co2_tons"]

    # 🌍 baseline safe level
    baseline = 120

    # 🔥 warming depends on how far above baseline you are
    warming = (co2 - baseline) * 0.003

    # ❄️ recovery if below safe level
    recovery = 0
    if co2 < baseline:
        recovery = (baseline - co2) * 0.002

    # net temperature change
    state["temperature"] += warming - recovery

    # clamp temperature
    state["temperature"] = max(0.5, state["temperature"])

    # other systems
    update_temperature(state)
    emission_feedback(state)
    apply_climate_effects(state)



def tipping_points(state):

    """
    Compatibility wrapper.
    """

    check_tipping_points(state)



def stochastic_damage(state):

    """
    Compatibility wrapper.
    """

    climate_disaster(state)