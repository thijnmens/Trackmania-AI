using Grapevine;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;

namespace Server;

internal static class Program
{
	public static void Main(string[] args)
	{
		var serverBuilder = RestServerBuilder.UseDefaults();
		serverBuilder.ConfigureServices += (IServiceCollection services) =>
		{
			services.Configure<LoggerFilterOptions>(options => options.MinLevel = LogLevel.Critical);
		};

		using var server = serverBuilder.Build();
		
		server.Start();
		
		Console.WriteLine("Press enter to quit");
		Console.ReadLine();
	}
}

