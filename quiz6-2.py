import sys
star_list = [("*" * i).center(int(sys.argv[1]) * 2) for i in range(1,(int(sys.argv[1]) * 2) + 1,2)]
star_list.extend(star_list[-2::-1])
for i in star_list: print(i)