import copy

def concat_list(list_1,list_2):
    list_final = copy.copy(list_1)
    for i in list_2:
        list_final.append(i)
    return list_final

sample_list_1 = [3,2,6,5,4]
sample_list_2 = [9,8,0,0,6,8]
print("The concatenated list is", concat_list(sample_list_1,sample_list_2))