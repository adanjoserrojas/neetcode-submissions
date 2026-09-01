class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Explanation: Use a decreasing monotonic stack to store the indices of the
        # next warmer day, 
        # This is O(n) time and space because in the worse scenario we have to store the
        # len of the entire array in stack and res in case every day is warmer than the one before
        

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
             
            stack.append(i)
            
        
        return res
        