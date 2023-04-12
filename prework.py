# 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(username):
    """Display a simple greeting"""
    print("hello_" + username.upper() + "!")
    
hello_name('username')


# 2 Write a function to print odd numbers from 1-100 and returns nothing 

def first_odds():
    """Write a python to print odd numbers from 1-100 and returns nothing"""
    x = 1
    while x <= 100:
        if x % 2 == 1:
            print(x)
        x += 1
first_odds()
    

 # 3 Write a python function, max_num_in_a_list to return the max number in a list.

def max_num_in_a_list(a_list):

    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

print(max_num_in_a_list([5, 12, 387, 62]))   


# 4 Write a function to return if a given year is a leap year.

a_year = input("What year would you like to check?")
def is_a_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year% 100 != 0):
        return True

    return False
if is_a_leap_year(int(a_year)):
    print("Its a leap year.")
else:
    print("It is not a leap year.")
