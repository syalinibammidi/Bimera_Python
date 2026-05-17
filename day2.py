#1.  Check Employee promotion eligibility
age=int(input("age of employee "))
salary=int(input("enter the salary"))
expe=int(input("enter the experience"))
if age>25 and salary>50000 and expe>5:
    print("eligible for promotion")
else:
    print(" not eligible for promotion")
#2.Check student distinction category
math=int(input("enter the math marks"))
english=int(input("enter the eng marks"))
science=int(input("enter the sci marks"))
if math>=75 and english>=75 and science>=75:
    print("Distinction")
elif math>=35 and english>=35 and science>=35:
    print("pass")
else:
    print("fail")

#3. Check website login system
user=input("Enter username: ")
password=input("Enter password: ")
otp=input("Enter otp: ")
correct_username="admin"
correct_password="1234"
correct_otp="5678"
if user==correct_username and password==correct_password and otp==correct_otp:
    print("Login successful")
else:
    print("Login failed")

#4. Check internet package category
speed=int(input("enter speed: "))
data=int(input("enter data: "))
day=int(input("enter remaining days: "))
if speed>100 and data>500 and day>20:
    print("premium plan")
elif speed>50 and data>200:
    print("standard plan")
else:
    print("basic plan")
#5.Check job eligibility
degree=input("enter degree yes or no :")
age_=int(input("age"))
exp_=int(input("enter the experience"))
if degree=="yes" and exp_>=2 and age_>21:
    print("eligible")
else:
    print("not eligible")

#6. Check flight boarding eligibility
ticket = input("do you have a valid ticket? (yes/no):")
passport= input("do you have a valid passport? (yes/no):")
luggage_weight = float(input("enter your luggage weight in kg:"))
if ticket.lower() == "yes" and passport.lower() == "yes" and luggage_weight <= 25:
    print("eligible for flight boarding")
else:
    print(" not eligible for flight boarding")
#7. Check scholarship eligibility
marks = int(input("enter your marks:"))
family_income = float(input("enter your family income in lakhs:"))
attendance = float(input("enter your attendance percentage:"))
if marks >= 85 and attendance >= 75 and family_income <= 300000:
    print("eligible for the scholarship")
else:
    print("not eligible for the scholarship")


#8. Check mobile unlock system
pin = int(input("enter your pin:"))
face_detection_status = input("is face detection available? (yes/no):")
fingerprint_status = input("is fingerprint recognition available? (yes/no):")
if pin == 1234 or face_detection_status.lower()== "yes" or fingerprint_status.lower() == "yes":
    print("unlocked ")
else:
    print("locked")
    
#9.Check hotel booking eligibility
room=int(input("enter the no of rooms"))
days=int(input("enetr no of days: "))
budget=int(input("enetre the budget: "))
if room>=2 and days>=3 and budget>50000:
    print("luxary booking")
elif room>=1 and days>=1 and budget>20000:
    print("stanadrd bookin")
else:
    print("budget booking")
    
#10. Check exam topper category
sub1_marks = int(input("enter your marks in subject 1:"))
subj2_marks = int(input("enter your marks in subject 2:"))
subj3_marks = int(input("enter your marks in subject 3:"))
total= sub1_marks + subj2_marks + subj3_marks
if total>= 270:
    print("TOPPER")
elif total >= 180:
    print("AVG")
else:
    print("NEEDS IMPROVEMENT")
    
#11.Check gym membership category
age = int(input("enter your age:"))
weight = float(input("enter your weight in kg:"))
height = float(input("enter your height in cm:"))
if age >= 18 and weight >= 50 and height >= 150:
    print("fitness category a ")
elif age >= 16 and weight >= 40 and height >=140:
    print("fitness category b")
else:
    print("fitness category c")
    
#12.Check traffic penalty system
h=input("helmet yes or no:")
l=input("license yes or no: ")
speed=int(input("enter speed"))
if h=="yes" and l=="yes" and speed<80:
    print("No fine")
elif h=="no" and l=="no" and speed>100:
    print("heavy fine")
else:
    print("normal fine")

    
#13. Check movie ticket pricing
age1 = int(input("enter your age:"))
day1 = input("enter the day of the week:")
membership = input("do you have a membership card? (yes/no):")
if age1<18 and day1.lower()=="sunday" and membership.lower() == "yes":
    print("50% discount")
elif  membership.lower() == "yes":
    print("25% discount")
else:
    print("no discount")

#14.Check weather alert system
temperature =   int(input("enter the temperature in degree Celsius:"))
wind_speed = int(input("enter the wind speed in km/h:"))
rain_status = input("is it raining? (yes/no):")
if temperature> 40 and wind_speed > 50 and rain_status.lower () =="no":
    print("heat alert")
elif wind_speed > 30 and rain_status.lower() == "yes":
    print("storm alert")
else:
    print("normal weather")
    
#15.Check online shopping offer
purchase_amount = float(input("enter your purchase amount in dollars:"))
coupon_availbility = input("do you have a coupon code? (yes/no):")
membership_status = input("are you a member of the loyalty program? (yes/no):")
if purchase_amount >= 10000 and coupon_availbility.lower() == "yes" and membership_status.lower() == "yes":
    print("maximum discount")
elif purchase_amount >= 5000 and coupon_availbility.lower() == "yes":
    print("medium discount")
else:
    print("no discount")

#16. Check server room access
idcard_status       = input("do you have a valid ID card? (yes/no):")
fingerprint_status  = input("is fingerprint recognition available? (yes/no):")
access_level = int(input("enter your access level (1-10):"))
if idcard_status.lower() == "yes" and fingerprint_status.lower() == "yes" and access_level > 5:
    print("access granted")
else:
    print("access restricted")
    
#17.Check sports team selection
speed_score = int(input("enter your speed score:"))
fitness_score =     int(input("enter your fitness score:"))
discipline_score = int(input("enter your discipline score:"))
if speed_score >= 80 and fitness_score >= 80 and discipline_score >= 80:
    print("selected")
elif speed_score >= 60 and fitness_score >= 60 and discipline_score >= 60:
    print("waiting list")
else:
    print("not selected")

#18. Check laptop purchase recommendation
budget = float(input("enter your budget in dollars:"))
storage =   int (input("enter your storage requirement in GB:"))
ram = int(input("enter the required RAM in GB:"))       
if ( budget >= 100000 and ram>= 16 and storage >= 512):
    print("gaming laptop")
elif (budget >= 50000 and ram >= 8 and storage >= 256):
    print("office laptop")
else:
    print("basic laptop")
    
#19. Check bank loan approval
salary =    int(input("enter your salary:"))
credit_score =  int(input("enter your credit score:"))
experiance  = int(input("enter your years of experience:"))
if salary >= 50000 and credit_score >= 750 and experiance >= 3:
    print("loan approved")
else : 
    print("loan rejected")

#20.Check smart home security system'''
door = input("is the door closed? (yes/no):")
camera = input("is the security camera active? (yes/no):")
alarm= input("is the alarm system armed? (yes/no):")
if door.lower() == "yes" and camera.lower() == "yes" and alarm.lower() == "yes":
    print("home is secure")
else:
    print("home security compromised")