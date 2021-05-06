var = {
    "key1": [],  # a list
    "key2": {},  # a dictionary
    "key3": "value3"
}

print(var)

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "number_of_visits": 7},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart", "Munich"],
        "number_of_visits": 19}
}
print(travel_log)

var2 = ["A", "B", ["C", "D"]]
print(var2)

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "number_of_visits": 7
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart", "Munich"],
        "number_of_visits": 19
    }
]
print(travel_log)
