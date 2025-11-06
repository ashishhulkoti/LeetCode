class Node:
    def __init__(self, tokenId = None, currTime = None):
        self.next = None
        self.prev = None
        self.tokenId = tokenId
        self.time = currTime

class TokenList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, tokenId, currTime) -> Node: 
        newToken = Node(tokenId, currTime)
        newToken.next = self.head.next
        newToken.prev = self.head
        self.head.next = newToken
        newToken.next.prev = newToken
        return newToken
        
    
    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenList = TokenList()
        self.tokenDict = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenDict[tokenId] = self.tokenList.addNode(tokenId, currentTime)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenDict:
            if (currentTime - self.tokenDict[tokenId].time) < self.timeToLive:
                self.tokenList.deleteNode(self.tokenDict[tokenId])
                self.tokenDict[tokenId] = self.tokenList.addNode(tokenId, currentTime)


    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        node = self.tokenList.head.next
        while (node != self.tokenList.tail) and (node.time + self.timeToLive) > currentTime:
            count += 1
            node = node.next
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)