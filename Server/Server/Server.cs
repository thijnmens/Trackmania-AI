using System.Text;
using System.Text.Json.Serialization;
using Grapevine;
using NetMQ.Sockets;
using Newtonsoft.Json;

namespace Server;

[RestResource]
public class HttpServer
{
	[RestRoute("POST", "/")]
	public async Task PostData(IHttpContext context)
	{
		await using var data = context.Request.InputStream;
		using var streamReader = new StreamReader(data, Encoding.UTF8);
		Connection.SendMessage(await streamReader.ReadToEndAsync());
	}
}