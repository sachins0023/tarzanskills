# Becoming a 10x Software Developer : The Journey continues — Day 2
September 06, 2019
Hello Everyone,
Since my path to becoming a software developer is a continuous process over a period of time, I request you to go through my previous blog to be up-to-date with my progress. However I will try my level best to keep things as simple and easy to understand without any prior research.
Today’s session was all about Git Branching and operations in Python programming along with introduction to variables and data types in Python.
Before we started with Git Branching, in relation to yesterday’s session on git push, we found out the way to have our login credentials to github saved. This is very important because otherwise, every time, the terminal will prompt you to enter your username and password which is a tedious process.
To store your credentials for git push, use
```
git config credential.helper store
```
```
git push https://github.com/owner/repo.git
```
Here, ‘owner’ has to be replaced with your github username and ‘repo’ with your repository name.

#### Git Branching
In a team project, each individual works on their own branch and once the code is in working condition, the individual has to do a pull request to the manager who manages the master branch. In this way, the code in the master branch is always executable without errors or unwanted results. If another branch wants to add their code, then the manager adds it to the master branch provided it doesn’t cause any discrepancy. If any problems are encountered, the manager could manage the editing or deletion of the branch.
After completion of each work, the individual does a git pull to check whether their code is same as what the master has. If the master has some changes that the individual doesn’t have, then it is updated in the individual’s file through git pull. If the master has an updated file for which the individual also made changes, then the individual has to incorporate the earlier committed code in master into his update and make sure both the updates work.
##### Some Git commands introduced:
```
git branch — to see the branches
git branch <name> — to create a new branch
git checkout <name> — to switch branch
git checkout -b <name> — to create a branch and switch into it
```
#### Operations in Python programming
Python programming blesses us with a wide range of arithmetic and logic operations like Addition(+), Subtraction(-), Multiplication(\*), Division(/), Exponential(**), Parenthesis(()) and Modulus(%) as its arithmetic operators and Greater than(>), Less then (<), Greater than or equal to (>=), Less than or equal to(<=), and Not equal to(!=) as its Logic operators.
Since these operations could occur in a single statement, there is a need for priorities to be given to the operators to decide which would be evaluated first. The arithmetic operators have a higher priority than logic operators. The priority of arithmetic operators can be easily remembered by PEMDAS.
i.e. Parenthesis>Exponential>Multiplication>Division>Addition>Subtraction
Even though modulus is not mentioned here, since it involves division to find the remainder, it could be prioritized after multiplication.
Some important observations are:
* In the case of arithmetic operations, if one of the number is a decimal, then the answer will always be a decimal except in the case of complex numbers.
* In python, j is used to denote square root of -1.
* In terms of complex numbers, it never gives you zero as ending digit post decimal with j.
* Division of two integers or floats always return a float value.
Some examples of arithmetic operations:
```
30/6=5.0
2j+3j=5j
1–2.0=-1.0
2j*3j=-6+0j
1/4j=-0.25j
1j/4j=0.25 +0j
1%2.0=1.0
1%2j=error
1j%4j=error
```
* In **from decimal import Decimal**,
operations should be enclosed without quotes while numbers have to be put in quotes to attain exact values. Due to how floating numbers are defined sum of 1.1+2.2 gives a result of 3.3000000000000003 and is mathematically incorrect. Hence **Decimal** can be used to attain mathematically accurate values for similar discrepancies.
* **from fractions import Fraction**
helps you work with fractions and their arithmetic and logical applications.
* Note: Always in the case of solving arithmetic problems involving decimals try to use **from decimal import Decimal** and include the numbers in quotes inside **Decimal()**
#### Variable, Data Types and Type Casting
Variables are something with a particular data type to which we can assign data. Variables must always have meaningful names when declared.
###### Naming Convention
1. Camel convention- every new word in variable name starts with capital. [Used for C, C++]
ex: FirstName, firstName
2. Pascal convention- all the words are separated with underscore. [Used for Python]
ex: first_name, last_name
###### Data Types
Based on data types of variables, there are two kinds of languages:
1. Statically typed languages. ex: C,C++,Java
-It requires the data type to be specified during the declaration of the variable.
2. Dynamically typed languages. ex: Python2, Python3
-It automatically identifies the data type of the variable based on the input data.
In python, some of the basic data types are:
* Integers (int)
* Floating point numbers (float)
* Complex Numbers (complex)
* Strings (string)
* Boolean (bool)
* Unsigned Integer type (uint)
* Date/Time types (time)
* Enumerated type (enum)
###### Type Casting
Conversion of the value of a variable to accomodate the change in data type mentioned.
ex: Conversion of integer values into float if data type is declared as float
```
a = 2.75
b = int(a)
print(b)
```
outputs
```
2
```
Here, even though a is a floating variable, b takes the value of int data type. Hence an integer value is outputted.
Today we also dealt with solving some quantitative based question which can improve our problem solving skills. With that, I have pretty much covered the main points discussed in today’s session. More content to follow tomorrow.
Signing off for today. :)
