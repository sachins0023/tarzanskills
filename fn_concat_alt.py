import copy

def concat_list(list_1,list_2):
    list_final = []
    if len(list_1)<len(list_2):
        check_list = copy.copy(list_1)
    elif len(list_1)>=len(list_2):
        check_list = copy.copy(list_2)
    for i in range(len(check_list)):
        list_final.append(list_1[i])
        list_final.append(list_2[i])
    if len(list_1)<len(list_2):
        for i in range(len(check_list),len(list_2)):
            list_final.append(list_2[i])
    elif len(list_1)>=len(list_2):
        for i in range(len(check_list),len(list_1)):
            list_final.append(list_1[i])
    return list_final

sample_list_1 = [3,2,6,5,4,8,9,1,1,2,2]
sample_list_2 = [9,8,0,0,6,8]
print("The concatenated list is", concat_list(sample_list_1,sample_list_2))