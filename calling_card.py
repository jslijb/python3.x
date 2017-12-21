# # -*- coding:utf-8 -*-
# '''名片管理系统'''
import sys

card_dict = {}


def print_card_menu():
    print('1:input card info')
    print("2:pass")
    print('3:pass')
    print("4:select one card's info")
    print('5:print all cards info')


def save_card(card_info_list, i):
    card_dict[str(i)] = card_info_list


def print_card_info(key):
    print('\t\t'.join(card_dict[key]))

def card_info_input(object):
    '''输入名片上的个项目如果名字，qq，微信，电话号码等'''
    prompt_message = "please input" + " " + object + ":"
    object = input(prompt_message)
    return object


def get_card_info():
    '''获取名字，qq，微信，电话号码'''
    name = card_info_input('name')
    check_card_info(name,'name','length', 20)
    qq = card_info_input('qq')
    check_card_info(qq,'qq','length', 9)
    weixin = card_info_input('weixin')
    check_card_info(weixin,'weixin','length', 10)
    telphone_code = card_info_input('telphone_code')
    check_card_info(telphone_code,'name','telphone_code', 11)
    return [name,qq,weixin,telphone_code]


def check_card_info(object_data,object, check_type, object_len):
    '''
    检查输入的数据是否合法，包括长度，数据类型，以及各项目的规则，如电话号码
    object_data 代表输入的名字/qq/微信/电话号码
    obje 代表name,qq,weixin,telphone
    check_type:length/[0-9]/str 等
    object_len:name,qq,weixin,telphone 这些项目的最大长度
    '''
    if check_type == 'length':
        if len(object_data) > object_len:
            i = 0
            while i < 2:
                print(object+"'s maximum length is:", object_len, "please reinput")
                print("The maximum number of input errors is 3 times")
                print("After 3 consecutive errors, the program will exit")
                i = i + 1
                object_new_len = call_card_info(object)
                # print('object_len:',object_len)
                if object_new_len < object_len:
                    print("input", object, "success")
                    break
            else:
                print("The number of errors inputted to the maximum")
                sys.exit('1')
        elif len(object_data) == 0:
            print(object,"length is not null,please reinput")
            call_card_info(object)
        else:
            print("input", object, "success")

    elif check_type == 'data_type':
        pass
    elif check_type == 'unique':
        pass


def call_card_info(object):
    object = card_info_input(object)
    # print(object)
    # print(len(object))
    return len(object)

def main():
    print_card_menu()
    i = 0
    while True:
        item = int(input("please input item: "))
        if item == 1:
            card_info_list = get_card_info()
            save_card(card_info_list, i)
            i = i + 1
            print(card_dict)
            continue
        elif item == 2:
            pass
        elif item == 3:
            pass
        elif item == 4:
            pass
        elif item == 5:
            for key in card_dict:
                print_card_info(key)
            break
        else:
            break


main()


