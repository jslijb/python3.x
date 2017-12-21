l1 = [3,2,1,9,6,7,5,8,4,0,3,10,23,2]
# def tosum(a,tag):
#     i = 0
#     while i < len(a):
#         sum = a[i]
#         j = i + 1
#         while j < len(a):
#             sum = sum + a[j]
#             if sum == tag:
#                 print (i,j)
#             sum = a[i]
#             j += 1
#         i += 1
#
# tosum(l1,5)

def two_sum(data_set,tag):
    i = 0
    while i < len(data_set):
        j = i + 1
        while j < len(data_set):
            if data_set[i] + data_set[j] == tag:
                print(i,j)
            j += 1
        i = i + 1

print(l1)
two_sum(l1,5)
