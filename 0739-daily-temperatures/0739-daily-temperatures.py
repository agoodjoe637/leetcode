class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        result= [0] * len(temperatures)
        for x,y in enumerate(temperatures):
            while days and days[-1][0] < y:
               a,b = days.pop()
               result[b] = x-b
            
               
            days.append([y,x])
        return result
            

            
               


        