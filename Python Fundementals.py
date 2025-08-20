# Python Fundementals - Personal notes for future me and some friends

# Printing

print("\nUse print("") to print a line, will auto make a new line")
print("Apparently you don't need a semicolon (;) to finish a line")
print('You can also use '' instead of "" to print a sentence')
print("ofc, new line is STILL \ n together")

print('print("You can use single qouation marks to print double qoutation marks and sometimes code like this")')

# Arithmetic operations
print("\nMath is pretty much the same as Java with some slight differences")

print("2 + 5")
print(2 + 5)

print("3 * 3")
print(3 * 3)

print("2 + 2 * 10")
print(2 + 2 * 10)

print("((28 * 3) * 21) - (55 / 5)")
print(((28 * 3) * 21) - (55 / 5))

print("Exactly what you thought right?\nIt follows the same order of operations as Java to a certain extent.")
print("Just remember to have the same amount of open and closed parenthesis")

operator_precedence = """
Precedence Level | Operator                     | Explanation
-----------------|------------------------------|-------------------------------
1 (highest)      | ( )                          | Parentheses
2                | **                           | Exponentiation
3                | -a, +a                       | Negative, positive argument
4                | *, /, //, %, @               | Multiplication, division, floor division, modulus, at
5                | +, -                         | Addition, subtraction
6                | <, <=, >, >=, ==, !=         | Less than, less than or equal, greater, greater or equal, equal, not equal
7                | not                          | Boolean Not
8                | and                          | Boolean And
9                | or                           | Boolean Or
"""

print(operator_precedence)

# Data Types

data_types = '''
1. int
x = 42
Java: int x = 42;

2. float
pi = 3.14
Java: float pi = 3.14f; OR double pi = 3.14;

3. complex
z = 2 + 3j
Java: No native support for complex numbers

4. str
name = "Alice"
Java: String name = "Alice";

5. bool
is_valid = True
Java: boolean isValid = true;

6. list
numbers = [1, 2, 3]
Java: List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3));

7. tuple
point = (10, 20)
Java: No native tuple support; use custom class or third-party libraries

8. set
unique_nums = {1, 2, 3}
Java: Set<Integer> uniqueNums = new HashSet<>(Arrays.asList(1, 2, 3));

9. dict
person = {"name": "Bob", "age": 30}
Java: Map<String, Object> person = new HashMap<>();
      person.put("name", "Bob");
      person.put("age", 30);

10. None
nothing = None
Java: Object nothing = null;

11. bytes
data = b"hello"
Java: byte[] data = "hello".getBytes();
'''

print(data_types)

data_types_summary = '''
Python -> Java type mapping:
int         -> int, long
float       -> float, double
complex     -> (no native Java type)
str         -> String
bool        -> boolean
list        -> List (ArrayList, LinkedList)
tuple       -> (no native Java type)
set         -> Set (HashSet, TreeSet)
dict        -> Map (HashMap, TreeMap)
None        -> null
bytes       -> byte[]
'''

print(data_types_summary)

# Commenting

print("\nInstead of // it's a # for comments")
print("For multiline comment you have to use three ' like this ")

print("\n'''\n\nText\n\n'''") # you can also add them after a line of code
'''

Visual for Multilines

'''

print('''You can print multiline comments! They are printed in the same fashion as you wrote them''')
print("(see code of this py file, used to display the order of precedence)")

# Input Reading

print("\nInstead of importing a Scanner and intializing it then doing the following:")
print("String x = input.nextLine();")
print('You do this: name = input("What is your name? ")')
print('lowercase input is your Scanner!')

this_makes_it_a_string = input("If you don't give a datatype it will automatically make it a String.\nType and see: ")
print(this_makes_it_a_string)

this_is_an_int = int(input("This one here will always be an int, please make sure it is: "))
print(this_is_an_int)

print("To make sure it reads a certain datatype do this: datatype( input(Blah blah blah) ).")
print("Basically surround the intial input command with int() or the data type you want")

print("if you are wondering how to change datatypes simply do what you do in Java...kind of")
print('''
Java: int SomeInt = (int) SomeFloat;
Python: some_int = int(some_float)
Extra! Python can round like this: rounded_int = round(some_float)
''')
print("Here's your int you typed a few moments ago using expansion:", float(this_is_an_int))

print('''
| Operation        | Description               | Python Example   | Result |
| ---------------- | ------------------------- | ---------------- | ------ |
| Truncation       | Removes decimal part      | int(5.9)         | 5      |
| Rounding         | Nearest whole number      | round(5.9)       | 6      |
| Ceiling (up)     | Always rounds up          | math.ceil(5.1)   | 6      |
| Expansion (type) | Converts int to float     | float(5)         | 5.0    |
''')

print('To use math.ceil make you type "import math" at the top of your code')

# Variables & some slight String manip

print("\nVariables work mostly in the same way as Java.")
print("Instead of camelCase, Python uses snake_case")
print("Yes, you can still do the latter but I recommend sticking to what that language perfers")

print("You can still concatenate in Python in the same way as Java.")
print('Ex:Hi, " + name + "!')
print('Ex: name + " is quite a nice name.')

print("But you can also use a comma to as a replacemet for +. It makes a space for you as well")
print('Ex: print("My name is", name)')

print('''
If we wanted to make a program that askes for basic info, we'd do it in this way

User Inputs:      
Given name: Steve
Family name: Adams
Street address: 776 Brick Road
City and postal code: Paris HM34 67W

Code:
name = input("Given name: ")
lastname = input("Family name: ")
address = input("Street address: ")
extra_addy = input("City and postal code: ")

Result:      
Steve Adams
776 Brick Road
Paris HM34 67W

Code for Result:
print((name), lastname + "\ n" + address + "\ n" + extra_addy)
      
You may have noticed I printed all of that using only ONE LINE.
You can still do this in Python in the same way using \ n and other means.
I if you want to use a variable with it, put parenthesis around it THEN add the comma.
Since we confirmed the "," is basically a "+" with a space after it, this allows us to save time.
''')

# | Code     | Meaning                         | Example                   | Output                 |
# |----------|----------------------------------|---------------------------|------------------------|
# | \n       | New line                         | print("Hello\nWorld")     | Hello                  |
# |          |                                  |                           | World                  |
# | \t       | Tab (horizontal)                 | print("Name:\tJohn")      | Name:   John           |
# | \\       | Backslash                        | print("C:\\path\\file")   | C:\path\file           |
# | \'       | Single quote                     | print('It\'s good')       | It's good              |
# | \"       | Double quote                     | print("He said \"hi\"")   | He said "hi"           |
# | \r       | Carriage return (rarely used)    | print("abc\rX")           | Xbc (overwrites 'a')   |
# | \b       | Backspace                        | print("abc\b")            | ab                     |
# | \f       | Form feed                        | print("Hello\fWorld")     | Hello[form feed]World  |
# | \a       | Bell (system beep, not visible)  | print("\a")               | (may beep)             |
# | \uXXXX   | Unicode character                | print("\u2764")           | ❤                      |

print("To know more about string manip commands, please look above this message in an editor.")