import snscrape.modules.twitter as sntwitter
import pandas as pd

keyword_MAX = 15000
total_MAX = 60000
plus = 0
num = []
# Creating list to append tweet data to
tweets_list = []
except_list = ['혐의', '기사', '배우', '뉴스', '출처']
search_list = ['은', '는', '이', '가']
total = 0

file = open("C:\\grad_project\\collect_dataset\\negative_word.txt", "r", encoding='utf-8')
while True:
    line = file.readline()
    if line == '':
        break
    except_list.append(line.strip('\n'))
file.close()

print(search_list)
print(except_list)

flag = False
# Using TwitterSearchScraper to scrape data and append tweets to list
for idx, keyword in enumerate(search_list):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_list[idx] + 'since:2017-01-01 until:2022-10-25').get_items()):
        if i >= keyword_MAX + plus or total >= total_MAX: # i는 keyword 별 검색 제한
            break
        for except_word in except_list: # 제외 키워드가 있으면 수집x
            if except_word in tweet.content:
                plus += 1 # 하나를 건너뛰므로 (i는 증가하지만 실제로 리스트에 추가하진 않았으므로)
                flag = True
                break
        if flag == True: # 추가하지 않고 건너뛰기 위함
            flag = False
            continue
        tweets_list.append([tweet.date, tweet.content])
        total += 1
        print("\'{0}\' {1}번째 트윗 수집 -- 총 트윗 : {2}개".format(keyword, i + 1 - plus, total))
    num.append(total)
    plus = 0
    
# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])
tweets_df.drop_duplicates(['Text'], ignore_index = True)
tweets_df.to_csv('./dataset/normal.csv', encoding='utf-8')
print(num)