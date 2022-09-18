import snscrape.modules.twitter as sntwitter
import pandas as pd

keyword_MAX = 300
total_MAX = 1000

# Creating list to append tweet data to
tweets_list = []
search_list = ['우울증 진단', '우울증 처방', '우울증 악화', '나 우울증이래']
total = 0
# Using TwitterSearchScraper to scrape data and append tweets to list
for idx, keyword in enumerate(search_list):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_list[idx] + 'since:2020-01-01 until:2022-09-18').get_items()):
        if i >= keyword_MAX or total >= total_MAX: # i는 keyword 별 검색 제한
            break
        tweets_list.append([tweet.date, tweet.content])
        total += 1
        print("\'{0}\' {1}번째 트윗 수집 -- 총 트윗 : {2}개".format(keyword, i + 1, total))
    
# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])
tweets_df.drop_duplicates(['Text'], ignore_index = True)
tweets_df.to_csv('./dataset/depression.csv', encoding='utf-8')