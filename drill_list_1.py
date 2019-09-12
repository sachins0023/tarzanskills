spam = ['apples', 'bananas', 'tofu', 'cats']

def spam_fn(s):
    output_string = ''
    for i in s:
        if (i == s[-1]):
            output_string = output_string + 'and '
            output_string = output_string + i
        else:
            output_string = output_string + i + ', '
    final_output = "'" + output_string + "'."
    return final_output

print(spam_fn(spam))