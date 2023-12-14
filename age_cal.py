#!/usr/bin/python3
year = input("what's your year of birth?: ")
month = input("what's your month of birth?: ")
date = input("what's your date of birth?: ")
current_year = input("what's the current year?: ")

age = int(current_year) - int(year)
print("your date of birth is ", end=" ")
print(date, "-",month,"-",year)

print("You are", age, end=" ")
print("years old")

