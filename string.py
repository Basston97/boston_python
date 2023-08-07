def convert_to_number(input_string):
    if input_string.isdigit():
        return int(input_string)
    else:
        try:
            return float(input_string) 
        except ValueError:
            return None

print(convert_to_number("123"))          
print(convert_to_number("-45"))          
print(convert_to_number("3.14"))        
print(convert_to_number("-2.71"))        
print(convert_to_number("not_a_number")) 
