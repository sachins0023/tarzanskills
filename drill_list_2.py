n = int(input("Number of scores: "))
A = []
for i in range(n):
    score = int(input("Enter the score: "))
    A.append(score)
A.sort()
print("Score of runner up is", A[1])