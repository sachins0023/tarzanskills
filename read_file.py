#Creating a file
def create_file(file_name):
    fo = open('/home/sachin/tarzan/tarzanskills/'+file_name+'.txt', 'x')
    fo.close()

#Writing to a file
def write_file(file_name):
    fo = open('/home/sachin/tarzan/tarzanskills/'+file_name+'.txt', 'w')
    text = input("Enter the data: ")
    fo.write(text)
    fo.close()

#Appending to a file
def append_file(file_name):
    fo = open('/home/sachin/tarzan/tarzanskills/'+file_name+'.txt', 'a')
    text = input("Enter the data: ")
    fo.write(text)
    fo.close()

#Reading from a file
def read_file(file_name):
    fo = open('/home/sachin/tarzan/tarzanskills/'+file_name+'.txt', 'r')
    text = fo.read()
    print(text)
    fo.close()

def del_file(file_name):
    os.remove(file_name)

create_file('file')
write_file('file')
append_file('file')
read_file('file')