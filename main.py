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


# =========================
# CREATE GAME STATE
# =========================

def create_state():

    return {
        "day": 1,
        "phase": "Early",
        "economy": 60,
        "public": 55,
        "carbon": create_carbon(),
        "co2_tons": 0,
        "temperature": 1.2,
        "climate_risk": 0,
        "difficulty": 1,
        "carbon_target": 140,
        "policies": [],
        "decision_log": [],
        "choices": [],
        "co2_history": [],
        "eco_history": [],
        "public_history": [],
        "temp_history": [],
        "recent_events": [],
        "crisis_level": 0,
        "current_scenario": None
    }


# =========================
# START GAME (WEB USE)
# =========================

def start_game():
    state = create_state()
    initialize_scenarios()

    scenario = get_random_scenario(state)
    state["current_scenario"] = scenario

    return state


# =========================
# NEXT TURN (WEB CORE ENGINE)
# =========================

def next_turn(state, choice_type):

    scenario = state.get("current_scenario")

    if not scenario:
        return state

    # SELECT CHOICE
    selected = scenario[choice_type]

    apply_choice(state, selected)
    policy_tracker(state, selected)
    log_decision(state, scenario, selected)

    daily_update(state)

    state["day"] += 1

    # NEXT SCENARIO
    if state["day"] <= 15:
        state["current_scenario"] = get_random_scenario(state)
    else:
        state["current_scenario"] = None

    return state


# =========================
# RECORD DATA
# =========================

def record_stats(state):

    state["co2_history"].append(state["co2_tons"])
    state["eco_history"].append(state["economy"])
    state["public_history"].append(state["public"])
    state["temp_history"].append(state["temperature"])


# =========================
# PHASE SYSTEM
# =========================

def update_phase(state):

    if state["day"] <= 5:
        state["phase"] = "Early"
    elif state["day"] <= 10:
        state["phase"] = "Development"
    else:
        state["phase"] = "Crisis"


# =========================
# DIFFICULTY SYSTEM
# =========================

def dynamic_difficulty(state):

    emissions = total_emissions(state)

    if emissions > 200:
        state["difficulty"] = 3
    elif emissions > 150:
        state["difficulty"] = 2
    else:
        state["difficulty"] = 1


# =========================
# CARBON TARGET SYSTEM
# =========================

def carbon_target_check(state):

    total = total_emissions(state)

    if total < state["carbon_target"]:
        state["public"] += 3
        state["economy"] += 2
    else:
        state["public"] -= 2


# =========================
# POLICY TRACKER
# =========================

def policy_tracker(state, choice):

    if "policy" in choice:
        state["policies"].append({
            "name": choice["policy"],
            "day": state["day"]
        })


# =========================
# DECISION LOG
# =========================

def log_decision(state, scenario, choice):

    state["decision_log"].append({
        "day": state["day"],
        "scenario": scenario["title"],
        "decision": choice["text"],
        "type": choice["type"]
    })


# =========================
# APPLY DECISION
# =========================

def apply_choice(state, choice):

    state["economy"] += choice["eco"]
    state["public"] += choice["pub"]

    state["choices"].append(choice["type"])

    if "carbon" in choice:
        for sector, value in choice["carbon"].items():
            change_sector(state, sector, value)

    # CLAMP VALUES
    state["economy"] = max(0, state["economy"])
    state["public"] = max(0, min(100, state["public"]))


# =========================
# DAILY UPDATE
# =========================

def daily_update(state):

    update_phase(state)
    dynamic_difficulty(state)
    policy_lag(state)
    emission_inertia(state)

    state["co2_tons"] = total_emissions(state)

    climate_update(state)
    tipping_points(state)
    stochastic_damage(state)

    carbon_target_check(state)
    record_stats(state)

    state["crisis_level"] = state["day"] // 5


# =========================
# OPTIONAL: CLI VERSION
# =========================

def run_cli_game():

    state = start_game()

    while state["day"] <= 15:

        scenario = state["current_scenario"]

        print("\nDAY", state["day"])
        print(scenario["title"])
        print(scenario["text"])

        print("1:", scenario["good"]["text"])
        print("2:", scenario["neutral"]["text"])
        print("3:", scenario["bad"]["text"])

        import random
        choice = str(random.randint(1,3))

        if choice == "1":
            state = next_turn(state, "good")
        elif choice == "2":
            state = next_turn(state, "neutral")
        else:
            state = next_turn(state, "bad")

    print(check_ending(state))
    return state