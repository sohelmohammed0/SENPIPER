# Open the access.log file
with open('access.log', 'r') as file:
    count = 0
    # Loop through each line and check for status code 200
    for line in file:
        if ' 200 ' in line:
            count += 1
print(f'Number of successful requests (status 200): {count}')

