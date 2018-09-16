总结一下:
这个是最基础版的爬虫，没有用解析库，没有用框架。解析html那一块正则表达式那边还是比较复杂的，容易出错，不友好。


1_spider_base
分析一下代码：
10行：猫眼做了简单的反爬虫处理，不带headers，User-Agent 会提示恶意访问
26行：正则表达式，贪婪匹配和懒惰匹配
33行：yield的用法，生成器
44行-47行：文件的write用法，json.dumps ensure_ascii=False保证了输出是中文不是unicode


2_spider_mysql
主要是在win上安装了mysql的社区版
python用第三方库pymysql来连接mysql，获取操作游标，根据游标在执行数据库语句。
db常见的方法：db.cursor, db.commit, db.rollback, db.close
cursor常见的方法： cursor.execute, cursor.fetchone, cursor.fetchall, cursor.close
fetchone:返回结果的第一条数据，是元组形式
fetchall:返回结果是二重元组



