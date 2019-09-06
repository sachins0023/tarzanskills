string = 'abcac'
length = 12
string_length= len(string)
times= length//string_length
remaining= length%string_length
print(string*times+string[0:remaining])
print(string*times+string[0:4])
print(string*times+string[0:8])
print(string*times+string[0:-1])
print(string*times+string[-1:0])
print(string*times+string[-1:4])
print(string*times+string[-3:0])
print(string[-5:-1])
print(string[::-1])
print(string[0::-1])
print(string[:5:-1])
print(string[0:4:-1])
print(string[2:4:1])
print(string[4:0:-1])