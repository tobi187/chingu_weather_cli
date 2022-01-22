module CLIModel
open CommandLine

type options = {
    [<Option('o', "output", Default="txt", HelpText="output as json or text")>] output : string;
    [<Value(0, MetaName="cityname", Required=true)>] cityName : string;
    [<Option('f', "fahrenheit")>] fahrenheit : bool; 
    [<Option('c', "celsius")>] celsius : bool; 
    [<Option('l', "Choose out of Location Options")>] locOptions : bool;
}

