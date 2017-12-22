# coding = utf-8
from selenium import webdriver
import time
import  sys
import os
import mysql.connector
from my_python_lib import check_intel_ip
dr = webdriver.Chrome()
ecs_dict = {"sit": "i-94mvzolmz",
            "prd-1": "i-947f0upfu",
            "prd-2": "i-wz989icjinv8p9qnc8hb",
            "app-1": "i-94brane02",
            "app-2": "i-wz90egdlk9bxnw9rvsbh",
            "mbm": "i-94xch77yo",
            "core": "i-wz9fvttmu9vkeoz6gq81",
            "redis-1": "i-wz9hjd0n86ozyilxmri6",
            "商城-mbm": "i-wz9hftd4ce4kkmg0clf3",
            "商城-prd": 'i-wz93tjc72c6dkunlp20r',
            "svn":"i-94hbuio1n"
            }
secritygroup_dict = {}
secritygroup_ecs_dict = {}
'''secritygroup_dict = {
                    "prd-noddos-slb":"sg-wz98zb5wrh2ftbv8gf4n",
                     "prd-ddos-noslb":"sg-wz9g26ywqnwynxp2kglf",
                     "mbm-noslb":"sg-wz9blswgio3fldycwoei",
                     "商城专用":"sg-wz91wy2vjnk1md1spunm",
                     "app-slb":"sg-wz91bdeo0a0uniapsxyx",
                     "prd-slb":"sg-wz9hodl26qzqc7g3tsu7",
                     "sit知道创宇":"sg-wz9crgwctusssbi2u2vi",
                     "app知道创宇":"sg-wz9ajblutoh1v95nyr21",
                     "堡垒机":"sg-wz97mv2u6nt9c5il4xa8",
                     "prd-noddos-noslb":"sg-wz91gwksm4g0ktfkf0lq",
                     "mbm-slb":"sg-wz9d7ekjashm7wp5nwh4",
                     "sit":"sg-wz920gz8zjy8o0b311y4",
                     "系统默认":"sg-94txr288n",
                     "test2":"sg-wz9embug0xbcvdtdy0pq",
                     "test1":"sg-wz9dverxkchck6jt3mhu"
                     }'''

'''secritygroup_ecs_dict = {
                            "app知道创宇":"app-1,app-2",
                            "sit知道创宇":'sit',
                            "prd-slb":"prd-1,prd-2",
                            "商城专用":"商城-prd,商城-mbm"
                        }'''

ecs_secritygroup_dict = {}

def check_ecs_exist(ecs_name):
    '''检查ecs实例是否存在，如果存在返回1，如果不存在返回0'''
    if ecs_name.lower() in ecs_dict.keys():
        return 1
    else:
        print("输入的ecs别名不存在，请重新输入")
        return 0

def check_secritygroup_exist(secritygroup_name):
    '''
        这个函数的功能是判断安全组是否已存在
        返回1 表示存在，返回0表示不存在
     '''
    conn = conn_mysql()
    cursor = conn.cursor()
    # sql 语句是判断此secritygroup_name 是否存在如果存在就返回[(1,)] 这个列表，如果不存在就返回[(0,)] 这个列表
    cursor.execute('select COUNT(1) from secritygroup WHERE secritygroup_name = %s',(secritygroup_name,))
    values = cursor.fetchall()
    # print("values",values)
    if values == [(1,)]:
        return 1
    else:
        return 0

def check_secritygroup_exist_ecs(ecs_name,secritygroup_name):
    '''检查某个ECS是否属于某个安全组，如果属于就返回1，不属于就返回0'''

    conn = conn_mysql()
    cursor = conn.cursor()
    cursor.execute("select secritygroup_new_name from ecs WHERE  ecs_name = %s",(ecs_name,))
    values = cursor.fetchall()
    if ''.join(values.pop()) == secritygroup_name:
        return 1
    else:
        return 0

def print_enmu():
    print("请根据提示输入1-7这几个数，此程序只能手动结束")
    print("1:创建安全组")
    print("2:配置安全组规则，内网规则")
    print("3:配置安全组规则，外网规则")
    print("4:将ECS实例加入安全组中")
    print("5:删除安全组")
    print("6：退出程序")

