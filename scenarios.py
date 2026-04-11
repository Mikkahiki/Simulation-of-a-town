"""
REBALANCED SCENARIO ENGINE
Balanced for realism + winnable gameplay
"""

import random

# =========================
# SCENARIO POOL
# =========================

scenarios = [

# ================= ENERGY =================
{
"title":"Coal industry lobbying",
"text":"Coal companies demand relaxed emission laws.",

"good":{
"text":"Reject lobbying and enforce emission limits",
"eco":-2,
"pub":5,
"type":"green",
"carbon":{"energy":-6}
},

"neutral":{
"text":"Compromise with moderate rules",
"eco":1,
"pub":2,
"type":"neutral",
"carbon":{"energy":-2}
},

"bad":{
"text":"Relax emission restrictions",
"eco":5,
"pub":-4,
"type":"industrial",
"carbon":{"energy":8}
}
},

{
"title":"Renewable breakthrough",
"text":"New solar technology becomes viable.",

"good":{
"text":"Invest heavily in renewables",
"eco":3,
"pub":5,
"type":"green",
"carbon":{"energy":-8}
},

"neutral":{
"text":"Pilot small projects",
"eco":2,
"pub":2,
"type":"neutral",
"carbon":{"energy":-3}
},

"bad":{
"text":"Ignore technology",
"eco":4,
"pub":-2,
"type":"industrial",
"carbon":{"energy":4}
}
},

{
"title":"Oil price crash",
"text":"Cheap fossil fuel floods the market.",

"good":{
"text":"Tax fossil fuels",
"eco":-1,
"pub":4,
"type":"green",
"carbon":{"energy":-5}
},

"neutral":{
"text":"Allow market adjustment",
"eco":2,
"pub":1,
"type":"neutral",
"carbon":{"energy":2}
},

"bad":{
"text":"Encourage fossil expansion",
"eco":6,
"pub":-4,
"type":"industrial",
"carbon":{"energy":7}
}
},

# ================= TRANSPORT =================
{
"title":"EV transition debate",
"text":"Debate on banning fuel vehicles.",

"good":{
"text":"Phase out fuel cars",
"eco":-2,
"pub":4,
"type":"green",
"carbon":{"transport":-7}
},

"neutral":{
"text":"Delay transition",
"eco":1,
"pub":1,
"type":"neutral",
"carbon":{"transport":-2}
},

"bad":{
"text":"Protect fuel car industry",
"eco":4,
"pub":-3,
"type":"industrial",
"carbon":{"transport":6}
}
},

{
"title":"Public transport expansion",
"text":"Mass transit funding proposed.",

"good":{
"text":"Build metro systems",
"eco":2,
"pub":5,
"type":"green",
"carbon":{"transport":-6}
},

"neutral":{
"text":"Expand slowly",
"eco":1,
"pub":2,
"type":"neutral",
"carbon":{"transport":-2}
},

"bad":{
"text":"Cancel funding",
"eco":3,
"pub":-3,
"type":"industrial",
"carbon":{"transport":5}
}
},

# ================= INDUSTRY =================
{
"title":"Factory emission scandal",
"text":"Major company caught polluting.",

"good":{
"text":"Fine company heavily",
"eco":-2,
"pub":6,
"type":"green",
"carbon":{"industry":-7}
},

"neutral":{
"text":"Issue warning",
"eco":0,
"pub":2,
"type":"neutral",
"carbon":{"industry":-3}
},

"bad":{
"text":"Ignore violation",
"eco":5,
"pub":-5,
"type":"industrial",
"carbon":{"industry":8}
}
},

{
"title":"Green manufacturing grants",
"text":"Industry requests clean tech funding.",

"good":{
"text":"Fund green factories",
"eco":3,
"pub":4,
"type":"green",
"carbon":{"industry":-7}
},

"neutral":{
"text":"Partial funding",
"eco":2,
"pub":1,
"type":"neutral",
"carbon":{"industry":-3}
},

"bad":{
"text":"Reject clean transition",
"eco":4,
"pub":-3,
"type":"industrial",
"carbon":{"industry":5}
}
},

# ================= DISASTERS =================
{
"title":"Major flood",
"text":"Extreme rain damages infrastructure.",

"good":{
"text":"Invest in resilience",
"eco":-3,
"pub":6,
"type":"adaptation",
"carbon":{"industry":-3}
},

"neutral":{
"text":"Emergency repair only",
"eco":-2,
"pub":2,
"type":"neutral"
},

"bad":{
"text":"Ignore climate causes",
"eco":-5,
"pub":-5,
"type":"failure",
"carbon":{"industry":5}
}
},

{
"title":"Heatwave crisis",
"text":"Record temperatures threaten population.",

"good":{
"text":"Heat response programs",
"eco":-2,
"pub":5,
"type":"adaptation",
"carbon":{"energy":-4}
},

"neutral":{
"text":"Short term response",
"eco":-1,
"pub":1,
"type":"neutral"
},

"bad":{
"text":"Do nothing",
"eco":-4,
"pub":-6,
"type":"failure",
"carbon":{"energy":6}
}
},

# ================= PUBLIC =================
{
"title":"Youth climate protest",
"text":"Students demand climate action.",

"good":{
"text":"Announce climate reforms",
"eco":-1,
"pub":7,
"type":"green",
"carbon":{"energy":-5}
},

"neutral":{
"text":"Meet protest leaders",
"eco":1,
"pub":2,
"type":"neutral"
},

"bad":{
"text":"Suppress protest",
"eco":3,
"pub":-7,
"type":"authoritarian",
"carbon":{"energy":4}
}
},

{
"title":"Election pressure",
"text":"Climate policy becomes political.",

"good":{
"text":"Campaign on climate action",
"eco":-2,
"pub":5,
"type":"green",
"carbon":{"energy":-5}
},

"neutral":{
"text":"Balanced messaging",
"eco":2,
"pub":1,
"type":"neutral"
},

"bad":{
"text":"Drop climate agenda",
"eco":4,
"pub":-5,
"type":"industrial",
"carbon":{"energy":6}
}
},

# ================= TECHNOLOGY =================
{
"title":"Battery innovation",
"text":"Energy storage improves.",

"good":{
"text":"Fund battery rollout",
"eco":3,
"pub":5,
"type":"green",
"carbon":{"energy":-8}
},

"neutral":{
"text":"Observe market",
"eco":2,
"pub":2,
"type":"neutral",
"carbon":{"energy":-3}
},

"bad":{
"text":"Ignore innovation",
"eco":4,
"pub":-2,
"type":"industrial",
"carbon":{"energy":4}
}
},

{
"title":"Carbon capture",
"text":"Carbon capture proposed.",

"good":{
"text":"Build capture plants",
"eco":1,
"pub":3,
"type":"green",
"carbon":{"industry":-6}
},

"neutral":{
"text":"Research funding",
"eco":1,
"pub":1,
"type":"neutral",
"carbon":{"industry":-2}
},

"bad":{
"text":"Reject project",
"eco":3,
"pub":-3,
"type":"industrial",
"carbon":{"industry":4}
}
},

# ================= AGRICULTURE =================
{
"title":"Methane regulation",
"text":"Farm emissions reviewed.",

"good":{
"text":"Regulate methane",
"eco":-2,
"pub":4,
"type":"green",
"carbon":{"agriculture":-6}
},

"neutral":{
"text":"Voluntary targets",
"eco":1,
"pub":1,
"type":"neutral",
"carbon":{"agriculture":-2}
},

"bad":{
"text":"No regulation",
"eco":4,
"pub":-4,
"type":"industrial",
"carbon":{"agriculture":5}
}
}

]

# =========================
# SCENARIO SYSTEM
# =========================

scenario_deck = []

def initialize_scenarios():
    global scenario_deck
    scenario_deck = scenarios.copy()
    random.shuffle(scenario_deck)

def get_random_scenario():
    global scenario_deck

    if len(scenario_deck) == 0:
        scenario_deck = scenarios.copy()
        random.shuffle(scenario_deck)

    return scenario_deck.pop(0)