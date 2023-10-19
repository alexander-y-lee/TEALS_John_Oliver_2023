import primitive_helper  # import is used to access properties from another file
import object_helper

#### Primitive Referencing (aka copying values)

## Without Functions()
x = 10  # copy the primitive, numeric value of 10 and assign to the newly created variable (container) x with scope of main.py
y = x  # copy the value inside x, which is the primitive, numeric value 10, to variable y

true_or_false = primitive_helper.get_number_six(
) == primitive_helper.six and primitive_helper.six == 6  # a == b ?, b == c ?, then a == c ?
if (primitive_helper.get_number_six() == 7):
  print("primitive_helper.get_number_six() is producing {}...".format(7))
elif (true_or_false):  # you can have unlimited elif (else if)
  print("primitive_helper.get_number_six() working properly? {}".format(
      true_or_false))
else:
  print(
      "primitive_helper.get_number_six() is {} and not 6, fixing this for you..."
      .format(primitive_helper.get_number_six()))
  while (primitive_helper.get_number_six() != 6):  # != means not equal to
    if (primitive_helper.get_number_six() < 6):
      primitive_helper.six = primitive_helper.six - 1
    else:
      primitive_helper.six = primitive_helper.six + 1
  # end of while loop
# end of if/else statement

## Question 1:
# 1.A) Would primitive_helper.six get fixed to 6 if get_number_six() returned 7?
# 1.B) Is there anything wrong with the code?

six = primitive_helper.six  # go to the address of primitive_helper.py, grab the value of six with scope of primitive_helper.py, copy this value then assign to the newly created variable six with scope of main.py;
x = x - six  # 10 - 6, then copy the value to x, so now x is 4;
print("x is now {}".format(x))  # x with scope of main.py is now 4
print("y is still {}".format(y))  # y with scope of main.py is still 10

x = x * 111  # multiply 111 with value inside x with scope of main.py, and re-assign to x
print("x is now {}".format(x))  # x == 444
print("x/100 is {}".format(
    x / 100))  # 4.44, / is floating division (keep decimals)
print("x//100 is {}".format(
    x // 100))  # 4, // is integer division (remove decimals)
print(
    "x itself is still {}".format(x)
)  # x still 444 because we never re-assigned the new values to x, only a copy of primitive x was being divided by 100

## With Functions()
x = 10  # re-assign x with scope of main.py with the numeric value of 10
print("x is now {} again".format(x))  # x with scope of main.py is now 10 again

six = six + 999  # increment six with scope of main.py by 999


def x_local_six():  # define, or create a function called x_local_six()
  six = primitive_helper.get_number_six(
  )  # call the function property get_number_six() inside primitive_helper.py file, which returns the numeric value 6, and assign to newly created local function scope variable six
  six += 1  # increment local function scope variable six by 1
  x = six  # create a new local function scope variable x, and assign the value of local six to it; both x and six here are defined locally, and therefore have priority over main.py x and main.py six
  x = x + 2  # 7 + 2
  print("x inside x_local_six() is {}".format(
      x))  # x inside local function scope of x_local_six() is 9
  # end of x_local_six() function


x_local_six()  # call, or run the function add_six()
print("x outside x_local_six() is still {}".format(
    x))  # x in main.py scope is still 10
print("six outside x_local_six() is still {}".format(
    six))  # six in main.py scope is still 1005

y = 20  # re-assign numeric value of 20 to y


def y_local_seven(
    y
):  # define, or create a function that takes in a variable parameter called y, whatever data type that "y" could be
  seven = six + 1
  y = y + seven
  print("y inside y_local_seven() is {}".format(
      y))  # y is 27 inside y_local_seven()
  # end of y_local_seven() function


y_local_seven(
    y
)  # call, or run the function y_local_seven() with an argument of y, so  this function then copies the value of the argument y, which is the numeric value 20, and assigns this 20 to a newly created local variable y
print(
    "y outside y_local_seven() is still {}".format(y))  # y outside is still 20

## Question 2: Please help me correct the comments below ##

z = 70


def subtract_then_return(asdf, y):  # ??
  print("asdf inside subtract_then_return() is {}".format(asdf))
  z = asdf - y  # ??
  # MISSING: print z # Guess what happens, and why ??
  z = y - asdf  # ??
  # MISSING print z # Guess what happens, and why ??
  return z  # ??
  # end of subtract_then_return() function


z = subtract_then_return(y, z)  # ??
# MISSING: print z # Guess what happens, and why ??

#### Object Referencing (aka Aliasing, aka memory address)

# Without Functions
x = [
]  # assign the memory address of a newly created empty list[] object to container x
print("x is now {}".format(
    x))  # x now has the address which points to that empty list []
y = x  # copy the value of x to y, which is the address
x.append("Hello")  # go to the memory address inside x and append "Hello"
y.append("World")  # go to the memory address inside y and append "World"
print("x is now {}".format(
    x))  # go to the memory address inside x and print the list
print("y is now {}".format(
    y))  # go to the memory address inside y and print the list

# With Functions
list_of_names = [
]  # assign the memory address of a newly created empty list[] object into the newly created variable called "list_of_names" with scope of main.py
name = "Christina"  # assign the primitive string value copy of "Christina"

## Question 3: Please help me correct the comments below ##

list_of_names.append(name)
print("list_of_names is now {}".format(list_of_names))

name = "Mason"


def add_name_to_list(name):
  list_of_names.append(
      name)  # go to the memory address inside list_of_names and append
  # end of add_name_to_list() function


add_name_to_list(name)
print(
    "list_of_names after add_name_to_list() is {}".format(list_of_names))  # ??

name = "Kirti"
object_helper.add_value_to_list(name, list_of_names)
# MISSING: print list_of_names # Guess what happens, and why ??


def add_name_to_local_list_of_names(name):
  name = different_name
  list_of_names = []  # ??
  list_of_names.append(name)  # ??
  # end of add_name_to_local_list_of_names() function


different_name = name
different_name = "Alex"
add_name_to_local_list_of_names(name)
# MISSING: print list_of_names  # Guess what happens, and why ??

# print(add_name_to_list("John Oliver")) # ?? Guess what happens, and why ??
