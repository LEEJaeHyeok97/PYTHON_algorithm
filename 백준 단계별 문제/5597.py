student = [1]
count = 0

for i in range(31):
    student.append(0)

while(True):
    if(count == 28):
        break

    s = int(input())
    student[s] = 1
    count+=1

for i in range(31):
    if(student[i] == 0):
        print(i)
