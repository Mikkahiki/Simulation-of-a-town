"""
GRAPH ENGINE

Scientific visualization system.

Displays:
Climate trends
Economic trends
Forecast models
Risk projections
Decision behaviour
Scientific correlations
Uncertainty bands

Goal:
Make simulation results look like research data.
"""

import matplotlib.pyplot as plt

from analytics import pearson_r
from data import risk_probability, sustainability_index
from stats import mean, moving_average, simple_forecast, std_dev

# =========================
# CO2 PROGRESS REPORT
# =========================

def show_co2_progress(state):

    print("\nCARBON ANALYSIS")

    start = state["co2_history"][0]

    current = state["co2_tons"]

    change = current-start

    print("Net change:",change)

    print("Average:",round(mean(state["co2_history"]),2))

    print("Deviation:",round(std_dev(state["co2_history"]),2))

    if change < 0:

        print("Trend: Decarbonizing")

    else:

        print("Trend: Increasing emissions")



# =========================
# MAIN GRAPH SYSTEM
# =========================

def show_graphs(state):

    co2 = state["co2_history"]

    eco = state["eco_history"]

    temp = state["temp_history"]

    public = state["public_history"]

    days = list(range(1,len(co2)+1))


    co2_graph(days,co2)

    economy_graph(days,eco)

    temperature_graph(days,temp)

    public_graph(days,public)

    correlation_graph(state)

    risk_graph(state)

    sustainability_graph(state)

    decision_graph(state)



# =========================
# CO2 GRAPH
# =========================

def co2_graph(days,co2):

    avg = mean(co2)

    sd = std_dev(co2)

    smooth = moving_average(co2)

    forecast = simple_forecast(co2)

    plt.figure()

    plt.plot(days,co2,label="CO2")

    plt.plot(days,smooth,label="Trend")

    plt.axhline(avg,label="Mean")

    plt.axhline(avg+sd,linestyle="dashed")

    plt.axhline(avg-sd,linestyle="dashed")

    plt.scatter(

    len(co2)+1,

    forecast,

    label="Forecast"

    )

    plt.title("Carbon emissions trend")

    plt.xlabel("Day")

    plt.ylabel("CO2")

    plt.legend()

    plt.show()



# =========================
# ECONOMY GRAPH
# =========================

def economy_graph(days,eco):

    plt.figure()

    plt.plot(days,eco)

    plt.title("Economic strength")

    plt.xlabel("Day")

    plt.ylabel("Economy")

    plt.axhline(

    mean(eco),

    linestyle="dashed"

    )

    plt.show()



# =========================
# TEMPERATURE GRAPH
# =========================

def temperature_graph(days,temp):

    plt.figure()

    plt.plot(days,temp)

    plt.axhline(1.5,linestyle="dashed")

    plt.axhline(2.0,linestyle="dashed")

    plt.axhline(2.5,linestyle="dashed")

    plt.title("Temperature change")

    plt.xlabel("Day")

    plt.ylabel("Temperature")

    plt.show()



# =========================
# PUBLIC SUPPORT GRAPH
# =========================

def public_graph(days,public):

    plt.figure()

    plt.plot(days,public)

    plt.title("Public approval")

    plt.xlabel("Day")

    plt.ylabel("Support")

    plt.axhline(50,linestyle="dashed")

    plt.show()



# =========================
# CORRELATION GRAPH
# =========================

def correlation_graph(state):

    co2 = state["co2_history"]

    eco = state["eco_history"]

    r = pearson_r(co2,eco)

    plt.figure()

    plt.scatter(co2,eco)

    plt.title("Economy vs emissions")

    plt.xlabel("CO2")

    plt.ylabel("Economy")

    plt.show()

    print("Pearson correlation:",round(r,3))



# =========================
# RISK PROJECTION GRAPH
# =========================

def risk_graph(state):

    risks=[]

    for i in range(len(state["co2_history"])):

        fake_state={

        "temp":state["temp_history"][i],

        "co2_tons":state["co2_history"][i],

        "economy":state["eco_history"][i],

        "public":state["pub_history"][i]

        }

        risks.append(

        risk_probability(fake_state)

        )

    days=range(1,len(risks)+1)

    plt.figure()

    plt.plot(days,risks)

    plt.title("Climate risk probability")

    plt.xlabel("Day")

    plt.ylabel("Risk %")

    plt.show()



# =========================
# SUSTAINABILITY INDEX
# =========================

def sustainability_graph(state):

    scores=[]

    for i in range(len(state["co2_history"])):

        fake_state={

        "economy":state["eco_history"][i],

        "public":state["pub_history"][i],

        "co2_tons":state["co2_history"][i],

        "temp":state["temp_history"][i],

        "crisis_level":0

        }

        scores.append(

        sustainability_index(fake_state)

        )

    days=range(1,len(scores)+1)

    plt.figure()

    plt.plot(days,scores)

    plt.title("Sustainability index")

    plt.xlabel("Day")

    plt.ylabel("Score")

    plt.show()



# =========================
# DECISION BEHAVIOUR
# =========================

def decision_graph(state):

    good=state["choices"].count("good")

    neutral=state["choices"].count("neutral")

    bad=state["choices"].count("bad")

    labels=[

    "Good",
    "Neutral",
    "Bad"

    ]

    values=[

    good,
    neutral,
    bad

    ]

    plt.figure()

    plt.bar(labels,values)

    plt.title("Decision behaviour")

    plt.ylabel("Count")

    plt.show()



# =========================
# RESEARCH DASHBOARD
# =========================

def dashboard(state):

    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.plot(state["co2_history"])
    plt.title("CO2")

    plt.subplot(2,2,2)
    plt.plot(state["eco_history"])
    plt.title("Economy")

    plt.subplot(2,2,3)
    plt.plot(state["temp_history"])
    plt.title("Temperature")

    plt.subplot(2,2,4)
    plt.plot(state["public_history"])
    plt.title("Public")

    plt.tight_layout()

    plt.show()