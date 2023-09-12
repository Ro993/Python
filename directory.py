from datetime import date 
import os
import pywhatkit


a = input("Enter what you want to do: ")

if( a == '1'):
    today = date.today()
    print("Current date:", today)


elif(a=='2'):
    path =input("Enter your path")
    os.makedirs(path)

    print("Succesfully created directory ", path)
    print(os.getcwd())

elif(a=='3'):

  pywhatkit.sendwhatmsg("+91 7688999695", "Tera account ho gya",10,1)

elif(a=='4'):

     path = "D:/python"
     entries = os.listdir('D:/python')
     os.listdir('D:/python/')
     print(entries)
    
     