def open_aly_index():
    '''登录阿里云控制台首页'''
    dr.get("https://signin.aliyun.com/ibd/login.htm")
    dr.find_element_by_id("user_principal_name").clear()
    dr.find_element_by_id("user_principal_name").send_keys("ibd_devops@ibd")
    time.sleep(1)
    dr.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/div[2]/span").click()
    time.sleep(1)
    dr.find_element_by_id("password_ims").clear()
    dr.find_element_by_id("password_ims").send_keys("9NGnGzSnYiZivLqjgs2mKF#f")
    dr.find_element_by_xpath("/html/body/div[2]/div/form/div[4]/div[2]/div/input").click()

def open_secritygroup_index():
    '''打开安全组设置首页'''
    dr.get("https://ecs.console.aliyun.com/#/securityGroup/region/cn-shenzhen")

def get_init_secritygroup_id(secritygroup_name):
    '''获取新创建安全组的id'''
    open_secritygroup_index()
    # 选中搜索安全组的类型，这里要选中以"安全组名称"来搜索
    # dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[1]/select").click()
    #
    # dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[1]/select").send_keys(secritygroup_name)
    # dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[1]/select").click()
    secritygroup_id = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/table[1]/tbody/tr/td[2]/div/p[1]/span").text
    return  secritygroup_id

def get_old_secritygroup_id(secritygroup_name):
    '''获取已有安全组的id'''
    conn = conn_mysql()
    cursor = conn.cursor()
    cursor.execute('select secritygroup_id from secritygroup WHERE secritygroup_name = %s',(secritygroup_name,))
    values = cursor.fetchall()
    secritygroup_id = ''.join(values.pop())
    return  secritygroup_id

"""
def check_secritygroup_exist(secritygroup_name):
    '''检查安全组是否已存在，存在返回1，不存在返回0'''
    # 打开创建安全组页面首页
    open_secritygroup_index()
    # 搜索类型为"安全组名称"
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[1]/select").send_keys("安全组名称")
    time.sleep(1)
    # 向搜索框里输入安全组的名称
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[2]/input").send_keys(secritygroup_name.lower())
    time.sleep(1)
    # 点击搜索按钮
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/button").click()
    time.sleep(1)
    try:
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[4]/div/div/span")
        # print("这个安全组：", secritygroup_name, "不存在,需要创建")
    except:
        # print("这个安全组：",secritygroup_name,"已存在,请勿重新创建")
        #安全组存在返回1，不能重复创建安全组
        return 1
    # 安全组不存在返回0 需要创建此安全组
    return 0
"""

"""
def check_ecs_exist_secritygroup(ecs_name,secritygroup_name):
    '''检查某个ecs 是否存在于某个安全组中，存在返回1，不存在返回0'''
    # 检查安全组id是否存在
    secritygroup_code = check_secritygroup_exist(secritygroup_name)
    ecs_code = check_ecs_exist(ecs_name)
    if secritygroup_code == 1 and ecs_code == 1:
        # 点击管理实例
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/table[1]/tbody/tr/td[9]/div/div/button[4]").click()
        time.sleep(1)
        # 向 ecs 实例搜索框中输入 ecs 别名
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/form/div[2]/input").send_keys(ecs_name)
        time.sleep(1)
        # 点击搜索按钮
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/form/button").click()
        time.sleep(1)
        try:
            #获取ecs 的名字
            result = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[4]/div/div/span").text
        except:
            #print(ecs_name, "不在", secritygroup_name, "这个安全组中")
            return 1
        else:
            print(ecs_name,"不在",secritygroup_name,"这个安全组中")
            return 0
    else:
        print("所输入的ecs或者安全组不存在，请重新输入")
        input_item()
"""
def check_secritygroup_name():
    '''检查secritygroup_name 输入的值是否合法
    要以字母开头，长度在2-128个字符，这里一个汉字算1个字符，1个标点符号算1个字符
    如果输入10 就跳转至最初始菜单页面
    '''

    secritygroup_name = input("请输入安全组的名字，以字母开头，长度在2-128个字符。注意1个汉字和一个标点符号都算一个字符。如需要回到初始菜单页面，请输入10：")
    code = check_secritygroup_exist(secritygroup_name)
    if secritygroup_name == '10':
        stat = 0
    elif not secritygroup_name[0].isalpha():
        print("安全组名称输入错误，要以字母开头，请重新输入")
        stat = 2
    elif not 2 <= len(secritygroup_name) <= 128:
        print("安全组名称的长度在2-128个字符，输入的长度不符合要求，请重新输入")
        stat = 3
    elif code == 1:
        print("此安全组已存在")
        stat = 4
    else:
        stat = 1
    return (secritygroup_name,stat)

