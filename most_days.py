def top_10_days(tweets):
    copia = tweets.copy()
    copia['change_format'] = copia['date'].dt.strftime('%d-%m-%Y')
    days = copia['change_format'].value_counts()[:10]
    return days.index.values 