age = 27
name = "Philipp"
todayIsCold = False

print("Hello my name is {} and I am {} years old.".format(name, age))


if age > 18:
    print("You are older than 18")
else:
    print("You are younger than 18")


def hello(thestring="default value"):
    print("Output of function: " + thestring)

hello("Hello World!")
hello()

dognames = ["Fido", "Sean", "Sally", "Hansdampf" , 43321, False, 3.1415]

print(dognames)

dognames.insert(0, "Jane")

print(dognames)

print(dognames[2])
print(len(dognames))

del(dognames[2])

print(dognames)
print(len(dognames))

dognames[2] = "ReplaceName"

print(dognames)
print(len(dognames))

dognames2 = ["Fido", "Sean", "Sally"]

for dog in dognames2:
    print(dog)

for x in range(1,100):
    print(x)

while age < 30:
    print(age)
    age += 1

dogs = {"Fido":8, "Sally":17, "Sean":2}
print(dogs)
print(dogs["Sally"])

dogs = {"Fido":8, "Sally":17, "Sean":2}
del(dogs["Sally"])
print(dogs)

dogs["Sara"] = 6
print(dogs)


class Dog:

    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    dogInfo = "Hey dogs are cool"
    
    def bark(self, str):
        print("BARK!" + str)

mydog = Dog("fido", 13, "Brown")
mydog.bark("yeah")

#mydog.name = "Fido"
#mydog.age = 16

print(mydog.name)
print(mydog.age)

print(Dog.dogInfo)
