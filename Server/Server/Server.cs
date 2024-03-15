using System.Text;
using System.Text.Json.Serialization;
using Grapevine;
using Newtonsoft.Json;
using Server.Json;

namespace Server;

[RestResource]
public class HttpServer
{
	[RestRoute("POST", "/")]
	public async Task PostData(IHttpContext context)
	{
		await using (var data = context.Request.InputStream)
		{
			using (var streamReader = new StreamReader(data, Encoding.UTF8))
			{
				Console.Clear();
				var vehicleData = JsonConvert.DeserializeObject<VehicleData>(await streamReader.ReadToEndAsync()) ??
				                  new VehicleData();
				Console.WriteLine(vehicleData.Position);
				Console.WriteLine(vehicleData.Dir);
			}
		}
	}
}