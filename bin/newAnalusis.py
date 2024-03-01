import functools
import pymysql
import jieba
import json
import csv

# 加载停用词
stopwords_path = "D:\zzx\wechat-report\\bin\stops.txt"
with open(stopwords_path, "r", encoding="utf-8") as stopword_file:
    stopwords = set(stopword_file.read().splitlines())

conn = pymysql.connect(
    host='175.178.201.158',
    user='root',
    password='aass2233',
    db='jiughim',
    charset='utf8mb4',
    port=3306
)

cur = conn.cursor()

# 获取最长的一句话
print('获取最长的一句话 begin')
cur.execute("SELECT * FROM log WHERE content NOT LIKE '%http%' ORDER BY LENGTH(content) DESC LIMIT 1")
max_item = cur.fetchone()
print(max_item)
print('获取最长的一句话 end')

# 进行分词
print('分词 begin')
word_count_map = {}
cur.execute("SELECT * FROM log")
for item in cur.fetchall():
    content = item[3]
    word_arr = [word for word in jieba.lcut_for_search(content) if word not in stopwords]
    for word in set(word_arr):  # 使用set去除重复的词，提高效率
        word_count_map[word] = word_count_map.get(word, 0) + 1

word_count_arr = [{'word': word, 'count': count} for word, count in word_count_map.items()]

result = {'word': sorted(word_count_arr, key=lambda x: x['count'], reverse=True)}
print('分词 end')

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False)

# 保存结果为 CSV 文件
csv_file_path = "result.csv"
with open(csv_file_path, "w", encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["word", "count"])  # 写入表头
    for word_data in result['word']:
        csv_writer.writerow([word_data['word'], word_data['count']])