def check_port():
    '''检查端口输入是否有效'''
    port = input("请输入端口号，端口号必须是纯数字，范围1-65535,如需要返回初始界面请输入10：")
    if port == '10':
        stat = 0
    elif not port.isnumeric():
        print("端口必须是纯数字，请重新输入")
        stat = 2
    elif not 1 <= int(port) <= 65535:
        print("端口号的范围1-65535，请重新输入")
        stat = 3
    else:
        port = port + '/' + port
        stat = 1
    return (port,stat)

def check_conf_desc():
    conf_desc = input("请输入规则描述信息\n长度2-256个字符，注意1个汉字和1个标点符号都算1个字符。\n不能以http或https开头.\n如果要回到初始输入界面请输入10： ")
    if conf_desc == '10':
        stat = 0
    elif not 2 <= len(conf_desc) <= 256:
        stat = 2
    elif conf_desc[0:4] == 'http':
        print("安全组描述信息不能以http开头")
        stat = 3
    elif conf_desc[0:5] == 'https':
        print("安全组描述信息不能以https开头")
        stat = 4
    else:
        stat = 1
    return (conf_desc,stat)

def check_secritygroup_discrbe():
    '''检查secritygroup_discrbe 输入的值是否合法
        长度在2-256个字符，这里一个汉字算1个字符，1个标点符号算1个字符
        不能以http或者https 开头
        如果输入10 就跳转至最初始菜单页面
    '''
    secritygroup_discrbe = input("请输入安全组的描述信息，长度在2-256个字符。注意1个汉字和一个标点符号都算一个字符，不能以http或者https开头。如需要回到初始菜单页面，请输入10：")
    if secritygroup_discrbe == '10':
        stat = 0
    elif not 2 <= len(secritygroup_discrbe) <= 256:
        stat = 2
    elif secritygroup_discrbe[0:4] == 'http':
        print("安全组描述信息不能以http开头")
        stat = 3
    elif secritygroup_discrbe[0:5] == 'https':
        print("安全组描述信息不能以https开头")
        stat = 4
    else:
        stat = 1
    return (secritygroup_discrbe,stat)

def check_ip():
    '''检查输入的ip地址是否符合要求'''
    ip = input("请输入公网的ip地址：")
    code = check_intel_ip(ip)
    if ip == '10':
        stat = 0
    elif code == 1:
        stat = 1
    else:
        stat = 2
    ip = ip + '/32'
    return (ip,stat)

def create_secritygroup(secritygroup_name,secritygroup_discrbe):
    '''创建安全组'''

    open_secritygroup_index()
    dr.refresh()
    # 点击"创建安全组"按钮
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/span[1]/a").click()
    time.sleep(1)
    # 输入安全组的名称
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/div[1]/div/input").send_keys(secritygroup_name)
    time.sleep(1)
    # 输入安全组的描述
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/div[2]/div/textarea").send_keys(secritygroup_discrbe)
    time.sleep(1)
    # 点击"确定" 按钮
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
    time.sleep(1)
    #  点击关闭，暂时不设置规则
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]").click()
    secritygroup_id = get_init_secritygroup_id(secritygroup_name)
    insert_secritygroup_table_mysql(secritygroup_id,secritygroup_name,secritygroup_discrbe)


def remove_secritygroup(secritygroup_name):
    '''删除安全组
    删除安全组的条件：
        1、安全组中没有任何的ECS实例
        2、安全组没有和任何安全组实施关联策略
    '''
    code = check_secritygroup_exist(secritygroup_name)
    if code == 1:
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/table[1]/tbody/tr/td[1]/input").click()
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/table[2]/tfoot/tr/td[2]/div[1]/div/div/button").click()
        dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
        del secritygroup_dict[secritygroup_name]
        print(secritygroup_dict)
    else:
        print(secritygroup_name,"这个安全组不存在")

