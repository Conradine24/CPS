#Name: CPS (commission Payout System)
#Author: Conradine Powell
#Date Created: 03/28/2022
#Course: ITT103
#Purpose: This program will take numeraous input from the user to calcualte their comission. It is program to run until the user inputs a    //  certain  number as directed"""



def class_1(sales_amount):#creating a function to pass sales amount to and theb calculate a percentage  based on tghe amount of sales 
  if sales_amount <1000:
    sales_amount= sales_amount*0.06 #after each checks and calculate the apropriate percentage. it returns the comission in the same variable 
    return sales_amount
  elif sales_amount >1000 and sales_amount <2000:
    sales_amount= sales_amount*0.07
    return sales_amount 
  elif sales_amount>2000:
    sales_amount= sales_amount*0.10
    return sales_amount 

 
def class_2(sales_amount):
  if sales_amount <1000:
    sales_amount= sales_amount*0.04   #after each checks and calculate the apropriate percentage. it returns the comission in the same variable 
    return sales_amount
  elif sales_amount >=1000:
    sales_amount= sales_amount*0.06
    return sales_amount
  

def class_3(sales_amount):
 
    sales_amount= sales_amount*0.045
    return sales_amount
 

print("*********MAIN MENU**********")
print("1--------Calulate Sales Data")
print("Any key to exit the Program")

while int(input("Please select a numerical option: ")) ==1: # this will loop until the user enter any other oprion to end the program 

    sales_person_number =input("Enter you Sales Number: ")
    sales_amount = float(input("Enter your sales amount: "))
    while (sales_amount <=0):  # keeps looping until the user put tghe correct sales amount . nothing 0 or less 
        print("The sales amount must be greater than 0")
        sales_amount = float(input("Enter your sales amount: "))
        
    class_type = int(input("Enter your class type: "))
    while class_type < 1 or class_type >3 :
      class_type = int(input("Please enter the correct class:  1:  2:  3 "))
      

    
      if class_type == 1:
          total=class_1(sales_amount)
          print("Sales ID: ",sales_person_number )
          print("Class: ",class_type )
          print("Total Saes: ",sales_amount)
          print("Total comission: ",total )

      elif class_type == 2:
          total = class_1(sales_amount)
          print("Sales ID: ",sales_person_number )
          print("Class: ",class_type )
          print("Total Saes: ",sales_amount)
          print("Total comission: ",total )


      elif class_type == 3:
          total = class_3(sales_amount)
          print("Sales ID: ",sales_person_number)
          print("Class: ",class_type)
          print("Total Saes: ",sales_amount)
          print("Total comission: ",total)

   
    print("*********MAIN MENU**********")
    print("1--------Calulate Sales Data")
    print("Any key to exsit the Program")
      
  
print("You have chose to exit the program")
sys.exit("Marks is less than 20")



