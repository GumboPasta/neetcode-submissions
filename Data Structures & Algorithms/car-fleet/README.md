# Car Fleet

**Difficulty:** Medium

There are cars traveling to the same destination on a single-lane road. Given each car's starting position, its speed, and the target distance, group cars into fleets, where a fleet forms when a faster car catches up to a slower car ahead of it before reaching the destination. Return the number of distinct fleets that will arrive.

## Example 1

Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
Output: 3
Explanation: The cars starting at 10 and 8 merge into one fleet, the car at 0 travels alone, and the cars at 5 and 3 merge into another fleet, giving 3 fleets total.

## Example 2

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, so it forms a single fleet.

Constraints: all car positions are unique and less than the target distance.

Full problem statement: https://neetcode.io/problems/car-fleet
