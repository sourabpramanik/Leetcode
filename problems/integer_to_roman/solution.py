class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        i=0;
        res=""
        
        while num>0:
            if num>=integers[i]:
                num-=integers[i]
                res+=roman[i]
            else:
                i+=1
        
        return res