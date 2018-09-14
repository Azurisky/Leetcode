class Twitter(object):


    ## Not heap, slow
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fol = {}
        self.post = {}
        self.index = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.post[userId] = self.post.get(userId, [])
        self.post[userId].append([self.index, tweetId])
        self.index -= 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        ans = []
        tmp = []
        if userId in self.post:
            for i in self.post[userId]:
                tmp.append(i)
        
        if userId in self.fol:
            for i in self.fol[userId]:
                if i in self.post:
                    for j in self.post[i]:
                        if j not in tmp:
                            tmp.append(j)
        for i in sorted(tmp):
            ans.append(i[1])
        return ans[:10]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.fol[followerId] = self.fol.get(followerId, [])
        self.fol[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.fol[followerId] = self.fol.get(followerId, [])
        if followeeId in self.fol[followerId]:
            index = self.fol[followerId].index(followeeId)
            self.fol[followerId] = self.fol[followerId][:index] + self.fol[followerId][index+1:]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)