# This is a project I did on 27/5/2022.
# I did this for my semester 2 Math T Project
import math

def summation(f, range):
   r = 0
   for i in range:
      r += f(i)
   return r

def simpson(f, h, min, max):
   n = math.floor((max - min) / (h * 2))

   g = lambda i: f(min + i * h)

   a = g(0)
   b = summation(lambda i: g(2 * i - 1), range(1, n + 1))
   c = summation(lambda i: g(2 * i), range(1, n))
   d = g(2 * n)

   return (h / 3) * (a + (4 * b) + (2 * c) + d)


f = lambda x: (math.e**((-x)**3))

# main function
n = 6
while n < 7:
    min = 0
    max = 0.5
    h = (max-min)/n
    result = simpson(f, h, min, max)

    print(" x | f(x)")
    print("f({:4f}):".format(min),round(f(min), 6))
    for i in range(1,n):
    	print("f({:4f}):".format(min+h*i),round(f(min+h*i), 6))
    print("f({:4f}):".format(max),round(f(max), 6))
    print("Number of trapezium is ", n)
    print("Total area is: ", round(result, 6), "(Correct to 6 decimal points)\n")

    n += 2
