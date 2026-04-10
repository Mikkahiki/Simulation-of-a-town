import random

from analysis import full_analysis
from carbon import *
from climates import *
from endings import check_ending
from events import *
from graphs import dashboard
from policy import *
from scenarios import get_random_scenario, initialize_scenarios
from stats import *
from ui import *
from export_data import export_results
from graphs import dashboard


# =========================
# START GAME
# =========================

def start_game():
    state = create_state()
    initialize_scenarios()
    return state


# =========================
# NEXT TURN (CORE ENGINE)
# =========================

def next_turn(state, choice_type):
    
    scenario = state.get("current_scenario")

    if scenario:
        selected = scenario[choice_type]

        apply_choice(state, selected)
        policy_tracker(state, selected)
        log_decision(state, scenario, selected)

        daily_update(state)
        state["day"] += 1

    # get next scenario
    if state["day"] <= 15:
        scenario = get_random_scenario()
        state["current_scenario"] = scenario
    else:
        state["current_scenario"] = None

    return state

# =========================
# CREATE GAME STATE
# =========================

def create_state():

    return {

    "day":1,

    "phase":"Early",

    "economy":60,

    "public":55,

    "carbon":create_carbon(),

    "co2_tons":0,

    "temperature":1.2,

    "climate_risk":0,

    "difficulty":1,

    "carbon_target":140,

    "policies":[],

    "decision_log":[],

    "choices":[],

    "co2_history":[],

    "eco_history":[],

    "public_history":[],

    "temp_history":[],

    "recent_events":[],

    "crisis_level":0

    }


# =========================
# RECORD DATA
# =========================

def record_stats(state):

    state["co2_history"].append(
    state["co2_tons"]
    )

    state["eco_history"].append(
    state["economy"]
    )

    state["public_history"].append(
    state["public"]
    )

    state["temp_history"].append(
    state["temperature"]
    )


# =========================
# PHASE SYSTEM
# =========================

def update_phase(state):

    if state["day"]<=5:

        state["phase"]="Early"

    elif state["day"]<=10:

        state["phase"]="Development"

    else:

        state["phase"]="Crisis"


# =========================
# DIFFICULTY SYSTEM
# =========================

def dynamic_difficulty(state):

    emissions=total_emissions(state)

    if emissions>200:

        state["difficulty"]=3

    elif emissions>150:

        state["difficulty"]=2

    else:

        state["difficulty"]=1


# =========================
# CARBON TARGET SYSTEM
# =========================

def carbon_target_check(state):

    total=total_emissions(state)

    if total<state["carbon_target"]:

        state["public"]+=3

        state["economy"]+=2

        print("\nCarbon target achieved")

    else:

        state["public"]-=2


# =========================
# POLICY TRACKER
# =========================

def policy_tracker(state,choice):

    if "policy" in choice:

        state["policies"].append({

        "name":choice["policy"],

        "day":state["day"]

        })


# =========================
# DECISION LOG
# =========================

def log_decision(state,scenario,choice):

    state["decision_log"].append({

    "day":state["day"],

    "scenario":scenario["title"],

    "decision":choice["text"],

    "type":choice["type"]

    })


# =========================
# CARBON FORECAST
# =========================

def carbon_forecast(state):

    if len(state["co2_history"])<3:

        return state["co2_tons"]

    avg=sum(
    state["co2_history"][-3:]
    )/3

    return round(avg*1.02)


# =========================
# SCIENTIFIC REPORT
# =========================

def scientific_report(state):

    print("\n--- SCIENTIFIC REPORT ---")

    print(
    "Emission trend:",
    carbon_trend(state)
    )

    print(
    "Carbon intensity:",
    carbon_intensity(state)
    )

    print(
    "Sustainability:",
    carbon_sustainability(state)
    )

    print(
    "Forecast emissions:",
    carbon_forecast(state)
    )


# =========================
# APPLY DECISION
# =========================

def apply_choice(state,choice):

    state["economy"]+=choice["eco"]

    state["public"]+=choice["pub"]

    state["choices"].append(
    choice["type"]
    )

    if "carbon" in choice:

        for sector,value in choice["carbon"].items():

            change_sector(

            state,

            sector,

            value

            )


    # Stability clamps
    state["economy"]=max(
    0,
    state["economy"]
    )

    state["public"]=max(
    0,
    min(100,state["public"])
    )


# =========================
# DAILY SIMULATION UPDATE
# =========================

def daily_update(state):

    update_phase(state)

    dynamic_difficulty(state)

    policy_lag(state)

    emission_inertia(state)

    state["co2_tons"]=total_emissions(state)

    climate_update(state)

    tipping_points(state)

    stochastic_damage(state)

    carbon_target_check(state)

    record_stats(state)

    state["crisis_level"]=state["day"]//5


# =========================
# STATUS DISPLAY
# =========================

def show_status(state):

    print("\n================")

    print("DAY:",state["day"])

    print("PHASE:",state["phase"])

    print("Economy:",state["economy"])

    print("Public:",state["public"])

    print("CO2:",state["co2_tons"])

    print("Target:",state["carbon_target"])

    print(
    "Temperature:",
    round(state["temperature"],2)
    )

    print("Risk:",
    state["climate_risk"]
    )

    print("Difficulty:",
    state["difficulty"]
    )

    print("================")


# =========================
# MAIN GAME LOOP
# =========================

def run_game():

    state=create_state()

    print_intro()

    initialize_scenarios()

    while state["day"]<=15:

        show_status(state)

        scientific_report(state)


        # SCENARIO DRAW
        scenario=get_random_scenario()


        print("\nSCENARIO")

        print(scenario["title"])

        print(scenario["text"])


        print("\n1",scenario["good"]["text"])

        print("2",scenario["neutral"]["text"])

        print("3",scenario["bad"]["text"])


        choice=input("\nDecision:")


        if choice=="1":

            selected=scenario["good"]

        elif choice=="2":

            selected=scenario["neutral"]

        else:

            selected=scenario["bad"]


        apply_choice(state,selected)

        policy_tracker(state,selected)

        log_decision(

        state,

        scenario,

        selected

        )


        daily_update(state)

        state["day"]+=1


    # ENDING
    ending=check_ending(state)

    print("\nFINAL RESULT")

    print(ending)


    print("\nFINAL SCIENTIFIC REPORT")

    carbon_report(state)

    statistical_report(state)

    full_analysis(state)

    dashboard(state)
    export_results(state)



# =========================
# START GAME
# =========================

def run_game():
    state = create_state()
    
    # (everything else stays the same)

    return state 
