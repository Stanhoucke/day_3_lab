def return_10():
    return 10

def add( number_1, number_2 ):
    add_result = number_1 + number_2
    return add_result

def subtract(number_1, number_2):
    subtract_result = number_1 - number_2
    return subtract_result

def multiply(number_1, number_2):
    multiply_result = number_1 * number_2
    return multiply_result

def divide(number_1, number_2):
    divide_result = number_1 / number_2
    return divide_result

def length_of_string(test_string):
    string_length = len(test_string)
    return string_length

def join_string(string_1, string_2):
    join_string = string_1 + string_2
    return join_string

def add_string_as_number(string_1, string_2):
    add_result = int(string_1) + int(string_2)
    return add_result

def number_to_full_month_name(number):
    if number == 1:
        result = "January"
    elif number == 3:
        result = "March"
    elif number == 9:
        result = "September"
    return result

def number_to_short_month_name(number):
    if number == 1:
        first_month_string = "Jan"
        return first_month_string
    elif number == 4:
        fourth_month_string = "Apr"
        return fourth_month_string
    elif number == 10:
        tenth_month_string = "Oct"
        return tenth_month_string

def length_of_side(number):
    cube_volume = number * number * number
    return cube_volume

def string(text):
    string_reversed = text[::-1]
    return string_reversed

def f_to_c(ftemp):
    converted_temp = (ftemp-32) * 5 / 9
    return converted_temp
