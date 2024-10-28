""" <- note gpt transcribed the problem description here
Problem Description:

All the competitors in a stock car race have completed their qualifying laps. After each lap, the driver with the slowest "best" time (i.e., the highest lap time) is eliminated. If multiple drivers tie for the slowest time, all of them are eliminated. The process continues until only one driver remains or the laps end.

You are given a two-dimensional string array with each driver's name and their lap time in seconds for each lap. Your task is to return the drivers in the order in which they were eliminated, ending with the last driver or drivers remaining. When multiple drivers are eliminated in the same lap, their names should be listed alphabetically.

Notes:
- You are not expected to provide the most optimal solution, but a solution with a time complexity not worse than O(laps.length * laps[0].length) will be within the execution time limit.

Input:
- A 2D list `laps`, where each sub-list represents a lap. Each sub-list contains strings of the format "Name Time", where `Name` is the driver's name and `Time` is the lap time in seconds (a positive integer).

Output:
- A list of strings representing the names of the drivers in the order they were eliminated. When drivers are eliminated in the same lap, they should be listed alphabetically.

Example:

laps = [["Harold 160", "Gina 155", "Juan 160"],
        ["Sam 152", "Gina 155", "Harold 160"],
        ["Gina 150", "Juan 151"]]

Output:
["Juan", "Harold", "Gina"]

Explanation:
- First lap: 
    - Gina has the fastest time of 155 seconds.
    - Harold and Juan both have the slowest time of 160 seconds, so both are eliminated.
  
- Second lap: 
    - Gina again has the fastest time of 155 seconds.
    - Harold has the slowest time of 160 seconds, but he was already eliminated, so we don't consider him. Sam has 152 seconds and survives this lap.
  
- Third lap: 
    - Gina survives with a time of 150 seconds.
    - Juan is eliminated with 151 seconds.

The elimination order is: ["Juan", "Harold", "Gina"]

Constraints:
1. You can assume that every lap has at least one driver.
2. Driver names are unique.
3. Times are always positive integers.
"""
