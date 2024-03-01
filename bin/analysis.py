import functools

import pymysql
import jieba
import json

conn = pymysql.connect(
    host='175.178.201.158',
    user='root',
    password='aass2233',
    db='jiughim',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

cur.execute("select * from log")

r = cur.fetchall()
result = {}

# 获得最长的一句话
print('获取获得最长的一句话 begin')
max_item = None
for item in r:
    content = item[3]
    if (max_item is None or len(content) > len(max_item[3])) and content.find('http') == -1:
        max_item = item
print(max_item)
print('获取获得最长的一句话 end')

# # 进行分词
print('分词 begin')
word_arr = []
for item in r:
    content = item[3]
    seg_list = jieba.cut(content)
    word_arr = word_arr + list(seg_list)
word_count_map = {}
for word in word_arr:
    if word in word_count_map:
        word_count_map[word] = word_count_map[word] + 1
    else:
        word_count_map[word] = 1
word_count_arr = []
for word in word_count_map:
    o = {
        'word': word,
        'count': word_count_map[word]
    }
    word_count_arr.append(o)


def custom_sort(x, y):
    if x['count'] > y['count']:
        return -1
    if x['count'] < y['count']:
        return 1
    return 0


result['word'] = sorted(word_count_arr, key=functools.cmp_to_key(custom_sort))
print('分词 end')

with open("result.json", "w", encoding="utf-8") as f:
    f.write(
        json.dumps(result, ensure_ascii=False)
    )
