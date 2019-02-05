namespace Randomizer.ConsoleUI
{
    static class StandardMessages
    {
        public static string WelcomeMessage => "Welcome to my TV Episode Randomizer App";

        public static string LoopAgain => "Do you want to go again? y / n : ";

        public static string AskForTitle => "Please enter the name of a tv show you wish to randomize : ";

        public static string MenuOptionsMessages =>
        @"Please enter one of the following menu options:
                    1. Get another random episode for your current show
                    2. Enter a different Show
                    3. Exit App \n
                    >>>> ";
    }
}
