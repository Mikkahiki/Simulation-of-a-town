import random


# =========================
# NORMAL EVENTS
# =========================
def create_events():

    normal_events=[

    {
    "id":"energy_transition",

    "question":
    "City scientists report rising emissions from power plants. How do you respond?",

    "difficulty":1,

    "options":[

    {
    "text":"Massive renewable investment",

    "co2":-18,
    "eco":-10,
    "pub":8,
    "human":6,

    "tag":"Green transition",

    "type":"green",

    "chain":"green_transition",

    "risk":25
    },

    {
    "text":"Gradual transition plan",

    "co2":-7,
    "eco":-3,
    "pub":3,
    "human":3,

    "tag":"Balanced",

    "type":"balanced",

    "risk":15
    },

    {
    "text":"Protect fossil industry",

    "co2":12,
    "eco":9,
    "pub":-6,
    "human":-5,

    "tag":"Industrial growth",

    "type":"industrial",

    "chain":"fossil_dependence",

    "risk":45
    }

    ]

    },



    {
    "id":"transport_expansion",

    "question":
    "Traffic congestion and emissions rising. Transport reform?",

    "difficulty":1,

    "options":[

    {
    "text":"Build metro system",

    "co2":-12,
    "eco":-7,
    "pub":7,
    "human":6,

    "type":"green",

    "risk":20
    },

    {
    "text":"Electric vehicle incentives",

    "co2":-9,
    "eco":-4,
    "pub":5,
    "human":4,

    "type":"green",

    "risk":18
    },

    {
    "text":"Expand highways",

    "co2":10,
    "eco":6,
    "pub":-4,
    "human":-3,

    "type":"industrial",

    "risk":40
    }

    ]

    },



    {
    "id":"agriculture_policy",

    "question":
    "Farm sector emissions rising.",

    "difficulty":2,

    "options":[

    {
    "text":"Subsidize sustainable farming",

    "co2":-10,
    "eco":-5,
    "pub":6,
    "human":5,

    "type":"green",

    "risk":20
    },

    {
    "text":"Carbon tax on agriculture",

    "co2":-8,
    "eco":-6,
    "pub":-2,
    "human":3,

    "type":"policy",

    "risk":28
    },

    {
    "text":"Ignore problem",

    "co2":9,
    "eco":3,
    "pub":-5,
    "human":-4,

    "type":"ignore",

    "risk":50
    }

    ]

    },



    {
    "id":"tech_research",

    "question":
    "University proposes carbon capture research funding.",

    "difficulty":2,

    "options":[

    {
    "text":"Fund breakthrough research",

    "co2":-14,
    "eco":-8,
    "pub":6,
    "human":5,

    "type":"innovation",

    "chain":"tech_breakthrough",

    "risk":22
    },

    {
    "text":"Small research grant",

    "co2":-5,
    "eco":-2,
    "pub":2,
    "human":2,

    "type":"innovation",

    "risk":12
    },

    {
    "text":"Reject funding",

    "co2":5,
    "eco":2,
    "pub":-3,
    "human":-3,

    "type":"economic",

    "risk":35
    }

    ]

    }

    ]



# =========================
# CRISIS EVENTS
# =========================

    crisis_events=[

    {
    "id":"heatwave",

    "question":
    "Extreme heatwave causing power shortages.",

    "difficulty":2,

    "options":[

    {
    "text":"Emergency cooling centers",

    "co2":3,
    "eco":-7,
    "pub":9,
    "human":8,

    "type":"humanitarian",

    "risk":30
    },

    {
    "text":"Let market respond",

    "co2":0,
    "eco":3,
    "pub":-8,
    "human":-9,

    "type":"economic",

    "risk":60
    }

    ]

    },



    {
    "id":"flooding",

    "question":
    "Storm surge flooding coastal districts.",

    "difficulty":3,

    "options":[

    {
    "text":"Sea defense program",

    "co2":5,
    "eco":-9,
    "pub":6,
    "human":7,

    "type":"adaptation",

    "risk":35
    },

    {
    "text":"Relocate citizens",

    "co2":2,
    "eco":-6,
    "pub":3,
    "human":9,

    "type":"adaptation",

    "risk":25
    }

    ]

    }

    ]

    return normal_events,crisis_events



