float prev_speed = 0; // Used for calculation acceleration
float g_dt = 0; // Used for calculating acceleration

void Main() {
	print("Plugin Started");
}

void Render() {

	CSceneVehicleVisState@ vps = VehicleState::ViewingPlayerState();
	if (vps is null) {
		return;
	}
	
	SendMessage(vps);
}

void Update(float dt) {
	g_dt = dt;
}

class VehicleData {
	float speed;
	float acceleration;
	float inputLeft;
	float inputRight;
	float inputForward;
	float inputBackwards;
	uint gear;
	float rpm;
	vec3 location;
	vec3 direction;

	string toJson() {
		return "{" +
			'"speed":' + tostring(speed) +
			',"acceleration":' + tostring(acceleration) +
			',"inputLeft":' + tostring(inputLeft) +
			',"inputRight":' + tostring(inputRight) +
			',"inputForward":' + tostring(inputForward) +
			',"inputBackwards":' + tostring(inputBackwards) +
			',"gear":' + tostring(gear) +
			',"rpm":' + tostring(rpm) +
			',"location":"' + location.ToString() + '"' +
			',"direction":"' + direction.ToString() + '"' +
		"}";
	}
}

void SendMessage(CSceneVehicleVisState@ vis) {
	VehicleData vehicleData = VehicleData();

	// Calculate speed
	vehicleData.speed = vis.FrontSpeed * 3.6f;
	vehicleData.acceleration = ((vehicleData.speed - prev_speed) / (g_dt / 1000));
	prev_speed = vehicleData.speed;

	// Get inputs
	vehicleData.inputLeft = vis.InputSteer < 0 ? Math::Abs(vis.InputSteer) : 0.0f;
	vehicleData.inputRight = vis.InputSteer > 0 ? vis.InputSteer : 0.0f;
	vehicleData.inputForward = vis.InputGasPedal;
	vehicleData.inputBackwards = vis.InputBrakePedal;

	// Get gears
	vehicleData.gear = vis.CurGear;
	vehicleData.rpm = VehicleState::GetRPM(vis);

	// Location
	vehicleData.location = vis.Position;
	vehicleData.direction = vis.Dir
	
	// Send to C# server
	Net::HttpPost("http://localhost:1234", vehicleData.toJson(), "application/json").Start();
}
