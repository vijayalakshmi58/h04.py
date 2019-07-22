# h04.py
num = int(input())
mylist = list(map(int,input().split()))
mydict = {}
anslist = []
for a in mylist:
    if a in mydict:
        mydict[a] += 1
    else:
        mydict[a] = 1
for a in mydict:
    if mydict[a]==1:
        anslist.append(a)
print(*anslist)
