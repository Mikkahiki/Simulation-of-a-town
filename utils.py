

import random
import time

# ---------- TEXT DISPLAY ----------

def slow_print(text,speed=0.02):

    """
    Story style text printing.
    """

    for char in text:

        print(char,end="",flush=True)

        time.sleep(speed)

    print()



# ---------- SECTION BREAK ----------

def divider():

    print("\n"+"="*40+"\n")



# ---------- INPUT VALIDATION ----------

def safe_input(options):

    """
    Ensures valid player choice.
    """

    while True:

        choice = input("\nChoose option: ")

        if choice.isdigit():

            num = int(choice)

            if 1 <= num <= len(options):

                return num-1

        print("Invalid input")



# ---------- RANDOM HELPERS ----------

def percent_roll(chance):

    """
    Random probability check.
    """

    return random.randint(1,100) <= chance



def random_range(low,high):

    return random.randint(low,high)



# ---------- DATA FORMAT ----------

def clamp(value,low,high):

    """
    Keeps values inside limits.
    """

    return max(low,min(high,value))



def percent_change(old,new):

    if old == 0:

        return 0

    return ((new-old)/old)*100



# ---------- STORY HELPERS ----------

def story_title(text):

    print("\n---",text,"---\n")



def warning(text):

    print("\n⚠ WARNING:",text)



def success(text):

    print("\nSUCCESS:",text)



def failure(text):

    print("\nFAILURE:",text)



# ---------- STATE HELPERS ----------

def add_history(state):

    """
    Stores daily values.
    """

    state["co2_history"].append(

    state["co2_tons"]

    )

    state["eco_history"].append(

    state["economy"]

    )

    state["temp_history"].append(

    state["temp"]

    )

    state["public_history"].append(

    state["public"]

    )



# ---------- RANDOM STORY TEXT ----------

def random_news():

    news = [

    "Scientists warn about emissions",

    "Climate protests grow",

    "Green tech breakthrough",

    "Heatwave damages crops",

    "Global talks stall",

    "Renewable prices fall",

    "Carbon markets unstable",

    "New climate study released"

    ]

    return random.choice(news)



# ---------- DEBUG TOOL ----------

def debug_state(state):

    """
    Developer debug print.
    """

    print("\nDEBUG STATE\n")

    for key,value in state.items():

        print(key,":",value)

        