# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



 #Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check if the age is zero
if age == 0:
    print("Error: Age cannot be zero.")
#check if age is greater or equal to 18
elif age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")