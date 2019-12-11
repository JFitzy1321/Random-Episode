using System;

namespace Randomizer.ConsoleUI
{
    public class MyConsole : IConsoleComm
    {
        public bool AskToLoopAgain()
        {
            while (true)
            {
                try
                {
                    WriteMessage("\nWant to find another random episode or find another show? y / n : ", NewLineCharacter.No);
                    string input = ReadLine();

                    return EvaluateResponse(input);
                }
                catch (ArgumentException)
                {
                    WriteMessage(@"Invalid Entry. Please enter 'y' or 'n'");
                    continue;
                }
                catch (Exception ex)
                {
                    WriteMessage($"An exception was catch: {ex.Message}");
                    WriteMessage("Closing app. Goodbye!");
                    return false;
                }
            }
        }

        public string ReadLine()
        {
            try
            {
                return Console.ReadLine();
            }
            catch (ArgumentException ex)
            {
                throw ex;
            }
        }

        public void WriteMessage(string message, NewLineCharacter charReturn = NewLineCharacter.Yes)
        {
            try
            {
                if (charReturn != NewLineCharacter.Yes)
                    Console.Write(message);
                else
                    Console.WriteLine(message);
            }
            catch
            {
                throw;
            }
        }

        private bool EvaluateResponse(string answer)
        {
            if (string.IsNullOrEmpty(answer) || string.IsNullOrWhiteSpace(answer))
                throw new ArgumentNullException("Please type something in before pressing enter!");

            var ansLower = answer.ToLower();

            if (!ansLower.StartsWith('y') && !ansLower.StartsWith('n'))
                throw new ArgumentException("Input must either be yes or no! Try again.");

            return ansLower.StartsWith('y');
        }
    }
}
