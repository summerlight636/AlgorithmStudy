# 해쉬!
# note = dict()
# for key, val in note.items():
n = int(input())
note = dict()
for i in range(n):
    note[input()] = 1
for i in range(n-1):
    note[input()] = 0
for key, val in note.items():
    if val == 1:
        print(key)
        break