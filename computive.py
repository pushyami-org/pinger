import cmath
import math
from os import environ
from datetime import datetime


def main():
    # a = float(environ['A'])
    # b = float(environ['B'])
    # c = float(environ['C'])
    num = int(environ['NUM'])
    # num = 40

    # cmplx_computing(a, b, c, num)
    begin = datetime.now()
    if num <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(num):
            print(i, "=>", recur_fibo(i))
    end = datetime.now()
    diff = end - begin

    print str(i) + " Fibo finish time: " + str(diff)
    # armstrong_number(num)


def recur_fibo(n):
    """Recursive function to
    print Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


def armstrong_number(numb):
    for num in range(10, numb + 1):
        sums = 0

        # find the sums of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sums += digit ** 3
            temp //= 10

        if num == sums:
            print(num)


def cmplx_computing(a,b,c,num):
    # calculate the discriminant
    d = math.pow(b, 2) - (4 * a * c)
    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(sol1, sol2))
    num_sqrt = cmath.sqrt(cmath.sqrt(cmath.sqrt(cmath.sqrt(num))))
    print "sqr root is " + str(num_sqrt)
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
            else:
                print(num, "is a prime number")

            # if input number is less than
            # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")


if __name__ == '__main__':
    main()
