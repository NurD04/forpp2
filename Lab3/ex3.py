a = int(input()) #size of list
nums = []
rep = {}
cnt = 0
for i in range(a):
    nums.append(input())
uniq = set(nums)
for i in uniq:
    for j in nums:
        if i == j:
            cnt += 1
    if cnt > 1:
        rep[i] = cnt
    cnt = 0
print("Уникальные элементы списка", uniq, sep=' - ')
print("Повторяющиеся элементы списка и их количество", rep, sep='-')
