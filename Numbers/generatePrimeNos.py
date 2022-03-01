def sievePrimeGen(n):
    primes = [True] * (n + 1)
    ans = []
    for i in range(2, int(n * (1 / 2) + 1)):
        if primes[i] == True:
            for j in range(i * 2, n + 1, i):
            
                primes[j] = False
       
    for i in range(2, n + 1):
        if primes[i] == True:
            ans.append(i)
        i += 1
    return ans

print(sievePrimeGen(int(input("Enter the number upto which prime nos. should be generated - "))))

"""
    * n = number uptill which prime nos are to be generated
    * primes initially has all elements True by default
    * LOGIC
        * Instead of checking wheather all nums are prime - we remove(make them False) the multiples of prime nos less than sqrt of n
         * Remaining ones which are True are Prime and False are non Prime
         * 
         * COMPLEXITY - O(N * log(log(n)))
"""