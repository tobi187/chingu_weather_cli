module CLIModel
open CommandLine

type options = {
    [<Value(0, MetaName="cityname", Required=true)>] cityName : string;
    [<Option('f', "fahrenheit", Group="tempUnit")>] fahrenheit : bool; 
    [<Option('c', "celsius", Group="tempUnit")>] celsius : bool; 
    [<Option('l', "locationOptions", HelpText="Choose out of Location Options")>] locOptions : bool;
}

