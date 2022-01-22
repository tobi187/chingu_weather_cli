module APIModel

type APIMapModel = {
    cityLoc: string
    lat: string
    lon: string
}


type APIWeatherModel = {
    temp: string
    cond: string // cloudy sunny etc
    foresight: string
}