import math

def question_1():

    formula="y=mx+c"
    print(formula)

    x= float(input ("Enter variable to find slope of linear equation: "))
    m= 0.5
    c= 2.5

    y= m * x + c
    print('Slope of linear equation: ' , y  )


question_1()

#sum of the given numbers from the user
def question_2():
    num = int(input('How many numbers: '))
    sum = 0
    for n in range(num):
        numbers = float(input('Enter number : '))
        sum+=numbers
    print('Sum of the numbers is :', sum)


question_2()

#use of while loop
def question_3():

     x=list(range(1,20))
     sum=0
     for num in x:
         while sum<34:
             sum+=num

     print('sum of the numbers :',sum)

question_3()

#use of if-elif-else
def circle(radius=0):

    area = math.pi*(radius**2)

    return area


print('Area of the circle: ',circle(2.5))

num=(circle(2))
if num<20:
    print("LESS than 20")
elif num>20:
    print("greater than 20")
else:
    print("equal to 20")

#use of if else in for loop
for x in range(2, 10):
    for n in range(2, x):
        if x % n == 0:
            print(x, 'equals', n, '*', x/n)
            break
        else:
            print(x, 'is a prime number')




#to produce a full length string:
my_list = ["Hello", "my", "name", "is", "John Cena"]
name = ''
for x in range(0,len(my_list)):
    name = name + my_list[x]

print(name)


#"Happy Birthday" song
name=input("Enter any name:")
def Birthday(name):
    return("Happy Birthday to you Happy Birthday dear "+name)

print(Birthday(name))


#produce squared value of odd numbers only from the list my_numbers.
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers=[]
for each in my_numbers:
    if(each%2==1):
        for eachs in my_list:
            if(each**2==eachs):
                my_numbers.append(each ** 2)


print(new_numbers)


#list comprehension
my_list = [x*y for x in [20, 40, 60] for y in [2, 4, 6]]

print(my_list)


# concept of Named Tuple and Ordered dictionary

from collections import namedtuple

point = namedtuple('point',['x','y'])
p=point(2,3)
print(p)

color=namedtuple('color',['red','green','blue'])
c=color(255,255,255)
print(c)

x= {
    "z":1,
    "t":2,
    "c":3
}
print(x)

from collections import OrderedDict
d=OrderedDict(a=123,b=2323,c=1212)
print(d)
print(d.get("a"))




