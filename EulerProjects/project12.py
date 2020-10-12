# Python 3 efficient program for counting the 
# number of numbers <=N having exactly 
# 9 divisors 

from math import sqrt 
MAX = 100000

prime = [ True for i in range(MAX + 1)] 
# Function to mark the primes 
def sieve(): 

	# mark the primes 
	k = int(sqrt(MAX)) 
	for p in range(2,k,1): 
		if (prime[p] == True):
			# mark the factors of prime as non prime 
			for i in range(p * 2,MAX,p): 
				prime[i] = False

# Function for finding no. of divisors 
def divCount(n): 
	# Traversing through all prime numbers 
	total = 1
	for p in range(2,n+1,1): 
		if (prime[p]): 
			# calculate number of divisor 
			# with formula total div = 
			# (p1+1) * (p2+1) *.....* (pn+1) 
			# where n = (a1^p1)*(a2^p2).... 
			# *(an^pn) ai being prime divisor 
			# for n and pi are their respective 
			# power in factorization 
			count = 0
			if (n % p == 0): 
				while (n % p == 0): 
					n = n / p 
					count += 1
				
				total = total * (count + 1) 
			
	return total 

# Function to find the first triangular number 
def findNumber(n): 
	if (n == 1): 
		return 3

	# initial number 
	i = 2

	# initial count of divisors 
	count = 0

	# prestore the value 
	second = 1
	first = 1

	# iterate till we get the first triangular number 
	while (count <= n): 
		# even 
		if (i % 2 == 0): 
			# function call to count divisors 
			first = divCount(i + 1) 

			# multiply with previous value 
			count = first * second 
		
		# odd step 

		else: 
			# function call to count divisors 
			second = divCount(int((i + 1) / 2)) 

			# multiply with previous value 
			count = first * second 
		
		i += 1
	return i * (i - 1) / 2

# Driver Code 
if __name__ == '__main__': 
	n = 498


	# Call the sieve function for prime 
	sieve() 
	print(int(findNumber(n))) 

# This code is contributed by 
# Surendra_Gangwar 
