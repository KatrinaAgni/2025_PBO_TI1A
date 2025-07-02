import sqlite3
import pandas as pd
from konfigurasi import DB_PATH

def execute_query(sql, params=None):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return None
    finally:
        conn.close()

def fetch_query(sql: str, params=None, fetch_all=True):
    import sqlite3
    from konfigurasi import DB_PATH

    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        return cursor.fetchall() if fetch_all else cursor.fetchone()
    except sqlite3.Error as e:
        print(f"SQLite Error (fetch_query): {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_dataframe(sql: str, params: tuple = None):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        df = pd.read_sql_query(sql, conn, params=params)
        return df
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return None
    finally:
        if conn:
            conn.close()
