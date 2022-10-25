import csv
import pandas as pd
tweets_list = []


f = open("./clean_dataset/clean_depression.csv", encoding = 'cp949')
data = csv.reader(f)
for row in data:
    if row[0] == "":
        continue
    tweets_list.append([row[1],row[2], 1])
f.close()

f = open("./clean_dataset/clean_normal.csv", encoding = 'cp949')
data = csv.reader(f)
for row in data:
    if row[0] == "":
        continue
    tweets_list.append([row[1],row[2], 0])
f.close()

tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text', 'label'])
tweets_df.drop_duplicates(['Text'], ignore_index = True)
tweets_df.to_csv('./clean_dataset/tweets_dataset_final3.csv', encoding='cp949')