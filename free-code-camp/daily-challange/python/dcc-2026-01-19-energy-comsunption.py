"""

Energy Consumption

Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.

To compare them, convert both values to joules using the following conversions:

    1 Calorie equals 4184 joules.
    1 watt-hour equals 3600 joules.

Return:

    "Workout" if the workout used more energy.
    "Devices" if the device used more energy.
    "Equal" if both used the same amount of energy.

Tests

    Passed: 1. compare_energy(250, 50) should return "Workout".
    Passed: 2. compare_energy(100, 200) should return "Devices".
    Passed: 3. compare_energy(450, 523) should return "Equal".
    Passed: 4. compare_energy(300, 75) should return "Workout".
    Passed: 5. compare_energy(200, 250) should return "Devices".
    Passed: 6. compare_energy(900, 1046) should return "Equal".

"""

def compare_energy(calories_burned, watt_hours_used):
    cal = 4184 #joules
    wh= 3600 #joules
    jo_cal = cal *  calories_burned
    jo_wh = wh * watt_hours_used
    if jo_cal > jo_wh:
        return "Workout"
    elif jo_cal == jo_wh:
        return "Equal"
    else:
        return "Devices"
    return 