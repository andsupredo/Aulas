def fb(n):
    if not n % 3 == 0 and not n % 5 == 0:
       return n
    if n % 3 == 0 and n % 5 == 0:
        return ('FizzBuzz')
    if n % 3 == 0:
       return ('Fizz')
    if n % 5 == 0:
        return ('Buzz')


print(fb(13))