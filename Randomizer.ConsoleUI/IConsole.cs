namespace Randomizer.ConsoleUI
{
    public enum NewLineCharacter {  Yes, No }

    public interface IConsole
    {
        void WriteMessage(string message, NewLineCharacter charReturn = NewLineCharacter.Yes);
        string ReadLine();
        bool AskToLoopAgain();
    }
}
