#encoding=utf-8
import pymysql


class MysqldbHelper:
    def __init__(self):
        self.conn = object()

    def set_conn(self):
        # self.conn = pymysql.connect(host=h,port = pt,user = u,passwd =p,db = dbname)
        self.conn = pymysql.connect(host='192.168.4.134', port=3306, user='lzw', passwd='tca.iscas', db='domain_db',charset='utf8')

    def get_url(self):
        self.set_conn()
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        ## 或者这样写： cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute("select Domain_Name,Registrant_Name,Creation_Date from Domain_WhoisInfo limit 100")
        for r in cur.fetchall():
            print(r)
        self.conn.close()

if __name__ == "__main__":
    db = MysqldbHelper()
    ret = db.get_url()
    print ret


