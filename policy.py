

from data import INERTIA_FACTOR, POLICY_DECAY, POLICY_MIN_EFFECT

# ---------- APPLY ACTIVE POLICIES ----------

def apply_active_policies(state):

    """
    Applies daily policy effects.
    Policies weaken over time.
    """

    remaining = []

    for policy in state["policies"]:

        apply_policy_effect(state,policy)

        policy["days_left"] -= 1

        decay_policy(policy)

        if policy["days_left"] > 0:

            remaining.append(policy)

        else:

            policy_expired(policy)

    state["policies"] = remaining



# ---------- APPLY SINGLE POLICY ----------

def apply_policy_effect(state,policy):

    """
    Applies one policy effect.
    """

    state["co2_tons"] += int(
    policy["daily_co2"]
    )

    state["economy"] += int(
    policy["daily_eco"]
    )

    state["public"] += int(
    policy["daily_pub"]
    )



# ---------- POLICY DECAY ----------

def decay_policy(policy):

    """
    Policy effects weaken gradually.
    """

    policy["daily_co2"] *= POLICY_DECAY

    policy["daily_eco"] *= POLICY_DECAY

    policy["daily_pub"] *= POLICY_DECAY

    # Minimum effect cutoff

    if abs(policy["daily_co2"]) < POLICY_MIN_EFFECT:

        policy["daily_co2"] = 0

    if abs(policy["daily_eco"]) < POLICY_MIN_EFFECT:

        policy["daily_eco"] = 0

    if abs(policy["daily_pub"]) < POLICY_MIN_EFFECT:

        policy["daily_pub"] = 0



# ---------- POLICY EXPIRATION ----------

def policy_expired(policy):

    print("\nPolicy expired:",policy["name"])



# ---------- EMISSION INERTIA ----------

def emission_inertia(state):

    """
    Emissions change slowly due to infrastructure.
    """

    if len(state["co2_history"]) < 2:

        return

    yesterday = state["co2_history"][-1]

    today = state["co2_tons"]

    adjusted = (

    today*(1-INERTIA_FACTOR)

    +

    yesterday*INERTIA_FACTOR

    )

    state["co2_tons"] = int(adjusted)



# ---------- POLICY CHAINS ----------

def check_policy_chain(state):

    """
    Some policies unlock others.
    """

    names = [

    p["name"]

    for p in state["policy_history"]

    ]

    # Renewable chain

    if (

    "Solar Subsidy" in names

    and

    "Grid Modernization" in names

    and

    "EV Incentive" not in names

    ):

        unlock_green_transition(state)



# ---------- UNLOCK POLICY ----------

def unlock_green_transition(state):

    print(

    "\nPolicy chain unlocked: Green Transition Act"

    )

    state["policies"].append({

    "name":"Green Transition Act",

    "daily_co2":-8,

    "daily_eco":4,

    "daily_pub":5,

    "days_left":6,

    "duration":6,

    "story":"Mass renewable transition"

    })



# ---------- DELAYED EFFECT SYSTEM ----------

def delayed_effects(state):

    """
    Some policies activate later.
    """

    for policy in state["policies"]:

        if "delay" in policy:

            policy["delay"] -= 1

            if policy["delay"] == 0:

                activate_delayed(policy)



def activate_delayed(policy):

    print(

    "\nDelayed impact activated:",

    policy["name"]

    )



# ---------- POLICY RISK ----------

def policy_risk(state):

    """
    Aggressive policy risks backlash.
    """

    for policy in state["policies"]:

        if policy["daily_eco"] < -8:

            state["public"] -= 2

            print(

            "Economic pain causes protests"

            )



# ---------- POLICY MEMORY SCORE ----------

def policy_score(state):

    """
    Measures long term policy direction.
    """

    score = 0

    for policy in state["policy_history"]:

        score += policy["daily_co2"] * -1

    return score



# ---------- POLICY REPORT ----------

def policy_report(state):

    print("\n--- ACTIVE POLICIES ---\n")

    if len(state["policies"]) == 0:

        print("No active policies")

        return

    for p in state["policies"]:

        print(

        p["name"],
        "Days:",p["days_left"],
        "CO2:",round(p["daily_co2"],1),
        "Eco:",round(p["daily_eco"],1),
        "Public:",round(p["daily_pub"],1)

        )