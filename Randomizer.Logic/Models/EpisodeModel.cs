using System;

namespace Randomizer.Logic
{
    public class EpisodeModel
    {
        public int Id { get; set; }
        public int Season { get; set; }
        public int Number { get; set; }

        #region Comparision Operators and Methods
        public override bool Equals(object obj)
        {
            if (obj == null)
                return false;

            return this.Equals(obj as EpisodeModel);
        }
        public override int GetHashCode()
        {
            // i don't know what this method is for, but fuck it
            // it makes the compiler shut the hell up and stop showing warnings
            unchecked
            {
                var hash = (int)Math.Pow(Math.PI, 2);
                hash = (hash * 1321) * Id;
                hash = (hash * 1321) * Season;
                hash = (hash * 1321) * Number;

                return hash;
            }
        }
        private bool Equals(EpisodeModel other)
        {
            if (other == null)
                return false;

            if (ReferenceEquals(this, other))
                return true;

            return this == other;
        }

        public static bool operator ==(EpisodeModel one, EpisodeModel two)
        {
            return (one.Season == two.Season && one.Number == two.Number);
        }

        public static bool operator !=(EpisodeModel one, EpisodeModel two)
        {
            return !(one.Season == two.Season && one.Number == two.Number);
        }
        #endregion
    }
}