class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        quotient = 0    
        dend = abs(dividend)
        dor = abs(divisor)
        
        while dend >= dor :
            temp= dor
            multiplier = 1
            while dend >= temp:
                dend -= temp
                quotient += multiplier
                multiplier += multiplier
                temp += temp
                

            
            
        if (dividend < 0 and divisor >= 0) or (divisor <0 and dividend >= 0):
            quotient = -quotient
        
        
        return min(2147483647, max(-2147483648,quotient))    

            
        
            
            