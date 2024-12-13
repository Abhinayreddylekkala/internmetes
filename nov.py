'''num = int(input("enter the value"))
if num > 0 :
    print("+ive")
elif num < 0 :
        print("-ive")
else :
    print("zero")'''
'''def amma(name): #defination function with argument 
    print("good morning", name)
amma("abhi") #function call
amma("konda")'''
'''def fuct(num): # recation function
    if num <=0:
        return error
    if num == 1:
        return 1
    else:
        return (num * fuct(num - 1))
print(fuct(int(input("enter number: "))))'''
#example........................................
'''a = int(input("enter the value1 : "))
b = int(input("enter the value2 : "))
choice = input("enter operation(add,sub,multi,div):")
if choice == 'add':
    print(a+b)
elif choice == 'sub':
    print("sub",a-b)
elif choice =='multi':
    print("multi",a*b)
elif choice =='div':
    if b == 0:
        print("error:divison by zero is not allowed")
    else:
        print("div", a/b)'''

'''num1 = int(input("enter the first number: "))
print(type(num1))
num2 = int(input("enter the second number: "))2
sum = num1 + num2
print(sum)'''
'''num = int(input("enter the number "))
if num%2 == 0:
    print("even")
else :
    print("odd")'''

'''#function definition
def greet(name):
    print("hello",name)
    #calling function
greet("ram")'''
'''def add(num1,num2):
    sum = num1 + num2
    print("sum ",sum)

add(2,3)'''
'''def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 // num2
print("choice")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter choice (1/2/3/4): ")
if choice in ['1', '2', '3', '4']:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", sub(num1, num2))
    elif choice == '3':
        print("Result:", multi(num1, num2))
    elif choice == '4':
        print("Result:", div(num1, num2))
else:
    print("Invalid input. Please select a valid operation.")'''
# recursive function
# loop 
'''lang = ["cpp","c","python"]
lang[0:2] = "add" # mutable (adding if a data to list or replace )
print(lang[0:2])'''
'''list1 = [10,22,33,44,55,66,77,88,46,35,39]
print(len(list1))
print(list1[2:8:5])
for i in list1:
    print(i)'''
a = int(input("enter the first number" ))
b = int(input("enter the second number" ))
if a > b:
    print("a is greater than b")
    if (a - b) % 2 ==0:
        print("even")
    else:
        print("odd")
else:
    print("a is greater than b")
