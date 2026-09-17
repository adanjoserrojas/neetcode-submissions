class Twitter:


    def __init__(self):
        self.following: dict[int, set] = {}
        self.tweets: dict[int, list] = {}
        self.time: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.following[userId] = set()
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId)) 
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        followees = self.following[userId]
        all_tweets = []
        all_tweets.extend(self.tweets[userId])

        for followee in followees:
            all_tweets.extend(self.tweets.get(followee, []))
        
        all_tweets.sort(reverse=True)

        return [tweet_id for time, tweet_id in all_tweets[:10]]
          

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        if followerId not in self.tweets:
            self.tweets[followerId] = []

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

