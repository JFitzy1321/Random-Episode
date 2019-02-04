using System;

namespace Randomizer.ConsoleUI
{
    class MyConsole : IConsoleComm
    {
        public bool AskToLoopAgain()
        {
            try
            {
                WriteMessage(StandardMessages.LoopAgain, NewLineCharacter.No);

                var answer = ReadLine();

                return EvaluateResponse(answer);
            }
            catch
            {
                throw;
            }
        }

        public string ReadLine()
        {
            try
            {
                return Console.ReadLine();
            }
            catch
            {
                throw;
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
