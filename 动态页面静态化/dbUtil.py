import pymysql

'''#债转
SELECT 
  AssignmentId , CEIL(COUNT(1) / 10) cnt
FROM
  mbm_repaymentplan r 
WHERE r.IsValid = 1 
 AND r.principal > 0 
 AND datatype = 1
   AND r.AssignmentId IS NOT NULL
GROUP BY   AssignmentId  DESC

#普通标的
SELECT mb.creditId , CEIL(COUNT(1) / 10) cnt
FROM mbm_bid mb , mbm_credit mc 
WHERE mb.creditId = mc.id AND mc.creditstatus IN (5,6) AND mb.isvalid = 1 AND mb.datatype = 1  
GROUP BY mb.creditId  
'''



try:
    #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='ibd_loc',port=3306,charset='utf8')
    cur=conn.cursor()#获取一个游标
    cur.execute('select * from uc_god where id < 10')
    data=cur.fetchall()
    for d in data :
        #注意int类型需要使用str函数转义
        print(d[4])
    cur.close()#关闭游标
    conn.close()#释放数据库资源
except  Exception as msg :
    print(msg)
    print("查询失败")