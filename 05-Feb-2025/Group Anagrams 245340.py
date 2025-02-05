# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        ans = []
        for word in strs:
            alp = [0]*26
            for letter in word:
                alp[ord(letter)-97] += 1
            word_dict[tuple(alp)].append(word)
        for i in word_dict:
            ans.append(word_dict[i])
        return ans

