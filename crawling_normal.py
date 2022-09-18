import snscrape.modules.twitter as sntwitter
import pandas as pd

keyword_MAX = 250
total_MAX = 1000
plus = 0

tweets_list = []
search_list = ['은', '는', '이', '가']
total = 0
# Using TwitterSearchScraper to scrape data and append tweets to list
for idx, keyword in enumerate(search_list):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_list[idx] + 'since:2020-01-01 until:2022-09-18').get_items()):
        if i >= keyword_MAX + plus or total >= total_MAX: # i는 keyword 별 검색 제한
            break
        if '우울' in tweet.content:
            plus += 1 # 하나를 건너뛰므로 (i는 증가하지만 실제로 리스트에 추가하진 않았으므로)
            continue
        tweets_list.append([tweet.date, tweet.content])
        total += 1
        print("\'{0}\' {1}번째 트윗 수집 -- 총 트윗 : {2}개".format(keyword, i + 1, total))
    plus = 0
    
# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])
tweets_df.drop_duplicates(['Text'], ignore_index = True)
tweets_df.to_csv('./dataset/normal.csv', encoding='utf-8')