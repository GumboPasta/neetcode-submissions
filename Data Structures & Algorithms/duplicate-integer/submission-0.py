class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Key Data Structure: HashSet - Only stores unique values

        # First create a hashset to store unqiue values
        uniqueValues = set()

        # Iterate through the array 
        for num in nums:
            # Key Idea: First check if the value is there
            if num in uniqueValues:
                # If the value is already stored in the hashset we return true
                return True
                # Otherwise we add value to hashset
            uniqueValues.add(num)
        # If iteration finishes means all values are unique - return False
        return False


        # Example: [1,2,3,3]

        # First Iteration  Set : [1]
        # Second Iteration Set : [1,2]
        # Third Iteration Set : [1,2,3]
        # Fourth Iteration Set : [1,2,3] - its in the set so return True

        # Time Complexity: O(n) - Since we iterate through the array once




