class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        heap = list(counter.keys())
        heapq.heapify(heap)
        while heap:
            val = heap[0]
            for k in range(groupSize):
                if counter[val+k] == 0: # run out of the next cards
                    return False
                counter[val+k] -= 1
                if counter[val+k] == 0: 
                    if val+k != heapq.heappop(heap):
                        return False
        return True
        




        












        if len(hand) % groupSize != 0:
            return False
        hashmap = Counter(hand)
        hand = [t for t in hashmap.keys()]
        heapq.heapify(hand)
        # size = 0
        while hand:
            n = hand[0]
            for i in range(n, n+groupSize):
                if i not in hashmap:
                    return False
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    if i != hand[0]: 
                        return False # since there is smaller number but there is no number in between this number and the greater values
                    heapq.heappop(hand)
        return True
            


        # if len(hand) < 2:
        #     return True
        # hand.sort()
        # group = set()
        # group.add(hand[0])
        # l,r = 0,0
        # res = 0
        # while r < len(hand)-1:
        #     if len(group) == groupSize:
        #         group = set()
        #         res += 1
        #     # group.add(hand[l])
        #     # l = r
        #     r = r+1
        #     if hand[r] not in group and hand[r]-hand[l] == 1:
        #         group.add(hand[r])
        #         l=r
        #     # group.add(hand[l])
        #     # group.add(hand[r])
        # if len(group) == groupSize :
        #     return True
        # return False
            


        