#-*- coding:utf-8 -*-
#calculate the location of words计算单词处于文件中的位置,
import string
import os
inputfile = open('C:\Users\ljb\Desktop\sharsh.txt','r')
outputfile = open('C:\Users\ljb\Desktop\hello.txt','w+')
lines = inputfile.readlines()
for line in lines:
    if line.strip() != '':
        outputfile.write(line)
inputfile.close()
lines1 = outputfile.readlines()
l1 = []
for line1 in lines1:
    for c in string.punctuation:
        line1 = line1.strip().replace(c,'')
    l1.append(line1.split())
i = 0
while i < len(l1):
    j = 0
    while j < len(l1[i]):
        if l1[i][j] == 'there':
            print i+1,j+1
        j += 1
    i += 1
'''i = 0
while i < len(lines):
    s = lines[i]
    for c in string.punctuation:
        s = s.strip().replace(c,'')
        l2 = s.split()
    #print l2
    l1.append(l2)
    i += 1'''
#print l1[0].index('there')
outputfile.close()

