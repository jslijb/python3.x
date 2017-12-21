#coding = utf-8
import time
import datetime
i = 1
start_time=datetime.datetime.now()
while i < 100:
    for j in range(1,i+1):
        print('%d%s%d%s%d' %(i,'x',j,'=',i*j),end='  ')
    print()
    i = i + 1
end_time=datetime.datetime.now()
# print("start_time:",start_time)
# print("end_time:",end_time)
print("The time used for this cycle:",(end_time - start_time).microseconds)


a = 1
b = 1
start_time1 = datetime.datetime.now()
while a < 100:
    while b <= a:
        print('%d%s%d%s%d' %(a,'x',b,'=',a*b),end='  ')
        b = b + 1
    print()
    a = a + 1
    b = 1
end_time1 = datetime.datetime.now()
#print()
print("The time used for this cycle1:",(end_time1 - start_time1).microseconds)