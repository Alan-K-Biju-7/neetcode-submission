import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        result = []
        minHeap = []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count,tweetid =  self.tweetMap[followeeId][index]
                minHeap.append([count,tweetid,followeeId,index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            
            count,tweetid,followeeId,index = heapq.heappop(minHeap)
            result.append(tweetid)
            if index >= 0:
                count,tweetid = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[count,tweetid,followeeId,index - 1])
        return result        


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:

            self.followMap[followerId].remove(followeeId)
        
