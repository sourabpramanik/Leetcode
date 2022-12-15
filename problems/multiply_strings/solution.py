class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hashMap={
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
        }

        # converting num1
        val1=0
        for ch in num1:
            val1+=hashMap[ch]
            val1*=10
        val1//=10
    
        # converting num2
        val2=0
        for ch in num2:
            val2+=hashMap[ch]
            val2*=10
        val2//=10

        return str(val1*val2)

