#Using the range() Function
for value in range(1,6):
    print(value)


#Using range() to Make a List of Numbers
numbers=list(range(1,6))
print(numbers)

#Using range() to  to skip numbers in a given range.
even_numbers=list(range(2,11,3))#adds 3 to the initial number in the range
even_numbers=list(range(2,11,2))#adds 2 to the initial number in the range
print(even_numbers)

#using the range() function to  create almost any set of numbers you want.
squares=[]
for value in range(1,11):
    square=value**2
    # squares.append(square)
    squares.append(value**2)
print(squares)

#Simple Statistics with a List of Numbers
digits=[1,2,3,4,5,6,7,8,9,0]
smallest_digit=min(digits)
print(smallest_digit)

largest_digit=max(digits)
print(largest_digit)

summation=sum(digits)
print(summation)

#List Comprehensions
squares=[value**2 for value in range(1,11)]
print(squares)