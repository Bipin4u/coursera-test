'''
jack and jill were passing through the jungle on there way . they encountered a monster who told they 
will be allowed to escape when solve a puzzle for him .
given N number of empty bucket . olny below mentioned operation are allowed to add frout
1 double the count of the frout 
2 increment individual bucket by one
3 we cannot remove or decrease number of frout in a bucket

example
input array: [2,3[
output 4

input array: [16,16,16]
output 7

'''
import re
test=list()
count=0
x=input("give the array")
xy=re.findall("[0-9]+",x)
for i in range(len(xy)):
    xy[i]=int(xy[i])
for i in xy:
    test.append(0)
if(min(xy)>0):

    for i in range(len(test)):
        test[i]=1
        count=count+1

while min(xy)>=(max(test)*2):
    for i in range(len(test)):
        test[i]=test[i]*2
    count=count+1

while xy!=test:
    if max(test)<min(xy):
        for i in range(len(test)):
            test[i]=test[i]+1
        count=count+1
    else:
        for i in range(len(test)):
            if xy[i]>test[i]:
                test[i]=test[i]+1
                count=count+1
print(count)
