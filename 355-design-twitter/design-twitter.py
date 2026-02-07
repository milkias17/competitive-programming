class Twitter:

    def __init__(self):
        self.users = defaultdict(dict)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {}

        user_entry = self.users[userId]
        if "tweets" in user_entry:
            self.users[userId]["tweets"].append((self.timestamp, tweetId))
        else:
            tmp = deque()
            tmp.append((self.timestamp, tweetId))
            self.users[userId]["tweets"] = tmp
        
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users[userId]
        heap = []
        if "tweets" in user:
            for tweet in user["tweets"]:
                if len(heap) < 10:
                    heappush(heap, tweet)
                elif tweet[0] > heap[0][0]:
                    heappop(heap)
                    heappush(heap, tweet)
        
        if "following" in user:
            for following in user["following"]:
                if following not in self.users:
                    continue
                cur = self.users[following]
                if "tweets" not in cur:
                    continue
                for tweet in self.users[following]["tweets"]:
                    if len(heap) < 10:
                        heappush(heap, tweet)
                    elif tweet[0] > heap[0][0]:
                        heappop(heap)
                        heappush(heap, tweet)
        
        res = [None] * len(heap)
        cur = len(heap) - 1
        while heap:
            res[cur] = heappop(heap)[-1]
            cur -= 1
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        user_entry = self.users[followerId]
        if "following" in user_entry:
            user_entry["following"].add(followeeId)
        else:
            tmp = set()
            tmp.add(followeeId)
            user_entry["following"] = tmp
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        user_entry = self.users[followerId]
        if "following" not in user_entry:
            return

        user_entry["following"].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)