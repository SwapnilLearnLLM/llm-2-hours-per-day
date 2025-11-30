capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Beinsheim", "Berlin"],
    "India": {
        "num_times": 8,
        "cities_visited": ["Mumbai", "Pune", "Bangalore"]
    }
}

print(travel_log["India"]["cities_visited"][2])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])