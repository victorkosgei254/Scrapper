from genericpath import exists


def finder(nums,target):
    hash_map = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            print(i,nums[i])
            return i, nums[i]
        else:
            hash_map[nums[i]] = i

def palindrome(string):
    if string == string[::-1]:
        print('True')
        return True
    else:
        print('False')
        False


def getCombination(sum, array):
    solution = {}
    for i in array:
        if sum-i in array:
            solution[i] = sum -i 
            array.remove(i) 
            try: 
                array.remove(sum-i)
            except(ValueError):
                pass
    print(solution)


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,12,16,4]
    # target = 7
    # finder(nums,target)
    string = '12321'
    palindrome(string)
    getCombination(10 ,nums)

