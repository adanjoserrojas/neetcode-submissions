class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}
        
        if k == 0:
            return topK

        for i, num in enumerate(nums):
            
            if nums[i] not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        
        print(freqMap)

        top_k = sorted(freqMap, key=freqMap.get, reverse=True)[:k]

        return top_k

            
            
