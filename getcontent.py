import requests
import json
import pymysql
import time

class lagou():
    conn = None
    cursor = None
    str2 = ""

    '''
    @:param  type String 要查询的招聘信息类型
    @:param  page int 页码
    '''
    def __init__(self):
        pass
    def send(self,type,page):
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
        # self.cookie = 'JSESSIONID=ABAAABAAAIAACBIF10F9F5095E3996B1D4E430221D2EDAB; _ga=GA1.2.869400212.1516417544; _gid=GA1.2.1728642938.1516417544; user_trace_token=20180120110544-ce0e2328-fd8e-11e7-af46-525400f775ce; LGSID=20180120110544-ce0e27e7-fd8e-11e7-af46-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7Ghk60yUKm0FNkUs00_hFp00000PW4pNb00000X4yzGW.THL0oUhY1x60UWdBmy-bIfK15ynknHnsmWfznj0snH0LP1T0IHYvPHcvnHbdP1KDrDn3fRDzwjTzrRR3wDNAfRFAwbf3rfK95gTqFhdWpyfqn101n1csPHnsPausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYE5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5HfLPHDs%26tpl%3Dtpl_10085_15730_11224%26l%3D1500117464%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m6c247d9c%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D220%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn%26inputT%3D5874; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20180120110544-ce0e29fc-fd8e-11e7-af46-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516417544,1516418100; X_HTTP_TOKEN=2b1e88ba7290682bd9f3f53173109489; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=10; gate_login_token=""; _putrc=BC07111EBF1A084F; login=true; unick=%E7%A8%8B%E9%BE%99%E9%A3%9E; gate_login_token=93fe752fe14fc6ca06f9601442bbec2628ea9bbb40b3b9b0; _gat=1; TG-TRACK-CODE=index_hotsearch; SEARCH_ID=e2e7ae3c77344e9690ffababb0aafd4a; LGRID=20180120111914-b14e6906-fd90-11e7-a55b-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516418355'
        # self.cookies = {i.split("=")[0]: i.split("=")[-1] for i in self.cookie.split("; ")}

        # 爬取拉钩招聘网 必须要将header请求信息补全
        self.header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=ABAAABAAAIAACBIF10F9F5095E3996B1D4E430221D2EDAB; _ga=GA1.2.869400212.1516417544; _gid=GA1.2.1728642938.1516417544; user_trace_token=20180120110544-ce0e2328-fd8e-11e7-af46-525400f775ce; LGSID=20180120110544-ce0e27e7-fd8e-11e7-af46-525400f775ce; LGUID=20180120110544-ce0e29fc-fd8e-11e7-af46-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516417544,1516418100; X_HTTP_TOKEN=2b1e88ba7290682bd9f3f53173109489; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=10; gate_login_token=""; gate_login_token=93fe752fe14fc6ca06f9601442bbec2628ea9bbb40b3b9b0; login=false; unick=""; _putrc=""; _gat=1; TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516421262; LGRID=20180120120741-75d7a5aa-fd97-11e7-a55b-5254005c3644; SEARCH_ID=f5e11f58f686456f9d8698df74935267',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_{}'.format(type),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.data = {
            'first': 'false',
            'pn': page,
            'kd': type.lower()
        }
        self.type = type
        self.page = page
    def mysql_conn(self):

        self.conn = pymysql.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "root",
            db = "lagou",
            charset = "utf8"
        )
        try:
            self.cursor = self.conn.cursor()
        except Exception:
            print("数据库连接失败！")
            exit()

    def getlist(self):
        sql = "SHOW COLUMNS FROM data"
        self.cursor.execute(sql)
        str1 = ""
        for i in  self.cursor.fetchall():
            if i[0] != 'id':
                str1 += i[0] + ','
        str1 = str1.strip(',')
        return str1

    def senddta(self,str2):
        sql = "INSERT INTO data({}) VALUES{}".format(self.getlist(), str2.strip(','))

        num = self.cursor.execute(sql)
        if num:
            print("入库成功,用时{}".format(time.time() - start))
        lagou_obj.close()

    def main(self):

        re = requests.post(self.url,headers=self.header,data=self.data)
        data = json.loads(re.content.decode())
        #提取关键招聘信息
        data = data['content']['positionResult']['result']
        if data :
            print("第{}页的数据获取完成".format(self.page+1))
        else :
            lagou_obj.senddta(self.str2)
            exit("关于{}的数据获取完成".format(self.type))
        sqlstr = sqlstr1=""

        for da in data:
            sqlstr1=''
            sqlstr += '('
            sqlstr1 += "'"+self.type+"',"
            sqlstr1 += "'"+str(da['companyId'])+"',"
            sqlstr1 += "'" + str(da['workYear']) + "',"
            sqlstr1 += "'" + str(da['education']) + "',"
            sqlstr1 += "'" + str(da['jobNature']) + "',"
            sqlstr1 += "'" + str(da['positionName']) + "',"
            sqlstr1 += "'" + str(da['financeStage']) + "',"
            sqlstr1 += "'" + str(da['companyLogo']) + "',"
            sqlstr1 += "'" + str(da['industryField']) + "',"
            sqlstr1 += "'" + str(da['city']) + "',"
            sqlstr1 += "'" + str(da['salary']) + "',"
            sqlstr1 += "'" + str(da['positionAdvantage']) + "',"
            sqlstr1 += "'" + str(da['companyShortName']) + "',"
            sqlstr1 += "'" + str(da['district']) + "',"
            sqlstr1 += "'" + str(da['createTime']) + "',"
            sqlstr1 += '"' + str(da['companyLabelList']) + '",'
            sqlstr1 += "'" + str(da['companySize']) + "',"
            sqlstr1 += "'" + str(da['companyFullName']) + "',"
            sqlstr += sqlstr1.strip(",")
            sqlstr += "),"

        self.str2 += sqlstr
        return sqlstr;


    def close(self):
        # 关闭资源
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    start = time.time()
    lagou_obj = lagou()
    lagou_obj.mysql_conn()
    str2 = "";

    for i in range(1,100):  # JAVA 329  php 303 C 270  python 97  Android 292 .net 130 c# 46  node.js go asp
        try:
            lagou_obj.send("U3D",i) #  C++ 100 -125   C#
            str2 += lagou_obj.main()

        except Exception :
            print("出错了")
            lagou_obj.send("c#", i)  # C++ 100 -125   C#
            lagou_obj.main()
lagou_obj.senddta(str2)




