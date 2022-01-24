module APIWorker
open APIModel
open FSharp.Data
open System


let mapboxApiKey = Environment.GetEnvironmentVariable "mapbox_apikey"
let openWeatherApiKey = Environment.GetEnvironmentVariable "openweather_apikey" 

type Location = JsonProvider<"DataExamples/mapbox.json">
type Weather = JsonProvider<"DataExamples/openweather.json">



let geoLoc cityName = 
    let link = $"https://api.mapbox.com/geocoding/v5/mapbox.places/{cityName}.json?access_token={mapboxApiKey}"
    printfn "%A" link
    let data = Location.Load(link)
    
    if data.Features.Length < 1 then 
        printfn "Location not found"
        exit 0

    let feat = data.Features.[0]
    
    let location: APIMapModel = {
        cityLoc = feat.PlaceName
        lat = feat.Center[1].ToString()
        lon = feat.Center[0].ToString()
    }
    location


let getLocList cityName = 
    let link = $"https://api.mapbox.com/geocoding/v5/mapbox.places/{cityName}.json?access_token={mapboxApiKey}"
    let data = Location.Load(link)

    if data.Features.Length < 1 then 
        printfn "Location not found"
        exit 0

    let dataList = Array.map (fun (x: Location.Feature) -> {cityLoc=x.PlaceName; lat=x.Center[1].ToString(); lon=x.Center[0].ToString()}) data.Features
    printfn "%A" dataList
    dataList

   

let getWeather loc cel =
    let tempUnit = if cel then "metric" else "imperial"
    let link = $"https://api.openweathermap.org/data/2.5/onecall?lat={loc.lat}&lon={loc.lon}&appid={openWeatherApiKey}&units={tempUnit}&exclude=minutely,alerts,daily"
    
    let data = Weather.Load(link)

    {
        temp = data.Current.Temp.ToString()
        cond = data.Current.Weather.[0].Description
        foresight = data.Hourly.[4].Weather.[0].Description
    }

   

let writeData (data:APIWeatherModel) (locData:APIMapModel) tempUnit =
    
    let filename = @"result.txt"
    let file = IO.File.ReadAllLines @"Results/result.txt"
    let message = [|$"Location: {locData.cityLoc}"; $"Temperature: {data.temp} {tempUnit}"; $"Conditions: {data.cond}"; $"Foresight: {data.foresight}"; "\n"|]
    IO.File.WriteAllLines (@"Results/result.txt", (Array.append file message))
    printfn "The result was saved to %s" filename

