import pymysql

def add():
    db = pymysql.connect("localhost", "root", "Fan18610083440", "HMinfo")
    curosr = db.cursor()
    sql = """INSERT INTO HMinfo.hmtest(name, user_id, contribute) VALUES ('jhon',1234,'asdf')"""
    try:
        curosr.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


if __name__ == '__main__':
    add()