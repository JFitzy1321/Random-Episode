using System;

namespace Randomizer.Common.Exceptions
{
    public class BadApiCallException : Exception
    {
        public BadApiCallException(string message) : base(message)
        { }

        public BadApiCallException(string message, Exception innerException) : base(message, innerException)
        { }
    }
}