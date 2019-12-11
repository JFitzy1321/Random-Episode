using System;
using Xunit;
using Randomizer.ConsoleUI;
using System.Reflection;
using System.Linq;

namespace Randomizer.UnitTests
{
    public class ConsoleIOTests
    {
        private bool GetPrivateMethodResults(string input)
        {
            var type = typeof(MyConsole);
            var consolePrivate = Activator.CreateInstance(type);
            MethodInfo method = type.GetMethods(BindingFlags.NonPublic | BindingFlags.Instance)
                .Where(x => x.Name == "YesOrNoEvaluation" && x.IsPrivate)
                .First();

            return (bool)method.Invoke(consolePrivate, new object[] { input });
        }

        [Theory]
        [InlineData("y")]
        [InlineData("Y")]
        [InlineData("yes")]
        [InlineData("YES")]
        [InlineData("YaaaaAaaAaAAAAAAAAAA")]
        public void DoWhileLoopInputTest_ReturnsTrue(string input)
        {
            IConsole console = new MyConsole();

            var actual = GetPrivateMethodResults(input);

            Assert.True(actual);
        }

        [Theory]
        [InlineData("n")]
        [InlineData("N")]
        [InlineData("no")]
        [InlineData("NO")]
        [InlineData("NNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOooooooo")]
        public void DoWhileLoopInputTest_ReturnsFalse(string input)
        {
            IConsole console = new MyConsole();

            bool actual = GetPrivateMethodResults(input);

            Assert.False(actual);
        }

        [Theory]
        [InlineData("")]
        [InlineData("1231123")]
        [InlineData("one two three")]
        [InlineData("    ")]
        [InlineData("this is an invalid string")]
        public void DoWhileLoopInputTest_ThrowException(string input)
        {
            IConsole console = new MyConsole();

            Assert.ThrowsAny<Exception>(() => GetPrivateMethodResults(input));
        }
    }
}

