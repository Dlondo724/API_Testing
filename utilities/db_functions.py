import sqlite3


def database_connection(path_to_db):
    """connects to the sqlite database and returns the connection"""
    return sqlite3.connect(path_to_db)


def database_execution(cursor_object, sql_statement):
    return cursor_object.execute(sql_statement)


def database_results_fetch_one(db_response):
    return db_response.fetchone()
