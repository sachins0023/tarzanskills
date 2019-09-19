def merge_sort(list_1,list_2):
    new_list = []
    for i in list_1:
        for j in range(i,len(list_2)):
            if i<list_2[j]:
                new_list.append(i)
                break
            else:
                new_list.append(list_2[j])
    return new_list

sample_list_1 = [1,3,5,7,9]
sample_list_2 = [2,4,6]
print("The concatenated sorted list is", merge_sort(sample_list_1,sample_list_2))