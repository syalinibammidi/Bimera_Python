#1. Check whether employee age is above 21 and salary is above 30000
age=int(input("age"))
salary=int(input("salary"))
if age>21 and salary>30000:
    print("Satisfy")
else:
    print("not")

#2. Check whether student passed in two subjects
sub1=int(input("Enter sub1 marks"))
sub2=int(input("Enter sub2 marks"))
if sub1>=35 and sub2>=35:
    print("you have passed")
else:
    print("you have failed")

#3. Check whether entered value is between two ranges
n=int(input("enter num"))
#range
if n>10 and n<20:
    print("in range")
else:
    print("not in range")
#4. Check whether username and password are correct
name=input("name?")
password=input("password?")
corn="admin"
corp="123"
if name==corn and password==corp:
    print("succes")
else:
    print("not allowed")

#5. Check whether temperature is within safe range
temp=int(input("enter temp"))
#range
if temp>20 and temp<60:
    print("in safe  range")
else:
    print("not in  safe range")

#6. Check whether both entered numbers are even
a1=int(input("enter num 1"))
a2=int(input("enter num 2"))
if a1%2==0 and a2%2==0:
    print("even")
else:
    print("not even")
#7. Check whether both entered numbers are positive
n1=int(input("enter num 1"))
n2=int(input("Enter num 2"))
if n1>0 and n2>0:
    print("Both are positive")
else:
    print("not")

#8. Check whether person is eligible for driving
age1 = int(input("Enter age: "))
license1 = input("yes or no: ")

if age1 >= 18 and license1 == "yes":
    print("eligible for driving")
else:
    print("not eligible for driving")

#9. Check whether project progress meets deadline condition
rem_days=int(input("Enter rem days"))
per=int(input("Enter completion percentage"))
if rem_days>5 and per>85:
    print("meeting deadline")
else:
    print("not meeting deadline")

#10. Check whether attendance and marks satisfy eligibility
atte=int(input("enter attedance"))
marks=int(input("enter marks "))
if atte>75 and marks>35:
    print("eligible")
else:
    print("not eligible")

#11. Check whether entered role is Admin or Manager
role=(input("enter role"))
if role=="admin" or role=="manager":
    print("Access garnted")
else:
    print("access not granted")

#12. Check whether student scored distinction in any one subject
sub1=int(input("enter sub 1"))
sub2=int(input("enter sub 2"))
if sub1>75 or sub2>75:
    print("Distinct pass")
else:
    print(" no distinction")

#13. Check whether entered day is weekend
day = input("enter a day ").lower()

if day == "sunday" or day== "saturday":
    print("weekend")
else:
    print("weekday")

#14. Check whether selected category matches two possible values
cat=input("enter category")
if cat=="computer" or cat=="it":
    print(" Category Matched")
else:
    print(" Category not matched")

#15. Check whether salary or experience satisfies requirement
salary1=int(input("enter salary"))
exp=int(input("enter experience"))
if salary1>50000 or exp>3:
    print("expertie")
else:
    print("not expertie")

#16. Check whether temperature is extremely low or high
temperature=int(input("enter temperature"))
lower=20
higher=45
if temperature<20:
    print("extremely low temp")
elif temperature>45:
    print("extremely high temp")
else:
    print("moderate")
#17. Check whether entered username matches predefined values
role1=(input("enter role"))
if role1=="admin" or role1=="manager":
    print("Access garnted")
else:
    print("not granted")

#18. Check whether selected option belongs to given choices
op=input("enter the option").lower()
if op=="b" or op=="b" or op=="c":
    print("granted")
else:
    print("not granted")
    #strip()==> removes the space

#19. Check whether entered city matches allowed cities
city=input("enter the city").lower()
if city=="hyd" or city=="vizag" or city=="delhi":
    print("eligible cities")
else:
    print("ineligible cities")

#20. Check whether entered number matches predefined values
number=int(input("Enter the number"))
if number==2 or number==4 or number==6:
    print("Number matched")
else:
    print("Number not matched")

#21. Check whether user is not admin
user=input("Enter your username")
if user !="admin":
    print("You are not admin")
else:
    print("You are admin")

#22. Check whether entered number is not positive
user_num=int(input("Enter the number"))
if user_num<=0:
    print("Not positive")
else:
    print("is postive")

#23.Check whether entered value is not empty
value = input("enter a value:")
if value.strip() != "":
    print("the value is not empty ")
else:
    print("the value is empty")

#24.Check whether file is not available
file_name= input("enter the file name:")
if file_name.strip() != "":
    print("the file is available")
else:
    print("the file is not available")

#25.Check whether employee is not active
employee_status = input("enter employee status (active/inactive):")
if employee_status.lower() != "active":
    print("the employee is not active")
else:
    print("the employee is active")
    
#26.Check whether project status is not completed
project_status = input("enter project status (completed/in progress):")
if project_status.lower() != "completed":
    print("the project is not completed")
else:
    print("the project is completed")
    
#27.Check whether password is not correct
password = input("enter your password:")
if password != "7684":
        print(" password is not correct")
else:
    print("password is correct")
    
#28.Check whether temperature is not safe
temperature = int(input("enter the temperature:"))
if temperature != 0 and temperature != 100:
    print("the temperature is  safe")
else:
    print("the temperature is not safe")
    
#29. Check whether selected option is not allowed
option = input("enter an option :")
if option.upper() != "A" and option.upper() != "B" and option.upper() != "C":
    print("the option is not allowed")
else:
    print("the option is allowed")
    
#30. Check whether marks are not passing marks'''
marks = int(input("enter your marks:"))
if marks != 35:
    print("the marks are not passing marks")
else:
    print("the marks are passing marks")