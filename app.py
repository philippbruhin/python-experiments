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
