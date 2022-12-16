public class Day1
{
    static void Main()
    {
        string[] lines = File.ReadAllLines(@"");
        Answer(lines);
    }

    static void Answer(string[] lines)
    {
        List<int> result = new();
        int start = 0;
        for (int i = 0; i <= lines.Length - 1; i++)
        {
            if (String.IsNullOrEmpty(lines[i]))
            {
                string[] temp = lines;
                int[] myInts = Array.ConvertAll<string, int>(lines[start..i], int.Parse);
                result.Add(myInts.Sum());
                start = i + 1;
            }
        }
        result = result.OrderByDescending(x => x).ToList();
        Console.WriteLine("Part1:" + result[0]);
        Console.WriteLine("Part1:" + result.GetRange(0, 3).Sum());

    }
}