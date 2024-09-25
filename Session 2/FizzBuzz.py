"""Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number."""

def fizzbuzz(n):
    for x in range(1, n+1):
        if x % 5 == 0:
            print('Buzz')
        elif x % 3 == 0:
            print('Fizz')
        else:
            print(x)


fizzbuzz(13)