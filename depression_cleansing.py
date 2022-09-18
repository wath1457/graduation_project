import csv
from cleanText import cleanText

f = open("./dataset/depression.csv", encoding = 'utf-8')
data = csv.reader(f)
tweets_list = []
row_list = []
tmp = [] # 중복 check
count = 1
minus_index = 0 # 중복 데이터때문에 꼬인 index 맞추기
reduplication = 0
for row in data:
    for val in row:
         # 데이터 구조가 index, Datetime, text 이므로 text일때만 cleaning 진행
        if count % 3 == 0:
            row_list.append(cleanText(val))
        else:
            row_list.append(val)
        count += 1

    # 중복 제거
    if row_list[2] in tmp: # 트윗 내용이 이미 한번 저장된 내용이면 넘김
        minus_index += 1
        reduplication += 1
    else:
        if row_list[0] == '':
            tweets_list.append(row_list)
        else:
            row_list[0] = int(row_list[0]) - minus_index
            tweets_list.append(row_list)
            tmp.append(row_list[2])
    row_list = []
f.close()

f = open("./clean_dataset/clean_depression.csv", 'w', encoding = 'utf-8', newline='')
wr = csv.writer(f)
for row in tweets_list:
    wr.writerow(row)
f.close()
print("중복 개수 : " + str(reduplication))