print("License Process by Vishal")
name = input("Name : ")
bloodgroup = input("Blood Group : ") 
address = input("Address : ").strip() 
while(True):
    try:
        age = int(input("Age: ")) 
        break
    except:
        print("Enter only numbers") 
while(True):
    try:
        aadharNumber = eval(input("Aadhar Number: ")) 
        if len(str(aadharNumber)) ==12:
            break 
        else:
            print("Your aadhar number must have 12 digits")
    except:
        print("Enter only nummber") 
print("1.Two Wheeler") 
print("2.Four Wheeler")
vehicle = int(input("Enter your details:")) 
if age >= 12 and age < 60:
    print("Successfully submitted the application") 
else:
    print("Your are not eligible for the license")

