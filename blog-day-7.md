# Becoming a 10x Software Developer : The Journey continues — Day 7

September 11, 2019

Hello Everyone,

I request you to go through my previous blog to be up-to-date with my progress. However I will try my level best to keep things as simple and easy to understand without any prior research.

Today, we started with File Handling. In relation to that, a bunch of commands from os package in python was discussed. These are important as it has the ability to interact with your operating system no matter which one it is. Some of the examples of these commands are:

```
os.getcwd()                 - Displays the current working directory
os.chdir('<path>')          - Changes the directory to <path>
os.path.abspath('<path>')   - Returns an absolute path with filename mentioned even if it doesn't exit actually in the system
os.path.relpath('<path>')   - Returns the relative path  with filename mentioned
os.path.dirname('<path>')   - Gives you the path to the directory  before last '/'
os.path.isabs('<path>')     - Checks whether <path> is an absolute path
os.path.basename('<path>')  - The last name after '/' is displayed
os.path.exists('<path>')    - Checks whether <path> exists
os.path.isdir('path')       - Checks whether <path> corresponds to a directory
os.path.isfile('path')      - Checks whether <path> corresponds to a file
os.path.getsize('<path>')   - Returns the size of the file
os.listdir('<path>')        - Returns the list of elements in <path>
os.mkdir('filename')        - Creates a directory with name 'filename'
```

### Create, Write, Read and Append to a file

File objects: file objects lets you use, access and manipulate files
i.e.
```
file_object = open('<filename>', '<mode>')
```

File objects when declared has three attributes:
* name
* mode
* closed

```
fo.name     - returns the name of the file
fo.mode     - returns the mode of the file
fo.closed   - checks whether the file is closed or not
```
#### Creating a file

Creates a file:
```
fo = open('<filename>', 'x')
fo.close()
```

#### Writing a file

Write some data into the file:
```
fo = open('<filename>', 'w')
text = 'Enter text'
fo.write(text)
fo.close()
```

#### Reading a file

Read all of the data from the file and print it:
```
fo = open('<filename>', 'r')
text = fo.read()
print(text)
fo.close()
```

#### Appending a file

Appending to an already made file
```
fo = open('<filename>', 'a')
text = 'Enter new text'
fo.write(text)
fo.close()
```

#### Modes

Modes are the information we give saying how we want our file to be utilised. Some of the examples of modes are:  

```
'x'     - creates a new file and returns the file object. Returns error if file already exists.
'r'     - opens a file in read mode. Pointer at the beginning.
'a'     - creates a file if it doesn't exist, opens the file in append mode else. Pointer at the end.
'w'     - creates a file in write mode. If file exists, overwrites the file. Pointer at the beginning.
'r+'    - opens in read and write mode. Pointer stays at beginning of the file and overwrites the characters on by one when written into.
'rb'    - opens a file in binary read mode. Pointer at beginning
'ab'    - creates/appends in binary append mode if file not present/present. Pointer at the end.
'wb'    - creates/ overwrites in binary write mode if file not present/present. Pointer at the beginning.
'a+'    - creates/ append and read a file in binary append mode. Pointer at end.
'rb+'   - opens in binary read and write mode. Pointer at start.
'ab+'   - creates/ append and append a file in binary append mode. Pointer at end.
```
Note that 'r', 'r+', 'rb', 'rb+' modes won't create a file if it doesn't already exist.

#### seek()
seek() is a function that lets you move your pointer in a file to the desired input.

Syntax:
```
seek(offset, from what)
```

Some examples are:
```
seek(0,0)   - Takes you to the beginning of the file
seek(0,2)   - Takes you to the end of the file
seek(0,1)   - Takes you to the current position in a file
```

In the case of mode = 'a+', even though read is allowed, since the current pointer stays at the end of the file, reading is not actually possible. When we ask the program to read from the file, it would return only empty string. However, with the help of seek(), you can traverse to different parts of the file and keep the pointer there. From there, the read() function could be used.

Note that append mode is completely independent to .append() (which belongs to lists)

This briefly sums up the contents of discussion of Day-7.

Signing off
