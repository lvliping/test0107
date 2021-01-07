# coding=utf-8
import pymysql
import traceback

ip = "10.168.74.181"
user = "root"
password = "root1234"
database = "kun_dam"

# ip = "192.168.0.131"
# user = "root"
# password = "bmsoft@123"
# database = "kun_dam"

def insert_delete_update(sql):
    cur = None
    conn = None
    try:
        conn = pymysql.Connect(host=ip, user=user, password=password, database=database, charset='UTF8')
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
        conn = pymysql.Connect(host=ip, user=user, password=password, database=database, charset='UTF8')
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        # print(data)
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
def update_data():
    sql1 = """SELECT view_name,topic_code,topic_full_code from dp_dev_physic_view_bak"""
    view_data = select(sql1)
    for view_data1 in view_data:
        print(view_data1)
        sql2 = """SELECT view_name from dp_dev_physic_view"""
        view_name = select(sql2)
        for name in view_name:
            if name == view_data1[0]:
                sql = """inset into dp_dev_physic_view(topic_code,topic_full_code) values(view_data1[1],view_data1[2])"""
                insert_delete_update(sql)
                break
if __name__ == '__main__':
    update_data()