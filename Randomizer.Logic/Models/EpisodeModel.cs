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
                var hash = 0x000123;
                hash *= Id;

                return hash;
            }
        }
        private bool Equals(EpisodeModel other)
        {
            if (this.GetType() != other.GetType())
                return false;

            if (Object.ReferenceEquals(other, null))
                return false;

            if (Object.ReferenceEquals(this, other))
                return true;

            return (this.Season == other.Season) && (this.Number == other.Number);
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