using System.Collections.Generic;

namespace Randomizer.Logic
{
    /// <Summary>
    /// This class is just for handling json deseralization
    /// </Summary>
    class JsonModel
    {
        public int id { get; set; }
        public embedded _embedded { get; set; }
    }

    public class embedded
    {
        public List<EpisodeModel> episodes { get; set; }

        public embedded(List<EpisodeModel> ep) => episodes = ep;
    }
}
