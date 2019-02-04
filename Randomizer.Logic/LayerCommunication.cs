using System;
using System.Threading.Tasks;
using Randomizer.Infrastructure;

namespace Randomizer.Logic
{
    public class LayerCommunication : ILayerCommunication
    {
        private TVShow show;

        public bool CallApi()
        {
            try
            {
                var results = TVMazeCaller.CallApi_Sync(show.QueryableTitle);
                SetEpisodeList(results);
                return true;
            }
            catch
            {
                return false;
            }
        }

        public async Task<bool> CallApi_Async()
        {
            try
            {
                return true;
            }
            catch
            {
                return false;
            }
        }
        public Tuple<int, int> GetRandomPair()
        {
            return show.GetRandomPair();
        }

        public Task<Tuple<int, int>> GetRandomPair_Async()
        {
            throw new NotImplementedException();
        }

        public void SetTvTitle(string title)
        {
            show = new TVShow(title);
        }

        private void SetEpisodeList(string apiResults)
        {
            try
            {
                var episodes = new embedded(EpisodeManager.Parse(apiResults));

                show.SetEpiodes(episodes);
            }
            catch
            {
                throw;
            }
        }
    }
}