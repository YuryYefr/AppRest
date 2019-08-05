import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_table(conn, project):
    sql = ''' INSERT INTO Rest_table(col1, col2, col3, col4, col5, col6, col7, col8, col9, col10)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return project


def update_task(conn, task):
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
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Rest_table WHERE id = 1")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    return rows
