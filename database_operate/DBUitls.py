# coding=utf-8
import pymysql
import traceback
from commen.config import ip, port, user, data_password, database


def insert_delete_update(sql):
    cur = None
    conn = None
    try:
        conn = pymysql.Connect(host=ip, user=user, password=data_password, database=database, charset='UTF8')
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except:
        print(traceback.format_exc())
    finally:
        try:
            if cur:
                cur.close()
        except:
            print('运行错误')
        finally:
            if conn:
                conn.close()


def select(sql):
    cur = None
    conn = None
    try:
        conn = pymysql.Connect(host=ip, user=user, password=data_password, database=database, charset='UTF8')
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchone()[0]
        print(data)
        return data

    except:
        print(traceback.format_exc())
    finally:
        try:
            if cur:
                cur.close()
        except:
            print('错误')
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    sql = """SELECT * FROM dam_dq_check """
    select(sql)
    # insert_delete_update('insert into student_llp values("0019","wang","yuwen",90);')
