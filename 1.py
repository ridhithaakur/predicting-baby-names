Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>># -*- coding: utf-8 -*-

#comparing two names and finding which is more popular and also finding the maximum popularity of the names.
import csv
#importing the baby names file
print ("Welcome to the baby name analyzer!")
#initialising the variables
repeat = "yes"
count = 0
count1= 0
count2= 0
year= " "

while repeat.lower().strip() == "yes":


 with open("usa_baby_names.csv", "r") as file:
    reader = csv.reader(file)
    search = input("What analysis would you like to run (name comparison/maximum popularity)?")
    if search == "name comparison": # finding the most popular name, between two names.

       n1 = str(input("Enter the first name to analyze: ")) #input value1 from the user
       n2 = str(input("Enter the second name to analyze: ")) #input value2 from the user
       for i in reader:
        if i[0]==n1:
         count = int(i[2])+count
        elif i[0]==n2:
         count1 = int(i[2])+count
      
       if count> count1:
        print (n1," was more popular than",n2, "(",count,count1,")!")
       elif count< count1:
        print (n2," was more popular than",n1, count,count1)
        repeat = input("Would you like to run another analysis (yes/no)? ") #the code will be terminated, if No is entered


    elif search == "maximum popularity": # searching maximum popularity of the name.
      n3 = str(input("Enter a name to analyze: "))
      for j in reader:
        if j[0]==n3:
          if int(j[2]) > count2:
            count2= int(j[2])
            year= j[1]
      print(n3,"was most popular in",year,"with a frequency of",count2)
      repeat = input("Would you like to run another analysis (yes/no)? ")
    else:
     print("Sorry, that type of analysis is not supported. ")
     repeat = input("Would you like to run another analysis (yes/no)? ")
