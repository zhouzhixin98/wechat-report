import pymysql
import re
from pymysql.converters import escape_string

conn = pymysql.connect(
    host='175.178.201.158',
    user='root',
    password='aass2233',
    db='jiughim',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

with open(r"D:\zzx\ltjl\究纪心\为爱失去穿衣自由的性感可人儿.txt", encoding='utf-8') as f:
    lines = f.readlines()
    filter_lines = []
    reg = "^.*\s\(.+\):"

    for line in lines:
        # 去除转发的聊天记录 简单过滤
        if (line.startswith('为爱失去穿衣自由的性感可人儿') or line.startswith('究纪心🐸')) and re.match(reg, line):
            filter_lines.append(line.strip())

for line in filter_lines:
    s1 = line.find(" ")
    s2 = line.find("):")
    name = line[:s1]
    time = line[s1 + 2:s2]
    content = line[s2 + 2:]
    print(line)
    insert_sql = f"insert into log(user,datetime,content) values ('{name}','{time}' ,'{escape_string(content)}')"
    cur.execute(insert_sql)
conn.commit()
