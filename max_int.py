# Take repeatable ints from user until a negative number is inputed. Then print the highest number inputed.
# Step 1: Initialize variables
# Step 2: Loop through input from user
# Step 3: Stop loop if input from user is negative
# Step 4: Print out highest number
# https://github.com/1thorarinn/max_int.git

run = True;
max_int = 0
while run:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
    if num_int < 0:
        run = False
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line