
N = int(input())
S = list(input())

flag = False
for i in range(N):
    if flag:
        if S[i] == '\"':
            flag = False
    else:
        if S[i] == '\"':
            flag = True
        if S[i] == ',':
            S[i] = '.'
print(''.join(S))


