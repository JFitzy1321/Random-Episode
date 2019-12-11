using System;
using System.Net.Http;
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
            while (true)
            {
                try
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
                    return;
                }
                catch (Exception ex)
                {
                    if (ex is HttpRequestException)
                    {
                        myConsole.WriteMessage($"Bad api request. closing program:\n {ex.InnerException.Message}");
                        Environment.Exit(-1);
                    }
                    else if (ex is ArgumentException)
                    {
                        myConsole.WriteMessage("Please enter a valid tv show title!");
                        continue;
                    }
                }
            }
        }
        private static void PostcedingLoops() //opposite of preceding
        {
            while (true)
            {
                myConsole.WriteMessage(StandardMessages.MenuOptionsMessages, NewLineCharacter.No);

                try
                {
                    var userMenuChoice = int.Parse(myConsole.ReadLine());

                    switch (userMenuChoice)
                    {
                        case 1: // get another random ep pair
                            GetRandomPair();
                            return;
                        case 2: // set another tv show name
                            FirstLoop();
                            return;
                        case 3: // exit
                            Environment.Exit(0);
                            break;
                        default: // invalid input
                            myConsole.WriteMessage("Invalid menu option! Try again");
                            continue;
                    }

                }
                catch (FormatException)
                {
                    myConsole.WriteMessage("Invalid input! Try again");
                    continue;
                }
            }
        }
    }
}
