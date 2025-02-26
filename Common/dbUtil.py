import psycopg2

class Database:
    def __init__(self, db_name):
        self.db_name=db_name
        self.connection=None

    def connect(self):
        self.connection=psycopg2.connect(self.db_name)

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        """执行查询"""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params or [])
        self.connection.commit()
        cursor.close()
        self.close()

    def fetch_all(self, query, params=None):
        """获取所有结果"""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params or [])
        results = cursor.fetchall()
        cursor.close()
        self.close()
        return results

    def fetch_one(self, query, params=None):
        """获取单个结果"""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params or [])
        result = cursor.fetchone()
        cursor.close()
        self.close()
        return result
