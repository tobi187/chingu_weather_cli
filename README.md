# Chingu Weather Cli

## Overview
This Project is my Version of the [Chingu Solo Project Weather CLI](https://github.com/chingu-voyages/soloproject-tier3-chinguweather). 
It's a commandline app which let's you enter a City and return the a few Weather Details.
I've created two versions, one in [Fsharp](#FSharp) and one in [Python](#Python), which do mostly the same but each version got a few extra features.

## FSharp

### Features
* Get the temperature, condition of a specified location
* Choose between celsius and fahrenheit
* Save result to a text file
* Choose location out of a list of matching possibilities

### Running the project
* Dotnet 6 is needed
* In the chingu_weather_test folder run "dotnet build"
* Move to dir bin/Debug/.net6/
* Now you can run the programm, ex: .\chingu_weather_test.exe London -c

### Dependencies
* [CommadlineParser.Fsharp](https://github.com/commandlineparser/commandline)
* [FSharp.Data](https://github.com/fsprojects/FSharp.Data/)

### ExampleImages

![fsharpHelpText](https://user-images.githubusercontent.com/61592216/151048257-b897d160-d62b-47b4-b82f-44b819690f93.png)

![fsharpTextOutput](https://user-images.githubusercontent.com/61592216/151048312-dbed9324-2fb1-4e2b-a86d-9557a3bea5ac.png)

## Python

### Features
* Get the temperature, condition of a specified location
* Choose between celsius and fahrenheit
* Choose between saving in json or text (or not save at all) 
* Change the locations of save files

### Running the project
* Python3 is needed
* (win) py .\main.py London -c -s json
* (linux/mac) pyhton3 main.py London -c -s json

### Dependencies
* [requests](https://pypi.org/project/requests/)

### ExampleImages

![pyHelpText](https://user-images.githubusercontent.com/61592216/151048382-becbc47f-a8b2-43f4-a700-533102bb9129.png)

![pyOutput](https://user-images.githubusercontent.com/61592216/151049489-7be0af98-c459-4735-9e81-815de036b19c.png)
