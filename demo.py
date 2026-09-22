x = "Javeed"
print(x)

height  = 6.0
print(height,"\n")

#Lists

numbers  = [1,2,3,4,5]
print("numbers: \n",numbers)

#tuples
coordinates = (10,50)
print(coordinates,"\n")


#Dictionaries
person = {
    "name" : "Alice",
    "age" : 30
}
print("\n Dictionary : ",person,"\n")

#Loops
for i in range(1,11) : 
    print(f"13 * {i} = {13*i}")

def factorial(num):
    if(num < 1):
        return 1
    return num * factorial(num - 1)

print("\n",factorial(4))