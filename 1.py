import math
import sys
def discriminantfinder(a,b,c): return (b ** 2) - (4 * (a * c))
def rootfinder(a,b,c):
    x1, x2 = (-b + math.sqrt((b**2) - (4 * (a * c)))) / 2 * a, (-b - math.sqrt((b**2) - (4 * (a * c)))) / 2 * a
    if x1 != x2:
        return x1,x2
    else:
        return x1   
def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        if discriminantfinder(a,b,c) > 0: print("There are 2 solutions.\nSolutions: {}".format(rootfinder(a,b,c)))           
        elif discriminantfinder == 0: print("There is only one solution.\nSolution: {}".format(rootfinder(a,b,c)))            
        else: print("There is no real solution.")            
    except:
        print("Please give only int as input.")
        main()
main()

    
    