def minion_game(s):
    # your code goes here
    l = list(s)
    v = ['A' , 'E' , 'I' , 'O' , 'U']
    l1 = []
    l2 = []
    for i in range(len(l)):
        if (l[i] not in v):
            l1.append(l[i])
            st = l[i]
            for j in (l[i+1:]):
                st = st + j
                l1.append(st)
        else:
            l2.append(l[i])
            st = l[i]
            for j in (l[i+1:]):
                st = st + j
                l2.append(st)
    # print(l1)
    # print(l2)

    # print(l1)
    # print(l2)

    set1 = set(l1)
    l1_count = []
    set2 = set(l2)
    l2_count = []
    for i in list(set1):
        count = l1.count(i)
        l1_count.append(count)
    for i in list(set2):
        count = l2.count(i)
        l2_count.append(count)

    # print(list(set1))
    # print(l1_count)
    # print(list(set2))
    # print(l2_count)

    if sum(l1_count)>sum(l2_count):
        print("Stuart",sum(l1_count))
    elif sum(l1_count)<sum(l2_count):
        print("Kevin",sum(l2_count))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)