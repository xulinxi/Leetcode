# 1797. Design Authentication Manager

import time as t

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = dict()
        self.timeToLive = timeToLive
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        # ***Note: use "self.""
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        
        # limit: limit time; how much time left
        limit = currentTime - self.timeToLive
        if tokenId in self.tokens and self.tokens[tokenId] > limit:
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        
        count = 0
        limit = currentTime - self.timeToLive
        for token in self.tokens:
            if self.tokens[token] > limit:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
