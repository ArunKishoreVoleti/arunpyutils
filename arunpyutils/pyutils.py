class Pyutils:

    # A method to find if a number is even or not
    def is_even(self, number):
        if number%2==0 and number>0:
            return True
        return False

    # A method to find if a number is odd or not
    def is_odd(self, number):
        if number%2==1 and number>0:
            return True
        return False

    # A method to find Sum of First N Numbers
    def sum_n(self, number):
        return (number * (number+1))//2

    # A method to find if a number is prime or not
    def is_prime(self, number):
        if number<2:
            return False
        for fact in range(2, 1+int(number**.5)):
            if number%fact==0:
                return False
        return True
    
    # A method to find if an year is leap or not
    def is_leap_year(self, year):
        if year%400 == 0 or (year%4 == 0 and year%100 != 0):
            return True
        return False
    
    # A method to identify if a number is palendrome or not
    def is_palendrome_number(self, number):
        if str(number) == str(number)[::-1]:
            return True
        return False        