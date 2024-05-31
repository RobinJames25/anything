# Use a for loop to print the numbers from 1 to 20, inclusive.
numbers=range(1,21)
for number in numbers:
    print(number)

#Make a list of the numbers from one to one hundred, and then use a for loop to print the numbers.
numbers=range(1,101)
for number in numbers:
    print(number)

#Make a list of the numbers from one to one one hundred, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
numbers=list(range(1,101))
smallest=min(numbers)
print(smallest)
largest=max(numbers)
print(largest)
summation=sum(numbers)
print(summation)

# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number. Use a for loop to print each number
numbers=list(range(1,20,2))
for number in numbers:
    print(number)

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
numbers=list(range(3,30,3))
for number in numbers:
    print(number)

#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cu
cube=[]
for value in range(1,11):
    cube.append(value**3)
print(cube)

# Use a list comprehension to generate a list of the first 10 cubes.
cube=[value**3 for value in range(1,11)]
print(cube)