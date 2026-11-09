class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.tweets = defaultdict(list) #userId -> list of [count, tweetIds]
        self.count = 0 #timestamp (more negative=more recent)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followings[userId].add(userId)
        minheap = []
        feed = []

        #for each person that the user is following
        for followee in self.followings[userId]:
            #if the person made any tweets
            if followee in self.tweets:
                #get the most recent tweet from that person
                index = len(self.tweets[followee]) - 1
                count, tweetId = self.tweets[followee][index]
                #push tweet to heap, if the same followee is encountered again, we will get the next most recent
                heapq.heappush(minheap, [count, tweetId, followee, index - 1])

        while minheap and len(feed) < 10:
            count, tweetId, followee, index = heapq.heappop(minheap)
            feed.append(tweetId)

            if index >= 0: #if that person has any more tweets
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(minheap, [count, tweetId, followee, index - 1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)
