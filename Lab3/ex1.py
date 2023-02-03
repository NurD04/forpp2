nums = []
res = []
cnt = 0
cou = 0
k = int(input())  #how many elements in list
while cnt < k:
    nums.append(int(input()))
    cnt += 1
target = int(input())
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            if nums[i] + nums[j] == target:
                res.append(i)
                res.append(j)
                cou += 1
    if cou == 1:
        print(res)
        break