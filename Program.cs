using System;

class Program
{
    static void Main()
    {
        int[] arrayado = { 1, 2, 3, 4, 5 };
        Span<int> span = array.AsSpan();

        span[1] = 10; // pq é um a mais ou a menos ahco eu

        foreach (int numero in span)
        {
            Console.WriteLine(numero);
        }
        Console.WriteLine("Se isto funcionar batam palmas");
    }
    
}
