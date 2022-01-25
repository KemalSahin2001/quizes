def normalyear(a):
    if(a % 4 == 0):
        return True 
    else:
        return False
def mult100(a):
    if(a % 100 == 0):
        if(a % 400 == 0):
            return a
        return False
    else:
        return a    
def mult4000(a):
    if(a % 4000 == 0):
        return False
    else:
        return a
def isitpositive(a):
    if a > 0:
        return True
while(True):
    try:
        year = int(input("Year: "))
        if(isitpositive(year)):
            break
        else:
            raise ValueError
    except:
        print("Wrong input. Use only positive integer.")

if(normalyear(mult100(mult4000(year)))):
    print("{} is leap year.".format(year))
else:
    print("{} is not leap year.".format(year))