using Newtonsoft.Json;

namespace Trackmania_AI_Trainer.Data;

public class VehicleData
{
    [JsonProperty("AirBrakeNormed")] public int AirBrakeNormed;

    [JsonProperty("BulletTimeNormed")] public int BulletTimeNormed;

    [JsonProperty("CurGear")] public int CurGear;

    [JsonProperty("Dir")] public string Dir;

    [JsonProperty("DiscontinuityCount")] public int DiscontinuityCount;

    [JsonProperty("EngineOn")] public string EngineOn;

    [JsonProperty("FLBreakNormedCoef")] public int FLBreakNormedCoef;

    [JsonProperty("FLDamperLen")] public int FLDamperLen;

    [JsonProperty("FLIcing01")] public int FLIcing01;

    [JsonProperty("FLSlipCoef")] public int FLSlipCoef;

    [JsonProperty("FLSteerAngle")] public int FLSteerAngle;

    [JsonProperty("FLTireWear01")] public int FLTireWear01;

    [JsonProperty("FLWheelRot")] public int FLWheelRot;

    [JsonProperty("FLWheelRotSpeed")] public int FLWheelRotSpeed;

    [JsonProperty("FRBreakNormedCoef")] public int FRBreakNormedCoef;

    [JsonProperty("FRDamperLen")] public int FRDamperLen;

    [JsonProperty("FRIcing01")] public int FRIcing01;

    [JsonProperty("FrontSpeed")] public int FrontSpeed;

    [JsonProperty("FRSlipCoef")] public int FRSlipCoef;

    [JsonProperty("FRSteerAngle")] public int FRSteerAngle;

    [JsonProperty("FRTireWear01")] public int FRTireWear01;

    [JsonProperty("FRWheelRot")] public int FRWheelRot;

    [JsonProperty("FRWheelRotSpeed")] public int FRWheelRotSpeed;

    [JsonProperty("GroundDist")] public int GroundDist;

    [JsonProperty("InputBrakePedal")] public int InputBrakePedal;

    [JsonProperty("InputGasPedal")] public int InputGasPedal;

    [JsonProperty("InputIsBraking")] public bool InputIsBraking;

    [JsonProperty("InputSteer")] public int InputSteer;

    [JsonProperty("InputVertical")] public int InputVertical;

    [JsonProperty("IsGroundContact")] public bool IsGroundContact;

    [JsonProperty("IsReactorGroundMode")] public bool IsReactorGroundMode;

    [JsonProperty("IsTopContact")] public bool IsTopContact;

    [JsonProperty("IsTurbo")] public bool IsTurbo;

    [JsonProperty("IsWheelsBurning")] public bool IsWheelsBurning;

    [JsonProperty("Left")] public string Left;

    [JsonProperty("Position")] public string Position;

    [JsonProperty("RaceStartTime")] public int RaceStartTime;

    [JsonProperty("ReactorAirControl")] public string ReactorAirControl;

    [JsonProperty("ReactorInputsX")] public bool ReactorInputsX;

    [JsonProperty("RLBreakNormedCoef")] public int RLBreakNormedCoef;

    [JsonProperty("RLDamperLen")] public int RLDamperLen;

    [JsonProperty("RLIcing01")] public int RLIcing01;

    [JsonProperty("RLSlipCoef")] public int RLSlipCoef;

    [JsonProperty("RLSteerAngle")] public int RLSteerAngle;

    [JsonProperty("RLTireWear01")] public int RLTireWear01;

    [JsonProperty("RLWheelRot")] public int RLWheelRot;

    [JsonProperty("RLWheelRotSpeed")] public int RLWheelRotSpeed;

    [JsonProperty("RRBreakNormedCoef")] public int RRBreakNormedCoef;

    [JsonProperty("RRDamperLen")] public int RRDamperLen;

    [JsonProperty("RRIcing01")] public int RRIcing01;

    [JsonProperty("RRSlipCoef")] public int RRSlipCoef;

    [JsonProperty("RRSteerAngle")] public int RRSteerAngle;

    [JsonProperty("RRTireWear01")] public int RRTireWear01;

    [JsonProperty("RRWheelRot")] public int RRWheelRot;

    [JsonProperty("RRWheelRotSpeed")] public int RRWheelRotSpeed;

    [JsonProperty("SimulationTimeCoef")] public int SimulationTimeCoef;

    [JsonProperty("SpoilerOpenNormed")] public int SpoilerOpenNormed;

    [JsonProperty("TurboTime")] public int TurboTime;

    [JsonProperty("Up")] public string Up;

    [JsonProperty("WaterImmersionCoef")] public int WaterImmersionCoef;

    [JsonProperty("WaterOverDistNormed")] public int WaterOverDistNormed;

    [JsonProperty("WaterOverSurfacePos")] public string WaterOverSurfacePos;

    [JsonProperty("WetnessValue01")] public int WetnessValue01;

    [JsonProperty("WingsOpenNormed")] public int WingsOpenNormed;

    [JsonProperty("WorldCarUp")] public string WorldCarUp;

    [JsonProperty("WorldVel")] public string WorldVel;

    public string ToJson()
    {
        return JsonConvert.SerializeObject(this, Formatting.None);
    }
}