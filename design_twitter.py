import heapq
from typing import List
from collections import defaultdict


class Twitter:
    def __init__(self) -> None:
        self.following_mapping = defaultdict(set)
        self.tweets_mapping = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_mapping[userId].add((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweets_mapping[userId])
        for followee_id in self.following_mapping[userId]:
            feed.extend(self.tweets_mapping[followee_id])

        feed.sort(reverse=True)
        feed = [t[-1] for t in feed]
        return feed[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following_mapping[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_mapping[followerId].discard(followeeId)


class Twitter:
    def __init__(self) -> None:
        self.following_mapping = defaultdict(set)
        self.tweets_mapping = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_mapping[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user_ids_to_consider = self.following_mapping[userId]
        user_ids_to_consider.add(userId)
        max_heap = []

        for user_id in user_ids_to_consider:
            tweets = self.tweets_mapping[user_id]

            if not tweets:
                continue

            last_index = len(tweets) - 1
            time, tweet_id = tweets[last_index]
            heapq.heappush(max_heap, (time, tweet_id, user_id, last_index - 1))

        output = []

        while max_heap and len(output) < 10:
            time, tweet_id, user_id, last_index = heapq.heappop(max_heap)
            output.append(tweet_id)

            if last_index >= 0:
                time, tweet_id = self.tweets_mapping[user_id][last_index]
                heapq.heappush(max_heap, (time, tweet_id, user_id, last_index - 1))

        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following_mapping[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_mapping[followerId].discard(followeeId)


def test():
    twitter = Twitter()
    twitter.postTweet(1, 10)
    twitter.postTweet(2, 20)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.follow(1, 2)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))


if __name__ == "__main__":
    test()
