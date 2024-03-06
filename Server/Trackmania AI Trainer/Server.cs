using System.Text;
using Grapevine;
using Newtonsoft.Json;
using Trackmania_AI_Trainer.Data;

namespace Trackmania_AI_Trainer;

[RestResource]
public class Server
{
    [RestRoute("Post", "/")]
    public async Task PostData(IHttpContext context)
    {
        await using (var data = context.Request.InputStream)
        {
            using (var streamReader = new StreamReader(data, Encoding.UTF8))
            {
                Console.Clear();
                var vehicleData = JsonConvert.DeserializeObject<VehicleData>(await streamReader.ReadToEndAsync()) ?? new VehicleData();
                Console.WriteLine(vehicleData.ToJson());
            }
        }
        
        await context.Response.SendResponseAsync(HttpStatusCode.Ok);
    }
}