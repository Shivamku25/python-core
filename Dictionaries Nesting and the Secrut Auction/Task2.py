capitals = {
    "France": "Paris",
    "Germany": "Berlin"

}
# Nested list in dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
#
# }

#print Lille
#print(travel_log["France"][0])

#nested_list = ["A", "B", ["C", "D"]]
# print D

#print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    },

}
print(travel_log["France"]["cities_visited"][2])