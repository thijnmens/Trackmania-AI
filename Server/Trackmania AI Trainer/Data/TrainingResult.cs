namespace Trackmania_AI_Trainer.Data;

public class TrainingResult
{
    public int TimeToComplete { get; private set; }
    public int Crashes { get; private set; }

    public TrainingResult(int timeToComplete, int crashes)
    {
        this.TimeToComplete = timeToComplete;
        this.Crashes = crashes;
    }
}