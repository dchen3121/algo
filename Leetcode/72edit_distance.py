class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1 == word2:
            return 0

        distance = [[0 for i in range(len(word2))] for j in range(len(word1))]

        # set up initial edges
        count1 = count2 = distance[0][0] = 0 if word1[0] == word2[0] else 1
        bool1 = bool2 = True
        for i in range(1, len(word1)):
            if word1[i] == word2[0] and bool1:
                count1 -= 1
                bool1 = False
            count1 += 1
            distance[i][0] = count1
        for i in range(1, len(word2)):
            if word2[i] == word1[0] and bool2:
                count2 -= 1
                bool2 = False
            count2 += 1
            distance[0][i] = count2
        
        # dp
        for l1 in range(1, len(word1)):
            for l2 in range(1, len(word2)):
                increment = 0 if word1[l1] == word2[l2] else 1
                distance[l1][l2] = min(
                    distance[l1 - 1][l2] + 1,
                    distance[l1][l2 - 1] + 1,
                    distance[l1 - 1][l2 - 1] + increment
                )
        
        return distance[-1][-1]


# Difficulty: hard
# Key points:
# Dynamic programming. Consider two words word1 and word2, and define
# distance(l1, l2) to be the minimum distance between word1[:l1] and word2[:l2]
# Then distance(len(word1), len(word2)) is what we're looking for.
#                        | distance(l1 - 1, l2 - 1) + 1 
# distance(l1, l2) = min | distance(l1 - 1, l2) + 1
#                        | distance(l1, l2 - 1) + 0 if word1[l1] == word2[l2] else 1
# Store results dynamically in a 2d array and compute.
