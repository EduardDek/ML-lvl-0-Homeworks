
nums = [1,1,1,1]

pair = 0
for i in range (0,len(nums)):
    for a in range(i+1, len(nums)):
        if nums[i]==nums[a]:
            pair +=1
print(pair)
