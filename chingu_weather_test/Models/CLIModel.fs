module CLIModel
open CommandLine

type options = {
    [<Value(0, MetaName="cityname", Required=true)>] cityName : string;
    [<Option('f', "fahrenheit")>] fahrenheit : bool; 
    [<Option('c', "celsius")>] celsius : bool; 
    [<Option('l', "Choose out of Location Options")>] locOptions : bool;
}

