def top_10_users(tweets, users):
    users_id = tweets['userId'].value_counts()[:10]
    users_id = list(users_id.index.values)
    top = users[users.userId.isin(users_id)]
    return top