# i have these ints 235235234 i want them to be reversed in a list

def reversTheseInts(nums):
    # return [int(num) for num in str(nums)[::-1]]
    # numsLen = len(str(nums))
    
    list_of_reversed = []
    for i in str(nums):
        # print(numsLen)
        # print(str(nums[numsLen-1]))
        list_of_reversed.append(str(nums)[::-1])
        # numsLen -= 1

    print(list_of_reversed)
reversTheseInts(23487234)
# print(reversTheseInts(23487234))