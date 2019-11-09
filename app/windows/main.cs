using System;
namespace app {
    class app {
        public static void Main(string[] args) {
            Console.Write("Welcome to pymath available calculators include algebra, chemistry, geometry, physics\nWhich do you want?: ")
            input = Console.ReadLine();
        }
        public static void algebra() {
            Console.Write("Welcome to the algebra part of pymath available calculators include logorithm calc(log), and quadratic equation calc(quad)!\nWhich do you want?: ");
            input = Console.ReadLine();
        }
        public static void geometry() {
            Console.Write("Welcome to the geometry part of pymath available calculators include circumfrence calculator(circ), pythagorean theorem calc(pythag), area calc(area)\nWhich do you want?: ");
            input = Console.ReadLine();
        }
        public static void physics() {
            Console.Write("Welcome to the physics portion of pymath! available calculators include acceleration calc(acc), displacement calculator(disp), speed calc(speed), tangental acceleration calc(tangacc), velocity calc (velocity), tangental speed calc(tanspeed)\nWhich do you want?: ");
            input = Console.ReadLine();
        }
        public static void chemistry() {
            // WIP
        }
    }
}