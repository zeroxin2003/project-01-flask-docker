import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    """连接 PostgreSQL 数据库"""
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        dbname=os.environ.get("DB_NAME", "devops_db"),
        user=os.environ.get("DB_USER", "devops"),
        password=os.environ.get("DB_PASSWORD", "secret123"),
    )
    return conn

def init_db():
    """创建访问记录表（如果不存在）"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            count INTEGER NOT NULL DEFAULT 0
        )
    """)
    # 确保至少有一条记录
    cur.execute("SELECT COUNT(*) FROM visits")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO visits (count) VALUES (0)")
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    """首页：记录访问次数并显示"""
    try:
        init_db()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE visits SET count = count + 1 WHERE id = 1")
        conn.commit()
        cur.execute("SELECT count FROM visits WHERE id = 1")
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f"""
        <html>
        <head><title>DevOps Project - Live on VPS!</title></head>
        <body style="font-family: Arial; max-width: 600px; margin: 80px auto; text-align: center;">
            <h1>🚀 Flask + PostgreSQL + Docker Compose</h1>
            <p>This page has been visited <strong>{count}</strong> time(s).</p>
            <p>Refresh the page to increment the counter.</p>
            <hr>
            <p style="color: gray;">Data is stored in PostgreSQL — survives container restart</p>
        </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
        <body style="font-family: Arial; max-width: 600px; margin: 80px auto; text-align: center;">
            <h1>⚠️ Database not ready</h1>
            <p>Waiting for PostgreSQL to start...</p>
            <p style="color: gray;">Error: {e}</p>
            <p>Please refresh the page in a few seconds.</p>
        </body>
        </html>
        """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
