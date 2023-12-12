using System;
using System.Linq;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Numerics;

/// @author kurkilmo
/// @version 10.12.2023
/// <summary>
/// 
/// </summary>
public class Day8 {
    /// <summary>
    /// 
    /// </summary>

    public static string[] lines;
    
    public static void Main()
    {
        lines = File.ReadAllLines("input.txt");
        lines[0] = lines[0].Trim();

        Stopwatch timer = new();
        int[] directions = new int[lines[0].Length];
        for (int i = 0; i < lines[0].Length; i++) {
            char c = lines[0][i];
            switch (c) {
                case 'L':
                    directions[i] = 0;
                    break;
                case 'R':
                    directions[i] = 1;
                    break;
                default:
                    Console.WriteLine($"???: {c}");
                    break;
            }
        }

        Dictionary<string, string[]> map = new();
        for (int i = 2; i < lines.Length; i++) {
            string[] spl = lines[i].Split(" = ");
            string addres = spl[0];
            string[] destinations = spl[1].Split(", ");
            string left = destinations[0][1..4];
            string right = destinations[1][..3];
            map.Add(addres, new [] {left, right});
        }
        Console.WriteLine(map.ToString());
        // Part 2

        List<string> keys = map.Keys.Where(key => key[2] == 'A').ToList();
        //keys = new List<string>{"GRQ", "RXV", "RMJ", "RVG", "KCR", "PGF"};
        BigInteger count = 0;//2147400000;
        int interval = 500000;
        int intervalCount = 0;

        int directionPointer = 0;
        timer.Start();
        while (keys.Any(key => key[2] != 'Z')) {
            for (int keyIndex = 0; keyIndex < keys.Count; keyIndex++) {
                keys[keyIndex] = map[keys[keyIndex]][directions[directionPointer]];
            }
            
            count++;
            intervalCount++;
            directionPointer++;
            
            if (intervalCount == interval) {
                Console.WriteLine($"Count: {count}, Keys: {string.Join(", ", keys)}");
                intervalCount = 0;
            }

            if (directionPointer == directions.Length) directionPointer = 0;
        }
        timer.Stop();
        Console.WriteLine($"Part 2: Count: {count}, time: {timer.Elapsed.Seconds}");
    }
}
