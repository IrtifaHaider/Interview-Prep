def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in hashmap:
            return [hashmap[needed], i]

        hashmap[num] = i


nums = list(map(int, input("Enter numbers separated by space: ").split())) # user input for array

target = int(input("Enter target: "))

result = twoSum(nums, target)

print("Indices:", result)
