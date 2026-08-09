class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Key Data Structure: Graph (Topological Sort via DFS)

        # Step 1: every character gets a node in the graph with no edges yet
        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()

        # Step 2: compare each pair of adjacent words to extract ordering rules
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            # invalid case: a longer word can't come before its own prefix
            # e.g. "abc" before "ab" is impossible in any alphabet
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            # find the FIRST character where the two words differ
            # that tells us: this character in word1 comes before that character in word2
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break  # only the first difference matters, stop looking

        # Step 3: topological sort using DFS with cycle detection
        # state[char] can be:
        #   not present  → not yet visited
        #   True         → currently being explored (if we see this again, it's a cycle)
        #   False        → fully explored, safe, already added to result
        state = {}
        result = []

        def has_cycle(char):
            if char in state:
                return state[char]  # True = cycle found, False = already safe

            state[char] = True  # mark as "currently exploring"

            for neighbor in adj[char]:
                if has_cycle(neighbor):
                    return True  # cycle detected deeper in the graph

            state[char] = False  # mark as fully explored, no cycle
            result.append(char)  # add AFTER exploring neighbors (post-order)
            return False

        # run DFS from every character to make sure we cover disconnected letters too
        for char in adj:
            if has_cycle(char):
                return ""  # invalid ordering, cycle exists

        # result was built in reverse topological order — flip it
        result.reverse()
        return "".join(result)

        # Time Complexity:  O(C) — C = total characters across all words
        # Space Complexity: O(1) — at most 26 letters possible in adj/state/result