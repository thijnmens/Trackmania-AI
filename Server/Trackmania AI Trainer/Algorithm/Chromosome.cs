using GeneticSharp;

namespace Trackmania_AI_Trainer.Algorithm;

public class Chromosome: ChromosomeBase
{
    public Chromosome() : base(10)
    {
        CreateGenes();
    }

    public override Gene GenerateGene(int geneIndex)
    {
        throw new NotImplementedException();
    }

    public override IChromosome CreateNew()
    {
        return new Chromosome();
    }
}