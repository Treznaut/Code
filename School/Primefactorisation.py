import mathsplus #This is a package me and my friend coded

num = int(input('What do you want the prime factor of? '))

number = mathsplus.Hcf_lcm([num])

prime_factors = number.prime_factors(number.numbers)

print(prime_factors)

#This is the code in the package
#https://pypi.org/project/mathsplus/
#Link to the Package
#
#def prime_factors(self):
#   i = 2
#   n=self.numbers[0]
#   factors = []
#   while i * i <= n:
#       if n % i:
#           i += 1
#       else:
#           n //= i
#           factors.append(i)
#   if n > 1:
#       factors.append(n)
#   return factors