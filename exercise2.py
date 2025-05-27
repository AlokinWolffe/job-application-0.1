volunteers = {
    "Anna": {
        "availability": ["pondělí", "úterý", "pátek"],
        "locations": ["Praha", "Brno"]
    },
    "Boris": {
        "availability": ["středa", "čtvrtek", "pátek"],
        "locations": ["Brno"]
    },
    "Cyril": {
        "availability": ["pondělí", "pátek"],
        "locations": ["Praha"]
    },
    "Dana": {
        "availability": ["úterý", "čtvrtek"],
        "locations": ["Ostrava"]
    },
    "Eva": {
        "availability": ["pondělí", "úterý", "středa", "čtvrtek", "pátek"],
        "locations": ["Praha", "Brno", "Ostrava"]
    }
}

def best_day_for_location(location: str):

    days = {
        "pondělí": {
            "volunteers": []
        },
        "úterý": {
            "volunteers": []
        },
        "středa": {
            "volunteers": []
        },
        "čtvrtek": {
            "volunteers": []
        },
        "pátek": {
            "volunteers": []
        },
    }

    for key in volunteers:
        if location in volunteers[key]["locations"]:
            for day in volunteers[key]["availability"]:
                days[day]["volunteers"].append(key)

    best_day_val = 0
    best_day = ""

    for key in days:
        if len(days[key]["volunteers"]) >= best_day_val:
            best_day_val = len(days[key]["volunteers"])
            best_day = key

    return (best_day, days[best_day]["volunteers"])

def suggest_plan(location: str):

    volunteers_copy = volunteers.copy()

    days = {
        "pondělí": {
            "volunteers": []
        },
        "úterý": {
            "volunteers": []
        },
        "středa": {
            "volunteers": []
        },
        "čtvrtek": {
            "volunteers": []
        },
        "pátek": {
            "volunteers": []
        },
    }

    for key in list(volunteers_copy):
        if location not in volunteers_copy[key]["locations"]:
            print("del", key)
            del volunteers_copy[key]
    
    res = ' '.join(sorted(volunteers_copy, key=lambda key: len(volunteers_copy[key])))

    #sorted volunteers are assigned to days from lowest to highest (amount of days they work)
    #days without volunteers are assigned first
    #following volunteers then take over 1 shift of lower sorted volunteers that have more than 1

    return

print(best_day_for_location("Brno"))

print(suggest_plan("Brno"))