
#Join 
x= "Sky"
z= "Tan"
y= "Jun"
a= "Yuan"
Sequence = (x,z,y,a)
name = "_". join(Sequence)
print(name)

#string find
s= "That I ever did see. Dusty as the Dusty handle on the door"
index = s.find("Dusty")
print (index)
if "Hello" in s:
    print (y)
else:
    print (a)
if "Dusty" in s:
    print (z)
d= "My name is Sky and I am an intern in DrWHo"
keyword = input ("what word are you looking for?")
print ("You are looking for "+ keyword)
if keyword in d:
    print ("found it!")
else:
    print ("Not found... please try again")
    keyword = input ("what word are you looking for?")

#Split
s = "Its to easy"
words = s.split()
print(words)
print (len(words))
print (len(s))
word ="Easy"
x = list(word)
print(x)

#Random 
import random
print (random.random())
print (random.randrange(0,100))
print (random.uniform(0,10))
randomlist = random.sample(range(0,10), 5)
print (randomlist)

#Elesif
a = int(10)
guess = input ("Please guess the number")
x = int(guess)
if x < a:
    print ("Higher")
    print ("------")
if x > a:
    print ("Lower")
    print ("------")
else:
    print ("You got it!")

#Forloop
city = ['Tokyo','New York','Toronto', 'Hong Kong']
print ("Cities loop:")
for x in city:
    print("City: " + x)
print ("\n")
num = [1,2,3,4,5,6,7,8,9]
print("x^2 loop")
for x in num:
    y=x*x
    print (str(x) + "*" + str(x) + "=" + str(y))

#Coursera
n= 10
while n > 0 :
    print(n)
    n= n-1
print("hello world")

x=10
g= 10+x *(x-1)
print(g)
y= g/3
print (y)

print (float(99) + 100)
i =42.723123
type (i)
f = int(i)
print(f)
type (f)


