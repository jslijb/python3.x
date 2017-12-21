# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def openSite(url,id,totalPages):
    #driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()
    print("1=====")
    driver.get(url)
    print("2====")
    element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[12]/dl/dd/div/table/tbody/tr[1]/td[1]')))
    print("3====")
    data = driver.page_source
    print("4====")
    #time.sleep(5)
    print(data)

    tmpFile = 'data/html/tmp.html-' + str(id)
    txtFile = open(tmpFile, 'w',encoding='utf-8')
    txtFile.writelines(data)

    outputFileName = 'data/html/creditInfo-' + str(id) + '.html'
    newFile = open(outputFileName, 'w',encoding='utf-8')
    file_object = open(tmpFile, 'r',encoding='utf-8')

    try:
        for line in file_object:
            if line.strip() == '<script language="javascript">':
                break
            newFile.writelines(line)
    finally:
        file_object.close()
        newFile.close()

    driver.close()

    return driver

def appendFile(target,id,totalPages):

    try:
        sourceFile = open('data/paging_credit_script.txt', 'r',encoding='utf-8')
        targetFile = open(target, 'a', encoding='utf-8')

        for line in sourceFile:
            temp = line
            if '#totalPages#' in line.strip():
                temp = line.replace('#totalPages#',str(totalPages))

            if '#CPID#' in line.strip():
                temp = line.replace('#CPID#', 'creditInfo-'+str(id))

            targetFile.writelines(temp)


    except Exception as msg:
        print(msg)

    finally:
        sourceFile.close()
        targetFile.close()


def createHtml(baseUrl, dataFile):

    sourceFile = open(dataFile, 'r')

    count = 20752
    for line in sourceFile:
        print('开始处理:%s' %line)
        line = line.strip('\n')
        print('line',line)
        id = line.split(',')[0]
        totalPages = line.split(',')[1]
        url = baseUrl+str(id)
        print("url:",url)
        print("start call openSite function")
        openSite(url,id,totalPages)
        print("call openSite function sucess")
        print("start call appendFile function")
        appendFile('data/html/creditInfo-'+ str(id) + '.html', id, totalPages)
        print("call appendFine function sucess")

        count -= 1
        print('还未处理的：%d' %count)


if __name__ == '__main__':
   '''
    url = 'http://localhost:8080/portal/invest/creditInfo.action?creditId=19815'
    openSite(url)
    appendFile('paging_script.txt', 'creditInfo-19815-2.html', 1000)
    '''
   baseUrl = 'http://www.ibdp2p.com/invest/creditInfo.action?creditId='
   print("start call createHtml function")
   createHtml(baseUrl,'data/credit-info-1.txt')
   print("call createHtml function success")
