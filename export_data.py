import json

def export_results(state):

    data={

    "temperature":round(state["temperature"],2),

    "co2":state["co2_tons"],

    "economy":state["economy"],

    "public":state["public"],

    "score":state["sustainability"]

    }

    with open("results.json","w") as f:

        json.dump(data,f)