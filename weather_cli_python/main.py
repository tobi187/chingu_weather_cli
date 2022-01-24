import sys
from cli_functionality import special_case, input_validation
from api_action import get_weather, get_location

help_text = """
Chingu Weather CLI Python3 Implementation v 1.0.0

  -h, --help:                           print help text
  cityname (first arg) (required):      provide the City name 
  -s:                                   choose output + save. Valid options = no_save (default), json, text
  -c, --celsius:                        set Celsius to temperature Unit
  -f, --fahrenheit:                     set Fahrenheit to temperature Unit
  --json-path                           set path to location to save json result (without arg to print path)
  --text-path                           set path to location to save json result (without arg to print path)
"""


def main(argv: list[str]) -> None:
    special_case(argv)
    location, celsius, save_option = input_validation(argv)
    temp_unit = "metric" if celsius else "imperial"
    loc_data = get_location(city_name=location, temp_system=temp_unit)
    weather_data = get_weather(city_model=loc_data)
    if save_option == "no_save":
        weather_data.text_output(save=False)
    elif save_option == "text":
        weather_data.text_output(save=True)
    elif save_option == "json":
        weather_data.json_output()
    else:
        print("Something went wrong")


if __name__ == "__main__":
    main(sys.argv[1:])
