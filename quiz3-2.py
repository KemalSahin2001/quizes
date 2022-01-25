import sys
inptlist = sys.argv[1].split(",")
lst = [int(inptlist[i]) for i in range(len(inptlist)) if int(inptlist[i]) > 0]
stlst = set(lst)
lst = list(stlst)
lst.sort()
for i in lst:
    if i == 1:
        temp = i
        for j in range(len(lst)):
            try: 
                lst.pop(i)
                i += temp
            except : break
    else:
        i -= 1
        temp = i
        for j in range(len(lst)):
            try: 
                lst.pop(i)
                i += temp
            except : break
for i in lst: print(i,end=" ")




        



    


