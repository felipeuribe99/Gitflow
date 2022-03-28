def top_10_retweets(tweets):
    retweets = tweets.sort_values('retweetCount',ascending=False)
    return retweets.head(10)