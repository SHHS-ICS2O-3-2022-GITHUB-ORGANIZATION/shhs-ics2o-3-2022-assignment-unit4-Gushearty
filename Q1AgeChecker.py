#get a number input
#if the number is between 5 and 11 it tells you that you are in elementary
#if the number is between 12 and 14 then it tells you that you are in Intermediate school
#if the number is between 15 and 18 then it tells you that you are in High School
#if the number is more than 18 then it tells you that you are in College or University
age = int(input("Enter your age: "))
if age < 12 and age > 4:
  print("you are in elementary school")
elif age < 15 and age > 11:
  print("You are in intermediate school")
elif age < 19 and age > 14:
  print("You are in high school")
elif age > 20:
  print("You are in college/University")
