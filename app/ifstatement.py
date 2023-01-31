#An if statement is a construct that enables a program to specify an alternative path of execution.
# python has several types of seletion statements: one-way if statement, two way if-else statemenst, nested if statements, multi-way if-elif-else and conditional expression.
radius = int(input("type radius here: "))
if radius >= 0:
    area = radius * radius * 3.14159
    print("the area for the circle of radius", radius, "is", area)

number = int(input("enter an integer: "))    
if number % 5 == 0:
    print("HiFive")
if number % 2 == 0:
    print("HiEven")

#Write an if statement that assigns 1 to x if y is greater than 0.
#x = int(input("enter value for x: "))
y = int(input("type your integer for y here: "))

if y > 0:
    x = 1
    print(y)
    print(x)

#write an if statement that increases pay by 3% if score is greater than 90.
score = float(input("enter your score here: "))
pay = float(input("enter pay: "))
if score > 90:
    pay += 0.03
    
    print("since your score is", score, "your pay will be: ", pay)
else:
    print("your score did not meet the requirement")