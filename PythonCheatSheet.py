#print a Message in Python
print("Hello World in Python")

#store data in variable
variable="Hello world in Variable"

#print a variable
print(variable)

#create integer variable
integervariable=10
integervariable2=20

#do arithmetic operation on integer
print(integervariable+integervariable2)

string1="Hello"
string2="world"
#concatenate String
print(string1+" "+string2)

#create list
list_data=[10,20,30,40,10]

#print list
print(list_data)

#print list value at position 1
print(list_data[1])

#print list length size
print(len(list_data))

#print total count of value 10 in list
print(list_data.count(10))

#append a data in list
list_data.append(60)

#print all list using for each
for l in list_data:
    print(l)

#remove item from list at position
list_data.pop(2)

#print all list data
for l in list_data:
    print(l)

#print last index data of list
print(list_data[-1])

#create tuple
tuple_data=(10,20)

#print tuple
print(tuple_data)

#print tuple value at position
print(tuple_data[1])

#import json library
import json

#create 3 integer variable
a=10
b=20
c=30

#if example
if a>b:
    print("A is Greater")
else:
    print("B is Greater")

#if elif else example
if a>b and a>c:
    print("A is Greater")
elif b>c and b>a:
    print("B is Greater")
else:
    print("C is greater")

#create key value dictionary data
dic_data={"name":"Rahul","age":25}

#add extra key in dictionary
dic_data['work']="Developer"

#print dict data
print(dic_data)

#print name key value
print(dic_data['name'])

#print work key value
print(dic_data['work'])



#create list of dict data
list_dic_data=[{"name":"Rahul","age":"25"},{"name":"Aman","age":"30"}]

#printing first list name value
print(list_dic_data[0]['name'])
#print second list name value
print(list_dic_data[1]['name'])

#adding item into list
list_dic_data.append({"name":"vishal","age":"40"})

#printing third item name value
print(list_dic_data[2]['name'])

#printing all dic item with key and value
for key,data in dic_data.items():
    print("Data : "+str(data)+" key : "+str(key))

#printing all dic item value only
for value in dic_data.values():
    print("Value : "+str(value))

#taking user input
data=input("Enter Your Name.")
#pinting user input data
print(data)

#while loop example
number=10
while number!=0:
    print(number)
    number=number-1

#simple function example
def simpleFunction():
    print("Calling Simple Function")

#calling the function
simpleFunction()

#simple function with argument exmple
def simpleFunctionWithArgument(argument):
    print("Name is "+argument)

#calling the function
simpleFunctionWithArgument("Supecoders")

#simple function with argument and return exmple
def simpleFunctionWithArgumentAndReturn(a,b):
    return a+b

#printing the return data
returndata=simpleFunctionWithArgumentAndReturn(10,20)
print(returndata)

#creating simple class
class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

#intializing class object with data
dog=Animal("Dog","25")

#print the value
print(dog.getAge())
print(dog.getName())

#writing data into file
with open("file.txt","w") as fileobj:
    fileobj.write("Hello world in Python")

#appending data into file
with open("file.txt","a") as fileobj:
    fileobj.write("\nAgain Hello World")

#reading data from file
lines=[]
with open("file.txt") as fileobj:
    lines=fileobj.readlines()

for line in lines:
    print(line)

#try except example to handle error
inputno=input("Enter a Number")
try:
    print(int(inputno))
except:
    print("Not a Number")

#run for loop from 0 to 20
for i in range(20):
    print(i)

#run for loop from 10 to 20
for i in range(10,20):
    print(i)

#create a list from ranger here list data contain 10 to 20  all number
list_ranger=list(range(10,20))
print(list_ranger)

#print max value of list
print("Max : "+str(max(list_ranger)))
#print min value of list
print("Min : "+str(min(list_ranger)))
#print sum of list
print("sum : "+str(sum(list_ranger)))

#dict to json convert
json1=json.dumps(dic_data)
#print json data
print(json1)
#json to dict convert
json_to_dic=json.loads(json1)

#print dic data
print("Dic "+str(json_to_dic))