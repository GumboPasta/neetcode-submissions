class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Key Data Structure: Hashmap and Bucket Sort

        # Create a hashmap to store 
        freqMap = {}

        # Iterate through the array 
        for num in nums:
            
            # Add unique number and frequency to hashmap
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        # Create an array to store frequencies (Index = Frequency) (Value = List of numbers)
        count = [[] for _ in range(len(nums) + 1)]

        # Iterate through the hashmap
        for value in freqMap:
            count[freqMap[value]].append(value)

        res = []
        # Iterate through our Array
        for index in range(len(count)-1, -1, -1):
            for num in count[index]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []

        # Ideation: KEY(The max frequency a number can have is the length of the array)
        # We have a hashmap to track unique number and respective frequency
        # We have an array of size len(nums) where we store the numbers (index = frequency) (value = list of unique numbers)