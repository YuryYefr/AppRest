import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Connecting db"""
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    """Creating blank table"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_table(conn, project):
    """Use this to read/write"""
    sql = ''' INSERT OR IGNORE INTO Rest_table(col1, col2, col3, col4, col5, col6, col7, col8, col9, col10)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return project


def update_table(conn, task):
    """Updating table from client"""
    sql = ''' UPDATE Rest_table
              SET col1 = ?,
                    col2 = ?,
                    col3 = ?,
                    col4 = ?,
                    col5 = ?,
                    col6 = ?,
                    col7 = ?,
                    col8 = ?,
                    col9 = ?,
                    col10 = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return task


def select_all_cells(conn):
    """To create client table"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM Rest_table WHERE id = 1")
    rows = cur.fetchall()
    return rows
