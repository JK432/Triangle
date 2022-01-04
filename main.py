#Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether the triangle is 
#A. Equilateral triangle 
#B. Right angle triangle 
#C. Doesn’t come in both categories
x=int(input())
y=int(input())
z=int(input())

if(x==y==z):
  print("Equilateral Triangle")
elif(x**2+y**2==z**2):
  print("Right Angle Triangle")
else:
  print("Doesn't come in both cases")
