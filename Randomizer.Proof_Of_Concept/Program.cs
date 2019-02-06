using System.IO;
using System.Linq;
using System;
using Randomizer.Infrastructure;

namespace Randomizer.Proof_Of_Concept
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a tv show title : ");

            var name = Console.ReadLine();
            var apiTitle = ConvertToApiTitle(name);

            var results = TVMazeCaller.CallApi_Sync(apiTitle);

            Console.WriteLine("Writing JSON from api to file");
            using (StreamWriter output = new StreamWriter(File.Create($"{ System.AppDomain.CurrentDomain.BaseDirectory }\\..\\..\\..\\{ name }_results.json")))
            {
                output.Write(results);
            }

        }

        private static string ConvertToApiTitle(string title)
        {
            var charArray = title.ToLower().Where(c => char.IsLetterOrDigit(c) || char.IsWhiteSpace(c)).ToArray();
            return new string(charArray).Replace(' ','+');
        }
    }
}
