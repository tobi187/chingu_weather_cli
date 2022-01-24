import dataclasses
import json


@dataclasses.dataclass
class WeatherModel:
    # cityName: str
    city_details: str
    temp: int
    condition: str
    future_condition: str
    temp_unit: str

    def text_output(self, save: bool) -> None:
        print(f"""
        The current Temperature in {self.city_details} is {self.temp} {self.temp_unit}
        The conditions are currently: {self.condition}
        What you should expect: {self.future_condition}
        """)
        if save:
            with open("config.json", "r") as file:
                path: str = json.load(file)["save_locations"]["text"]
            with open(path, "a") as file:
                file.writelines([
                    f"\nLocation: {self.city_details}",
                    f"\nTemperature: {self.temp} {self.temp_unit}",
                    f"\nConditions: {self.condition}",
                    f"\nFuture Conditions: {self.future_condition}",
                    "\n"
                ])

            print(f"Saved to {file.name} ({path})")

    def json_output(self) -> None:
        json_data = {"location": self.city_details, "temperature": self.temp, "temperatureUnit": self.temp_unit,
                     "condition": self.condition, "futureCondition": self.future_condition}
        print(json.dumps(json_data, indent=2))
        with open("config.json", "r+") as file:
            path = json.load(file)["save_locations"]["json"]
        with open(path, "r+") as file:
            data = json.load(file)
            data["results"].append(json_data)
            file.seek(0)
            json.dump(data, file, indent=2)
            print(f"Saved to {file.name}")


@dataclasses.dataclass
class CityModel:
    city_name: str
    lat: float
    lon: float
    temp_system: str
    city_desc: str
