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
    let link = $"https://api.openweathermap.org/data/2.5/weather?lat={loc.lat}&lon={loc.lon}&appid={openWeatherApiKey}&units={tempUnit}"
    
    let data = Weather.Load(link)

    {
        temp = data.Main.Temp.ToString()
        cond = data.Weather.[0].Main
        foresight = data.Weather.[0].Description
    }

   
