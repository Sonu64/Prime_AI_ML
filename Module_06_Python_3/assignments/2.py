def average(nums):
    sum = 0
    n = len(nums)
    for number in nums:
        sum += number
    return sum/n

myList = [10, 20, 30]
print(f"Average of {myList} is {average(myList)}.")
    