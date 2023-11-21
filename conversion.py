# Program ask user a year we were born and calculate our age and print it

birth_year = input('Birth year: ')
#here we need to convert string to integer cze python does not know it
#because the input function stored in birth_year) give us a string so we can't do operation on string and int without conversion
#we will use function called int()
age = 2023 - int(birth_year) 
print(age)

#to print type of variable we use function called type()
print(type(age))
print(type(birth_year))

print("*************EXERCICES************************\n")
print("Ask a user their weight(in pounds)") 
print("convert it to kilograms and  print on the terminal\n")
print("*************SOLUTION************************\n")

weight = input('what is your weight please(lbs)? ')
weight_in_kgs = int(weight) * 0.45 #we converted weigt into int 1 pound is equal to approximately 0.453592 kilograms
print(weight_in_kgs)
