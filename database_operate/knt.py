# coding=utf-8
import pymysql
import traceback

# ip = "10.168.74.181"
# user = "root"
# password = "root1234"
# database = "kun_dam"

ip = "192.168.12.200"
user = "root"
password = "root1234"
database = "kun_dam"

def insert_delete_update(sql):
    cur = None
    conn = None
    print("insert_delete_update:", sql)
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
# def update_data():
#     sql1 = """SELECT tab_name,topic_code,topic_full_code from dp_dev_physic_tab_bak"""
#     tab_data = select(sql1)
#     sql2 = """SELECT tab_name from dp_dev_physic_tab"""
#     tab_name = select(sql2)
#     # print(tab_data, tab_name)
#     for tab_data1 in tab_data:
#         print(tab_data1, tab_name)
#         if (tab_data1[0],) in tab_name:
#             print(tab_data1[0])
#             "inset into dp_dev_physic_tab(topic_code,topic_full_code) values(tab_data1[1],tab_data1[2])"
#             sql = "update dp_dev_physic_tab set topic_code=\"{1}\",topic_full_code=\"{2}\" where tab_name=\"{0}\"".format(*tab_data1)
#             insert_delete_update(sql)

def update_data():
    sql1 = """SELECT tab_name,topic_code,topic_full_code from dp_dev_physic_tab_bak"""
    tab_data = select(sql1)
    sql2 = """SELECT tab_name from dp_dev_physic_tab"""
    tab_name = select(sql2)
    for tab_data1 in tab_data:
        print(tab_data1)
        for name in tab_name:
            if name[0] == tab_data1[0]:
                print(name[0])
                # sql = """inset into dp_dev_physic_tab("topic_code","topic_full_code") values("%s","%s") """ % (tab_data1[1], tab_data1[2])
                sql = """update dp_dev_physic_tab c set c.topic_code="%s",c.topic_full_code="%s" where c.tab_name="%s" """ % (tab_data1[1], tab_data1[2], name[0])
                insert_delete_update(sql)


if __name__ == '__main__':
    update_data()