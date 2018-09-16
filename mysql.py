# 利用pymysql第三方库来连接MYSQL数据库
import pymysql


def connect_and_create_db():
    db = pymysql.connect(host='localhost', user='root', password='root123', port=3306)
    cursor = db.cursor()
    # 获取数据库的操作游标
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print("Database version=%s", data)
    cursor.execute('CREATE DATABASE spider DEFAULT CHARACTER SET utf8')
    # 科普一下: CREATE DATABASE '数据库名' DEFAULT CHARACTER SET utf8（将数据库的默认编码格式设置为utf8）
    cursor.close()
    db.close()


def create_table():
    db = pymysql.connect(host='localhost', user='root', password='root123', port=3306, db='spider')
    cursor = db.cursor()
    sql = 'CREATE TABLE students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)
    cursor.close()
    db.close()


def insert_data_to_db():
    db = pymysql.connect(host='localhost', user='root', password='root123', port=3306, db='spider')
    cursor = db.cursor()
    id = '10221801'
    name = 'lbj2'
    age = 90
    sql = 'INSERT INTO students(id, name, age) VALUES(%s, %s, %s)'
    # 使用占位符%s
    try:
        cursor.execute(sql, (id, name, age))
        # 事务的原子性,ACID
        db.commit()
    except:
        db.rollback()
    cursor.close()
    db.close()


def update_table():
    db = pymysql.connect(host='localhost', user='root', password='root123', port=3306, db='spider')
    cursor = db.cursor()
    sql = 'UPDATE students SET age = %s WHERE name = %s'
    age = 100
    name = 'Bob'
    try:
        cursor.execute(sql, (age, name))
        db.commit()
    except:
        db.rollback()
    cursor.close()
    db.close()


if __name__ == '__main__':
    # create_table()
    # insert_data_to_db()
    update_table()
