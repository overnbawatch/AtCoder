
Inp = input().split(' ')
list = []
for n in range(int(Inp[0])):
    list.append(input())

cnt = 0
for i in range(int(Inp[0]) - 1):
    for k in range(i + 1, int(Inp[0])):
        for j in range(int(Inp[1])):
            if list[i][j] == 'o' or list[k][j] == 'o':
                if j == int(Inp[1]) - 1:
                    cnt = cnt + 1
                continue
            else:
                break

print(cnt)
