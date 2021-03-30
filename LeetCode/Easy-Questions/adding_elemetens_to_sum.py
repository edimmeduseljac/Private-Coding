nums = [3,3]

target = 6

index = 0
output = []
for i in enumerate(nums):
    if nums[index] + nums[index - 1] == target:
        output.append(nums.index(nums[index]))
        output.append(nums.index(nums[index+1]))     
        print()
        output.sort()
        break
    else: 
        index += 1
print(output)

# Fehler wenn beide Zahlen im Array nums[] dieselben sind!