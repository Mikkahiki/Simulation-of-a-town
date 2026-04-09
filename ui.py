

import time

# =========================
# PRINT ENGINE
# =========================

def slow_print(text,speed=0.015):

    """
    Story narrative printing.
    """

    for char in text:

        print(char,end="",flush=True)

        time.sleep(speed)

    print()



def divider():

    print("\n"+"="*60+"\n")



def section(title):

    divider()

    print(title.upper())

    divider()



# =========================
# INTRO STORY
# =========================

def print_intro():

    section("MAYOR BRIEFING")

    slow_print(
    "You have been elected mayor of a rapidly growing city."
    )

    slow_print(
    "Your decisions will shape the economy, public trust,"
    )

    slow_print(
    "and the planet's future."
    )

    slow_print(
    "Balance growth with sustainability."
    )



# =========================
# PHASE SYSTEM
# =========================

def phase_banner(day,phase):

    print("\nDAY",day)

    print("SIMULATION PHASE:",phase)



# =========================
# CHOICE SYSTEM
# =========================

def get_choice(options):

    print()

    for i,opt in enumerate(options):

        print(

        f"{i+1}. {opt['text']}"

        )

        if "tag" in opt:

            print(
            "   impact:",
            opt["tag"]
            )

    while True:

        try:

            choice=int(

            input("\nDecision: ")

            )

            if 1<=choice<=len(options):

                return options[choice-1]

        except:

            pass

        print("Invalid choice.")



# =========================
# WORLD DASHBOARD
# =========================

def show_state(state):

    section("CITY DASHBOARD")

    print(

    "Carbon emissions:",
    state["co2_tons"]

    )

    print(

    "Temperature rise:",
    round(state["temperature"],2),
    "C"

    )

    print(

    "Economy:",
    state["economy"]

    )

    print(

    "Public approval:",
    state["public"]

    )

    print(

    "Crisis level:",
    state["crisis_level"]

    )



# =========================
# POLICY TRACKER
# =========================

def policy_panel(state):

    print("\nACTIVE POLICIES")

    if not state["active_policies"]:

        print("None")

        return

    for policy in state["active_policies"]:

        print(

        "-",
        policy["name"],
        "days left:",
        policy["duration"]

        )



# =========================
# AI ADVISOR
# =========================

def advisor_panel(text):

    print(

    "\nAI POLICY ADVISOR"

    )

    print(

    text

    )



# =========================
# RISK SYSTEM
# =========================

def risk_warning(state):

    risk=state["crisis_level"]*20

    if risk>80:

        print(

        "\nCLIMATE ALERT: EXTREME RISK"

        )

    elif risk>50:

        print(

        "\nCLIMATE ALERT: HIGH RISK"

        )

    elif risk>25:

        print(

        "\nCLIMATE ALERT: RISING RISK"

        )



# =========================
# NEWS NETWORK
# =========================

def news(message):

    section("GLOBAL NEWS NETWORK")

    print(message)



# =========================
# CLIMATE BRIEFING
# =========================

def climate_brief(state):

    print("\nCLIMATE BRIEFING")

    t=state["temperature"]

    if t<1.5:

        print("Climate stable")

    elif t<2:

        print("Warming trends detected")

    elif t<2.5:

        print("Danger threshold approaching")

    else:

        print("Climate emergency conditions")



# =========================
# DECISION HISTORY
# =========================

def decision_history(state):

    print("\nRECENT DECISIONS")

    history=state["decision_history"][-5:]

    if not history:

        print("None")

        return

    for h in history:

        print("-",h)



# =========================
# COP SUMMIT SCREEN
# =========================

def cop_screen():

    section("COP CLIMATE SUMMIT")

    slow_print(

    "World leaders gather to negotiate emissions cuts."

    )



# =========================
# SCIENTIFIC REPORT UI
# =========================

def scientific_panel(title):

    print(

    "\n---",
    title,
    "---\n"

    )



# =========================
# DAY SUMMARY
# =========================

def day_summary(state):

    section("DAY SUMMARY")

    print(

    "CO2 change:",
    state["co2_history"][-1]

    )

    print(

    "Economy:",
    state["eco_history"][-1]

    )

    print(

    "Public:",
    state["pub_history"][-1]

    )



# =========================
# FINAL REPORT UI
# =========================

def final_report():

    section("SIMULATION COMPLETE")

    print(

    "Generating scientific analysis..."

    )

    time.sleep(1)



# =========================
# DIFFICULTY FEEDBACK
# =========================

def difficulty_message(level):

    if level==1:

        print(

        "\nDifficulty increased: Public expectations rising."

        )

    if level==2:

        print(

        "\nDifficulty increased: Climate instability rising."

        )

    if level>=3:

        print(

        "\nDifficulty increased: Crisis era."

        )