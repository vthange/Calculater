while True :

#Table print Function
 def print_table() :
  print("________________________********_______________________")
  print("Table Print")
  a=int(input("Enter the number\n"))
  for i in range(1,11):
   if a>5000 :
     print("Enter a number less than 5000")
     break
   b=a*i
   print(b)
   
#print_table()

#Addiction Function
 def addiction () :
  print("________________________********_______________________")
  print("Addiction")
  a=int(input("Enter the number\n"))
  b=int(input("Enter the number\n"))
  c=a+b
  print("Addiction of \n",a,'+',b,'is' ,c)

#addiction()

#substaction Function

 def substaction () :
  print("________________________********_______________________")
  print("Substaction")
  a=int(input("Enter the number\n"))
  b=int(input("Enter the number\n"))
  c=a-b
  print("Addiction of \n",a,'-',b,'is' ,c)

#substaction()

#Multplication Function

 def multplication () :  
  print("________________________********_______________________")
  a=int(input("Enter the number\n"))
  b=int(input("Enter the number\n"))
  c=a*b
  print("Addiction of \n",a,'*',b,'is' ,c)

#multplication ()

#Division Function
 def division () :
  print("________________________********_______________________")
  a=int(input("Enter the number\n"))
  b=int(input("Enter the number\n"))
  c=a/b
  print("Addiction of \n",a,'/',b,'is' ,c)
#division()

 print("Welcome to a Calculater \n Please Choose a Number \n 1.Addiction \n 2.Substaction \n 3.Multplication \n 4.Division \n 5.Table Print \n 6.Exit")
 a=int(input("Enter the number \n"))
 if a==1 :
  addiction()
 elif a==2 :
  substaction()
 elif a==3 :
  multplication()
 elif a==4 :
  division()
 elif a==5:
  print_table()
 elif a==6:
  print("Thank You")
 else :
  print("Enter a valid number")

 print("Thank You\n\n\n\n\n\n\n\n")
