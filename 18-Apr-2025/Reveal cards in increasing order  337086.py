# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        idx = deque(range(len(deck)))
        res = [0] * len(deck)
        order = []
        while idx:
            curr = idx.popleft()
            order.append(curr)
            if idx:
                idx.append(idx.popleft())
        for i, idx in enumerate(order):
            res[idx] = sorted_deck[i]
        return res
