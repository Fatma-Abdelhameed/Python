        
import math
def divide_string(str1, str2):
    str1_len = math.ceil(len(str1) / 2)
    str2_len = math.ceil(len(str2) / 2)
    form_of_string = (str1[:str1_len] + str2[:str2_len]) + (str1[str1_len:len(str1)] + str2[str2_len:len(str2)])
    return form_of_string

print(divide_string("hello", "welcome")) #output helwelcloome