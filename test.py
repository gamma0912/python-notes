

def what(boo: str, foo: str) -> str: 
    """
    This function is a test for future reference. It prints hi, then boo, the foo in the same line.

    Args:
        boo (string): the first string after hi is printed
        foo (string): the second string after hi is printed

    Returns: 
        Returns the total length of the string printed

    Raises:
        No exceptions raised
    """
    print ("hi" + boo + foo)
    return len("hi") + len(boo) + len(foo)

length = what(" everybody ", "how are you doing")
print(length)
pew = ["one", "two", "three", 4, (5, "six")]
print (pew)

def add(*nums): #this type of argument allows for as many args as u want
    result = sum(int(i) for i in nums)
    return result

print(add(5, 3, 5, 7, "15"))



"""
----------NOTES----------
instead of &, |, ! we have and, or, not
elif instead of else if
"a is b" and "a in b"
'not in' also exists

"for i in range(start, stop, step)" or "for i in range(5)"
one, two, three, four = 1, 2, 3, 4

tuples are just immutable lists

object.copy() makes a shallow copy(simply a new reference to the original), meaning a change to the original changes the copy
object.deepcopy() makes a new object, a change to the original does not affect the copy

arr.sort() changes the original list
sorted(arr) returns a new list

in Python string is a primitive data type

-----------STRING---------
***check if a string is all white space/alphabets/numbers***
string = "  "
print(string.isspace())  # True
print(string.isalnum())  # False, NOTE: spaces dont count as alphabets
print(string.isalpha())  # False

***remove chars from left/right based on argument***
string = "This is a sentence with       "
# Remove trailing spaces from the right
print(string.rstrip())  # "This is a sentence with"
string = "this here is a sentence…..,,,,aaaaasd"
print(string.rstrip(“.,dsa”))  # "this here is a sentence"
print(string.lstrip(“.,dsa”))  # "this here is a sentence"

***sample from string at intervals***
my_string = "This is just a sentence"
print(my_string[0:10:3])  # Tssu   #from index 0 to 10, step = 3

***add separator between print entries***
print("29", "01", "2022", sep="/")  # 29/01/2022
print("name", "domain.com", sep="@")  # name@domain.com

--------LIST-------------
***sampling from list***
spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['bat', 'rat']

>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]

***count the number of times an element appears in a list/tuple***
names = ["Besim", "Albert", "Besim", "Fisnik", "Meriton"]
print(names.count("Besim"))  # 2 

>>> _, _, *first, _ = [1, 2, 3, 4, 5]
>>> print(first)  # [3, 4]

***manipulate strings/list***
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

***enumerate to increment both count and get element at index
>>> for count, value in enumerate(values):
...     print(count, value)
...
0 a
1 b
2 c

***assign list elements to variables***
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition = cat

***see which index an element is at in a list/tuple***
my_list = ['a', 1, 'f', 'a', 5, 'a']
print(my_tuple.index('f'))  #  2

***find most frequent element***
my_list = ['1', 1, 0, 'a', 'b', 2, 'a', 'c', 'a']
print(max(set(my_list), key=my_list.count))  # a

***remove duplicates by changing into a set and back***
my_set = set([1, 2, 1, 2, 3, 4, 5])
print(list(my_set))  # [1, 2, 3, 4, 5]

---------SETS----------
***combine 2 sets***
first_set = {4, 5, 6}
second_set = {1, 2, 3}
print(first_set.union(second_set))  # {1, 2, 3, 4, 5, 6}

----------DICTIONARY-------------
***get all the keys/values of a dict in a list form***
>>>dictionary = {"a": 1, "b": 2, "c": 3}
>>>keys = dictionary.keys()          ##works for dictionary.values as wel
>>>print(list(keys))  # ['a', 'b', 'c']


---------CLASS----------
***customize what happens when print class***
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return repr('Rectangle with area=' + str(self.a * self.b))

print(Rectangle(3, 4))  # 'Rectangle with area=12'



"""