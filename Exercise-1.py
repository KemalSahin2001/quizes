nonprimes = list(set([x for x in range(2,50) for y in range(2,int((x/2) + 1)) if x % y == 0]))
primes = [x for x in range(2,50) if x not in nonprimes]
print(nonprimes,"\n")
print(primes)