def conf_secritygroup(secritygroup_name):
    open_secritygroup_index()
    dr.refresh()
    # 先选择合适的需要配置安全组
    secritygroup_id = get_old_secritygroup_id(secritygroup_name)
    # 向搜索框里输入安全组id
    dr.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[2]/input').send_keys(
        secritygroup_id)
    time.sleep(1)
    # 点击搜索按钮
    dr.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/button").click()
    time.sleep(1)

    # 点击"配置规则" 按钮
    dr.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/table[1]/tbody/tr/td[9]/div/div/button[5]").click()
    time.sleep(1)

def conf_secritygroup_intranet(secritygroup_name,secritygroup_grant_name,port,conf_discrbe):

    conf_secritygroup(secritygroup_name)
    #点击添加安全规则
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/button[3]").click()
    time.sleep(2)
    #输入端口号
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/div[5]/div[1]/input").send_keys(port)
    time.sleep(1)
    #点击授权对象的框
    dr.find_element_by_xpath('//*[@id="s2id_autogen1"]/a/span[1]').click()
    time.sleep(1)
    # 选择合适的安全组
    #dr.find_element_by_xpath("/html/body/div[9]/ul").click()

    secritygroup_grant_id = get_old_secritygroup_id(secritygroup_grant_name)
    dr.find_element_by_xpath('//*[@id="select2-drop"]/div/input').send_keys(secritygroup_grant_id)
    time.sleep(1)

    dr.find_element_by_xpath('/html/body/div[9]/ul').click()
    time.sleep(1)

    #输入配置描述信息
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/div[9]/div/textarea").send_keys(conf_discrbe)
    time.sleep(1)
    #点击确定按钮
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()


def conf_secritygroup_intel(secritygroup_name,port,ip,secritygroup_desc):
    conf_secritygroup(secritygroup_name)
    dr.refresh()
    # 选择公网入网方向
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/ul/li[3]/a").click()
    time.sleep(1)
    # 点击 添加安全组规则
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/button[3]").click()
    time.sleep(1)
    # 输入端口号
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/div[5]/div[1]/input").send_keys(port)
    time.sleep(1)
    # 输入ip 地址
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/div[8]/div[1]/textarea").send_keys(ip)
    time.sleep(1)
    # 输入规则描述信息
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/form/div[9]/div/textarea").send_keys(secritygroup_desc)
    time.sleep(1)
    # 点击确定按钮
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
    time.sleep(1)


def ecs_add_to_secritygroup (ecs_name,secritygroup_name):
    '''将某个ECS实例添加至某个安全组中'''
    # 先检查这个安全组中是否存在此ECS

    open_secritygroup_index()
    dr.refresh()
    secritygroup_id = get_old_secritygroup_id(secritygroup_name)
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[2]/input").send_keys(secritygroup_id)
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/button").click()
    time.sleep(1)
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/table[1]/tbody/tr/td[9]/div/div/button[4]").click()
    time.sleep(1)
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/button[2]").click()
    time.sleep(1)
    dr.find_element_by_xpath('//*[@id="s2id_autogen1"]/a/span[1]').click()
    time.sleep(1)
    dr.find_element_by_xpath('//*[@id="select2-drop"]/div/input').send_keys(ecs_dict[ecs_name])
    time.sleep(1)
    dr.find_element_by_xpath("/html/body/div[9]/ul").click()
    time.sleep(1)
    dr.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[1]').click()

    conn = conn_mysql()
    cursor = conn.cursor()
    cursor.execute('select secritygroup_new_name from ecs WHERE ecs_name = %s',(ecs_name,))
    result = cursor.fetchall()
    secritygroup_old_name = result[0][0]
    cursor.execute("update ecs set secritygroup_old_name=%s where ecs_name=%s", (secritygroup_old_name, ecs_name))
    cursor.execute("update ecs set secritygroup_new_name=%s where ecs_name=%s", (secritygroup_name,ecs_name))
    conn.commit()
    return secritygroup_old_name

