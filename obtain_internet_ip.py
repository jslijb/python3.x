# -*- coding: utf-8 -*-
# 此脚本功能获得外网IP地址，并使用发送到指定的邮箱。放入Windows自动化计划，每天都会发送一次
import  socket
import  urllib,urllib.request
import  re
import  os
import subprocess
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
import time

#访问下面3个外网地址，可以获得外网的IP地址，如果3个外网地址都无法访问到，那就返回外网地址为0，可能存在本地网络故障
#http://whois.pconline.com.cn
#http://www.net.cn/static/customercare/yourip.asp
#http://www.net.cn/static/customercare/yourip.asp
class Get_public_ip:
    def getip(self):
        try:
            myip = self.visit("http://whois.pconline.com.cn")
        except :

            try:
                myip = self.visit("http://www.net.cn/static/customercare/yourip.asp")
            except:
                    try:
                        myip = self.visit("http://ip.chinaz.com/getip.aspx")
                    except:
                        myip = '0'
        return myip

    def visit(self,url):
        urler = urllib.parse.urlparse(url)
        if url == urler.geturl():
            opener = urllib.request.urlopen(url)  # 打开‘url’这个地址
            strg = opener.read() # 读取网站的内容
            strg = strg.decode('gbk') # 以中文编码显示
        #match 和 search 一旦匹配成功，就返回一个match object对象，有下列方法：
        #group() 返回被RE匹配的字符串  ipaddr.group() --> 116.30.217.125
        # group(m,n) 显示第m组合第n组，不是m--n 之间的所有的组
        #start() 返回匹配开始的位置  ipaddr.start() -->769
        # end() 返回匹配结束的位置 ipaddr.end() ---> 783
        # span() 返回一个元组包含匹配(开始,结束)的位置  ipaddr.span() --> (769, 783)
        #print(ipaddr) 输出 <_sre.SRE_Match object; span=(769, 783), match='116.30.217.125'>
        #\d+ 表示匹配至少一位数字[0-9]   \. 表示转义
        # match() 函数只有开始位置匹配成功才返回，如果不匹配就返回none，search() 扫描整个字符串去匹配
        #实例
        # s = 'abcdabcdrwabcser'
        # re.match("((abc)+)",s).group()  --> 'abc'
        # re.match("((abc)+)",s).group(1)  --> 'abc'
        # re.match("((abc)+)",s).group(2)  --> 'abc'
        # re.match("((abc)+)",s).group(0,1,2) --> ('abc','abc','abc')
        # ss = 'cdreabcderabcdse'
        # re.match('abc',s)   返回none
        # 只有开头有匹配的，才会去匹配后续的，如果开头没有匹配，即使后面有匹配的也不匹配
        #
        ipaddr = re.search("\d+\.\d+\.\d+\.\d+",strg).group()
        #search() 前面的r表示使用raw字符串，这样所有的特殊字符都表示原字面意思，不用使用\转义。
        #例如：\\  如果不是有r的话，需要转义，re.search('////',s) 如果使用re.search(r'//',s)
        location = re.search(r'(.*)市(.*)',strg).group()
        location = location.expandtabs(1)
        return ipaddr + location

localIP = socket.gethostbyname(socket.gethostname())
print("本机局域网ip地址：%s\n\n" %(localIP))

if __name__ == "__main__":
    getmyip = Get_public_ip()
    print("getmyip:",getmyip.getip())
    if getmyip.getip() == '0':
        print("your computer not network !")
    else:
        inter_ip = getmyip.getip()
def _format_addr(s):
    name ,addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr))

from_addr = 'jslijb@126.com'
password = 'lijiangbo'
to_addr = ['410387903@qq.com','282268414@qq.com']
to_addr2 = 'lijb@ibdp2p.cn'
smtp_server = 'smtp.126.com'

msg = MIMEText(inter_ip, 'plain', "utf-8")
print(msg)
# msg['From'] = _format_addr('李江波 <%s>' % from_addr)
# for addr in to_addr:
msg['From'] = from_addr
msg['To'] = ','.join(to_addr)
print("msg['To']: ",msg['To'])

msg['Subject'] = Header('办公室外网ip地址：','utf-8').encode()
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
time.sleep(3)
server.sendmail(from_addr,to_addr,msg.as_string())

time.sleep(3)
server.quit()