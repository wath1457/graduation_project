import csv
import pandas as pd
from cleanText import cleanText

f = open("./dataset/normal.csv", encoding = 'utf-8')
data = csv.reader(f)
tweets_list = []
row_list = []
tmp = [] # 중복 check
count = 1

reduplication = 0
for row in data:
    for val in row:
         # 데이터 구조가 index, Datetime, text 이므로 text일때만 cleaning 진행
        if count % 3 == 0:
            row_list.append(cleanText(val))
        else:
            row_list.append(val)
        count += 1

    # 중복, 공백 제거
    if row_list[2] in tmp or row_list[2] == '': # 트윗 내용이 이미 한번 저장된 내용이면 넘김 
        reduplication += 1
    else:
        tweets_list.append([row_list[1],row_list[2]])
        tmp.append(row_list[2])
    row_list = []
f.close()

tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])
tweets_df.drop_duplicates(['Text'], ignore_index = True)
tweets_df.to_csv('./clean_dataset/clean_normal.csv', encoding='cp949')

print("제거 개수 : " + str(reduplication))