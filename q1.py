print("enter string")
a = str(input())
s = len(a)
def arjun(x,y):
    count = 0
    c = 0
   
    for i in range(y):
        if(x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u'):
            count = count + 1
        else:
            c = c + 1
    count = str(count)
    c = str(c)
   
    return count + "," + c
print("number of vowels and consonants:")
arjun(a,s)