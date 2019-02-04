namespace Randomizer.ConsoleUI
{
    public enum NewLineCharacter {  Yes, No }

    interface IConsole
    {
        void WriteMessage(string message, NewLineCharacter charReturn = NewLineCharacter.Yes);
        string ReadLine();
    }
}
