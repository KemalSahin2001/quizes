while(True):
    try:
        b = int(input("b: "))
        c = int(input("c: "))
        break
    except:
        print("Wrong input. Use only integer")
def deltafinder(b,c):
    delta = ((b ** 2) - (4 * c))
    return delta
root1 = (-b + (deltafinder(b,c) ** 0.5)) / 2
root2 = (-b - (deltafinder(b,c) ** 0.5)) / 2
print("""roots are:
 {}
 {}
 """.format(root1,root2))