# Write an algorithm that takes in an unsorted integer array and finds a pair with a given sum.

def target_pair(list, target):
    new_list = sorted(list)
    left = 0    
    right = (len(new_list) - 1)
    while left < right:
        if new_list[left] + new_list[right] == target:
            return(new_list[left], new_list[right])

        if new_list[left] + new_list[right] < target:
            left = left + 1
        else:
            right = right - 1

    return('no pairs sum to the target value')

list = [5,10,4,7,6,2]
print(target_pair(list, 9))