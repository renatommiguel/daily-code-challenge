"""
Plant the Crop

Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

    1 acre equals 4046.86 square meters.
    1 hectare equals 10,000 square meters.

Here's a list of crops that will be given as input and how much space a single plant takes:
Crop 	Space per plant
"corn" 	1 square meter
"wheat" 	0.1 square meters
"soybeans" 	0.5 square meters
"tomatoes" 	0.25 square meters
"lettuce" 	0.2 square meters

Return the number of plants that fit in the field, rounded down to the nearest whole plant.
Tests

Waiting: 1. get_number_of_plants(1, "acres", "corn") should return 4046.
Waiting: 2. get_number_of_plants(2, "hectares", "lettuce") should return 100000.
Waiting: 3. get_number_of_plants(20, "acres", "soybeans") should return 161874.
Waiting: 4. get_number_of_plants(3.75, "hectares", "tomatoes") should return 150000.
Waiting: 5. get_number_of_plants(16.75, "acres", "tomatoes") should return 271139.

"""




def get_number_of_plants(field_size, unit, crop):
    acre_to_sqm =  4046.86
    hectare_to_sqm = 10000
    crop_sqm_needed = {
        "corn":1,
        "wheat":0.1,
        "soybeans":0.5,
        "tomatoes":0.25,
        "lettuce":0.2,
    }
    if unit == "acres":
        area_sqm = field_size * acre_to_sqm
    elif unit == "hectares":
        area_sqm = field_size * hectare_to_sqm
    elif unit == "sqm":
        area_sqm = field_size
    else:
        print("Wrong unit")
        return False
    if crop not in crop_sqm_needed.keys():
        print("Wrong crop")
        return False
    crop =  crop_sqm_needed[crop]
    number_of_plants = (area_sqm / crop)//1
    print(number_of_plants)
    return number_of_plants


get_number_of_plants(1, "acres", "corn")
get_number_of_plants(2, "hectares", "lettuce")
get_number_of_plants(20, "acres", "soybeans")
get_number_of_plants(3.75, "hectares", "tomatoes")
get_number_of_plants(16.75, "acres", "tomatoes")