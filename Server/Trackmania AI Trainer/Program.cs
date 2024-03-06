using Grapevine;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;

namespace Trackmania_AI_Trainer;

internal static class Program
{
    public static void Main(string[] args)
    {
        var serverBuilder = RestServerBuilder.UseDefaults();
        serverBuilder.ConfigureServices += ConfigureServices;
        
        using var server = serverBuilder.Build();
        
        server.Start();

        Console.WriteLine("Press enter to stop the server");
        Console.ReadLine();
    }
    
    public static void ConfigureServices(IServiceCollection services)
    {
        // Change the logging level if it's too much
        services.Configure<LoggerFilterOptions>(options => options.MinLevel = LogLevel.Critical);
    }
}

