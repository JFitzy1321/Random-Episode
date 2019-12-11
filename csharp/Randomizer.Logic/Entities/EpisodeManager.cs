using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace Randomizer.Logic
{
    public class EpisodeManager
    {
        Random random = new Random();
        private List<EpisodeModel> epList = new List<EpisodeModel>();

        private List<EpisodeModel> exclusion = new List<EpisodeModel>();

        public Tuple<int, int> GetRandomPair()
        {
            while (true)
            {
                var randNum = random.Next(0, epList.Count);

                var chosen = epList[randNum];

                if (exclusion.Contains(chosen))
                    continue;

                exclusion.Add(chosen);
                return new Tuple<int, int>(chosen.Season, chosen.Number);
            }
        }

        public void SetSeEpisodes(embedded ep)
        {
            epList = ep.episodes;
        }

        public static List<EpisodeModel> Parse(string json)
        {
            try
            {
                var model = JsonConvert.DeserializeObject<JsonModel>(json);
                return model._embedded.episodes;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }
    }
}