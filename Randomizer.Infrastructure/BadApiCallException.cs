using System;
namespace Randomizer.Infrastructure
{
    public class BadApiCallException : Exception
    {
        public BadApiCallException(string message) : base(message)
        {
        }
    }
}