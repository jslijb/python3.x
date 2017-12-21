#!/usr/local/python3/bin/python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import codecs

def openSite(url,id,totalPages):
    #driver = webdriver.Chrome()
    driver = webdriver.PhantomJS(executable_path='/usr/local/phantomjs/bin/phantomjs')
    driver.get(url)

    data = ''
    try:
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="bidlt"]/ul/li[1]')))
    finally:
        data = driver.page_source
        driver.quit()

    #time.sleep(5)
    #print(data)

    tmpFile = 'data/html/tmp.html-' + str(id)
    txtFile = codecs.open(tmpFile, 'w',encoding='utf-8')
    txtFile.writelines(data)

    outputFileName = 'data/html/rightInfo-' + str(id) + '.html'
    newFile = codecs.open(outputFileName, 'w',encoding='utf-8')
    file_object = codecs.open(tmpFile, 'r',encoding='utf-8')

    try:
        for line in file_object:
            if line.strip() == '<script language="javascript">':
                break
            newFile.writelines(line)
    finally:
        file_object.close()
        newFile.close()

def appendFile(target,id,totalPages):

    sourceFile = codecs.open('data/paging_right_script.txt', 'r',encoding='utf-8')
    targetFile = codecs.open(target, 'a', encoding='utf-8')
    try:
        for line in sourceFile:
            temp = line
            if '#totalPages#' in line.strip():
                temp = line.replace('#totalPages#',str(totalPages))

            if '#CPID#' in line.strip():
                temp = line.replace('#CPID#', 'rightInfo-'+str(id))

            targetFile.writelines(temp)


    except Exception as msg:
        print(msg)

    finally:
        sourceFile.close()
        targetFile.close()


def createHtml(baseUrl, dataFile):

    sourceFile = codecs.open(dataFile, 'r')

    count = 40497
    for line in sourceFile:
        print('开始处理:%s' %line)
        line = line.strip('\n')
        id = line.split(',')[0]
        totalPages = line.split(',')[1]
        url = baseUrl+str(id)
        openSite(url,id,totalPages)
        appendFile('data/html/rightInfo-'+ str(id) + '.html', id, totalPages)

        count -= 1
        print('还未处理的：%d' %count)


if __name__ == '__main__':
   '''
    url = 'http://localhost:8080/portal/invest/creditInfo.action?creditId=19815'
    openSite(url)
    appendFile('paging_script.txt', 'creditInfo-19815-2.html', 1000)
    '''
   baseUrl = 'http://localhost:9080/invest/rightInfo.action?repaymentId='
   createHtml(baseUrl,'data/right-info.txt')
