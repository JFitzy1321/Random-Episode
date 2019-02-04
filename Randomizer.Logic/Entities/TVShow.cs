using System;
using System.Linq;
namespace Randomizer.Logic
{
    public class TVShow
    {
        private string userFriendlyTitle;

        private string queryableTitle;

        private EpisodeManager episodes;
        public string Title
        {
            get => userFriendlyTitle;
            set
            {
                userFriendlyTitle = value;
                QueryableTitle = value;
            }
        }

        public string QueryableTitle
        {
            get => queryableTitle;
            set
            {
                episodes = new EpisodeManager();
                queryableTitle = ConvertToQueryTitle(value);
            }
        }

        public TVShow()
        {
            episodes = new EpisodeManager();
        }

        public TVShow(string title) : this()
        {
            Title = title;
        }

        private string ConvertToQueryTitle(string title)
        {
            // need to remove any special characters from the title
            var charArray = title.ToLower().Where(c => char.IsLetterOrDigit(c) || char.IsWhiteSpace(c)).ToArray();

            //replace the whitespace with plus sign for api query
            return new string(charArray).Replace(' ', '+');
        }
        public Tuple<int, int> GetRandomPair() => episodes.GetRandomPair();
        public void SetEpiodes(embedded ep)
        {
            episodes.SetSeEpisodes(ep);
        }
    }
}