def ecs_remvoe_from_secritygroup(ecs_name,secritygroup_name):
    '''将某个ECS实例从某个安全组中删除'''
    open_secritygroup_index()
    dr.refresh()
    secritygroup_id = get_old_secritygroup_id(secritygroup_name)
    # 向搜索框里输入安全组id
    dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/div[2]/input').send_keys(secritygroup_id)
    time.sleep(1)
    #点击搜索按钮
    dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/form/button').click()
    time.sleep(1)
    # 点击管理实例
    dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/table[1]/tbody/tr/td[9]/div/div/button[4]').click()
    time.sleep(1)
    # 输入 ecs 实例名称
    dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/form/div[2]/input').send_keys(ecs_name)
    time.sleep(1)
    # 勾选此 ecs 实例
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/table[1]/tbody/tr/td[1]/input").click()
    time.sleep(1)
    # 点击移除安全组按钮
    dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/table[2]/tfoot/tr/td[2]/div[1]/div/div/button").click()
    time.sleep(1)
    # 点击确定按钮
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()



def input_item():
    '''输入编号,实现具体的功能'''

    while True:
        print_enmu()
        try:
            item = int(input("请输入编号 1-6："))
        except:
            print("输入有误，请重新输入")
            input_item()
        else:
            if item == 1:
                secritygroup_name,name_stat = check_secritygroup_name()
                # print("name_stat: ",name_stat)
                if  name_stat != 1:
                    continue
                secritygroup_discrbe,discrbe_stat = check_secritygroup_discrbe()
                # print("discrbe_stat: ",discrbe_stat)
                if discrbe_stat != 1:
                    continue

                if name_stat ==1 and discrbe_stat == 1:
                    # print('name_stat: ',name_stat,'discrbe_stat: ',discrbe_stat)
                    create_secritygroup(secritygroup_name, secritygroup_discrbe)
                else:
                    continue

            elif item == 2:
                print("请注意第一次输入的安全组名称是待配置的安全组名称")
                print("请注意第二次输入的安全组名称是授权那个安全组访问上一个安全组")
                secritygroup_name, name_stat_2_1 = check_secritygroup_name()
                if  name_stat_2_1 != 4:
                    continue
                secritygroup_grant_name,name_stat_2_2 = check_secritygroup_name()
                if  name_stat_2_2 != 4:
                    continue
                port,port_stat = check_port()
                if port_stat != 1:
                    continue
                conf_discrbe,stat = check_conf_desc()
                if stat != 1:
                    continue
                conf_secritygroup_intranet(secritygroup_name,secritygroup_grant_name,port,conf_discrbe)

            elif item ==3:
                secritygroup_name_3,name_stat_3 = check_secritygroup_name()
                if name_stat_3 != 4:
                    continue
                port_3,port_stat_3 = check_port()
                if port_stat_3 != 1:
                    continue
                ip,ip_stat = check_ip()
                if ip_stat != 1:
                    continue
                conf_discrbe_3,discrbe_stat_3 = check_secritygroup_discrbe()
                if discrbe_stat_3 != 1:
                    continue

                conf_secritygroup_intel(secritygroup_name_3,port_3,ip,conf_discrbe_3)

            elif item ==4:
                secritygroup_name,name_stat_4 = check_secritygroup_name()
                if name_stat_4 != 4:
                    continue
                ecs_name = input("请输入ECS的别名：")
                ecs_stat = check_ecs_exist(ecs_name)
                if ecs_stat != 1:
                    continue
                secritygroup_exist_ecs_stat = check_secritygroup_exist_ecs(ecs_name,secritygroup_name)
                if secritygroup_exist_ecs_stat == 1:
                    continue
                else:
                    secritygroup_old_name = ecs_add_to_secritygroup(ecs_name,secritygroup_name)
                    ecs_remvoe_from_secritygroup(ecs_name,secritygroup_old_name)


            elif item ==5:
                pass
            elif item ==6:
                print("程序结束")
                sys.exit(1)

def conn_mysql():
    conn = mysql.connector.connect(user='ibd', password='tiIXSUYjR4tZAOnQ', database='secritygroup',host='120.24.154.123')
    return conn

