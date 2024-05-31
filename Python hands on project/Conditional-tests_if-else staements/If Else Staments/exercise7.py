#Store the numbers 1 through 9 in a list
my_numbers=range(1,10)
#Loop through the list.
for numbers in my_numbers:
#Use an if-elif-else chain inside the loop to print the proper ordinal end￾ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
    if numbers == 1:
        print(str(numbers) + "st")
    elif numbers == 2:
        print(str(numbers) + "nd")
    elif numbers == 3:
        print(str(numbers) + "rd")
    else:
        print(str(numbers) + "th")