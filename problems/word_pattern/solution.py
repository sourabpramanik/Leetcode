class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        hashMap={}
        arr=s.split(" ")

        if len(p)!=len(arr):
            return False
        if len(set(p))!=len(set(arr)):
            return False
        i=0
        for i in range(len(p)):
            if arr[i] not in hashMap:
                hashMap[arr[i]]=p[i]
            elif hashMap[arr[i]]!=p[i]:
                return False


        return True