def create_table_mysql():
    conn = conn_mysql()
    cursor = conn.cursor()
    #创建secritygroup 表
    cursor.execute('create table IF NOT EXISTS secritygroup (secritygroup_id char(25) primary key,secritygroup_name varchar(30) not null UNIQUE ,secritygroup_desc varchar(80) not null)')
    # 创建 ecs 表
    cursor.execute('create table IF NOT EXISTS ecs ( ecs_id char(25) primary key,ecs_name varchar(30) not null UNIQUE ,secritygroup_new_name varchar(30) not null UNIQUE,secritygroup_old_name varchar(30))')




def insert_secritygroup_table_mysql(secritygroup_id,secritygroup_name,secritygroup_desc):
    conn = conn_mysql()
    cursor = conn.cursor()
    # 向ecs 表中插入数据
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) value(%s,%s,%s)',
    #                ['i-wz9hjd0n86ozyilxmri6', 'redis-1', 'mbm-slb'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values (%s,%s,%s)',
    #                ['i-wz9fvttmu9vkeoz6gq81', 'core', 'mbm-slb'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values (%s,%s,%s)',
    #                ['i-94xch77yo', 'mbm', 'mbm-slb'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values(%s,%s,%s)',
    #                ['i-wz90egdlk9bxnw9rvsbh', 'app-2', 'app知道创宇'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values (%s,%s,%s)',
    #                ['i-94brane02', 'app-1', 'app知道创宇'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values (%s,%s,%s)',
    #                ['i-947f0upfu', 'prd-1', 'prd-slb0'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values (%s,%s,%s)',
    #                ['i-wz989icjinv8p9qnc8hb', 'prd-2', 'prd-slb0'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values (%s,%s,%s)',
    #                ['i-94mvzolmz', 'sit', 'sit知道创宇'])
    # cursor.execute('insert into ecs(ecs_id,ecs_name,secritygroup_name) values (%s,%s,%s)',
    #                ['i-94hbuio1n', 'svn', '系统默认'])
    #向secritygroup 中插入数据
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['sit-noddos','sg-wz920gz8zjy8o0b311y4','sit没有高防情况下的安全组配置'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['mbm-slb', 'sg-wz9d7ekjashm7wp5nwh4', '包含 3台ecs实例：mbm,core,redis。有内网slb的情况下'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['prd-noddos-noslb', 'sg-wz91gwksm4g0ktfkf0lq', '包含prd-1 和 prd-2 没有高防和slb'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['堡垒机', 'sg-wz97mv2u6nt9c5il4xa8', '堡垒机专用安全组'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['app知道创宇', 'sg-wz9ajblutoh1v95nyr21', '只允许知道创宇的IP地址访问sit的80和443端口'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['sit知道创宇', 'sg-wz9crgwctusssbi2u2vi', '只允许知道创宇的IP地址访问sit的80和443端口'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['prd-slb', 'sg-wz9hodl26qzqc7g3tsu7', 'prd-1，prd-2 共享一个安全组。授信阿里云 ntp ip访问123端口.授信mbm通过内网访问prd所有的端口'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['app-slb', 'sg-wz91bdeo0a0uniapsxyx', 'app和gateway 部署slb的安全组'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['商城专用', 'sg-wz91wy2vjnk1md1spunm', '商城的所有服务器暂时放入同一个安全组'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['mbm-noslb', 'sg-wz9blswgio3fldycwoei', '包含 3台ecs实例：mbm,core,redis。没有内网slb的情况下'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['prd-ddos-noslb', 'sg-wz9g26ywqnwynxp2kglf', '包含prd-1 和 prd-2 没有slb'])
    # cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
    #                ['prd-noddos-slb', 'sg-wz98zb5wrh2ftbv8gf4n', 'prd-1,prd-2 没有高防的情况有slb的情况'])

    cursor.execute('insert into secritygroup(secritygroup_name,secritygroup_id,secritygroup_desc) values (%s,%s,%s)',
                   [secritygroup_name, secritygroup_id, secritygroup_desc])
    #提交，如果不提交，表中将不会有数据
    conn.commit()



def main():
    open_aly_index()
    input_item()
    # code = create_secritygroup('test4','test4')
    # print(code)


main()
