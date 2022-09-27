class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        def rec(i):
            if i>n:
                return
            stn = ""
            if i%3==0 and i%5==0:
                stn="FizzBuzz"
            elif i%3==0 and i%5!=0:
                stn="Fizz"
            elif i%5==0 and i%3!=0:
                stn="Buzz"
            else:
                stn = str(i)
            
            ans.append(stn)
            rec(i+1)
        
        rec(1)
        
        return ans