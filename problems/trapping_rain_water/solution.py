class Solution:
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume=0
        l=0
        r=len(bars)-1
        lmax=bars[l]
        rmax=bars[r]
        
        while l<=r:
            if bars[l]<=bars[r]:
                if lmax<bars[l]:
                    lmax=bars[l]
                else:
                    volume+=lmax-bars[l]
                l+=1
            else:
                if rmax<bars[r]:
                    rmax=bars[r]
                else:
                    volume+=rmax-bars[r]
                r-=1
                
        return volume
        