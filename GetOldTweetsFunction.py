import GetOldTweets3 as got
import pandas as pd
import time
from datetime import datetime, timedelta

def DownloadTweets(SinceDate, UntilDate, query, sleep=900, maxtweet=0):
    # create a list of day numbers
    since = datetime.strptime(SinceDate, "%Y-%m-%d")
    days = list(
        range(
            0,
            (
                datetime.strptime(UntilDate, "%Y-%m-%d")
                - datetime.strptime(SinceDate, "%Y-%m-%d")
            ).days
            + 1,
        )
    )
    tweets = []

    for day in days:
        init = (
            got.manager.TweetCriteria()
            .setQuerySearch(query)
            .setSince((since + timedelta(days=day)).strftime("%Y-%m-%d"))
            .setUntil((since + timedelta(days=day + 1)).strftime("%Y-%m-%d"))
            .setMaxTweets(maxtweet)
        )
        get = got.manager.TweetManager.getTweets(init)
        tweets.append(
            [
                [
                    tweet.username,
                    tweet.date,
                    tweet.text,
                    tweet.retweets,
                    tweet.geo,
                    tweet.favorites,
                ]
                for tweet in get
            ]
        )
        print("day", day + 1, "of", len(days), "completed")
        print("sleeping for", sleep, "seconds")
        time.sleep(sleep)

    tweets = [tweet for sublist in tweets for tweet in sublist]
    return tweets


since = "2019-12-19"
until = "2019-12-24"
search_terms = # whatever you want to search for as text. for multiple search words use OR between them.

tweets = DownloadTweets(since, until, query=search_terms, maxtweet=10000, sleep=900)

# create dataframe and checks
df = pd.DataFrame(
    tweets, columns=["user", "date", "text", "retweet", "location", "favorites"]
)

# check df
df.shape
df.head()
df.tail()
