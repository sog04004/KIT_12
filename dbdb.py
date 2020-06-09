import sqlite3

def dbcon():
    return sqlite3.connect('mydb.db')

def create_table():
    try:
        query = '''
            CREATE TABLE "users" (
                "id"    INTEGER NOT NULL,
                "name"  varchar(50) NOT NULL,
                "pw"    varchar(50) NOT NULL,
                PRIMARY KEY("id")
            )
        '''
        db = dbcon()
        c = db.cursor()
        c.execute(query)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(id, pw):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute("INSERT INTO users (name, pw) VALUES (?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM users')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def select_id(id):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id,)
        c.execute('SELECT * FROM users WHERE name = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def get_pw(id):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id,)
        c.execute('SELECT pw FROM users WHERE name = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret[0]