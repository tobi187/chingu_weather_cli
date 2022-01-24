import sys
from cli_functionality import special_case, input_validation
from api_action import get_weather, get_location


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
