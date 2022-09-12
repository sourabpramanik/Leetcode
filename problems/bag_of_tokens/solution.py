class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        maxScore = 0
        score = 0
        
        queue = collections.deque(tokens)
        
        while queue and (power>=queue[0] or score):
            while queue and power>=queue[0]:
                power -= queue.popleft()
                score += 1
                
            maxScore = max(maxScore, score)
            
            if queue and score:
                power += queue.pop()
                score -= 1
            
            
        
        return maxScore