

import math
import random

# =========================
# DESCRIPTIVE STATISTICS
# =========================

def mean(data):

    if not data:
        return 0

    return sum(data)/len(data)



def variance(data):

    if len(data) < 2:
        return 0

    m = mean(data)

    return sum(

        (x-m)**2

        for x in data

    )/(len(data)-1)



def std_dev(data):

    return math.sqrt(
        variance(data)
    )



def median(data):

    if not data:
        return 0

    d = sorted(data)

    n = len(d)

    mid = n//2

    if n%2==0:

        return (d[mid-1]+d[mid])/2

    return d[mid]



# =========================
# CORRELATION SYSTEM
# =========================

def pearson_r(x,y):

    if len(x)!=len(y):

        return 0

    if len(x)<2:

        return 0

    mx = mean(x)
    my = mean(y)

    numerator = sum(

        (a-mx)*(b-my)

        for a,b in zip(x,y)

    )

    denom_x = math.sqrt(

        sum((a-mx)**2 for a in x)

    )

    denom_y = math.sqrt(

        sum((b-my)**2 for b in y)

    )

    if denom_x==0 or denom_y==0:

        return 0

    return numerator/(denom_x*denom_y)



# =========================
# CHI SQUARE BEHAVIOUR TEST
# =========================

def chi_square(choices):

    good = choices.count("good")

    neutral = choices.count("neutral")

    bad = choices.count("bad")

    observed=[good,neutral,bad]

    total=sum(observed)

    if total==0:

        return 0

    expected=total/3

    chi=sum(

        (o-expected)**2/expected

        for o in observed

    )

    return round(chi,3)



# =========================
# TREND ANALYSIS
# =========================

def trend_slope(data):

    n=len(data)

    if n<2:

        return 0

    x=list(range(n))

    mx=mean(x)

    my=mean(data)

    numerator=sum(

        (xi-mx)*(yi-my)

        for xi,yi in zip(x,data)

    )

    denominator=sum(

        (xi-mx)**2

        for xi in x

    )

    if denominator==0:

        return 0

    return numerator/denominator



def moving_average(data,window=3):

    if len(data)<window:

        return data

    result=[]

    for i in range(len(data)):

        start=max(0,i-window+1)

        segment=data[start:i+1]

        result.append(

            mean(segment)

        )

    return result



# =========================
# FORECAST MODEL
# =========================

def simple_forecast(data):

    """
    Linear projection.
    """

    slope=trend_slope(data)

    if not data:

        return 0

    return round(

        data[-1]+slope

    ,2)



def volatility(data):

    """
    Measures instability.
    """

    return std_dev(data)



# =========================
# DATA NORMALIZATION
# =========================

def normalize(data):

    if not data:

        return []

    mn=min(data)

    mx=max(data)

    if mx-mn==0:

        return data

    return [

        (x-mn)/(mx-mn)

        for x in data

    ]



# =========================
# RISK MATHEMATICS
# =========================

def risk_level(value):

    if value<25:

        return "Low"

    if value<50:

        return "Moderate"

    if value<75:

        return "High"

    return "Extreme"



def probability(chance):

    return random.randint(
        1,100
    ) <= chance



# =========================
# Z SCORE ANALYSIS
# =========================

def z_score(value,data):

    sd=std_dev(data)

    if sd==0:

        return 0

    return (

        value-mean(data)

    )/sd



def outliers(data):

    result=[]

    for v in data:

        if abs(

            z_score(v,data)

        )>2:

            result.append(v)

    return result



# =========================
# DECISION ANALYSIS
# =========================

def decision_balance(choices):

    """
    Measures player behaviour.
    """

    total=len(choices)

    if total==0:

        return 0

    green=choices.count("good")

    return round(

        (green/total)*100

    ,1)



# =========================
# SCIENTIFIC REPORT
# =========================

def statistical_report(state):

    print("\n--- STATISTICAL ANALYSIS ---\n")

    co2=state["co2_history"]

    eco=state["eco_history"]

    pub=state["public_history"]

    temp=state["temp_history"]



    print(
    "Average CO2:",
    round(mean(co2),2)
    )

    print(
    "CO2 deviation:",
    round(std_dev(co2),2)
    )

    print(
    "CO2 trend:",
    round(trend_slope(co2),2)
    )

    print(
    "Forecast CO2:",
    simple_forecast(co2)
    )

    print(
    "Carbon/Economy correlation:",
    round(pearson_r(co2,eco),2)
    )

    print(
    "Carbon/Public correlation:",
    round(pearson_r(co2,pub),2)
    )

    print(
    "Decision chi-square:",
    chi_square(state["choices"])
    )

    print(
    "Decision sustainability:",
    decision_balance(state["choices"]),
    "%"
    )

    print(
    "Temperature volatility:",
    round(volatility(temp),2)
    )