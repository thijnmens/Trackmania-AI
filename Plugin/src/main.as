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

void SendMessage(CSceneVehicleVisState@ vehicleData) {
		
		// There is no easy way to convert an object to json with Json::* so i'm using this horrible thing for now

		string jsonData = '{' +
			'"AirBrakeNormed":' + Text::Format('%.0f', vehicleData.AirBrakeNormed) + ',' +
			'"BulletTimeNormed":' + Text::Format('%.0f', vehicleData.BulletTimeNormed) + ',' +
			//'"CamGrpStates":' + Text::Format('%.0f', vehicleData.CamGrpStates) + ',' +
			'"CurGear":' + Text::Format('%.0u', vehicleData.CurGear) + ',' +
			'"Dir":"' + vehicleData.Dir.ToString() + '",' +
			'"DiscontinuityCount":' + Text::Format('%.0f', vehicleData.DiscontinuityCount) + ',' +
			'"EngineOn":"' + vehicleData.EngineOn + '",' +
			'"FLBreakNormedCoef":' + Text::Format('%.0f', vehicleData.FLBreakNormedCoef) + ',' +
			'"FLDamperLen":' + Text::Format('%.0f', vehicleData.FLDamperLen) + ',' +
			//'"FLGroundContactMaterial":' + Text::Format('%.0f', vehicleData.FLGroundContactMaterial) + ',' +
			'"FLIcing01":' + Text::Format('%.0f', vehicleData.FLIcing01) + ',' +
			'"FLSlipCoef":' + Text::Format('%.0f', vehicleData.FLSlipCoef) + ',' +
			'"FLSteerAngle":' + Text::Format('%.0f', vehicleData.FLSteerAngle) + ',' +
			'"FLTireWear01":' + Text::Format('%.0f', vehicleData.FLTireWear01) + ',' +
			'"FLWheelRot":' + Text::Format('%.0f', vehicleData.FLWheelRot) + ',' +
			'"FLWheelRotSpeed":' + Text::Format('%.0f', vehicleData.FLWheelRotSpeed) + ',' +
			'"FRBreakNormedCoef":' + Text::Format('%.0f', vehicleData.FRBreakNormedCoef) + ',' +
			'"FRDamperLen":' + Text::Format('%.0f', vehicleData.FRDamperLen) + ',' +
			//'"FRGroundContactMaterial":' + Text::Format('%.0f', vehicleData.FRGroundContactMaterial) + ',' +
			'"FRIcing01":' + Text::Format('%.0f', vehicleData.FRIcing01) + ',' +
			'"FRSlipCoef":' + Text::Format('%.0f', vehicleData.FRSlipCoef) + ',' +
			'"FRSteerAngle":' + Text::Format('%.0f', vehicleData.FRSteerAngle) + ',' +
			'"FRTireWear01":' + Text::Format('%.0f', vehicleData.FRTireWear01) + ',' +
			'"FRWheelRot":' + Text::Format('%.0f', vehicleData.FRWheelRot) + ',' +
			'"FRWheelRotSpeed":' + Text::Format('%.0f', vehicleData.FRWheelRotSpeed) + ',' +
			'"FrontSpeed":' + Text::Format('%.0f', vehicleData.FrontSpeed) + ',' +
			'"GroundDist":' + Text::Format('%.0f', vehicleData.GroundDist) + ',' +
			'"InputBrakePedal":' + Text::Format('%.0f', vehicleData.InputBrakePedal) + ',' +
			'"InputGasPedal":' + Text::Format('%.0f', vehicleData.InputGasPedal) + ',' +
			'"InputIsBraking":' + vehicleData.InputIsBraking + ',' +
			'"InputSteer":' + Text::Format('%.0f', vehicleData.InputSteer) + ',' +
			'"InputVertical":' + Text::Format('%.0f', vehicleData.InputVertical) + ',' +
			'"IsGroundContact":' + vehicleData.IsGroundContact + ',' +
			'"IsReactorGroundMode":' + vehicleData.IsReactorGroundMode + ',' +
			'"IsTopContact":' + vehicleData.IsTopContact + ',' +
			'"IsTurbo":' + vehicleData.IsTurbo + ',' +
			'"IsWheelsBurning":' + vehicleData.IsWheelsBurning + ',' +
			'"Left":"' + vehicleData.Left.ToString() + '",' +
			'"Position":"' + vehicleData.Position.ToString() + '",' +
			'"RLBreakNormedCoef":' + Text::Format('%.0f', vehicleData.RLBreakNormedCoef) + ',' +
			'"RLDamperLen":' + Text::Format('%.0f', vehicleData.RLDamperLen) + ',' +
			//'"RLGroundContactMaterial":' + Text::Format('%.0f', vehicleData.RLGroundContactMaterial) + ',' +
			'"RLIcing01":' + Text::Format('%.0f', vehicleData.RLIcing01) + ',' +
			'"RLSlipCoef":' + Text::Format('%.0f', vehicleData.RLSlipCoef) + ',' +
			'"RLSteerAngle":' + Text::Format('%.0f', vehicleData.RLSteerAngle) + ',' +
			'"RLTireWear01":' + Text::Format('%.0f', vehicleData.RLTireWear01) + ',' +
			'"RLWheelRot":' + Text::Format('%.0f', vehicleData.RLWheelRot) + ',' +
			'"RLWheelRotSpeed":' + Text::Format('%.0f', vehicleData.RLWheelRotSpeed) + ',' +
			'"RRBreakNormedCoef":' + Text::Format('%.0f', vehicleData.RRBreakNormedCoef) + ',' +
			'"RRDamperLen":' + Text::Format('%.0f', vehicleData.RRDamperLen) + ',' +
			//'"RRGroundContactMaterial":' + Text::Format('%.0f', vehicleData.RRGroundContactMaterial) + ',' +
			'"RRIcing01":' + Text::Format('%.0f', vehicleData.RRIcing01) + ',' +
			'"RRSlipCoef":' + Text::Format('%.0f', vehicleData.RRSlipCoef) + ',' +
			'"RRSteerAngle":' + Text::Format('%.0f', vehicleData.RRSteerAngle) + ',' +
			'"RRTireWear01":' + Text::Format('%.0f', vehicleData.RRTireWear01) + ',' +
			'"RRWheelRot":' + Text::Format('%.0f', vehicleData.RRWheelRot) + ',' +
			'"RRWheelRotSpeed":' + Text::Format('%.0f', vehicleData.RRWheelRotSpeed) + ',' +
			'"RaceStartTime":' + Text::Format('%.0f', vehicleData.RaceStartTime) + ',' +
			'"ReactorAirControl":"' + vehicleData.ReactorAirControl.ToString() + '",' +
			//'"ReactorBoostLvl":' + Text::Format('%.0f', vehicleData.ReactorBoostLvl) + ',' +
			//'"ReactorBoostType":' + Text::Format('%.0f', vehicleData.ReactorBoostType) + ',' +
			'"ReactorInputsX":' + vehicleData.ReactorInputsX + ',' +
			'"SimulationTimeCoef":' + Text::Format('%.0f', vehicleData.SimulationTimeCoef) + ',' +
			'"SpoilerOpenNormed":' + Text::Format('%.0f', vehicleData.SpoilerOpenNormed) + ',' +
			'"TurboTime":' + Text::Format('%.0f', vehicleData.TurboTime) + ',' +
			'"Up":"' + vehicleData.Up.ToString() + '",' +
			'"WaterImmersionCoef":' + Text::Format('%.0f', vehicleData.WaterImmersionCoef) + ',' +
			'"WaterOverDistNormed":' + Text::Format('%.0f', vehicleData.WaterOverDistNormed) + ',' +
			'"WaterOverSurfacePos":"' + vehicleData.WaterOverSurfacePos.ToString() + '",' +
			'"WetnessValue01":' + Text::Format('%.0f', vehicleData.WetnessValue01) + ',' +
			'"WingsOpenNormed":' + Text::Format('%.0f', vehicleData.WingsOpenNormed) + ',' +
			'"WorldCarUp":"' + vehicleData.WorldCarUp.ToString() + '",' +
			'"WorldVel":"' + vehicleData.WorldVel.ToString() + '"' +
		'}';
		
		Net::HttpPost("http://localhost:1234", jsonData, "application/json").Start();
	}