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
        ["Juan 152", "Gina 155", "Harold 160"],
        ["Gina 150", "Juan 151"]]

Output:
["Juan", "Harold", "Gina"]

Explanation:
- First lap: 
    - Gina has the fastest time of 155 seconds.
    - Harold and Juan both have the slowest time of 160 seconds, so both are eliminated.
  
- Second lap: 
    - Gina again has the fastest time of 155 seconds.
    - Harold has the slowest time of 160 seconds, but he was already eliminated, so we don't consider him. Juan has 152 seconds and survives this lap.
  
- Third lap: 
    - Gina survives with a time of 150 seconds.
    - Juan is eliminated with 151 seconds.

The elimination order is: ["Juan", "Harold", "Gina"]

Constraints:
1. You can assume that every lap has at least one driver.
2. Driver names are unique.
3. Times are always positive integers.
"""

'''
my thoughts:

assume drivers are unique
use the split operator to separate the driver name and time
use the max function on times to get the slowest driver
use a set to store disqualified drivers


handle the case where duplicate drivers are eliminated in the same lap, sorted alphabetically
base case: no drivers in the lap, move to next lap
stopping condition: after all rows (laps) have been iterated over, then return result


some considerations
how do we handle the case where all drivers are eliminated in the same lap?



'''



def solution(laps):
    all_seen = set()  #using a set to track disqualified drivers. if there is a tie and we try to extend with a duplicate driver already in the set, because sets hold only uniques the duplicate driver is skipped and we only add the non-duplicate driver.
    #we use a set here as opposed to a list so that we can check if the driver is already disqualified
    #based on some research, using the not in operator on sets has O(1) time as it's built like a hash table, but using not in operator on arrays we get O(n) because we check all items 
    
    result = [] #output array
    
    for lap in laps: #iterate through rows
        current_drivers = [d for d in lap if d.split()[0] not in all_seen] #list of drivers who are not disqualified. in the last lap once all drivers are disqualified, only 1 remains and so naturally that one driver has the slowest time and gets added to the end of the result list.
        
        if not current_drivers:  #if we get an empty list, move to next lap
            break
        
        slowest_time = max(int(d.split()[1]) for d in current_drivers) #using max to get the slowest time, int typecast to convert from string
        slowest_drivers = [d.split()[0] for d in current_drivers if int(d.split()[1]) == slowest_time]
        
        slowest_drivers.sort() #sort any disqualified drivers alphabetically before adding them to the set, this ensures double disqualified drivers are sorted
        
        result.extend(slowest_drivers) #using extend instead of append to add multiple drivers at once in the case of a double disqualify
        all_seen.update(slowest_drivers) #set built in to update the set with the slowest drivers. if a driver in slowest driver already in all_seen then it skips over
    
    return result


#example from the screenshot to verify the solution
laps = [
    ["Harold 154", "Gina 155", "Juan 160"],
    ["Juan 152", "Gina 155", "Harold 160"],
    ["Harold 148","Gina 150", "Juan 151"]
]
out = solution(laps)
print(out)  #we should get "juan, harold, gina"

#screenshot doesnt have other cases to test unfortuntately.
