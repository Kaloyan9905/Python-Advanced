def forecast(*args):
    sunny = {}
    cloudy = {}
    rainy = {}
    result = ""

    for city, weather in args:
        if weather == "Sunny":
            sunny[city] = weather

    for city, weather in args:
        if weather == "Cloudy":
            cloudy[city] = weather

    for city, weather in args:
        if weather == "Rainy":
            rainy[city] = weather

    reworked_dict_rainy = sorted(rainy.items(), key=lambda x: x[0])
    reworked_dict_cloudy = sorted(cloudy.items(), key=lambda x: x[0])
    reworked_dict_sunny = sorted(sunny.items(), key=lambda x: x[0])

    for key, value in reworked_dict_sunny:
        result += f"{key} - {value}" + "\n"

    for key, value in reworked_dict_cloudy:
        result += f"{key} - {value}" + "\n"

    for key, value in reworked_dict_rainy:
        result += f"{key} - {value}" + "\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
