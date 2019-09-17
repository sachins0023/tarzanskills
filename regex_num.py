# import re
# s = 'My name is Varun and my phone number is +919860400249,My name is Varun and my phone number is +919860400249'
# regex = re.compile(r"\+([0-9]+)")
# # print(type(regex))
# matches = regex.search(s)
# # print(type(matches))
# print(matches.group())


# import re
# s = 'My name is Varun and my phone number is +919860400249,My name is Varun and my phone number is +919860400249,My name is Varun and my phone number is +919860400249,My name is Varun and my phone number is +919860400249'
# regex = re.compile(r"\+([0-9]+)")
# matches = regex.findall(s)
# for match in matches:
#     print(match)

# Strong Password Detection
# # Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long,
# # contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

import re
password = input("Enter password: ")
regex = re.compile(r"[a-z]+")
isPasswordStrong = True
matches = regex.search(password)
if matches is None:
    isPasswordStrong = False


regex = re.compile(r"[A-Z]+")

matches = regex.search(password)
if matches is None:
    isPasswordStrong = False


regex = re.compile(r"[0-9]+")

matches = regex.search(password)
if matches is None:
    isPasswordStrong = False

regex = re.compile(r"[a-zA-Z0-9]{8,}")

matches = regex.search(password)
if matches is None:
    isPasswordStrong = False

if isPasswordStrong:
    print("Password is Strong")
else:
    print("Password is Weak!")
