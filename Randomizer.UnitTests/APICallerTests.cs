using Randomizer.Infrastructure;
using Randomizer.Common.Exceptions;
using Xunit;

namespace Randomizer.UnitTests
{
    public class APICallerTests
    {
        [Theory]
        [InlineData("archer")]
        [InlineData("south+park")]
        [InlineData("bob's+burgers")]
        [InlineData("bobs+burger")]
        [InlineData("Bob's Burgers")]
        [InlineData("South Park")]
        public void TestAPICaller_ShouldHaveData(string title)
        {
            string excepted = TVMazeCaller.CallApi_Async(title).ToString();

            Assert.False(string.IsNullOrEmpty(excepted));
        }

        [Theory]
        [InlineData("asdkljhsdfasldhfj")]
        [InlineData("&$%^$%^")]
        [InlineData("Armer")]
        public void TestApiCaller_ShouldThrowException(string title)
        {
            Assert.ThrowsAnyAsync<BadApiCallException>(() => TVMazeCaller.CallApi_Async(title));
        }
        //TODO need to write tests to simulate bad connections or no internet
    }
}
