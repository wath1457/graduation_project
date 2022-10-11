import csv
import pandas as pd
from cleanText import cleanText

f = open("./dataset/normal.csv", encoding = 'utf-8')
data = csv.reader(f)
keywords = ['기쁨', '좋음', '행복', '사랑', '기쁘', '기뻐', '희망', '뿌듯', '흐뭇', '편안', '감사', '소망']
tweets_list = []
row_list = []
tmp = [] # 중복 check

count = 1 # text 부분만 추출하기 위한 변수
total = -1 # 클린징 전 데이터 개수
wrong_data = 0 # 잘못 크롤링된 데이터 개수
reduplication = -1 # 최상단 제외 / 중복 데이터 개수

for row in data:
    total += 1
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
        for word in keywords:
            if word in row_list[2]:
                tweets_list.append([row_list[1],row_list[2]])
                tmp.append(row_list[2])
                break
    row_list = []
    print(total)
f.close()

tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])
tweets_df.drop_duplicates(['Text'], ignore_index = True)
tweets_df.to_csv('./clean_dataset/clean_normal.csv', encoding='cp949')

print("중복 데이터 제거 개수 : " + str(reduplication))
print(f"잘못 수집된 데이터 제거 개수 : {total - len(tmp)}")
print(f"클린징 후 최종 데이터 개수 : {len(tmp)}")