# Python Fundementals - Personal Notes

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



