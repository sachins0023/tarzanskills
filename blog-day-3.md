# Becoming a 10x Software Developer : The Journey continues - Day 3

September 06, 2019

Hello Everyone,

I request you to go through my previous blog to be up-to-date with my progress. However I will try my level best to keep things as simple and easy to understand without any prior research.

After a couple of days of exploring through the world of Git, today, we anchored the ship in a particular direction. We decided to delve deeper into Python programming. So today's discussion includes, predominantly, features of Python programming like string slicing and functions.

#### String Slicing

String Slicing is used to slice a given sequence. For example, we have to write a program to display "abcac" repeatedly until total length becomes 12. The program is as follows:
```python
string = 'abcac'
length = 12
string_length= len(string)
times= length//string_length
remaining= length%string_length
print(string*times+string[0:remaining])
```
outputs
```
abcacabcacab
```

Here we require a part of the string to be extracted to get the desired output.

The syntax of slicing is 

```python
slice(start:end:step)
```
'start' is the starting point of the string. 'end' is the ending point of the string. 'step' is the number of jumps that takes place to consider the next character. By default, step = 1. If slice is defined as slice(::-1), it does a string reversal.

#### Input in Python

Input command is used when you want enter the required values only when the code block is run. This helps in removing hard coding in the code. This is a more dynamic approach.

Input Syntax

```
var = input("Message: ")
```

Here, whatever value you have entered when the "Message: " prompt is shown, will be stored as the value of var with the data type set to string.

#### Functions in Python
Functions are code blocks that takes input values as arguments and returns something. It can be called anywhere in the program and one of its main feature is its reusability.

Function Syntax

```
def add(a,b):
    value = a + b
    return value
```
Here is a function that adds two numbers passed to it. 'add' is the function name. 'a' and 'b' are the parameters. 'value' is returned once this function is executed. The function call for the above function is:

```
sum = add(number1,number2)
```

Some important terms associated with functions are:
1. Return Type : It is the data type of the value that the function must return. Since python is dynamically typed language, return type doesn't hold much significance here.

2. Function name : It is the name assigned to a function. It is important for the function to have a unique meaningful name because the function call requires the function name.

3. Arguments: They are the values you pass into the function parameters.

4. Parameters: They are the variables in the declaration of a function.

Today, we continued practicing with some quantitative based questions too. That's all for today folks.

Signing Off
