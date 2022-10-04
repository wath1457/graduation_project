import snscrape.modules.twitter as sntwitter
import pandas as pd

keyword_MAX = 10000
total_MAX = 200000
plus = 0
num = []
# Creating list to append tweet data to
tweets_list = []
except_list = ['혐의', '기사', '배우', '뉴스', '출처']
search_list = ['우울', '슬픔', '침울', '눈물', '속상', '자살', '무기력', '슬프', '슬퍼', '죽고', '불안']
total = 0
# Using TwitterSearchScraper to scrape data and append tweets to list
for idx, keyword in enumerate(search_list):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_list[idx] + 'since:2017-01-01 until:2022-10-03').get_items()):
        if i >= keyword_MAX + plus or total >= total_MAX: # i는 keyword 별 검색 제한
            break
        for except_word in except_list:
            if except_word in tweet.content:
                plus += 1 # 하나를 건너뛰므로 (i는 증가하지만 실제로 리스트에 추가하진 않았으므로)
                continue
        tweets_list.append([tweet.date, tweet.content])
        total += 1
        print("\'{0}\' {1}번째 트윗 수집 -- 총 트윗 : {2}개".format(keyword, i + 1, total))
    num.append(total)
    plus = 0
    
# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])
tweets_df.drop_duplicates(['Text'], ignore_index = True)
tweets_df.to_csv('./dataset/depression.csv', encoding='utf-8')
print(num)