# print()
# can print strings, numbers, and possibly variables*
print("hello world")
print("shane")
print("hello shane how are you?")
# print(type(3526ShaneleeSeoul))
print(2)  #####shane  Shane)
# this is a comment
print("world world q!)")

# declare a variable and manipulate that variable
hello = 33
print(hello)  # returns 33
print(hello + 2)  # returns 35


# basic datatypes (strings, numbers, lists, dictionaries)
print('first_string="me!"')
print("first_number=1")

first_string = "me!"
print(first_string)

first_number = 1
print(first_number)

num1 = 23245
string1412535 = "hellodsnceon"
string668940 = "hllcnabcuaebcl"
print(string1412535)
print(string668940)
print(num1)

coffeeaddict = "200"
coffee = "hello"
cafe = "35 + 7"
cheese = 200 - 5
crackers = 284 * 4
tasty_snack = cheese + crackers

print(coffeeaddict)
print(coffee)
print(cafe)
print(cheese)

print(coffeeaddict + coffee)
print(cheese + cheese)
print(coffee + cheese)
print(cheese + coffee)  # don't mix datatypes unless you know what you're doing!

type(cheese)
print(type(cheese))
print(type(tasty_snack))

empty_list = []
first_list = [1, 2, 3]
second_list = ["one", "two", "three"]
third_list = [1, 2, "three"]

print(empty_list)
print(first_list)
print("length of first_list:", len(first_list))
print(first_list[1])
print("the value of the first element in first_list:", first_list[0])

first_dictionary = {
    1: "one",
    2: "two",
    "three": 3,
    4: "dafshcleknaeslnvlsevnleavbevlesbvleasnclkasenclnaeclk",
}
print(len(first_dictionary))
print(first_dictionary[2])
print(first_dictionary["three"])


# functions (input())
def greeting():
    print("What's your name?")
    name = input()
    # print(type(int(name)))
    print("hello " + name + "!")
    # print(type(name))


# greeting()


def day_of_week():
    print("What day is it?")
    day = input()
    if day == "saturday":
        print("Correct!")
        # print(f"You said today is {day}!")
    elif day == "pizza":
        print("go get something to eat!")
    else:
        print("Nope!")


day_of_week()

# upload to git!
