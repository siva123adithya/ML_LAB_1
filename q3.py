list1 = []
list2 = []

a = int(input("enter number of elements in list1:"))
b = int(input("enter number of elements in list2:"))

for i in range(a):
    list1.insert(i, int(input()))
for i in range(b):
    list2.insert(i, int(input()))

def matching(l1, l2, x, y):
    count = 0
    for i in range(x):
        for j in range(y):
            if(l1[i] == l2[j]):
                count = count + 1
   
    return count

matching(list1,list2,a,b)


