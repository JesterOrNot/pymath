using System;
using System.Diagnostics;
namespace app
{
    class app
    {
        public static void Main(string[] args)
        {
            Console.Write("Welcome to pymath available calculators include algebra, chemistry, geometry, physics\nWhich do you want?: ");
            string input = Console.ReadLine();
            algebra();
        }
        public static void algebra()
        {
            Console.Write("Welcome to the algebra part of pymath available calculators include logorithm calc(log), and quadratic equation calc(quad)!\nWhich do you want?: ");
            string input = Console.ReadLine();
            if (input == "log")
            {
                Console.Write("What is the base?: ");
                string theBase = Console.ReadLine();
                Console.Write("What is the result?: ");
                string result = Console.ReadLine();
                string[] lines = { theBase, result };
                System.IO.File.WriteAllLines(@"app/data/output.txt", lines);
                ExecuteSysCmd("/usr/bin/python3", "app/lib/logexe.py < app/data/output.txt");
            }
        }
        public static void geometry()
        {
            Console.Write("Welcome to the geometry part of pymath available calculators include circumfrence calculator(circ), pythagorean theorem calc(pythag), area calc(area)\nWhich do you want?: ");
            string input = Console.ReadLine();
        }
        public static void physics()
        {
            Console.Write("Welcome to the physics portion of pymath! available calculators include acceleration calc(acc), displacement calculator(disp), speed calc(speed), tangental acceleration calc(tangacc), velocity calc (velocity), tangental speed calc(tanspeed)\nWhich do you want?: ");
            string input = Console.ReadLine();
        }
        public static void chemistry()
        {
            // WIP
        }
        public static void ExecuteSysCmd(string command, string args = "")
        {
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo.FileName = command;
            proc.StartInfo.Arguments = args;
            proc.Start();
            proc.WaitForExit();
        }
    }
}