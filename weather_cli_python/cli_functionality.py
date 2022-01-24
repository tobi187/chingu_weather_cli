from main import help_text
import json


def input_validation(args: list[str]):
    arg_list = {"-c": False, "-f": False, "location": args.pop(0), "-s": "no_save"}
    for index, command in enumerate(args):
        if command in arg_list.keys():
            if command == "-c" or command == "--celsius":
                arg_list["-c"] = True
            elif command == "-f" or command == "--fahrenheit":
                arg_list["-f"] = True
            else:
                arg_list[command] = arg_list[index + 1]

    # check if everything's alright
    if arg_list["-c"] != arg_list["-f"]:
        print("Please specify one Temperature unit")
        exit()

    if arg_list["-s"] not in ["no_save", "json", "text"]:
        print("invalid save (-o) argument")
        exit()

    # location, celsius, saveOption
    return arg_list["location"], arg_list["-c"], arg_list["-s"]


def special_case(args: list[str]) -> None:
    if args[0] == "-h" or args[0] == "--help":
        print(help_text)
        exit()
    if args[0] == "--json-path":
        with open("config.json", "r+") as file:
            conf = json.load(file)
            if len(args) < 2:
                print(conf["save_locations"]["json"])
            else:
                pass
        exit()
    elif args[0] == "--text-path":
        with open("config.json", "r+") as file:
            conf = json.load(file)
            if len(args) < 2:
                print(conf["save_locations"]["text"])
            else:
                pass
        exit()
        