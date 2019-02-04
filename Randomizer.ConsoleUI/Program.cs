using System;
using Randomizer.Logic;

namespace Randomizer.ConsoleUI
{
    class Program
    {
        private static ILayerCommunication commObj = new LayerCommunication();
        private static IConsoleComm myConsole = new MyConsole();

        static void Main(string[] args)
        {
            myConsole.WriteMessage(StandardMessages.WelcomeMessage);

            var isFirstLoop = true;
            do
            {
                if (isFirstLoop)
                    FirstLoop();
                else
                    PostcedingLoops();

            } while (myConsole.AskToLoopAgain());

            Console.WriteLine("goodbye ~ PhoneixKing");
        }

        private static void GetRandomPair()
        {
            var pair = commObj.GetRandomPair();
            myConsole.WriteMessage($"Try Season {pair.Item1} Episode {pair.Item2} ...");
        }
        private static void FirstLoop()
        {
            myConsole.WriteMessage(StandardMessages.AskForTitle, NewLineCharacter.No);
            var title = myConsole.ReadLine();

            commObj.SetTvTitle(title);
            if (commObj.CallApi())
            {
                GetRandomPair();
            }
            else
            {
                myConsole.WriteMessage("Something Went Wrong calling the api. closing app");
                Environment.Exit(-1);
            }

        }
        private static void PostcedingLoops()
        {

        }
    }
}
