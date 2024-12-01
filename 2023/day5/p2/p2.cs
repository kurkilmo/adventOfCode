using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Diagnostics;

/// @author kurkilmo
/// @version 06.12.2023
/// <summary>
/// </summary>
public class p2 {
    /// <summary>
    /// </summary>
    public static string[] lines;

    public static void Main() {
        Stopwatch timer = new();
        
        lines = File.ReadAllLines("input.txt");
        // Get maps
        List<List<List<Int64>>> maps = new();
        int mapIndex = 0;
        int lineIndex = 1;
        while (lineIndex < lines.Length) {
            lineIndex += 2;
            while (lines[lineIndex] != "") {
                string[] map = lines[lineIndex].Split(" ");
                List<Int64> mapList = map.Select(s => Int64.Parse(s)).ToList();
                try {
                    maps[mapIndex].Add(mapList);
                }
                catch {
                    maps.Add(new List<List<Int64>>());
                    maps[mapIndex].Add(mapList);
                }
                lineIndex++;
                if (lineIndex >= lines.Length) break;
            }

            mapIndex++;
        }
        
        // Get seeds and run maps
        Int64 minLocation = Int64.MaxValue;
        string[] seedRangesString = lines[0].Split(":")[1].Split(" ");
        Int64[] seedRanges = new Int64[seedRangesString.Length-1];
        for (Int64 i = 1; i < seedRangesString.Length; i++) {
            string s = seedRangesString[i].Trim();
            
            seedRanges[i-1] = Int64.Parse(s);
        }
        Console.WriteLine("Start going through seeds");
        for (Int64 i = 0; i < seedRanges.Length; i+=2) {
            timer.Start();
            Int64 seedStart = seedRanges[i];
            Int64 seedLength = seedRanges[i + 1];

            for (Int64 seed = seedStart; seed <= seedStart + seedLength; seed++) {
                Int64 mapped = seed;
                foreach (List<List<Int64>> map in maps) {
                    mapped = Map(mapped, map);
                }

                if (mapped < minLocation) minLocation = mapped;
            }
            timer.Stop();
            Console.WriteLine($"Seed range done, time: {timer.ElapsedMilliseconds / 1000.0} seconds");
            timer.Reset();
        }
        
        Console.WriteLine($"Min location: {minLocation}");
    }

    public static Int64 Map(Int64 seed, List<List<Int64>> map) {
        Int64 resSeed = seed;
        foreach (List<Int64> m in map) {
            Int64 destStart = m[0];
            Int64 sourceStart = m[1];
            Int64 length = m[2];
            
            if (seed >= sourceStart && seed < (sourceStart + length)) {
                resSeed = (destStart + (seed - sourceStart));
                break;
            }
        }

        return resSeed;
    }
}