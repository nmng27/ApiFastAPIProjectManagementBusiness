import oracledb
def connect_db():
    try:
        DATABASE_URL = ""
        conn = oracledb.connect(DATABASE_URL)
        return conn
    except Exception as e:
        raise e
