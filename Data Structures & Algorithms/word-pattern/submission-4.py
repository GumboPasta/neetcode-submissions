class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        p_mapp = {}
        word_mapp = {}

        n = len(pattern)
        j = 0
        words = s.split(" ")

        # base case: if lengths dont match
        if n != len(words):
            return False
    
        # iterate through the pattern and words
        for i in range(n):
            # isolate pattern and word
            pattern_s = pattern[i]
            word = words[i]
            
            # check if letter is present in letterMap
            if pattern_s in p_mapp:
                if p_mapp[pattern_s] != word:
                    return False
                else:
                    continue

            # check if word is present in wordMap
            if word in word_mapp:
                if word_mapp[word] != pattern_s:
                    return False
                else:
                    continue

            # update pointer and add to hashmap
            p_mapp[pattern_s] = word
            word_mapp[word] = pattern_s
            j += 1

        return True