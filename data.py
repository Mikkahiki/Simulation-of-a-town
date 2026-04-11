import random

# =========================
# CLIMATE CONSTANTS
# =========================

BASE_TEMP = 1.2
TEMP_PER_CO2 = 0.0004   # 🔧 slightly reduced (more realistic)
NATURAL_ABSORPTION = 3

EXTREME_EVENT_TEMP = 1.8
TIPPING_POINT_TEMP = 2.0
COLLAPSE_TEMP = 3.0


# =========================
# ECONOMIC CONSTANTS
# =========================

BASE_ECONOMY = 100
RECESSION_LEVEL = 40
BOOM_LEVEL = 150

GREEN_GROWTH_MULTIPLIER = 1.15   # 🔧 toned down
DIRTY_GROWTH_MULTIPLIER = 1.3


# =========================
# PUBLIC OPINION
# =========================

PUBLIC_PANIC_TEMP = 2.2
PUBLIC_TRUST_POLICY = 5
PUBLIC_ANGER_POLLUTION = -4
PUBLIC_CLIMATE_SUPPORT = 6


# =========================
# STOCHASTIC DAMAGE MODEL
# =========================

CLIMATE_DISASTER_CHANCE = {
    "low": 5,
    "medium": 12,
    "high": 25,
    "extreme": 45
}

DISASTER_DAMAGE = {
    "low": (2, 6),
    "medium": (5, 15),
    "high": (10, 30),
    "extreme": (25, 60)
}


def disaster_roll(temp):
    """
    Random climate damage based on temperature.
    """

    if temp < 1.5:
        level = "low"
    elif temp < 2:
        level = "medium"
    elif temp < 2.6:
        level = "high"
    else:
        level = "extreme"

    chance = CLIMATE_DISASTER_CHANCE[level]

    if random.randint(1, 100) <= chance:
        damage = random.randint(
            DISASTER_DAMAGE[level][0],
            DISASTER_DAMAGE[level][1]
        )
        return level, damage

    return None, 0


# =========================
# EMISSION INERTIA
# =========================

INERTIA_FACTOR = 0.85
INDUSTRY_LOCKIN = 0.9
GREEN_TRANSITION_DELAY = 3


# =========================
# SUSTAINABILITY INDEX (FIXED)
# =========================

def sustainability_index(state):
    """
    Balanced sustainability score.
    Higher = better future.
    """

    score = 0

    # ✅ Positive contributions
    score += state["economy"] * 0.25
    score += state["public"] * 0.25

    # Reward low CO2
    score += max(0, 120 - state["co2_tons"]) * 0.2

    # Reward low temperature
    score += max(0, 2.0 - state["temperature"]) * 40

    # Penalty (reduced)
    score -= state["crisis_level"] * 5

    return int(score)


# =========================
# CLIMATE TIPPING POINTS
# =========================

TIPPING_POINTS = [
    {
        "name": "Permafrost methane release",
        "temp": 1.8,
        "effect": 20,
        "text": "Methane trapped in permafrost is released."
    },
    {
        "name": "Greenland ice collapse",
        "temp": 2.3,
        "effect": 35,
        "text": "Major ice sheets begin irreversible melting."
    },
    {
        "name": "Amazon dieback",
        "temp": 2.5,
        "effect": 25,
        "text": "Rainforest carbon absorption collapses."
    },
    {
        "name": "Ocean circulation disruption",
        "temp": 2.8,
        "effect": 40,
        "text": "Ocean currents destabilize climate."
    }
]


# =========================
# COP NEGOTIATION DATA
# =========================

COP_POSITIONS = {
    "Developed": {
        "co2_cut": -15,
        "eco_cost": -10,
        "difficulty": 70
    },
    "Developing": {
        "co2_cut": -6,
        "eco_cost": -4,
        "difficulty": 40
    },
    "Oil States": {
        "co2_cut": -2,
        "eco_cost": -1,
        "difficulty": 20
    }
}

NEGOTIATION_SUCCESS = {
    "low": 30,
    "medium": 55,
    "high": 75
}


# =========================
# RISK MODELLING (FIXED BUG)
# =========================

def risk_probability(state):
    """
    Calculates probability of major climate damage.
    """

    risk = 0

    # 🔧 FIX: correct key name
    risk += state["temperature"] * 15

    risk += state["co2_tons"] * 0.03
    risk -= state["economy"] * 0.05
    risk -= state["public"] * 0.04

    return max(5, min(95, int(risk)))


# =========================
# SCIENTIFIC BASELINES
# =========================

GLOBAL_TARGET_CO2 = -50
NET_ZERO_TARGET = 0
PARIS_TEMP_LIMIT = 1.5


# =========================
# AI ADVISOR WEIGHTS
# =========================

AI_PRIORITIES = {
    "environment": 0.5,
    "economy": 0.3,
    "politics": 0.2
}


# =========================
# POLICY MEMORY DECAY
# =========================

POLICY_DECAY = 0.92
POLICY_MIN_EFFECT = 0.2


# =========================
# RANDOM NEWS SYSTEM
# =========================

NEWS_HEADLINES = [
    "Scientists warn emissions rising",
    "Global protests demand action",
    "Green technology breakthrough announced",
    "Extreme storms increase globally",
    "Youth climate movement grows",
    "Carbon markets fluctuate",
    "New renewable record set",
    "Heatwaves impact agriculture"
]


def random_news():
    return random.choice(NEWS_HEADLINES)