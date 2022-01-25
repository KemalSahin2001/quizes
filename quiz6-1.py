import sys
def print_Upper(blank,star,length):
    if star == (length * 2) - 1: 
        print(" " * (blank-1) + "*" * star)
        print_Lower(blank - 1,star -2,length)        
    else:
        print(" " * (blank-1) + "*" * star)
        print_Upper(blank - 1,star + 2,length)
def print_Lower(blank,star,length):
    if star == 1: print(" " * (blank+1) + "*" * star)
    else:
         print(" " * (blank+1) + "*" * star)
         print_Lower(blank + 1,star -2,length)

print_Upper(int(sys.argv[1]),1,int(sys.argv[1]))