travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, number_of_visits, city_list):
    # travel_log.insert(len(travel_log), {"country": country, "visits": number_of_visits, "cities": city_list})
    travel_log.append({"country": country, "visits": number_of_visits, "cities": city_list})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
