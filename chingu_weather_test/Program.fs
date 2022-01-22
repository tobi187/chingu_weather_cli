open System
open CLIModel
open System.Collections
open CommandLine
open APIModel
open APIWorker


[<EntryPoint>]
let main args =
    let parsedValues = Parser.Default.ParseArguments<options> args
    match parsedValues with
    | :? Parsed<options> as parsed -> 
        if parsed.Value.celsius && parsed.Value.fahrenheit then 
            printfn "Error"
            0
        else
            if parsed.Value.locOptions then
                let dataList = getLocList parsed.Value.cityName
                Array.iteri (fun i x -> printfn "%i: %s" (i + 1) x.cityLoc ) dataList
                printfn "\nType the number of the City you want to search for: "
                let cityNr = Console.ReadLine()
                try 
                    let value = dataList.[(int cityNr) - 1]
                    let weather = getWeather value parsed.Value.celsius
                    let tempChar = if parsed.Value.celsius then "° C" else "°F"
                    printfn "Current Temp in %s is %s %s.\nConditions are currently: %s.\nWhat should you expect: %s" value.cityLoc weather.temp tempChar weather.cond weather.foresight

                with
                    | :? System.IndexOutOfRangeException -> printfn "Error: Enter a Valid Number"
                    | :? System.FormatException -> printfn "Error: Enter a Valid Number"

                0
            else
                let data = geoLoc parsed.Value.cityName
                let weather = getWeather data parsed.Value.celsius
                let tempChar = if parsed.Value.celsius then "°C" else "°F"
                printfn "Current Temp in %s is %s %s.\nConditions are currently: %s.\nWhat should you expect: %s" data.cityLoc weather.temp tempChar weather.cond weather.foresight
                0

    | :? NotParsed<options> as notParsed -> 
        printfn "Error"
        0
    | _ -> 
        printfn "Error"
        0

