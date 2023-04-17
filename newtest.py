# Write a python function, max_num_in_a_list to return the max number in a list.

def max_num_in_a_list(a_list):

    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

print(max_num_in_a_list([5, 12, 387, 62]))

a_year = input("What year would you like to check?")
def is_a_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year% 100 != 0):
        return True

    return False
if is_a_leap_year(int(a_year)):
    print("Its a leap year.")
else:
    print("It is not a leap year.")


def is_consecutive():
    my_list = [1,2,3,4]
    new_list = [1,2,4,5]
    for i in range(my_list[0], my_list[0]+len(my_list)):
        new_list.append(i)
    print(new_list)
    if my_list == new_list:
    
     print("This is a consecutive list.")
    else:
     print("this is not a consecutive")





    





