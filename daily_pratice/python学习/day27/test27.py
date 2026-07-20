import pymysql
from pymysql.cursors import DictCursor
import pytest


# ---------- 工具：建连接 ----------
def get_conn():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root66',
        database='student_db',
        charset='utf8mb4',
        cursorclass=DictCursor,
        autocommit=False,
    )


def init_db(conn):
    """清空"""
    with conn.cursor() as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                stock INT DEFAULT 0,
                category VARCHAR(50)
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute("DELETE FROM orders")
        c.execute("DELETE FROM products")
    conn.commit()

def add_product(conn, name, price, stock, category):
    with conn.cursor() as c:
        c.execute(
            "INSERT INTO products (name, price, stock, category) VALUES (%s, %s, %s, %s)",
            (name, price, stock, category),
        )
    conn.commit()
    return c.lastrowid

def get_product(conn, pid):
    with conn.cursor() as c:
        c.execute("SELECT * FROM products WHERE id = %s", (pid,))
        return c.fetchone()

def list_products(conn):
    with conn.cursor() as c:
        c.execute("SELECT * FROM products ORDER BY id")
        return c.fetchall()

def update_product(conn, pid, **fields):
    if not fields:
        return 0
    sets = ', '.join(f'{k} = %s' for k in fields)
    values = list(fields.values()) + [pid]
    with conn.cursor() as c:
        rows = c.execute(f"UPDATE products SET {sets} WHERE id = %s", values)
    conn.commit()
    return rows

def delete_product(conn, pid):
    with conn.cursor() as c:
        rows = c.execute("DELETE FROM products WHERE id = %s", (pid,))
    conn.commit()
    return rows

def place_order(conn, user_id, product_id, quantity):
    try:
        with conn.cursor() as c:
            c.execute(
                "SELECT price, stock FROM products WHERE id = %s FOR UPDATE",
                (product_id,),
            )
            row = c.fetchone()
            if not row:
                raise Exception('商品不存在')
            if row['stock'] < quantity:
                raise Exception(f"库存不够，还剩 {row['stock']} 件")

            c.execute(
                "UPDATE products SET stock = stock - %s WHERE id = %s",
                (quantity, product_id),
            )
            c.execute(
                "INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                (user_id, product_id, quantity),
            )
        conn.commit()
        return c.lastrowid
    except Exception:
        conn.rollback()
        raise

class TestCRUD:
    @classmethod
    def setup_class(cls):
        cls.conn = get_conn()
        init_db(cls.conn)

    @classmethod
    def teardown_class(cls):
        cls.conn.close()

    def test_add_product(self):
        pid = add_product(self.conn, '测试商品', 99.9, 10, '测试')
        assert pid > 0

        p = get_product(self.conn, pid)
        assert p['name'] == '测试商品'
        assert p['price'] == 99.9
        assert p['stock'] == 10
        assert p['category'] == '测试'

    def test_list_products(self):
        init_db(self.conn)
        add_product(self.conn, 'A', 1, 1, 'X')
        add_product(self.conn, 'B', 2, 2, 'Y')
        rows = list_products(self.conn)
        assert len(rows) == 2

    def test_update_product(self):
        init_db(self.conn)
        pid = add_product(self.conn, '旧名字', 100, 5, '旧类')
        update_product(self.conn, pid, name='新名字', price=80)
        p = get_product(self.conn, pid)
        assert p['name'] == '新名字'
        assert p['price'] == 80
        assert p['stock'] == 5   # 没改

    def test_delete_product(self):
        init_db(self.conn)
        pid = add_product(self.conn, '待删除', 1, 1, 'X')
        rows = delete_product(self.conn, pid)
        assert rows == 1
        assert get_product(self.conn, pid) is None

class TestTransaction:
    @classmethod
    def setup_class(cls):
        cls.conn = get_conn()
        init_db(cls.conn)

    @classmethod
    def teardown_class(cls):
        cls.conn.close()

    def test_place_order_ok(self):
        init_db(self.conn)
        pid = add_product(self.conn, '可下单商品', 100, 10, '测试')
        oid = place_order(self.conn, 1, pid, 3)
        assert oid > 0

        p = get_product(self.conn, pid)
        assert p['stock'] == 7   # 10 - 3

    def test_place_order_not_enough(self):
        init_db(self.conn)
        pid = add_product(self.conn, '紧缺商品', 100, 2, '测试')
        # pytest 6.2+
        with pytest.raises(Exception):
            place_order(self.conn, 1, pid, 10)

        p = get_product(self.conn, pid)
        assert p['stock'] == 2   # 没变

    def test_place_order_not_exist(self):
        init_db(self.conn)
        with pytest.raises(Exception):
            place_order(self.conn, 1, 99999, 1)

class Database:
    def __init__(self, **config):
        self.config = config
        self.conn = None

    def open(self):
        if self.conn is None:
            self.conn = pymysql.connect(
                cursorclass=DictCursor, autocommit=False, **self.config
            )

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def run(self, sql, params=None):
        self.open()
        with self.conn.cursor() as c:
            rows = c.execute(sql, params or ())
        self.conn.commit()
        return rows

    def one(self, sql, params=None):
        self.open()
        with self.conn.cursor() as c:
            c.execute(sql, params or ())
            return c.fetchone()

    def all(self, sql, params=None):
        self.open()
        with self.conn.cursor() as c:
            c.execute(sql, params or ())
            return c.fetchall()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()


class TestDatabase:
    DB_CONFIG = dict(
        host='localhost', user='root', password='root66',
        database='student_db', charset='utf8mb4',
    )

    def test_context_manager(self):
        with Database(**self.DB_CONFIG) as db:
            db.run("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    price DECIMAL(10,2),
                    stock INT DEFAULT 0,
                    category VARCHAR(50)
                )
            """)
            db.run("DELETE FROM products")
            db.run(
                "INSERT INTO products (name, price, stock, category) VALUES (%s, %s, %s, %s)",
                ('书', 50, 10, '书籍'),
            )
            row = db.one("SELECT * FROM products WHERE name = %s", ('书',))
            assert row['price'] == 50

    def test_context_manager_auto_close(self):
        with Database(**self.DB_CONFIG) as db:
            db.run("SELECT 1")
        assert db.conn is None
