class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}

        for num in nums:

            if num in hashMap:
                hashMap[num] += 1
                continue
            hashMap[num] = 1

        sorted_dict = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict)[:k]
            
        