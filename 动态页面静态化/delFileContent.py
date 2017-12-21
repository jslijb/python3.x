import os


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    cnt = 0
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        try:
            newFile = open('E:/project/python_prj/ibd/data/html/rightInfo2/%s' %allDir ,'w', encoding='utf-8')
            with open(child,'r',encoding='utf-8') as source_file:
                for line in source_file:
                    if('<div id="page" class="paging">' not in line.strip()):
                        newFile.writelines(line)
                    else:
                        newFile.writelines('                    <div id="page" class="paging"></div>')
        except Exception as msg:
            print(msg)
        finally:
            newFile.close()
            source_file.close()
        cnt += 1
        print('已处理了%d' %cnt)

if __name__ == '__main__':

    filePathC = "E:/project/python_prj/ibd/data/html/rightInfo"
    eachFile(filePathC)
