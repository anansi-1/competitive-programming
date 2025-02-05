# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        count = 0
        for word in words:
            if not (Counter(word) - Counter(chars)):
                count += len(word)
        return count
      