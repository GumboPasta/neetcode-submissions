# Time Based Key-Value Store

**Difficulty:** Medium

Design a key-value store that supports storing multiple values for a key along with a timestamp, and retrieving the value associated with a key at or before a given timestamp.

## Example 1

Input: set("cat", "meow", 1), get("cat", 1), get("cat", 3), set("cat", "purr", 4), get("cat", 4), get("cat", 9)
Output: get("cat", 1) returns "meow", get("cat", 3) returns "meow", get("cat", 4) returns "purr", get("cat", 9) returns "purr"

## Example 2

Input: get("dog", 5)
Output: ""
Explanation: No value has ever been set for "dog", so an empty string is returned.

Constraints: timestamps for set operations on the same key are strictly increasing.

Full problem statement: https://neetcode.io/problems/time-based-key-value-store
