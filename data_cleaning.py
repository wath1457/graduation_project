## 데이터 클리닝 참조
## https://jeongwookie.github.io/2020/04/29/datascience/twitter/3-analyze-tweet-series-2-preprocessing/

import re
import csv

# Basic Cleaning Text Function
def CleanText(readData, Num=False, Eng=False):

    # Remove Retweets 
    text = re.sub('RT @[\w_]+: ', '', readData)

    # Remove Mentions
    text = re.sub('@[\w_]+', '', text)

    # Remove or Replace URL 
    text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ', text) # http로 시작되는 url
    text = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ', text) # http로 시작되지 않는 url
    
    # Remove Hashtag
    text = re.sub('[#]+[0-9a-zA-Z_]+', ' ', text)

    # Remove Garbage Words (ex. &lt, &gt, etc)
    text = re.sub('[&]+[a-z]+', ' ', text)

    # Remove Special Characters
    text = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', ' ', text)
    
    # Remove newline
    text = text.replace('\n',' ')
    
    if Num is True:
        # Remove Numbers
        text = re.sub(r'\d+',' ',text)
    
    if Eng is True:
        # Remove English 
        text = re.sub('[a-zA-Z]' , ' ', text)

    # Remove multi spacing & Reform sentence
    text = ' '.join(text.split())

    return text

f = open("./dataset/save.csv", encoding = 'utf-8')
data = csv.reader(f)
tweets_list = []
row_list = []
count = 1
for row in data:
    for val in row:
         # 데이터 구조가 index, Datetime, text 이므로 text일때만 cleaning 진행
        if count % 3 == 0:
            row_list.append(CleanText(val))
        else:
            row_list.append(val)
        count += 1
    tweets_list.append(row_list)
    row_list = []
f.close()

f = open("./clean_dataset/clean.csv", 'w', encoding = 'utf-8', newline='')
wr = csv.writer(f)
for row in tweets_list:
    wr.writerow(row)
f.close()
