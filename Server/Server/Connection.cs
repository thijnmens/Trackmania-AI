using NetMQ;
using NetMQ.Sockets;

namespace Server;

public static class Connection
{
	private static readonly RequestSocket RequestSocket = new RequestSocket();
	private static int _count = 0;

	public static void Init()
	{
		RequestSocket.Connect("tcp://localhost:5555");
	}

	public static void Close()
	{
		RequestSocket.Close();
	}
	
	public static void SendMessage(string vehicleData)
	{
		RequestSocket.SendFrame(vehicleData);
		RequestSocket.ReceiveFrameString();
		_count++;
	}
}