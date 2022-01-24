import json

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


def input_validation(args: list[str]):
    arg_list = {"-c": False, "-f": False, "location": args.pop(0), "-s": "no_save"}
    for index, command in enumerate(args):
        if command in arg_list.keys():
            if command == "-c" or command == "--celsius":
                arg_list["-c"] = True
            elif command == "-f" or command == "--fahrenheit":
                arg_list["-f"] = True
            else:
                arg_list[command] = args[index + 1]

    # check if everything's alright
    if arg_list["-c"] == arg_list["-f"]:
        print(help_text + "\n")
        print("Please specify one Temperature unit")
        exit()

    if arg_list["-s"] not in ["no_save", "json", "text"]:
        print(help_text + "\n")
        print("invalid save (-o) argument")
        exit()

    # location, celsius, saveOption
    return arg_list["location"], arg_list["-c"], arg_list["-s"]


def special_case(args: list[str]) -> None:
    if args[0] == "-h" or args[0] == "--help":
        print(help_text)
        exit()
    if args[0] == "--json-path":
        with open("config.json", "r") as file:
            conf = json.load(file)

        if len(args) < 2:
            print(conf["save_locations"]["json"])

        else:
            path = args[1]
            boiler_plate = {"results": []}
            with open(path, "w") as save_file:
                json.dump(boiler_plate, save_file, indent=2)
            conf["save_locations"]["json"] = path
            with open("config.json", "w") as file:
                json.dump(conf, file, indent=2)
            print(f"New json Result Save File: {path}")
        exit()

    elif args[0] == "--text-path":
        with open("config.json", "r") as file:
            conf = json.load(file)

        if len(args) < 2:
            print(conf["save_locations"]["text"])

        else:
            path = args[1]
            with open(path, "w") as file:
                file.write("Chingu Weather CLI Results: \n")
            conf["save_locations"]["text"] = path
            with open("config.json", "w") as file:
                json.dump(conf, file, indent=2)
            print(f"New json Result Save File: {path}")
        exit()
        