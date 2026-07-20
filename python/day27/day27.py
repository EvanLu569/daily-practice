'''
python操作MySQL
下载pymysql
pip install mysql
'''
import pymysql
from pymysql.cursors import DictCursor

# 建立连接
connection=pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    password="root66",
    database="student_db",
    charset="utf8mb4",
    cursorclass=DictCursor
)

# 增删改查
def insert_student(name:str,age:int,gender:str,class_id:int):
    with connection.cursor()as cursor:
        sql="insert into students(name,age,gender,class_id)values(%s,%s,%s,%s)"
        cursor.execute(sql,(name,age,gender,class_id))
        connection.commit()
        print(f"插入成功，新ID:{cursor.lastrowid}")
def query_by_class(class_id:int)->list[dict]:
    with connection.cursor()as cursor:
        sql="select name,age,gender from students where class_id=%s"
        cursor.execute(sql,(class_id,))
        return cursor.fetchall()

def query_one(student_id: int) -> dict | None:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        return cursor.fetchone()

def update_age(student_id: int, new_age: int):
    with connection.cursor() as cursor:
        sql = "UPDATE students SET age = %s WHERE id = %s"
        affected = cursor.execute(sql, (new_age, student_id))
        connection.commit()
        print(f"更新了 {affected} 行")


def delete_student(student_id: int):
    with connection.cursor() as cursor:
        sql = "DELETE FROM students WHERE id = %s"
        affected = cursor.execute(sql, (student_id,))
        connection.commit()
        print(f"删除了 {affected} 行")

# ===== 3. 批量操作 =====
def insert_many(student_list: list[tuple]):
    with connection.cursor() as cursor:
        sql = "INSERT INTO students (name, age, gender, class_id) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, student_list)    # 一次性插入多条
        connection.commit()
        print(f"批量插入 {cursor.rowcount} 行")

# ===== 4. 事务 =====
def transfer_score(from_student: int, to_student: int, score: int):
    """转移分数（事务示例）"""
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE students SET score = score - %s WHERE id = %s",
                (score, from_student)
            )
            cursor.execute(
                "UPDATE students SET score = score + %s WHERE id = %s",
                (score, to_student)
            )
        connection.commit()
        print("转移成功")
    except Exception as e:
        connection.rollback()     # 有任何错误就回滚
        print(f"转移失败，已回滚：{e}")

# ===== 5. 上下文管理器封装 =====
from contextlib import contextmanager

@contextmanager
def get_db():
    conn = pymysql.connect(
        host="localhost", user="root", password="root66",
        database="student_db", charset="utf8mb4", cursorclass=DictCursor,
    )
    try:
        yield conn
    finally:
        conn.close()
# 使用
with get_db() as db:
    with db.cursor() as cur:
        cur.execute("SELECT COUNT(*) AS total FROM students")
        print(cur.fetchone())


# ===== 6. 关闭连接 =====
connection.close()






