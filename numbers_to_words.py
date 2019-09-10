import num2word

string_name = Null
for index in range(1,1001):
    string_name = string_name.append(num2word.to_card(index))
string_length = len(string_name)
for index in range(0,string_length):
    string_name = string_name.replace(index,'')
print(len(string_name))