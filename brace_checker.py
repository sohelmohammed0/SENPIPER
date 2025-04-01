def check_braces(input_string):
    brace_count = 0
    
    for char in input_string:
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count < 0:
                return False
    
    return brace_count == 0

# Prompt user for input
input_string = input("Enter the string: ")

# Check braces and print result
result = check_braces(input_string)
print(result)
