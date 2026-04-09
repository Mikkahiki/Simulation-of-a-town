from analytics import leadership_style
from data import sustainability_index

# ---------- ENDING CALCULATOR ----------

def calculate_ending(state):

    score = sustainability_index(state)

    temp = state["temperature"]   # FIXED

    eco = state["economy"]

    public = state["public"]

    style = leadership_style(state["choices"])


    # GOOD ENDING

    if score > 120 and temp < 1.7:

        return golden_age(state,style)


    # NEUTRAL ENDING

    if score > 40:

        return fragile_balance(state,style)


    # BAD ENDING

    return climate_failure(state,style)



# ---------- GOOD ENDING ----------

def golden_age(state,style):

    text = """

THE GREEN TRANSFORMATION

Your policies triggered a green revolution.

Clean energy dominates industry.

Cities became sustainable.

Global temperatures stabilized.

Future generations will study your leadership.

"""

    if style == "Environmentalist":

        text += "\nYou are remembered as a climate visionary."

    elif style == "Balanced":

        text += "\nYou balanced growth and survival."

    else:

        text += "\nDespite your methods, disaster was avoided."


    return text



# ---------- NEUTRAL ENDING ----------

def fragile_balance(state,style):

    text = """

A FRAGILE WORLD

Climate damage continues.

But collapse was avoided.

Your compromises bought time.

Future leaders must finish the job.

"""

    if style == "Pragmatist":

        text += "\nHistory calls you a realist."

    else:

        text += "\nYour mixed decisions created mixed results."


    return text



# ---------- BAD ENDING ----------

def climate_failure(state,style):

    text = """

CLIMATE CASCADE

Tipping points triggered.

Economic shocks spread.

Climate refugees increased.

Global systems destabilized.

Your term ended in crisis.

"""

    if style == "Industrialist":

        text += "\nYou are blamed for ignoring warnings."

    else:

        text += "\nHistory debates what you could have done."


    return text



# ---------- DETAILED REPORT ----------

def ending_report(state):

    score = sustainability_index(state)

    print("\n--- FINAL METRICS ---\n")

    print("Temperature:",
    round(state["temperature"],2))   # FIXED

    print("CO2:",
    state["co2_tons"])

    print("Economy:",
    state["economy"])

    print("Public support:",
    state["public"])

    print("Sustainability:",
    score)


    if score > 120:

        print("Planet status: Stabilized")

    elif score > 40:

        print("Planet status: Uncertain")

    else:

        print("Planet status: Dangerous")



# Alias for main.py

def check_ending(state):

    return calculate_ending(state)