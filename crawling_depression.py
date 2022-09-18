import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('우울증 진단 since:2021-01-01 until:2022-09-18').get_items()):
    if i>100:
        break
    tweets_list2.append([tweet.date, tweet.content])
    print(str(i) + "번째 트윗 수집")
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Text'])

tweets_df2.to_csv('./dataset/save.csv', encoding='utf-8')