# =========================
# SCENARIO CHAINS
# =========================

def chain_events():

    return{

    "green_transition":[

    {
    "question":
    "Renewable boom creates skilled job demand.",

    "options":[

    {
    "text":"Create training programs",

    "co2":-6,
    "eco":7,
    "pub":6,
    "human":5,

    "type":"green"
    }

    ]

    }

    ],



    "fossil_dependence":[

    {
    "question":
    "Oil companies request expansion permits.",

    "options":[

    {
    "text":"Approve drilling",

    "co2":14,
    "eco":10,
    "pub":-6,
    "human":-7,

    "type":"industrial"
    }

    ]

    }

    ],



    "tech_breakthrough":[

    {
    "question":
    "Prototype carbon capture shows promise.",

    "options":[

    {
    "text":"Deploy pilot plant",

    "co2":-12,
    "eco":-4,
    "pub":5,
    "human":6,

    "type":"innovation"
    }

    ]

    }

    ]

    }



# =========================
# COP SUMMIT
# =========================

def cop_summit():

    return{

    "id":"cop",

    "question":
    "Global COP summit pressures cities to commit climate targets.",

    "options":[

    {
    "text":"Sign aggressive targets",

    "co2":-22,
    "eco":-11,
    "pub":10,
    "human":10,

    "type":"green"
    },

    {
    "text":"Moderate commitment",

    "co2":-11,
    "eco":-4,
    "pub":5,
    "human":5,

    "type":"balanced"
    },

    {
    "text":"Reject commitments",

    "co2":16,
    "eco":7,
    "pub":-11,
    "human":-9,

    "type":"industrial"
    }

    ]

    }



# =========================
# EVENT SELECTION
# =========================

def weighted_event(events,state):
    """
    Smarter event selection.
    Harder events appear as crisis rises.
    """
    # Make sure 'crisis_level' exists
    if "crisis_level" not in state:
        state["crisis_level"] = 0

    difficulty=state["crisis_level"]+1

    possible=[

    e for e in events

    if e["difficulty"]<=difficulty

    ]

    if not possible:

        possible=events

    return random.choice(possible)



def get_two_events(normal,crisis,state):

    # Make sure 'crisis_level' exists
    if "crisis_level" not in state:
        state["crisis_level"]=0

    events=[]

    events.append(

    weighted_event(normal,state)

    )

    crisis_chance=30+state["crisis_level"]*10

    if random.randint(1,100)<crisis_chance:

        events.append(

        weighted_event(crisis,state)

        )

    else:

        events.append(

        weighted_event(normal,state)

        )

    return events[0],events[1]



# =========================
# EVENT CONSEQUENCES
# =========================

def apply_event_chain(state,choice):

    chains=chain_events()

    if "chain" in choice:

        key=choice["chain"]

        if key in chains:

            return random.choice(

            chains[key]

            )

    return None


# =========================
# RANDOM SCENARIO FOR MAIN
# =========================

def get_random_scenario(state):
    """
    Returns a random scenario in the format main.py expects.
    Combines normal and crisis events.
    Prevents repeating recent scenarios.
    """

    normal, crisis = create_events()

    # create memory if missing
    if "recent_events" not in state:
        state["recent_events"] = []

    # filter already used events
    available = [
        e for e in normal
        if e["id"] not in state["recent_events"]
    ]

    # reset if all used
    if not available:
        state["recent_events"] = []
        available = normal

    # difficulty scaling
    difficulty = state["crisis_level"] + 1

    possible = [
        e for e in available
        if e["difficulty"] <= difficulty
    ]

    if not possible:
        possible = available

    event = random.choice(possible)

    # remember event
    state["recent_events"].append(event["id"])

    # keep memory small
    if len(state["recent_events"]) > 5:
        state["recent_events"].pop(0)

    # format for main.py (NO structure change)
    if len(event["options"]) >= 3:

        scenario = {

            "text": event["question"],

            "good": event["options"][0],

            "neutral": event["options"][1],

            "bad": event["options"][2]

        }

    else:

        options = event["options"] * 3

        scenario = {

            "text": event["question"],

            "good": options[0],

            "neutral": options[1],

            "bad": options[2]

        }

    return scenario