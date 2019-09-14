# Becoming a 10x Software Developer : The Journey continues — Day 9

September 13, 2019

Hello Everyone,

I request you to go through my previous blog to be up-to-date with my progress. However I will try my level best to keep things as simple and easy to understand without any prior research.

In Python programming language there are 4 collection data type namely,
1. List
2. Dictionary
3. Tuple
4. Set

Today we  discussed about sets.
### Sets
Set is an unordered collection of unique items. The elements are seperated by ',' and enclosed in '{}' braces.
```
s = {1,2,3,4,5}
* s.add(6)      - adds '6' to set s
```
If A = {1,2,3,4} and B = {4,5,6}
```
A-B = {1,2,3}
A&B = {4}
A|B = {1,2,3,4,5,6}
A^B = {1,2,3,5,6}
```

### Some more string functions

If s = 'hEllo'
```
* s.upper() = 'HELLO'
* s.lower() = 'hello'
* s.capitalise() = 'HEllo'
```
If s = 'today is friday'
```
* s.title()         - 'Today Is Friday'
* l = s.split()     - l = ["today", "is", "friday"]
* l = s.split("i")  - l = ["today ", "s friday"]
```
If l = ['h', 'e', 'l', 'l', 'o']
```
* s = "".join(l)    - s = hello
* s = "-".join(l)   - s = h-e-l-l-o
```
If s = "   tarzan \t skills \t \n"
```
* s.strip()           - s = "tarzan \t skills"
* s.rstrip()          - s = "   tarzan \t skills"
* s.lstrip()          - s = "tarzan \t skills \t \n"
```
### map()

If the input is taken in the form of a string (inputs seperated by spaces), map() function helps you to convert the values and store it in a list.
Ex. If the input required is in a list of integers and the values are inputted seperated by spaces, we have a string of the values seperated by spaces
```
l = list(map(int, input().split))
```
The above line of code basically receives your space seperated values as string, splits it to individual values as string, and maps the int type conversion through the values. The returned pointer is then converted to a list and stored in l.

The rest of the day, we started with Hackerrank. It was a really compettitive beginning and our objective is to achieve top 10000 in India as soon as possible. That's all for the day.

Signing off
