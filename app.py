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
hello("Hello World!")
hello()