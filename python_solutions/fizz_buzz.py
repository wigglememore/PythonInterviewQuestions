# if a multiple of 3, print Fizz
# if a multiple of 5, print Buzz
# if a multiple of 3 and 5, print Fizz Buzz


def fizz_buzz(last_number):
    for n in range(1, last_number+1):
        if n % 3 == 0 and n % 5 == 0:
            print(f'{n}: FizzBuzz')
        elif n % 3 == 0:
            print(f'{n}: Fizz')
        elif n % 5 == 0:
            print(f'{n}: Buzz')
        else:
            print(n)


fizz_buzz(30)
